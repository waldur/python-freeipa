import argparse
import json
import logging
import sys


def main():
    parser = argparse.ArgumentParser(description="Recreate API Commands from JSON api spec")

    source_group = parser.add_mutually_exclusive_group(required=True)

    source_group.add_argument(
        "--source-json", dest="source_json", action="store", default=None,
        help="Full path to json document, describing the API")

    source_group.add_argument(
        "--source-url", dest="source_url", action="store", default=None,
        help="fqdn of ipa server, to fetch the API from, requires kerberos ticket to be present")

    parsed_args = parser.parse_args()

    creator = MetaAPICreator(
        src_json=parsed_args.source_json,
        src_url=parsed_args.source_url
    )
    creator.run()


class MetaAPICreator:
    def __init__(self, src_json, src_url):
        self._src_json = src_json
        self._src_url = src_url
        self._json_spec = None
        self.log = logging.getLogger()
        fmt = logging.Formatter("%(levelname)s  %(message)s")
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(fmt)
        self.log.addHandler(handler)
        self.log.setLevel(logging.DEBUG)
        self._meta_api = []

    @property
    def meta_api(self):
        return self._meta_api

    @property
    def src_json(self):
        return self._src_json

    @property
    def src_url(self):
        return self._src_url

    @property
    def json_spec(self):
        if self._json_spec:
            return self._json_spec
        if self.src_json:
            json_spec = self._json_spec_from_file()
        else:
            json_spec = self._json_spec_from_url()
        self._json_spec = json_spec
        return self._json_spec

    def append(self, line, base_indent=None):
        if not line:
            base_indent = ''
        elif not base_indent:
            base_indent = ''
        else:
            base_indent = '    ' * base_indent
        self.meta_api.append('{0}{1}'.format(base_indent, line.rstrip()))

    @staticmethod
    def _name_mapping(name, _type):
        return '{0}_{1}'.format(_type, name)

    def _json_spec_from_file(self):
        try:
            with open(self.src_json) as json_file:
                return json.load(json_file)
        except OSError as err:
            self.log.fatal(err)
            sys.exit(1)

    def _json_spec_from_url(self):
        raise NotImplementedError

    def _class_header(self):
        self.append('from python_freeipa.client import Client')
        self.append('')
        self.append('')
        self.append('class ClientMeta(Client):')
        self.append('    version = \'{0}\''.format(self.json_spec['result']['messages'][0]['data']['server_version']))
        self.append('')
        self.append('    def __init__(self, host, verify_ssl=True):')
        self.append('        super(ClientMeta, self).__init__(host=host, verify_ssl=verify_ssl, version=self.version)')

    def _func_add(self, command, spec):
        self.append('')
        self.append('def {0}('.format(command), 1)
        self.append('    self,'.format(command), 2)
        self.log.info("adding function {0}".format(command))

        args_body, args_options = self.func_add_args(spec['takes_args'])
        opts_body, opts_options = self.func_add_options(spec['takes_options'])

        head_later = list()

        for i in args_options:
            if i['default_value']:
                head_later.append(i['head'])
            else:
                for line in i['head']:
                    self.append(line, 3)

        for i in opts_options:
            if i['default_value']:
                head_later.append(i['head'])
            else:
                for line in i['head']:
                    self.append(line, 3)

        for i in head_later:
            for line in i:
                self.append(line, 3)

        self.append('):'.format(command), 1)

        self.append('"""{0}'.format(spec['doc']), 2)
        for i in args_options:
            for line in i['doc']:
                self.append(line, 2)
        for i in opts_options:
            for line in i['doc']:
                self.append(line, 2)
        self.append('"""', 2)

        self.append("method = '{0}'".format(command), 2)
        for i in args_body:
            self.append(i, 2)
        for i in args_options:
            for line in i['body']:
                self.append(line, 2)
        for i in opts_body:
            self.append(i, 2)
        for i in opts_options:
            for line in i['body']:
                self.append(line, 2)

        self.append('')
        self.append('return self._request(method, _args, _params)', 2)

    def func_add_args(self, specs):
        options = list()
        body = list()

        body.append('')
        body.append('_args = list()')

        for spec in specs:
            options.append(self.func_add_arg(spec))
        return body, options

    def func_add_arg(self, spec):
        result = dict()
        result['body'] = list()
        result['doc'] = list()
        result['head'] = list()
        result['default_value'] = False
        if not isinstance(spec, dict):
            self.log.warning("found arg spec, that is not a dictionary, adding *args")
            return result
        self.func_add_arg_head(spec, result)
        return result

    def func_add_arg_head(self, spec, result):
        arg_name = spec['name']
        mapped_arg_name = self._name_mapping(arg_name, 'a')
        if 'default' in spec:
            result['default_value'] = True
            if isinstance(spec['default'], str):
                result['head'].append("{0}='{1}',".format(mapped_arg_name, spec['default']))
            elif isinstance(spec['default'], list):
                result['head'].append("{0}=None,".format(mapped_arg_name))
            else:
                result['head'].append("{0}={1},".format(mapped_arg_name, spec['default']))
        elif spec['required']:
            result['head'].append("{0},".format(mapped_arg_name))
        else:
            result['default_value'] = True
            result['head'].append("{0}=None,".format(mapped_arg_name))
        self.func_add_arg_doc(arg_name, spec, result, 'a')
        self.func_add_arg_body(arg_name, spec, result)

    def func_add_arg_doc(self, arg_name, spec, result, _prefix):
        mapped_arg_name = self._name_mapping(arg_name, _prefix)
        result['doc'].append(':param {0}: {1}'.format(mapped_arg_name, spec['doc']))
        _class = spec['class']
        if _class == 'Flag':
            _class = 'bool'
        elif _class == 'Dict':
            _class = 'dict'
        elif _class == 'Int':
            _class = 'int, min value {0}, max value {1}'.format(
                spec['minvalue'],
                spec['maxvalue']
            )
        elif _class == "IntEnum":
            _class = 'int, valid values {0}'.format(spec['cli_metavar'])
        elif _class == 'Str':
            _class = 'str'
        elif _class == "StrEnum":
            _class = 'str, valid values {0}'.format(spec['cli_metavar'])
        result['doc'].append(':type  {0}: {1}'.format(mapped_arg_name, _class))

    def func_add_arg_body(self, arg_name, spec, result):
        mapped_arg_name = self._name_mapping(arg_name, 'a')
        result['body'].append('_args.append({0})'.format(mapped_arg_name))

    def func_add_options(self, specs):
        options = list()
        body = list()

        body.append('')
        body.append('_params = dict()')

        for spec in specs:
            if spec['name'] == 'version':
                continue
            options.append(self.func_add_option(spec))
        return body, options

    def func_add_option(self, spec):
        result = dict()
        result['body'] = list()
        result['doc'] = list()
        result['head'] = list()
        result['default_value'] = False
        if not isinstance(spec, dict):
            self.log.warning("found option spec, that is not a dictionary, adding **kargs?")
            return result
        self.func_add_option_head(spec, result)
        return result

    def func_add_option_head(self, spec, result):
        arg_name = spec['name']
        mapped_arg_name = self._name_mapping(arg_name, 'o')
        if arg_name == 'all':
            result['default_value'] = True
            result['head'].append("{0}=True,".format(mapped_arg_name))
        elif 'default' in spec:
            result['default_value'] = True
            if isinstance(spec['default'], str):
                result['head'].append("{0}='{1}',".format(mapped_arg_name, spec['default']))
            elif isinstance(spec['default'], list):
                result['head'].append("{0}=None,".format(mapped_arg_name))
            else:
                result['head'].append("{0}={1},".format(mapped_arg_name, spec['default']))
        elif spec['required']:
            result['head'].append("{0},".format(mapped_arg_name))
        else:
            result['default_value'] = True
            result['head'].append("{0}=None,".format(mapped_arg_name))
        self.func_add_arg_doc(arg_name, spec, result, 'o')
        self.func_add_option_body(arg_name, spec, result)

    def func_add_option_body(self, arg_name, spec, result):
        mapped_arg_name = self._name_mapping(arg_name, 'o')
        if spec['required']:
            result['body'].append("_params['{0}'] = {1}".format(arg_name, mapped_arg_name))
        else:
            result['body'].append("if {0} is not None:".format(mapped_arg_name))
            result['body'].append("    _params['{0}'] = {1}".format(arg_name, mapped_arg_name))

    def _render(self):
        meta_api = '\n'.join(self.meta_api)
        return meta_api

    def run(self):
        self._class_header()
        for command, spec in self.json_spec['result']['commands'].items():
            self._func_add(command, spec)
        self.append('')
        with open('meta_api.py', 'w') as meta_api:
            meta_api.write(self._render())


if __name__ == '__main__':
    main()
