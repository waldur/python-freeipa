from python_freeipa.client import Client


class ClientMeta(Client):
    version = '2.231'

    def __init__(self, host, verify_ssl=True):
        super(ClientMeta, self).__init__(host=host, verify_ssl=verify_ssl, version=self.version)

    def aci_add(
            self,
            a_aciname,
            o_permissions,
            o_aciprefix,
            o_attrs=None,
            o_filter=None,
            o_group=None,
            o_memberof=None,
            o_permission=None,
            o_subtree=None,
            o_targetgroup=None,
            o_type=None,
            o_all=True,
            o_raw=False,
            o_selfaci=False,
            o_test=False,
    ):
        """
    Create new ACI.
        :param a_aciname: ACI name
        :type  a_aciname: str
        :param o_attrs: Attributes
        :type  o_attrs: str
        :param o_filter: Legal LDAP filter (e.g. ou=Engineering)
        :type  o_filter: str
        :param o_group: User group ACI grants access to
        :type  o_group: str
        :param o_memberof: Member of a group
        :type  o_memberof: str
        :param o_permission: Permission ACI grants access to
        :type  o_permission: str
        :param o_permissions: Permissions to grant(read, write, add, delete, all)
        :type  o_permissions: str
        :param o_subtree: Subtree to apply ACI to
        :type  o_subtree: str
        :param o_targetgroup: Group to apply ACI to
        :type  o_targetgroup: str
        :param o_aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type  o_aciprefix: str, valid values ['permission', 'delegation', 'selfservice', 'none']
        :param o_type: type of IPA object (user, group, host, hostgroup, service, netgroup)
        :type  o_type: str, valid values ['user', 'group', 'host', 'service', 'hostgroup', 'netgroup', 'dnsrecord']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_selfaci: Apply ACI to your own entry (self)
        :type  o_selfaci: bool
        :param o_test: Test the ACI syntax but don't write anything
        :type  o_test: bool
        """
        method = 'aci_add'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_filter:
            _params['filter'] = o_filter
        if o_group:
            _params['group'] = o_group
        if o_memberof:
            _params['memberof'] = o_memberof
        if o_permission:
            _params['permission'] = o_permission
        _params['permissions'] = o_permissions
        if o_subtree:
            _params['subtree'] = o_subtree
        if o_targetgroup:
            _params['targetgroup'] = o_targetgroup
        _params['aciprefix'] = o_aciprefix
        if o_type:
            _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_selfaci:
            _params['selfaci'] = o_selfaci
        if o_test:
            _params['test'] = o_test

        return self._request(method, _args, _params)

    def aci_del(
            self,
            a_aciname,
            o_aciprefix,
    ):
        """
    Delete ACI.
        :param a_aciname: ACI name
        :type  a_aciname: str
        :param o_aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type  o_aciprefix: str, valid values ['permission', 'delegation', 'selfservice', 'none']
        """
        method = 'aci_del'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        _params['aciprefix'] = o_aciprefix

        return self._request(method, _args, _params)

    def aci_find(
            self,
            a_criteria=None,
            o_selfaci=False,
            o_attrs=None,
            o_filter=None,
            o_group=None,
            o_memberof=None,
            o_aciname=None,
            o_permission=None,
            o_permissions=None,
            o_subtree=None,
            o_targetgroup=None,
            o_aciprefix=None,
            o_type=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
    ):
        """
    Search for ACIs.

    Returns a list of ACIs

    EXAMPLES:

     To find all ACIs that apply directly to members of the group ipausers:
       ipa aci-find --memberof=ipausers

     To find all ACIs that grant add access:
       ipa aci-find --permissions=add

    Note that the find command only looks for the given text in the set of
    ACIs, it does not evaluate the ACIs to see if something would apply.
    For example, searching on memberof=ipausers will find all ACIs that
    have ipausers as a memberof. There may be other ACIs that apply to
    members of that group indirectly.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_selfaci: Apply ACI to your own entry (self)
        :type  o_selfaci: Bool
        :param o_attrs: Attributes
        :type  o_attrs: str
        :param o_filter: Legal LDAP filter (e.g. ou=Engineering)
        :type  o_filter: str
        :param o_group: User group ACI grants access to
        :type  o_group: str
        :param o_memberof: Member of a group
        :type  o_memberof: str
        :param o_aciname: ACI name
        :type  o_aciname: str
        :param o_permission: Permission ACI grants access to
        :type  o_permission: str
        :param o_permissions: Permissions to grant(read, write, add, delete, all)
        :type  o_permissions: str
        :param o_subtree: Subtree to apply ACI to
        :type  o_subtree: str
        :param o_targetgroup: Group to apply ACI to
        :type  o_targetgroup: str
        :param o_aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type  o_aciprefix: str, valid values ['permission', 'delegation', 'selfservice', 'none']
        :param o_type: type of IPA object (user, group, host, hostgroup, service, netgroup)
        :type  o_type: str, valid values ['user', 'group', 'host', 'service', 'hostgroup', 'netgroup', 'dnsrecord']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'aci_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_selfaci:
            _params['selfaci'] = o_selfaci
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_filter:
            _params['filter'] = o_filter
        if o_group:
            _params['group'] = o_group
        if o_memberof:
            _params['memberof'] = o_memberof
        if o_aciname:
            _params['aciname'] = o_aciname
        if o_permission:
            _params['permission'] = o_permission
        if o_permissions:
            _params['permissions'] = o_permissions
        if o_subtree:
            _params['subtree'] = o_subtree
        if o_targetgroup:
            _params['targetgroup'] = o_targetgroup
        if o_aciprefix:
            _params['aciprefix'] = o_aciprefix
        if o_type:
            _params['type'] = o_type
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def aci_mod(
            self,
            a_aciname,
            o_aciprefix,
            o_attrs=None,
            o_filter=None,
            o_group=None,
            o_memberof=None,
            o_permission=None,
            o_permissions=None,
            o_subtree=None,
            o_targetgroup=None,
            o_type=None,
            o_all=True,
            o_raw=False,
            o_selfaci=False,
    ):
        """
    Modify ACI.
        :param a_aciname: ACI name
        :type  a_aciname: str
        :param o_attrs: Attributes
        :type  o_attrs: str
        :param o_filter: Legal LDAP filter (e.g. ou=Engineering)
        :type  o_filter: str
        :param o_group: User group ACI grants access to
        :type  o_group: str
        :param o_memberof: Member of a group
        :type  o_memberof: str
        :param o_permission: Permission ACI grants access to
        :type  o_permission: str
        :param o_permissions: Permissions to grant(read, write, add, delete, all)
        :type  o_permissions: str
        :param o_subtree: Subtree to apply ACI to
        :type  o_subtree: str
        :param o_targetgroup: Group to apply ACI to
        :type  o_targetgroup: str
        :param o_aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type  o_aciprefix: str, valid values ['permission', 'delegation', 'selfservice', 'none']
        :param o_type: type of IPA object (user, group, host, hostgroup, service, netgroup)
        :type  o_type: str, valid values ['user', 'group', 'host', 'service', 'hostgroup', 'netgroup', 'dnsrecord']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_selfaci: Apply ACI to your own entry (self)
        :type  o_selfaci: bool
        """
        method = 'aci_mod'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_filter:
            _params['filter'] = o_filter
        if o_group:
            _params['group'] = o_group
        if o_memberof:
            _params['memberof'] = o_memberof
        if o_permission:
            _params['permission'] = o_permission
        if o_permissions:
            _params['permissions'] = o_permissions
        if o_subtree:
            _params['subtree'] = o_subtree
        if o_targetgroup:
            _params['targetgroup'] = o_targetgroup
        _params['aciprefix'] = o_aciprefix
        if o_type:
            _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_selfaci:
            _params['selfaci'] = o_selfaci

        return self._request(method, _args, _params)

    def aci_rename(
            self,
            a_aciname,
            o_newname,
            o_aciprefix,
            o_attrs=None,
            o_filter=None,
            o_group=None,
            o_memberof=None,
            o_permission=None,
            o_permissions=None,
            o_subtree=None,
            o_targetgroup=None,
            o_type=None,
            o_all=True,
            o_raw=False,
            o_selfaci=False,
    ):
        """
    Rename an ACI.
        :param a_aciname: ACI name
        :type  a_aciname: str
        :param o_attrs: Attributes
        :type  o_attrs: str
        :param o_filter: Legal LDAP filter (e.g. ou=Engineering)
        :type  o_filter: str
        :param o_group: User group ACI grants access to
        :type  o_group: str
        :param o_memberof: Member of a group
        :type  o_memberof: str
        :param o_newname: New ACI name
        :type  o_newname: str
        :param o_permission: Permission ACI grants access to
        :type  o_permission: str
        :param o_permissions: Permissions to grant(read, write, add, delete, all)
        :type  o_permissions: str
        :param o_subtree: Subtree to apply ACI to
        :type  o_subtree: str
        :param o_targetgroup: Group to apply ACI to
        :type  o_targetgroup: str
        :param o_aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type  o_aciprefix: str, valid values ['permission', 'delegation', 'selfservice', 'none']
        :param o_type: type of IPA object (user, group, host, hostgroup, service, netgroup)
        :type  o_type: str, valid values ['user', 'group', 'host', 'service', 'hostgroup', 'netgroup', 'dnsrecord']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_selfaci: Apply ACI to your own entry (self)
        :type  o_selfaci: bool
        """
        method = 'aci_rename'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_filter:
            _params['filter'] = o_filter
        if o_group:
            _params['group'] = o_group
        if o_memberof:
            _params['memberof'] = o_memberof
        _params['newname'] = o_newname
        if o_permission:
            _params['permission'] = o_permission
        if o_permissions:
            _params['permissions'] = o_permissions
        if o_subtree:
            _params['subtree'] = o_subtree
        if o_targetgroup:
            _params['targetgroup'] = o_targetgroup
        _params['aciprefix'] = o_aciprefix
        if o_type:
            _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_selfaci:
            _params['selfaci'] = o_selfaci

        return self._request(method, _args, _params)

    def aci_show(
            self,
            a_aciname,
            o_aciprefix,
            o_location=None,
            o_all=True,
            o_raw=False,
    ):
        """
    Display a single ACI given an ACI name.
        :param a_aciname: ACI name
        :type  a_aciname: str
        :param o_location: Location of the ACI
        :type  o_location: DNParam
        :param o_aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type  o_aciprefix: str, valid values ['permission', 'delegation', 'selfservice', 'none']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'aci_show'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        if o_location:
            _params['location'] = o_location
        _params['aciprefix'] = o_aciprefix
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def adtrust_is_enabled(
            self,
    ):
        """Determine whether ipa-adtrust-install has been run on this system
        """
        method = 'adtrust_is_enabled'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def automember_add(
            self,
            a_cn,
            o_type,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_description=None,
    ):
        """
    Add an automember rule.
        :param a_cn: Automember Rule
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this auto member rule
        :type  o_description: str
        """
        method = 'automember_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automember_add_condition(
            self,
            a_cn,
            o_key,
            o_type,
            o_all=True,
            o_raw=False,
            o_description=None,
            o_automemberexclusiveregex=None,
            o_automemberinclusiveregex=None,
    ):
        """
    Add conditions to an automember rule.
        :param a_cn: Automember Rule
        :type  a_cn: str
        :param o_key: Attribute to filter via regex. For example fqdn for a host, or manager for a user
        :type  o_key: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this auto member rule
        :type  o_description: str
        :param o_automemberexclusiveregex: Exclusive Regex
        :type  o_automemberexclusiveregex: str
        :param o_automemberinclusiveregex: Inclusive Regex
        :type  o_automemberinclusiveregex: str
        """
        method = 'automember_add_condition'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['key'] = o_key
        _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_automemberexclusiveregex:
            _params['automemberexclusiveregex'] = o_automemberexclusiveregex
        if o_automemberinclusiveregex:
            _params['automemberinclusiveregex'] = o_automemberinclusiveregex

        return self._request(method, _args, _params)

    def automember_default_group_remove(
            self,
            o_type,
            o_all=True,
            o_raw=False,
            o_description=None,
    ):
        """
    Remove default (fallback) group for all unmatched entries.
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this auto member rule
        :type  o_description: str
        """
        method = 'automember_default_group_remove'

        _args = list()

        _params = dict()
        _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automember_default_group_set(
            self,
            o_automemberdefaultgroup,
            o_type,
            o_all=True,
            o_raw=False,
            o_description=None,
    ):
        """
    Set default (fallback) group for all unmatched entries.
        :param o_automemberdefaultgroup: Default (fallback) group for entries to land
        :type  o_automemberdefaultgroup: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this auto member rule
        :type  o_description: str
        """
        method = 'automember_default_group_set'

        _args = list()

        _params = dict()
        _params['automemberdefaultgroup'] = o_automemberdefaultgroup
        _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automember_default_group_show(
            self,
            o_type,
            o_all=True,
            o_raw=False,
    ):
        """
    Display information about the default (fallback) automember groups.
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'automember_default_group_show'

        _args = list()

        _params = dict()
        _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def automember_del(
            self,
            a_cn,
            o_type,
    ):
        """
    Delete an automember rule.
        :param a_cn: Automember Rule
        :type  a_cn: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        """
        method = 'automember_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['type'] = o_type

        return self._request(method, _args, _params)

    def automember_find(
            self,
            o_type,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_description=None,
    ):
        """
    Search for automember rules.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("automember-rule")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this auto member rule
        :type  o_description: str
        """
        method = 'automember_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        _params['type'] = o_type
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automember_find_orphans(
            self,
            o_type,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_remove=False,
            o_description=None,
    ):
        """
    Search for orphan automember rules. The command might need to be run as
    a privileged user user to get all orphan rules.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("automember-rule")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_remove: Remove orphan automember rules
        :type  o_remove: bool
        :param o_description: A description of this auto member rule
        :type  o_description: str
        """
        method = 'automember_find_orphans'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        _params['type'] = o_type
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_remove:
            _params['remove'] = o_remove
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automember_mod(
            self,
            a_cn,
            o_type,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """
    Modify an automember rule.
        :param a_cn: Automember Rule
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: A description of this auto member rule
        :type  o_description: str
        """
        method = 'automember_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automember_rebuild(
            self,
            o_hosts=None,
            o_users=None,
            o_type=None,
            o_all=True,
            o_no_wait=False,
            o_raw=False,
    ):
        """Rebuild auto membership.
        :param o_hosts: Rebuild membership for specified hosts
        :type  o_hosts: str
        :param o_users: Rebuild membership for specified users
        :type  o_users: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_wait: Don't wait for rebuilding membership
        :type  o_no_wait: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'automember_rebuild'

        _args = list()

        _params = dict()
        if o_hosts:
            _params['hosts'] = o_hosts
        if o_users:
            _params['users'] = o_users
        if o_type:
            _params['type'] = o_type
        _params['all'] = o_all
        if o_no_wait:
            _params['no_wait'] = o_no_wait
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def automember_remove_condition(
            self,
            a_cn,
            o_key,
            o_type,
            o_all=True,
            o_raw=False,
            o_description=None,
            o_automemberexclusiveregex=None,
            o_automemberinclusiveregex=None,
    ):
        """
    Remove conditions from an automember rule.
        :param a_cn: Automember Rule
        :type  a_cn: str
        :param o_key: Attribute to filter via regex. For example fqdn for a host, or manager for a user
        :type  o_key: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this auto member rule
        :type  o_description: str
        :param o_automemberexclusiveregex: Exclusive Regex
        :type  o_automemberexclusiveregex: str
        :param o_automemberinclusiveregex: Inclusive Regex
        :type  o_automemberinclusiveregex: str
        """
        method = 'automember_remove_condition'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['key'] = o_key
        _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_automemberexclusiveregex:
            _params['automemberexclusiveregex'] = o_automemberexclusiveregex
        if o_automemberinclusiveregex:
            _params['automemberinclusiveregex'] = o_automemberinclusiveregex

        return self._request(method, _args, _params)

    def automember_show(
            self,
            a_cn,
            o_type,
            o_all=True,
            o_raw=False,
    ):
        """
    Display information about an automember rule.
        :param a_cn: Automember Rule
        :type  a_cn: str
        :param o_type: Grouping to which the rule applies
        :type  o_type: str, valid values ['group', 'hostgroup']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'automember_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['type'] = o_type
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def automountkey_add(
            self,
            a_automountmapautomountmapname,
            a_automountlocationcn,
            o_automountinformation,
            o_automountkey,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
    ):
        """Create a new automount key.
        :param a_automountmapautomountmapname: Automount map name.
        :type  a_automountmapautomountmapname: IA5Str
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_automountinformation: Mount information
        :type  o_automountinformation: IA5Str
        :param o_automountkey: Automount key name.
        :type  o_automountkey: IA5Str
        """
        method = 'automountkey_add'

        _args = list()
        _args.append(a_automountmapautomountmapname)
        _args.append(a_automountlocationcn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['automountinformation'] = o_automountinformation
        _params['automountkey'] = o_automountkey

        return self._request(method, _args, _params)

    def automountkey_del(
            self,
            a_automountmapautomountmapname,
            a_automountlocationcn,
            o_automountkey,
            o_automountinformation=None,
            o_continue=False,
    ):
        """Delete an automount key.
        :param a_automountmapautomountmapname: Automount map name.
        :type  a_automountmapautomountmapname: IA5Str
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param o_automountinformation: Mount information
        :type  o_automountinformation: IA5Str
        :param o_automountkey: Automount key name.
        :type  o_automountkey: IA5Str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'automountkey_del'

        _args = list()
        _args.append(a_automountmapautomountmapname)
        _args.append(a_automountlocationcn)

        _params = dict()
        if o_automountinformation:
            _params['automountinformation'] = o_automountinformation
        _params['automountkey'] = o_automountkey
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def automountkey_find(
            self,
            a_automountmapautomountmapname,
            a_automountlocationcn,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_raw=False,
            o_automountinformation=None,
            o_automountkey=None,
    ):
        """Search for an automount key.
        :param a_automountmapautomountmapname: Automount map name.
        :type  a_automountmapautomountmapname: IA5Str
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_automountinformation: Mount information
        :type  o_automountinformation: IA5Str
        :param o_automountkey: Automount key name.
        :type  o_automountkey: IA5Str
        """
        method = 'automountkey_find'

        _args = list()
        _args.append(a_automountmapautomountmapname)
        _args.append(a_automountlocationcn)
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_automountinformation:
            _params['automountinformation'] = o_automountinformation
        if o_automountkey:
            _params['automountkey'] = o_automountkey

        return self._request(method, _args, _params)

    def automountkey_mod(
            self,
            a_automountmapautomountmapname,
            a_automountlocationcn,
            o_automountkey,
            o_newautomountinformation=None,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_automountinformation=None,
    ):
        """Modify an automount key.
        :param a_automountmapautomountmapname: Automount map name.
        :type  a_automountmapautomountmapname: IA5Str
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param o_newautomountinformation: New mount information
        :type  o_newautomountinformation: IA5Str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the automount key object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_automountinformation: Mount information
        :type  o_automountinformation: IA5Str
        :param o_automountkey: Automount key name.
        :type  o_automountkey: IA5Str
        """
        method = 'automountkey_mod'

        _args = list()
        _args.append(a_automountmapautomountmapname)
        _args.append(a_automountlocationcn)

        _params = dict()
        if o_newautomountinformation:
            _params['newautomountinformation'] = o_newautomountinformation
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_automountinformation:
            _params['automountinformation'] = o_automountinformation
        _params['automountkey'] = o_automountkey

        return self._request(method, _args, _params)

    def automountkey_show(
            self,
            a_automountmapautomountmapname,
            a_automountlocationcn,
            o_automountkey,
            o_automountinformation=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display an automount key.
        :param a_automountmapautomountmapname: Automount map name.
        :type  a_automountmapautomountmapname: IA5Str
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param o_automountinformation: Mount information
        :type  o_automountinformation: IA5Str
        :param o_automountkey: Automount key name.
        :type  o_automountkey: IA5Str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'automountkey_show'

        _args = list()
        _args.append(a_automountmapautomountmapname)
        _args.append(a_automountlocationcn)

        _params = dict()
        if o_automountinformation:
            _params['automountinformation'] = o_automountinformation
        _params['automountkey'] = o_automountkey
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def automountlocation_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
    ):
        """Create a new automount location.
        :param a_cn: Automount location name.
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'automountlocation_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def automountlocation_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete an automount location.
        :param a_cn: Automount location name.
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'automountlocation_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def automountlocation_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_cn=None,
    ):
        """Search for an automount location.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("location")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_cn: Automount location name.
        :type  o_cn: str
        """
        method = 'automountlocation_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def automountlocation_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display an automount location.
        :param a_cn: Automount location name.
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'automountlocation_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def automountlocation_tofiles(
            self,
            a_cn,
    ):
        """Generate automount files for a specific location.
        :param a_cn: Automount location name.
        :type  a_cn: str
        """
        method = 'automountlocation_tofiles'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def automountmap_add(
            self,
            a_automountlocationcn,
            a_automountmapname,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_description=None,
    ):
        """Create a new automount map.
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param a_automountmapname: Automount map name.
        :type  a_automountmapname: IA5Str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Description
        :type  o_description: str
        """
        method = 'automountmap_add'

        _args = list()
        _args.append(a_automountlocationcn)
        _args.append(a_automountmapname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automountmap_add_indirect(
            self,
            a_automountlocationcn,
            a_automountmapname,
            o_key,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_parentmap='auto.master',
            o_description=None,
    ):
        """Create a new indirect mount point.
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param a_automountmapname: Automount map name.
        :type  a_automountmapname: IA5Str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_key: Mount point
        :type  o_key: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_parentmap: Name of parent automount map (default: auto.master).
        :type  o_parentmap: str
        :param o_description: Description
        :type  o_description: str
        """
        method = 'automountmap_add_indirect'

        _args = list()
        _args.append(a_automountlocationcn)
        _args.append(a_automountmapname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        _params['key'] = o_key
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_parentmap:
            _params['parentmap'] = o_parentmap
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automountmap_del(
            self,
            a_automountlocationcn,
            a_automountmapname,
            o_continue=False,
    ):
        """Delete an automount map.
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param a_automountmapname: Automount map name.
        :type  a_automountmapname: IA5Str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'automountmap_del'

        _args = list()
        _args.append(a_automountlocationcn)
        _args.append(a_automountmapname)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def automountmap_find(
            self,
            a_automountlocationcn,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_automountmapname=None,
            o_description=None,
    ):
        """Search for an automount map.
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("map")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_automountmapname: Automount map name.
        :type  o_automountmapname: IA5Str
        :param o_description: Description
        :type  o_description: str
        """
        method = 'automountmap_find'

        _args = list()
        _args.append(a_automountlocationcn)
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_automountmapname:
            _params['automountmapname'] = o_automountmapname
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automountmap_mod(
            self,
            a_automountlocationcn,
            a_automountmapname,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify an automount map.
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param a_automountmapname: Automount map name.
        :type  a_automountmapname: IA5Str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: Description
        :type  o_description: str
        """
        method = 'automountmap_mod'

        _args = list()
        _args.append(a_automountlocationcn)
        _args.append(a_automountmapname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def automountmap_show(
            self,
            a_automountlocationcn,
            a_automountmapname,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display an automount map.
        :param a_automountlocationcn: Automount location name.
        :type  a_automountlocationcn: str
        :param a_automountmapname: Automount map name.
        :type  a_automountmapname: IA5Str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'automountmap_show'

        _args = list()
        _args.append(a_automountlocationcn)
        _args.append(a_automountmapname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def batch(
            self,
            a_methods=None,
    ):
        """None
        :param a_methods: Nested Methods to execute
        :type  a_methods: dict
        """
        method = 'batch'

        _args = list()
        _args.append(a_methods)

        _params = dict()

        return self._request(method, _args, _params)

    def ca_add(
            self,
            a_cn,
            o_ipacasubjectdn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_chain=False,
            o_raw=False,
            o_description=None,
    ):
        """Create a CA.
        :param a_cn: Name for referencing the CA
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_chain: Include certificate chain in output
        :type  o_chain: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipacasubjectdn: Subject Distinguished Name
        :type  o_ipacasubjectdn: DNParam
        :param o_description: Description of the purpose of the CA
        :type  o_description: str
        """
        method = 'ca_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['chain'] = o_chain
        _params['raw'] = o_raw
        _params['ipacasubjectdn'] = o_ipacasubjectdn
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def ca_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a CA.
        :param a_cn: Name for referencing the CA
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'ca_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def ca_disable(
            self,
            a_cn,
    ):
        """Disable a CA.
        :param a_cn: Name for referencing the CA
        :type  a_cn: str
        """
        method = 'ca_disable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def ca_enable(
            self,
            a_cn,
    ):
        """Enable a CA.
        :param a_cn: Name for referencing the CA
        :type  a_cn: str
        """
        method = 'ca_enable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def ca_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipacaissuerdn=None,
            o_ipacasubjectdn=None,
            o_description=None,
            o_ipacaid=None,
            o_cn=None,
    ):
        """Search for CAs.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipacaissuerdn: Issuer Distinguished Name
        :type  o_ipacaissuerdn: DNParam
        :param o_ipacasubjectdn: Subject Distinguished Name
        :type  o_ipacasubjectdn: DNParam
        :param o_description: Description of the purpose of the CA
        :type  o_description: str
        :param o_ipacaid: Dogtag Authority ID
        :type  o_ipacaid: str
        :param o_cn: Name for referencing the CA
        :type  o_cn: str
        """
        method = 'ca_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipacaissuerdn:
            _params['ipacaissuerdn'] = o_ipacaissuerdn
        if o_ipacasubjectdn:
            _params['ipacasubjectdn'] = o_ipacasubjectdn
        if o_description:
            _params['description'] = o_description
        if o_ipacaid:
            _params['ipacaid'] = o_ipacaid
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def ca_is_enabled(
            self,
    ):
        """
    Checks if any of the servers has the CA service enabled.
        """
        method = 'ca_is_enabled'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def ca_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify CA configuration.
        :param a_cn: Name for referencing the CA
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the Certificate Authority object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: Description of the purpose of the CA
        :type  o_description: str
        """
        method = 'ca_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def ca_show(
            self,
            a_cn,
            o_all=True,
            o_chain=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display the properties of a CA.
        :param a_cn: Name for referencing the CA
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_chain: Include certificate chain in output
        :type  o_chain: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'ca_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['chain'] = o_chain
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def caacl_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_ipacacategory=None,
            o_hostcategory=None,
            o_ipacertprofilecategory=None,
            o_servicecategory=None,
            o_usercategory=None,
    ):
        """Create a new CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_ipacacategory: CA category the ACL applies to
        :type  o_ipacacategory: str, valid values ['all']
        :param o_hostcategory: Host category the ACL applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_ipacertprofilecategory: Profile category the ACL applies to
        :type  o_ipacertprofilecategory: str, valid values ['all']
        :param o_servicecategory: Service category the ACL applies to
        :type  o_servicecategory: str, valid values ['all']
        :param o_usercategory: User category the ACL applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'caacl_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_ipacacategory:
            _params['ipacacategory'] = o_ipacacategory
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_ipacertprofilecategory:
            _params['ipacertprofilecategory'] = o_ipacertprofilecategory
        if o_servicecategory:
            _params['servicecategory'] = o_servicecategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def caacl_add_ca(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_ca=None,
    ):
        """Add CAs to a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ca: Certificate Authorities to add
        :type  o_ca: str
        """
        method = 'caacl_add_ca'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_ca:
            _params['ca'] = o_ca

        return self._request(method, _args, _params)

    def caacl_add_host(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Add target hosts and hostgroups to a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        """
        method = 'caacl_add_host'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def caacl_add_profile(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_certprofile=None,
    ):
        """Add profiles to a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_certprofile: Certificate Profiles to add
        :type  o_certprofile: str
        """
        method = 'caacl_add_profile'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_certprofile:
            _params['certprofile'] = o_certprofile

        return self._request(method, _args, _params)

    def caacl_add_service(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_service=None,
    ):
        """Add services to a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_service: services to add
        :type  o_service: str
        """
        method = 'caacl_add_service'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_service:
            _params['service'] = o_service

        return self._request(method, _args, _params)

    def caacl_add_user(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Add users and groups to a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'caacl_add_user'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def caacl_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'caacl_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def caacl_disable(
            self,
            a_cn,
    ):
        """Disable a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        """
        method = 'caacl_disable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def caacl_enable(
            self,
            a_cn,
    ):
        """Enable a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        """
        method = 'caacl_enable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def caacl_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_cn=None,
            o_ipacacategory=None,
            o_hostcategory=None,
            o_ipacertprofilecategory=None,
            o_servicecategory=None,
            o_usercategory=None,
    ):
        """Search for CA ACLs.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_cn: ACL name
        :type  o_cn: str
        :param o_ipacacategory: CA category the ACL applies to
        :type  o_ipacacategory: str, valid values ['all']
        :param o_hostcategory: Host category the ACL applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_ipacertprofilecategory: Profile category the ACL applies to
        :type  o_ipacertprofilecategory: str, valid values ['all']
        :param o_servicecategory: Service category the ACL applies to
        :type  o_servicecategory: str, valid values ['all']
        :param o_usercategory: User category the ACL applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'caacl_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn
        if o_ipacacategory:
            _params['ipacacategory'] = o_ipacacategory
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_ipacertprofilecategory:
            _params['ipacertprofilecategory'] = o_ipacertprofilecategory
        if o_servicecategory:
            _params['servicecategory'] = o_servicecategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def caacl_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_ipacacategory=None,
            o_hostcategory=None,
            o_ipacertprofilecategory=None,
            o_servicecategory=None,
            o_usercategory=None,
    ):
        """Modify a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_ipacacategory: CA category the ACL applies to
        :type  o_ipacacategory: str, valid values ['all']
        :param o_hostcategory: Host category the ACL applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_ipacertprofilecategory: Profile category the ACL applies to
        :type  o_ipacertprofilecategory: str, valid values ['all']
        :param o_servicecategory: Service category the ACL applies to
        :type  o_servicecategory: str, valid values ['all']
        :param o_usercategory: User category the ACL applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'caacl_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_ipacacategory:
            _params['ipacacategory'] = o_ipacacategory
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_ipacertprofilecategory:
            _params['ipacertprofilecategory'] = o_ipacertprofilecategory
        if o_servicecategory:
            _params['servicecategory'] = o_servicecategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def caacl_remove_ca(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_ca=None,
    ):
        """Remove CAs from a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ca: Certificate Authorities to remove
        :type  o_ca: str
        """
        method = 'caacl_remove_ca'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_ca:
            _params['ca'] = o_ca

        return self._request(method, _args, _params)

    def caacl_remove_host(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Remove target hosts and hostgroups from a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        """
        method = 'caacl_remove_host'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def caacl_remove_profile(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_certprofile=None,
    ):
        """Remove profiles from a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_certprofile: Certificate Profiles to remove
        :type  o_certprofile: str
        """
        method = 'caacl_remove_profile'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_certprofile:
            _params['certprofile'] = o_certprofile

        return self._request(method, _args, _params)

    def caacl_remove_service(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_service=None,
    ):
        """Remove services from a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_service: services to remove
        :type  o_service: str
        """
        method = 'caacl_remove_service'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_service:
            _params['service'] = o_service

        return self._request(method, _args, _params)

    def caacl_remove_user(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Remove users and groups from a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'caacl_remove_user'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def caacl_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display the properties of a CA ACL.
        :param a_cn: ACL name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'caacl_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def cert_find(
            self,
            a_criteria=None,
            o_issuedon_from=None,
            o_issuedon_to=None,
            o_revokedon_from=None,
            o_revokedon_to=None,
            o_validnotafter_from=None,
            o_validnotafter_to=None,
            o_validnotbefore_from=None,
            o_validnotbefore_to=None,
            o_max_serial_number=None,
            o_min_serial_number=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_no_service=None,
            o_service=None,
            o_cacn=None,
            o_host=None,
            o_no_host=None,
            o_no_user=None,
            o_subject=None,
            o_user=None,
            o_all=True,
            o_exactly=False,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_certificate=None,
            o_issuer=None,
            o_revocation_reason=None,
    ):
        """Search for existing certificates.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_issuedon_from: Issued on from this date (YYYY-mm-dd)
        :type  o_issuedon_from: DateTime
        :param o_issuedon_to: Issued on to this date (YYYY-mm-dd)
        :type  o_issuedon_to: DateTime
        :param o_revokedon_from: Revoked on from this date (YYYY-mm-dd)
        :type  o_revokedon_from: DateTime
        :param o_revokedon_to: Revoked on to this date (YYYY-mm-dd)
        :type  o_revokedon_to: DateTime
        :param o_validnotafter_from: Valid not after from this date (YYYY-mm-dd)
        :type  o_validnotafter_from: DateTime
        :param o_validnotafter_to: Valid not after to this date (YYYY-mm-dd)
        :type  o_validnotafter_to: DateTime
        :param o_validnotbefore_from: Valid not before from this date (YYYY-mm-dd)
        :type  o_validnotbefore_from: DateTime
        :param o_validnotbefore_to: Valid not before to this date (YYYY-mm-dd)
        :type  o_validnotbefore_to: DateTime
        :param o_max_serial_number: maximum serial number
        :type  o_max_serial_number: int, min value 0, max value 2147483647
        :param o_min_serial_number: minimum serial number
        :type  o_min_serial_number: int, min value 0, max value 2147483647
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_no_service: Search for certificates without these owner services.
        :type  o_no_service: Principal
        :param o_service: Search for certificates with these owner services.
        :type  o_service: Principal
        :param o_cacn: Name of issuing CA
        :type  o_cacn: str
        :param o_host: Search for certificates with these owner hosts.
        :type  o_host: str
        :param o_no_host: Search for certificates without these owner hosts.
        :type  o_no_host: str
        :param o_no_user: Search for certificates without these owner users.
        :type  o_no_user: str
        :param o_subject: Subject
        :type  o_subject: str
        :param o_user: Search for certificates with these owner users.
        :type  o_user: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_exactly: match the common name exactly
        :type  o_exactly: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("certificate")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_certificate: Base-64 encoded certificate.
        :type  o_certificate: Certificate
        :param o_issuer: Issuer DN
        :type  o_issuer: DNParam
        :param o_revocation_reason: Reason for revoking the certificate (0-10). Type "ipa help cert" for revocation reason details.
        :type  o_revocation_reason: int, min value 0, max value 10
        """
        method = 'cert_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_issuedon_from:
            _params['issuedon_from'] = o_issuedon_from
        if o_issuedon_to:
            _params['issuedon_to'] = o_issuedon_to
        if o_revokedon_from:
            _params['revokedon_from'] = o_revokedon_from
        if o_revokedon_to:
            _params['revokedon_to'] = o_revokedon_to
        if o_validnotafter_from:
            _params['validnotafter_from'] = o_validnotafter_from
        if o_validnotafter_to:
            _params['validnotafter_to'] = o_validnotafter_to
        if o_validnotbefore_from:
            _params['validnotbefore_from'] = o_validnotbefore_from
        if o_validnotbefore_to:
            _params['validnotbefore_to'] = o_validnotbefore_to
        if o_max_serial_number:
            _params['max_serial_number'] = o_max_serial_number
        if o_min_serial_number:
            _params['min_serial_number'] = o_min_serial_number
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_no_service:
            _params['no_service'] = o_no_service
        if o_service:
            _params['service'] = o_service
        if o_cacn:
            _params['cacn'] = o_cacn
        if o_host:
            _params['host'] = o_host
        if o_no_host:
            _params['no_host'] = o_no_host
        if o_no_user:
            _params['no_user'] = o_no_user
        if o_subject:
            _params['subject'] = o_subject
        if o_user:
            _params['user'] = o_user
        _params['all'] = o_all
        if o_exactly:
            _params['exactly'] = o_exactly
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_certificate:
            _params['certificate'] = o_certificate
        if o_issuer:
            _params['issuer'] = o_issuer
        if o_revocation_reason:
            _params['revocation_reason'] = o_revocation_reason

        return self._request(method, _args, _params)

    def cert_remove_hold(
            self,
            a_serial_number,
            o_cacn='ipa',
    ):
        """Take a revoked certificate off hold.
        :param a_serial_number: Serial number in decimal or if prefixed with 0x in hexadecimal
        :type  a_serial_number: int, min value -2147483648, max value 2147483647
        :param o_cacn: Name of issuing CA
        :type  o_cacn: str
        """
        method = 'cert_remove_hold'

        _args = list()
        _args.append(a_serial_number)

        _params = dict()
        if o_cacn:
            _params['cacn'] = o_cacn

        return self._request(method, _args, _params)

    def cert_request(
            self,
            a_csr,
            o_principal,
            o_add=False,
            o_all=True,
            o_chain=False,
            o_raw=False,
            o_cacn='ipa',
            o_profile_id=None,
            o_request_type='pkcs10',
    ):
        """Submit a certificate signing request.
        :param a_csr: CSR
        :type  a_csr: CertificateSigningRequest
        :param o_principal: Principal for this certificate (e.g. HTTP/test.example.com)
        :type  o_principal: Principal
        :param o_add: automatically add the principal if it doesn't exist (service principals only)
        :type  o_add: bool
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_chain: Include certificate chain in output
        :type  o_chain: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_cacn: Name of issuing CA
        :type  o_cacn: str
        :param o_profile_id: Certificate Profile to use
        :type  o_profile_id: str
        :param o_request_type: <request_type>
        :type  o_request_type: str
        """
        method = 'cert_request'

        _args = list()
        _args.append(a_csr)

        _params = dict()
        _params['principal'] = o_principal
        _params['add'] = o_add
        _params['all'] = o_all
        _params['chain'] = o_chain
        _params['raw'] = o_raw
        if o_cacn:
            _params['cacn'] = o_cacn
        if o_profile_id:
            _params['profile_id'] = o_profile_id
        _params['request_type'] = o_request_type

        return self._request(method, _args, _params)

    def cert_revoke(
            self,
            a_serial_number,
            o_revocation_reason=0,
            o_cacn='ipa',
    ):
        """Revoke a certificate.
        :param a_serial_number: Serial number in decimal or if prefixed with 0x in hexadecimal
        :type  a_serial_number: int, min value -2147483648, max value 2147483647
        :param o_revocation_reason: Reason for revoking the certificate (0-10). Type "ipa help cert" for revocation reason details.
        :type  o_revocation_reason: int, min value 0, max value 10
        :param o_cacn: Name of issuing CA
        :type  o_cacn: str
        """
        method = 'cert_revoke'

        _args = list()
        _args.append(a_serial_number)

        _params = dict()
        _params['revocation_reason'] = o_revocation_reason
        if o_cacn:
            _params['cacn'] = o_cacn

        return self._request(method, _args, _params)

    def cert_show(
            self,
            a_serial_number,
            o_out=None,
            o_all=True,
            o_chain=False,
            o_no_members=False,
            o_raw=False,
            o_cacn='ipa',
    ):
        """Retrieve an existing certificate.
        :param a_serial_number: Serial number in decimal or if prefixed with 0x in hexadecimal
        :type  a_serial_number: int, min value -2147483648, max value 2147483647
        :param o_out: File to store the certificate in.
        :type  o_out: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_chain: Include certificate chain in output
        :type  o_chain: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_cacn: Name of issuing CA
        :type  o_cacn: str
        """
        method = 'cert_show'

        _args = list()
        _args.append(a_serial_number)

        _params = dict()
        if o_out:
            _params['out'] = o_out
        _params['all'] = o_all
        _params['chain'] = o_chain
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_cacn:
            _params['cacn'] = o_cacn

        return self._request(method, _args, _params)

    def cert_status(
            self,
            a_request_id,
            o_all=True,
            o_raw=False,
            o_cacn='ipa',
    ):
        """Check the status of a certificate signing request.
        :param a_request_id: Request id
        :type  a_request_id: int, min value -2147483648, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_cacn: Name of issuing CA
        :type  o_cacn: str
        """
        method = 'cert_status'

        _args = list()
        _args.append(a_request_id)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_cacn:
            _params['cacn'] = o_cacn

        return self._request(method, _args, _params)

    def certmap_match(
            self,
            a_certificate,
            o_all=True,
            o_raw=False,
    ):
        """
    Search for users matching the provided certificate.

    This command relies on SSSD to retrieve the list of matching users and
    may return cached data. For more information on purging SSSD cache,
    please refer to sss_cache documentation.
        :param a_certificate: Base-64 encoded user certificate
        :type  a_certificate: Certificate
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'certmap_match'

        _args = list()
        _args.append(a_certificate)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def certmapconfig_mod(
            self,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_ipacertmappromptusername=None,
    ):
        """Modify Certificate Identity Mapping configuration.
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipacertmappromptusername: Prompt for the username when multiple identities are mapped to a certificate
        :type  o_ipacertmappromptusername: Bool
        """
        method = 'certmapconfig_mod'

        _args = list()

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipacertmappromptusername:
            _params['ipacertmappromptusername'] = o_ipacertmappromptusername

        return self._request(method, _args, _params)

    def certmapconfig_show(
            self,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Show the current Certificate Identity Mapping configuration.
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'certmapconfig_show'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def certmaprule_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_associateddomain=None,
            o_ipacertmappriority=None,
            o_description=None,
            o_ipacertmapmaprule=None,
            o_ipacertmapmatchrule=None,
            o_ipaenabledflag=True,
    ):
        """Create a new Certificate Identity Mapping Rule.
        :param a_cn: Certificate Identity Mapping Rule name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_associateddomain: Domain where the user entry will be searched
        :type  o_associateddomain: DNSNameParam
        :param o_ipacertmappriority: Priority of the rule (higher number means lower priority
        :type  o_ipacertmappriority: int, min value 0, max value 2147483647
        :param o_description: Certificate Identity Mapping Rule description
        :type  o_description: str
        :param o_ipacertmapmaprule: Rule used to map the certificate with a user entry
        :type  o_ipacertmapmaprule: str
        :param o_ipacertmapmatchrule: Rule used to check if a certificate can be used for authentication
        :type  o_ipacertmapmatchrule: str
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: bool
        """
        method = 'certmaprule_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_associateddomain:
            _params['associateddomain'] = o_associateddomain
        if o_ipacertmappriority:
            _params['ipacertmappriority'] = o_ipacertmappriority
        if o_description:
            _params['description'] = o_description
        if o_ipacertmapmaprule:
            _params['ipacertmapmaprule'] = o_ipacertmapmaprule
        if o_ipacertmapmatchrule:
            _params['ipacertmapmatchrule'] = o_ipacertmapmatchrule
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag

        return self._request(method, _args, _params)

    def certmaprule_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a Certificate Identity Mapping Rule.
        :param a_cn: Certificate Identity Mapping Rule name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'certmaprule_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def certmaprule_disable(
            self,
            a_cn,
    ):
        """Disable a Certificate Identity Mapping Rule.
        :param a_cn: Certificate Identity Mapping Rule name
        :type  a_cn: str
        """
        method = 'certmaprule_disable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def certmaprule_enable(
            self,
            a_cn,
    ):
        """Enable a Certificate Identity Mapping Rule.
        :param a_cn: Certificate Identity Mapping Rule name
        :type  a_cn: str
        """
        method = 'certmaprule_enable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def certmaprule_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipaenabledflag=True,
            o_associateddomain=None,
            o_ipacertmappriority=None,
            o_description=None,
            o_ipacertmapmaprule=None,
            o_ipacertmapmatchrule=None,
            o_cn=None,
    ):
        """Search for Certificate Identity Mapping Rules.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("rulename")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_associateddomain: Domain where the user entry will be searched
        :type  o_associateddomain: DNSNameParam
        :param o_ipacertmappriority: Priority of the rule (higher number means lower priority
        :type  o_ipacertmappriority: int, min value 0, max value 2147483647
        :param o_description: Certificate Identity Mapping Rule description
        :type  o_description: str
        :param o_ipacertmapmaprule: Rule used to map the certificate with a user entry
        :type  o_ipacertmapmaprule: str
        :param o_ipacertmapmatchrule: Rule used to check if a certificate can be used for authentication
        :type  o_ipacertmapmatchrule: str
        :param o_cn: Certificate Identity Mapping Rule name
        :type  o_cn: str
        """
        method = 'certmaprule_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_associateddomain:
            _params['associateddomain'] = o_associateddomain
        if o_ipacertmappriority:
            _params['ipacertmappriority'] = o_ipacertmappriority
        if o_description:
            _params['description'] = o_description
        if o_ipacertmapmaprule:
            _params['ipacertmapmaprule'] = o_ipacertmapmaprule
        if o_ipacertmapmatchrule:
            _params['ipacertmapmatchrule'] = o_ipacertmapmatchrule
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def certmaprule_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_associateddomain=None,
            o_ipacertmappriority=None,
            o_description=None,
            o_ipacertmapmaprule=None,
            o_ipacertmapmatchrule=None,
            o_ipaenabledflag=True,
    ):
        """Modify a Certificate Identity Mapping Rule.
        :param a_cn: Certificate Identity Mapping Rule name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_associateddomain: Domain where the user entry will be searched
        :type  o_associateddomain: DNSNameParam
        :param o_ipacertmappriority: Priority of the rule (higher number means lower priority
        :type  o_ipacertmappriority: int, min value 0, max value 2147483647
        :param o_description: Certificate Identity Mapping Rule description
        :type  o_description: str
        :param o_ipacertmapmaprule: Rule used to map the certificate with a user entry
        :type  o_ipacertmapmaprule: str
        :param o_ipacertmapmatchrule: Rule used to check if a certificate can be used for authentication
        :type  o_ipacertmapmatchrule: str
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: bool
        """
        method = 'certmaprule_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_associateddomain:
            _params['associateddomain'] = o_associateddomain
        if o_ipacertmappriority:
            _params['ipacertmappriority'] = o_ipacertmappriority
        if o_description:
            _params['description'] = o_description
        if o_ipacertmapmaprule:
            _params['ipacertmapmaprule'] = o_ipacertmapmaprule
        if o_ipacertmapmatchrule:
            _params['ipacertmapmatchrule'] = o_ipacertmapmatchrule
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag

        return self._request(method, _args, _params)

    def certmaprule_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a Certificate Identity Mapping Rule.
        :param a_cn: Certificate Identity Mapping Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'certmaprule_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def certprofile_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a Certificate Profile.
        :param a_cn: Profile ID for referring to this profile
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'certprofile_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def certprofile_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipacertprofilestoreissued=True,
            o_description=None,
            o_cn=None,
    ):
        """Search for Certificate Profiles.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("id")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipacertprofilestoreissued: Whether to store certs issued using this profile
        :type  o_ipacertprofilestoreissued: Bool
        :param o_description: Brief description of this profile
        :type  o_description: str
        :param o_cn: Profile ID for referring to this profile
        :type  o_cn: str
        """
        method = 'certprofile_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipacertprofilestoreissued:
            _params['ipacertprofilestoreissued'] = o_ipacertprofilestoreissued
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def certprofile_import(
            self,
            a_cn,
            o_file,
            o_description,
            o_all=True,
            o_raw=False,
            o_ipacertprofilestoreissued=True,
    ):
        """Import a Certificate Profile.
        :param a_cn: Profile ID for referring to this profile
        :type  a_cn: str
        :param o_file: Filename of a raw profile. The XML format is not supported.
        :type  o_file: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipacertprofilestoreissued: Whether to store certs issued using this profile
        :type  o_ipacertprofilestoreissued: Bool
        :param o_description: Brief description of this profile
        :type  o_description: str
        """
        method = 'certprofile_import'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['file'] = o_file
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['ipacertprofilestoreissued'] = o_ipacertprofilestoreissued
        _params['description'] = o_description

        return self._request(method, _args, _params)

    def certprofile_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_file=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_ipacertprofilestoreissued=True,
            o_description=None,
    ):
        """Modify Certificate Profile configuration.
        :param a_cn: Profile ID for referring to this profile
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_file: File containing profile configuration
        :type  o_file: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipacertprofilestoreissued: Whether to store certs issued using this profile
        :type  o_ipacertprofilestoreissued: Bool
        :param o_description: Brief description of this profile
        :type  o_description: str
        """
        method = 'certprofile_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_file:
            _params['file'] = o_file
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipacertprofilestoreissued:
            _params['ipacertprofilestoreissued'] = o_ipacertprofilestoreissued
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def certprofile_show(
            self,
            a_cn,
            o_out=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display the properties of a Certificate Profile.
        :param a_cn: Profile ID for referring to this profile
        :type  a_cn: str
        :param o_out: Write profile configuration to file
        :type  o_out: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'certprofile_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_out:
            _params['out'] = o_out
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def class_find(
            self,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
    ):
        """Search for classes.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'class_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def class_show(
            self,
            a_full_name,
            o_all=True,
            o_raw=False,
    ):
        """Display information about a class.
        :param a_full_name: Full name
        :type  a_full_name: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'class_show'

        _args = list()
        _args.append(a_full_name)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def command_defaults(
            self,
            a_full_name,
            o_kw=None,
            o_params=None,
    ):
        """None
        :param a_full_name: Full name
        :type  a_full_name: str
        :param o_kw: <kw>
        :type  o_kw: dict
        :param o_params: <params>
        :type  o_params: str
        """
        method = 'command_defaults'

        _args = list()
        _args.append(a_full_name)

        _params = dict()
        if o_kw:
            _params['kw'] = o_kw
        if o_params:
            _params['params'] = o_params

        return self._request(method, _args, _params)

    def command_find(
            self,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
    ):
        """Search for commands.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'command_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def command_show(
            self,
            a_full_name,
            o_all=True,
            o_raw=False,
    ):
        """Display information about a command.
        :param a_full_name: Full name
        :type  a_full_name: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'command_show'

        _args = list()
        _args.append(a_full_name)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def compat_is_enabled(
            self,
    ):
        """Determine whether Schema Compatibility plugin is configured to serve trusted domain users and groups
        """
        method = 'compat_is_enabled'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def config_mod(
            self,
            o_addattr=None,
            o_ca_renewal_master_server=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_ipamigrationenabled=None,
            o_ipagroupsearchfields=None,
            o_ipahomesrootdir=None,
            o_ipausersearchfields=None,
            o_ipamaxusernamelength=None,
            o_ipapwdexpadvnotify=None,
            o_ipasearchrecordslimit=None,
            o_ipasearchtimelimit=None,
            o_ipadefaultprimarygroup=None,
            o_ipadefaultloginshell=None,
            o_ipadomainresolutionorder=None,
            o_ipadefaultemaildomain=None,
            o_ipagroupobjectclasses=None,
            o_ipaselinuxusermapdefault=None,
            o_ipaselinuxusermaporder=None,
            o_ipauserobjectclasses=None,
            o_ipaconfigstring=None,
            o_ipakrbauthzdata=None,
            o_ipauserauthtype=None,
    ):
        """Modify configuration options.
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_ca_renewal_master_server: Renewal master for IPA certificate authority
        :type  o_ca_renewal_master_server: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipamigrationenabled: Enable migration mode
        :type  o_ipamigrationenabled: Bool
        :param o_ipagroupsearchfields: A comma-separated list of fields to search in when searching for groups
        :type  o_ipagroupsearchfields: IA5Str
        :param o_ipahomesrootdir: Default location of home directories
        :type  o_ipahomesrootdir: IA5Str
        :param o_ipausersearchfields: A comma-separated list of fields to search in when searching for users
        :type  o_ipausersearchfields: IA5Str
        :param o_ipamaxusernamelength: Maximum username length
        :type  o_ipamaxusernamelength: int, min value 1, max value 255
        :param o_ipapwdexpadvnotify: Number of days's notice of impending password expiration
        :type  o_ipapwdexpadvnotify: int, min value 0, max value 2147483647
        :param o_ipasearchrecordslimit: Maximum number of records to search (-1 or 0 is unlimited)
        :type  o_ipasearchrecordslimit: int, min value -2147483648, max value 2147483647
        :param o_ipasearchtimelimit: Maximum amount of time (seconds) for a search (-1 or 0 is unlimited)
        :type  o_ipasearchtimelimit: int, min value -1, max value 2147483647
        :param o_ipadefaultprimarygroup: Default group for new users
        :type  o_ipadefaultprimarygroup: str
        :param o_ipadefaultloginshell: Default shell for new users
        :type  o_ipadefaultloginshell: str
        :param o_ipadomainresolutionorder: colon-separated list of domains used for short name qualification
        :type  o_ipadomainresolutionorder: str
        :param o_ipadefaultemaildomain: Default e-mail domain
        :type  o_ipadefaultemaildomain: str
        :param o_ipagroupobjectclasses: Default group objectclasses (comma-separated list)
        :type  o_ipagroupobjectclasses: str
        :param o_ipaselinuxusermapdefault: Default SELinux user when no match is found in SELinux map rule
        :type  o_ipaselinuxusermapdefault: str
        :param o_ipaselinuxusermaporder: Order in increasing priority of SELinux users, delimited by $
        :type  o_ipaselinuxusermaporder: str
        :param o_ipauserobjectclasses: Default user objectclasses (comma-separated list)
        :type  o_ipauserobjectclasses: str
        :param o_ipaconfigstring: Extra hashes to generate in password plug-in
        :type  o_ipaconfigstring: str, valid values ['AllowNThash', 'KDC:Disable Last Success', 'KDC:Disable Lockout', 'KDC:Disable Default Preauth for SPNs']
        :param o_ipakrbauthzdata: Default types of PAC supported for services
        :type  o_ipakrbauthzdata: str, valid values ['MS-PAC', 'PAD', 'nfs:NONE']
        :param o_ipauserauthtype: Default types of supported user authentication
        :type  o_ipauserauthtype: str, valid values ['password', 'radius', 'otp', 'disabled']
        """
        method = 'config_mod'

        _args = list()

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_ca_renewal_master_server:
            _params['ca_renewal_master_server'] = o_ca_renewal_master_server
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipamigrationenabled:
            _params['ipamigrationenabled'] = o_ipamigrationenabled
        if o_ipagroupsearchfields:
            _params['ipagroupsearchfields'] = o_ipagroupsearchfields
        if o_ipahomesrootdir:
            _params['ipahomesrootdir'] = o_ipahomesrootdir
        if o_ipausersearchfields:
            _params['ipausersearchfields'] = o_ipausersearchfields
        if o_ipamaxusernamelength:
            _params['ipamaxusernamelength'] = o_ipamaxusernamelength
        if o_ipapwdexpadvnotify:
            _params['ipapwdexpadvnotify'] = o_ipapwdexpadvnotify
        if o_ipasearchrecordslimit:
            _params['ipasearchrecordslimit'] = o_ipasearchrecordslimit
        if o_ipasearchtimelimit:
            _params['ipasearchtimelimit'] = o_ipasearchtimelimit
        if o_ipadefaultprimarygroup:
            _params['ipadefaultprimarygroup'] = o_ipadefaultprimarygroup
        if o_ipadefaultloginshell:
            _params['ipadefaultloginshell'] = o_ipadefaultloginshell
        if o_ipadomainresolutionorder:
            _params['ipadomainresolutionorder'] = o_ipadomainresolutionorder
        if o_ipadefaultemaildomain:
            _params['ipadefaultemaildomain'] = o_ipadefaultemaildomain
        if o_ipagroupobjectclasses:
            _params['ipagroupobjectclasses'] = o_ipagroupobjectclasses
        if o_ipaselinuxusermapdefault:
            _params['ipaselinuxusermapdefault'] = o_ipaselinuxusermapdefault
        if o_ipaselinuxusermaporder:
            _params['ipaselinuxusermaporder'] = o_ipaselinuxusermaporder
        if o_ipauserobjectclasses:
            _params['ipauserobjectclasses'] = o_ipauserobjectclasses
        if o_ipaconfigstring:
            _params['ipaconfigstring'] = o_ipaconfigstring
        if o_ipakrbauthzdata:
            _params['ipakrbauthzdata'] = o_ipakrbauthzdata
        if o_ipauserauthtype:
            _params['ipauserauthtype'] = o_ipauserauthtype

        return self._request(method, _args, _params)

    def config_show(
            self,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Show the current configuration.
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'config_show'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def cosentry_add(
            self,
            a_cn,
            o_krbpwdpolicyreference,
            o_cospriority,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
    ):
        """None
        :param a_cn: <cn>
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_krbpwdpolicyreference: <krbpwdpolicyreference>
        :type  o_krbpwdpolicyreference: DNParam
        :param o_cospriority: <cospriority>
        :type  o_cospriority: int, min value 0, max value 2147483647
        """
        method = 'cosentry_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['krbpwdpolicyreference'] = o_krbpwdpolicyreference
        _params['cospriority'] = o_cospriority

        return self._request(method, _args, _params)

    def cosentry_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """None
        :param a_cn: <cn>
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'cosentry_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def cosentry_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_krbpwdpolicyreference=None,
            o_cospriority=None,
            o_cn=None,
    ):
        """None
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("cn")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_krbpwdpolicyreference: <krbpwdpolicyreference>
        :type  o_krbpwdpolicyreference: DNParam
        :param o_cospriority: <cospriority>
        :type  o_cospriority: int, min value 0, max value 2147483647
        :param o_cn: <cn>
        :type  o_cn: str
        """
        method = 'cosentry_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_krbpwdpolicyreference:
            _params['krbpwdpolicyreference'] = o_krbpwdpolicyreference
        if o_cospriority:
            _params['cospriority'] = o_cospriority
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def cosentry_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_krbpwdpolicyreference=None,
            o_cospriority=None,
    ):
        """None
        :param a_cn: <cn>
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_krbpwdpolicyreference: <krbpwdpolicyreference>
        :type  o_krbpwdpolicyreference: DNParam
        :param o_cospriority: <cospriority>
        :type  o_cospriority: int, min value 0, max value 2147483647
        """
        method = 'cosentry_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_krbpwdpolicyreference:
            _params['krbpwdpolicyreference'] = o_krbpwdpolicyreference
        if o_cospriority:
            _params['cospriority'] = o_cospriority

        return self._request(method, _args, _params)

    def cosentry_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """None
        :param a_cn: <cn>
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'cosentry_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def delegation_add(
            self,
            a_aciname,
            o_attrs,
            o_group,
            o_memberof,
            o_all=True,
            o_raw=False,
            o_permissions=None,
    ):
        """Add a new delegation.
        :param a_aciname: Delegation name
        :type  a_aciname: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_attrs: Attributes to which the delegation applies
        :type  o_attrs: str
        :param o_group: User group ACI grants access to
        :type  o_group: str
        :param o_memberof: User group to apply delegation to
        :type  o_memberof: str
        :param o_permissions: Permissions to grant (read, write). Default is write.
        :type  o_permissions: str
        """
        method = 'delegation_add'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['attrs'] = o_attrs
        _params['group'] = o_group
        _params['memberof'] = o_memberof
        if o_permissions:
            _params['permissions'] = o_permissions

        return self._request(method, _args, _params)

    def delegation_del(
            self,
            a_aciname,
    ):
        """Delete a delegation.
        :param a_aciname: Delegation name
        :type  a_aciname: str
        """
        method = 'delegation_del'

        _args = list()
        _args.append(a_aciname)

        _params = dict()

        return self._request(method, _args, _params)

    def delegation_find(
            self,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_attrs=None,
            o_group=None,
            o_memberof=None,
            o_aciname=None,
            o_permissions=None,
    ):
        """Search for delegations.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_attrs: Attributes to which the delegation applies
        :type  o_attrs: str
        :param o_group: User group ACI grants access to
        :type  o_group: str
        :param o_memberof: User group to apply delegation to
        :type  o_memberof: str
        :param o_aciname: Delegation name
        :type  o_aciname: str
        :param o_permissions: Permissions to grant (read, write). Default is write.
        :type  o_permissions: str
        """
        method = 'delegation_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_group:
            _params['group'] = o_group
        if o_memberof:
            _params['memberof'] = o_memberof
        if o_aciname:
            _params['aciname'] = o_aciname
        if o_permissions:
            _params['permissions'] = o_permissions

        return self._request(method, _args, _params)

    def delegation_mod(
            self,
            a_aciname,
            o_all=True,
            o_raw=False,
            o_attrs=None,
            o_group=None,
            o_memberof=None,
            o_permissions=None,
    ):
        """Modify a delegation.
        :param a_aciname: Delegation name
        :type  a_aciname: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_attrs: Attributes to which the delegation applies
        :type  o_attrs: str
        :param o_group: User group ACI grants access to
        :type  o_group: str
        :param o_memberof: User group to apply delegation to
        :type  o_memberof: str
        :param o_permissions: Permissions to grant (read, write). Default is write.
        :type  o_permissions: str
        """
        method = 'delegation_mod'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_group:
            _params['group'] = o_group
        if o_memberof:
            _params['memberof'] = o_memberof
        if o_permissions:
            _params['permissions'] = o_permissions

        return self._request(method, _args, _params)

    def delegation_show(
            self,
            a_aciname,
            o_all=True,
            o_raw=False,
    ):
        """Display information about a delegation.
        :param a_aciname: Delegation name
        :type  a_aciname: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'delegation_show'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def dns_is_enabled(
            self,
    ):
        """
    Checks if any of the servers has the DNS service enabled.
        """
        method = 'dns_is_enabled'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def dns_resolve(
            self,
            a_hostname,
    ):
        """Resolve a host name in DNS. (Deprecated)
        :param a_hostname: Hostname (FQDN)
        :type  a_hostname: str
        """
        method = 'dns_resolve'

        _args = list()
        _args.append(a_hostname)

        _params = dict()

        return self._request(method, _args, _params)

    def dns_update_system_records(
            self,
            o_all=True,
            o_dry_run=False,
            o_raw=False,
    ):
        """Update location and IPA server DNS records
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_dry_run: Do not update records only return expected records
        :type  o_dry_run: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'dns_update_system_records'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        _params['dry_run'] = o_dry_run
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def dnsconfig_mod(
            self,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_idnsallowsyncptr=None,
            o_ipadnsversion=None,
            o_idnszonerefresh=None,
            o_idnsforwarders=None,
            o_idnsforwardpolicy=None,
    ):
        """Modify global DNS configuration.
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_idnsallowsyncptr: Allow synchronization of forward (A, AAAA) and reverse (PTR) records
        :type  o_idnsallowsyncptr: Bool
        :param o_ipadnsversion: IPA DNS version
        :type  o_ipadnsversion: int, min value -2147483648, max value 2147483647
        :param o_idnszonerefresh: An interval between regular polls of the name server for new DNS zones
        :type  o_idnszonerefresh: int, min value 0, max value 2147483647
        :param o_idnsforwarders: Global forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_idnsforwardpolicy: Global forwarding policy. Set to "none" to disable any configured global forwarders.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        """
        method = 'dnsconfig_mod'

        _args = list()

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_idnsallowsyncptr:
            _params['idnsallowsyncptr'] = o_idnsallowsyncptr
        if o_ipadnsversion:
            _params['ipadnsversion'] = o_ipadnsversion
        if o_idnszonerefresh:
            _params['idnszonerefresh'] = o_idnszonerefresh
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy

        return self._request(method, _args, _params)

    def dnsconfig_show(
            self,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Show the current global DNS configuration.
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'dnsconfig_show'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def dnsforwardzone_add(
            self,
            a_idnsname,
            o_addattr=None,
            o_name_from_ip=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_skip_overlap_check=False,
            o_idnsforwarders=None,
            o_idnsforwardpolicy=None,
    ):
        """Create new DNS forward zone.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_name_from_ip: IP network to create reverse zone name from
        :type  o_name_from_ip: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_skip_overlap_check: Force DNS zone creation even if it will overlap with an existing zone.
        :type  o_skip_overlap_check: bool
        :param o_idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        """
        method = 'dnsforwardzone_add'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_name_from_ip:
            _params['name_from_ip'] = o_name_from_ip
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['skip_overlap_check'] = o_skip_overlap_check
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy

        return self._request(method, _args, _params)

    def dnsforwardzone_add_permission(
            self,
            a_idnsname,
    ):
        """Add a permission for per-forward zone access delegation.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        """
        method = 'dnsforwardzone_add_permission'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()

        return self._request(method, _args, _params)

    def dnsforwardzone_del(
            self,
            a_idnsname,
            o_continue=False,
    ):
        """Delete DNS forward zone.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'dnsforwardzone_del'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def dnsforwardzone_disable(
            self,
            a_idnsname,
    ):
        """Disable DNS Forward Zone.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        """
        method = 'dnsforwardzone_disable'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()

        return self._request(method, _args, _params)

    def dnsforwardzone_enable(
            self,
            a_idnsname,
    ):
        """Enable DNS Forward Zone.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        """
        method = 'dnsforwardzone_enable'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()

        return self._request(method, _args, _params)

    def dnsforwardzone_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_name_from_ip=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_idnszoneactive=None,
            o_idnsname=None,
            o_idnsforwarders=None,
            o_idnsforwardpolicy=None,
    ):
        """Search for DNS forward zones.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_name_from_ip: IP network to create reverse zone name from
        :type  o_name_from_ip: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_idnszoneactive: Is zone active?
        :type  o_idnszoneactive: Bool
        :param o_idnsname: Zone name (FQDN)
        :type  o_idnsname: DNSNameParam
        :param o_idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        """
        method = 'dnsforwardzone_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_name_from_ip:
            _params['name_from_ip'] = o_name_from_ip
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_idnszoneactive:
            _params['idnszoneactive'] = o_idnszoneactive
        if o_idnsname:
            _params['idnsname'] = o_idnsname
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy

        return self._request(method, _args, _params)

    def dnsforwardzone_mod(
            self,
            a_idnsname,
            o_addattr=None,
            o_delattr=None,
            o_name_from_ip=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_idnsforwarders=None,
            o_idnsforwardpolicy=None,
    ):
        """Modify DNS forward zone.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_name_from_ip: IP network to create reverse zone name from
        :type  o_name_from_ip: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        """
        method = 'dnsforwardzone_mod'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_name_from_ip:
            _params['name_from_ip'] = o_name_from_ip
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy

        return self._request(method, _args, _params)

    def dnsforwardzone_remove_permission(
            self,
            a_idnsname,
    ):
        """Remove a permission for per-forward zone access delegation.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        """
        method = 'dnsforwardzone_remove_permission'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()

        return self._request(method, _args, _params)

    def dnsforwardzone_show(
            self,
            a_idnsname,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a DNS forward zone.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'dnsforwardzone_show'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def dnsrecord_add(
            self,
            a_dnszoneidnsname,
            a_idnsname,
            o_afsdb_part_hostname=None,
            o_cname_part_hostname=None,
            o_dname_part_target=None,
            o_kx_part_exchanger=None,
            o_mx_part_exchanger=None,
            o_ns_part_hostname=None,
            o_ptr_part_hostname=None,
            o_srv_part_target=None,
            o_loc_part_altitude=None,
            o_loc_part_h_precision=None,
            o_loc_part_lat_sec=None,
            o_loc_part_lon_sec=None,
            o_loc_part_size=None,
            o_loc_part_v_precision=None,
            o_afsdb_part_subtype=None,
            o_cert_part_algorithm=None,
            o_cert_part_key_tag=None,
            o_cert_part_type=None,
            o_dlv_part_algorithm=None,
            o_dlv_part_digest_type=None,
            o_dlv_part_key_tag=None,
            o_ds_part_algorithm=None,
            o_ds_part_digest_type=None,
            o_ds_part_key_tag=None,
            o_kx_part_preference=None,
            o_loc_part_lat_deg=None,
            o_loc_part_lat_min=None,
            o_loc_part_lon_deg=None,
            o_loc_part_lon_min=None,
            o_mx_part_preference=None,
            o_naptr_part_order=None,
            o_naptr_part_preference=None,
            o_srv_part_port=None,
            o_srv_part_priority=None,
            o_srv_part_weight=None,
            o_sshfp_part_algorithm=None,
            o_sshfp_part_fp_type=None,
            o_tlsa_part_cert_usage=None,
            o_tlsa_part_matching_type=None,
            o_tlsa_part_selector=None,
            o_uri_part_priority=None,
            o_uri_part_weight=None,
            o_a6_part_data=None,
            o_a_part_ip_address=None,
            o_aaaa_part_ip_address=None,
            o_addattr=None,
            o_cert_part_certificate_or_crl=None,
            o_dlv_part_digest=None,
            o_ds_part_digest=None,
            o_naptr_part_flags=None,
            o_naptr_part_regexp=None,
            o_naptr_part_replacement=None,
            o_naptr_part_service=None,
            o_setattr=None,
            o_sshfp_part_fingerprint=None,
            o_tlsa_part_cert_association_data=None,
            o_txt_part_data=None,
            o_uri_part_target=None,
            o_loc_part_lon_dir=None,
            o_loc_part_lat_dir=None,
            o_a_extra_create_reverse=False,
            o_aaaa_extra_create_reverse=False,
            o_all=True,
            o_force=False,
            o_raw=False,
            o_structured=False,
            o_a6record=None,
            o_aaaarecord=None,
            o_afsdbrecord=None,
            o_aplrecord=None,
            o_arecord=None,
            o_certrecord=None,
            o_cnamerecord=None,
            o_dhcidrecord=None,
            o_dlvrecord=None,
            o_dnamerecord=None,
            o_dsrecord=None,
            o_hiprecord=None,
            o_ipseckeyrecord=None,
            o_dnsttl=None,
            o_keyrecord=None,
            o_kxrecord=None,
            o_locrecord=None,
            o_mxrecord=None,
            o_naptrrecord=None,
            o_nsecrecord=None,
            o_nsrecord=None,
            o_ptrrecord=None,
            o_rprecord=None,
            o_rrsigrecord=None,
            o_sigrecord=None,
            o_spfrecord=None,
            o_srvrecord=None,
            o_sshfprecord=None,
            o_dnsclass=None,
            o_tlsarecord=None,
            o_txtrecord=None,
            o_urirecord=None,
    ):
        """Add new DNS resource record.
        :param a_dnszoneidnsname: Zone name (FQDN)
        :type  a_dnszoneidnsname: DNSNameParam
        :param a_idnsname: Record name
        :type  a_idnsname: DNSNameParam
        :param o_afsdb_part_hostname: AFSDB Hostname
        :type  o_afsdb_part_hostname: DNSNameParam
        :param o_cname_part_hostname: A hostname which this alias hostname points to
        :type  o_cname_part_hostname: DNSNameParam
        :param o_dname_part_target: DNAME Target
        :type  o_dname_part_target: DNSNameParam
        :param o_kx_part_exchanger: A host willing to act as a key exchanger
        :type  o_kx_part_exchanger: DNSNameParam
        :param o_mx_part_exchanger: A host willing to act as a mail exchanger
        :type  o_mx_part_exchanger: DNSNameParam
        :param o_ns_part_hostname: NS Hostname
        :type  o_ns_part_hostname: DNSNameParam
        :param o_ptr_part_hostname: The hostname this reverse record points to
        :type  o_ptr_part_hostname: DNSNameParam
        :param o_srv_part_target: The domain name of the target host or '.' if the service is decidedly not available at this domain
        :type  o_srv_part_target: DNSNameParam
        :param o_loc_part_altitude: LOC Altitude
        :type  o_loc_part_altitude: Decimal
        :param o_loc_part_h_precision: LOC Horizontal Precision
        :type  o_loc_part_h_precision: Decimal
        :param o_loc_part_lat_sec: LOC Seconds Latitude
        :type  o_loc_part_lat_sec: Decimal
        :param o_loc_part_lon_sec: LOC Seconds Longitude
        :type  o_loc_part_lon_sec: Decimal
        :param o_loc_part_size: LOC Size
        :type  o_loc_part_size: Decimal
        :param o_loc_part_v_precision: LOC Vertical Precision
        :type  o_loc_part_v_precision: Decimal
        :param o_afsdb_part_subtype: AFSDB Subtype
        :type  o_afsdb_part_subtype: int, min value 0, max value 65535
        :param o_cert_part_algorithm: CERT Algorithm
        :type  o_cert_part_algorithm: int, min value 0, max value 255
        :param o_cert_part_key_tag: CERT Key Tag
        :type  o_cert_part_key_tag: int, min value 0, max value 65535
        :param o_cert_part_type: CERT Certificate Type
        :type  o_cert_part_type: int, min value 0, max value 65535
        :param o_dlv_part_algorithm: DLV Algorithm
        :type  o_dlv_part_algorithm: int, min value 0, max value 255
        :param o_dlv_part_digest_type: DLV Digest Type
        :type  o_dlv_part_digest_type: int, min value 0, max value 255
        :param o_dlv_part_key_tag: DLV Key Tag
        :type  o_dlv_part_key_tag: int, min value 0, max value 65535
        :param o_ds_part_algorithm: DS Algorithm
        :type  o_ds_part_algorithm: int, min value 0, max value 255
        :param o_ds_part_digest_type: DS Digest Type
        :type  o_ds_part_digest_type: int, min value 0, max value 255
        :param o_ds_part_key_tag: DS Key Tag
        :type  o_ds_part_key_tag: int, min value 0, max value 65535
        :param o_kx_part_preference: Preference given to this exchanger. Lower values are more preferred
        :type  o_kx_part_preference: int, min value 0, max value 65535
        :param o_loc_part_lat_deg: LOC Degrees Latitude
        :type  o_loc_part_lat_deg: int, min value 0, max value 90
        :param o_loc_part_lat_min: LOC Minutes Latitude
        :type  o_loc_part_lat_min: int, min value 0, max value 59
        :param o_loc_part_lon_deg: LOC Degrees Longitude
        :type  o_loc_part_lon_deg: int, min value 0, max value 180
        :param o_loc_part_lon_min: LOC Minutes Longitude
        :type  o_loc_part_lon_min: int, min value 0, max value 59
        :param o_mx_part_preference: Preference given to this exchanger. Lower values are more preferred
        :type  o_mx_part_preference: int, min value 0, max value 65535
        :param o_naptr_part_order: NAPTR Order
        :type  o_naptr_part_order: int, min value 0, max value 65535
        :param o_naptr_part_preference: NAPTR Preference
        :type  o_naptr_part_preference: int, min value 0, max value 65535
        :param o_srv_part_port: SRV Port
        :type  o_srv_part_port: int, min value 0, max value 65535
        :param o_srv_part_priority: Lower number means higher priority. Clients will attempt to contact the server with the lowest-numbered priority they can reach.
        :type  o_srv_part_priority: int, min value 0, max value 65535
        :param o_srv_part_weight: Relative weight for entries with the same priority.
        :type  o_srv_part_weight: int, min value 0, max value 65535
        :param o_sshfp_part_algorithm: SSHFP Algorithm
        :type  o_sshfp_part_algorithm: int, min value 0, max value 255
        :param o_sshfp_part_fp_type: SSHFP Fingerprint Type
        :type  o_sshfp_part_fp_type: int, min value 0, max value 255
        :param o_tlsa_part_cert_usage: TLSA Certificate Usage
        :type  o_tlsa_part_cert_usage: int, min value 0, max value 255
        :param o_tlsa_part_matching_type: TLSA Matching Type
        :type  o_tlsa_part_matching_type: int, min value 0, max value 255
        :param o_tlsa_part_selector: TLSA Selector
        :type  o_tlsa_part_selector: int, min value 0, max value 255
        :param o_uri_part_priority: Lower number means higher priority. Clients will attempt to contact the URI with the lowest-numbered priority they can reach.
        :type  o_uri_part_priority: int, min value 0, max value 65535
        :param o_uri_part_weight: Relative weight for entries with the same priority.
        :type  o_uri_part_weight: int, min value 0, max value 65535
        :param o_a6_part_data: A6 Record data
        :type  o_a6_part_data: str
        :param o_a_part_ip_address: A IP Address
        :type  o_a_part_ip_address: str
        :param o_aaaa_part_ip_address: AAAA IP Address
        :type  o_aaaa_part_ip_address: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_cert_part_certificate_or_crl: CERT Certificate/CRL
        :type  o_cert_part_certificate_or_crl: str
        :param o_dlv_part_digest: DLV Digest
        :type  o_dlv_part_digest: str
        :param o_ds_part_digest: DS Digest
        :type  o_ds_part_digest: str
        :param o_naptr_part_flags: NAPTR Flags
        :type  o_naptr_part_flags: str
        :param o_naptr_part_regexp: NAPTR Regular Expression
        :type  o_naptr_part_regexp: str
        :param o_naptr_part_replacement: NAPTR Replacement
        :type  o_naptr_part_replacement: str
        :param o_naptr_part_service: NAPTR Service
        :type  o_naptr_part_service: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_sshfp_part_fingerprint: SSHFP Fingerprint
        :type  o_sshfp_part_fingerprint: str
        :param o_tlsa_part_cert_association_data: TLSA Certificate Association Data
        :type  o_tlsa_part_cert_association_data: str
        :param o_txt_part_data: TXT Text Data
        :type  o_txt_part_data: str
        :param o_uri_part_target: Target Uniform Resource Identifier according to RFC 3986
        :type  o_uri_part_target: str
        :param o_loc_part_lon_dir: LOC Direction Longitude
        :type  o_loc_part_lon_dir: str, valid values ['E', 'W']
        :param o_loc_part_lat_dir: LOC Direction Latitude
        :type  o_loc_part_lat_dir: str, valid values ['N', 'S']
        :param o_a_extra_create_reverse: Create reverse record for this IP Address
        :type  o_a_extra_create_reverse: bool
        :param o_aaaa_extra_create_reverse: Create reverse record for this IP Address
        :type  o_aaaa_extra_create_reverse: bool
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_force: force NS record creation even if its hostname is not in DNS
        :type  o_force: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_structured: Parse all raw DNS records and return them in a structured way
        :type  o_structured: bool
        :param o_a6record: Raw A6 records
        :type  o_a6record: A6Record
        :param o_aaaarecord: Raw AAAA records
        :type  o_aaaarecord: AAAARecord
        :param o_afsdbrecord: Raw AFSDB records
        :type  o_afsdbrecord: AFSDBRecord
        :param o_aplrecord: Raw APL records
        :type  o_aplrecord: APLRecord
        :param o_arecord: Raw A records
        :type  o_arecord: ARecord
        :param o_certrecord: Raw CERT records
        :type  o_certrecord: CERTRecord
        :param o_cnamerecord: Raw CNAME records
        :type  o_cnamerecord: CNAMERecord
        :param o_dhcidrecord: Raw DHCID records
        :type  o_dhcidrecord: DHCIDRecord
        :param o_dlvrecord: Raw DLV records
        :type  o_dlvrecord: DLVRecord
        :param o_dnamerecord: Raw DNAME records
        :type  o_dnamerecord: DNAMERecord
        :param o_dsrecord: Raw DS records
        :type  o_dsrecord: DSRecord
        :param o_hiprecord: Raw HIP records
        :type  o_hiprecord: HIPRecord
        :param o_ipseckeyrecord: Raw IPSECKEY records
        :type  o_ipseckeyrecord: IPSECKEYRecord
        :param o_dnsttl: Time to live
        :type  o_dnsttl: int, min value -2147483648, max value 2147483647
        :param o_keyrecord: Raw KEY records
        :type  o_keyrecord: KEYRecord
        :param o_kxrecord: Raw KX records
        :type  o_kxrecord: KXRecord
        :param o_locrecord: Raw LOC records
        :type  o_locrecord: LOCRecord
        :param o_mxrecord: Raw MX records
        :type  o_mxrecord: MXRecord
        :param o_naptrrecord: Raw NAPTR records
        :type  o_naptrrecord: NAPTRRecord
        :param o_nsecrecord: Raw NSEC records
        :type  o_nsecrecord: NSECRecord
        :param o_nsrecord: Raw NS records
        :type  o_nsrecord: NSRecord
        :param o_ptrrecord: Raw PTR records
        :type  o_ptrrecord: PTRRecord
        :param o_rprecord: Raw RP records
        :type  o_rprecord: RPRecord
        :param o_rrsigrecord: Raw RRSIG records
        :type  o_rrsigrecord: RRSIGRecord
        :param o_sigrecord: Raw SIG records
        :type  o_sigrecord: SIGRecord
        :param o_spfrecord: Raw SPF records
        :type  o_spfrecord: SPFRecord
        :param o_srvrecord: Raw SRV records
        :type  o_srvrecord: SRVRecord
        :param o_sshfprecord: Raw SSHFP records
        :type  o_sshfprecord: SSHFPRecord
        :param o_dnsclass: <dnsclass>
        :type  o_dnsclass: str, valid values ['IN', 'CS', 'CH', 'HS']
        :param o_tlsarecord: Raw TLSA records
        :type  o_tlsarecord: TLSARecord
        :param o_txtrecord: Raw TXT records
        :type  o_txtrecord: TXTRecord
        :param o_urirecord: Raw URI records
        :type  o_urirecord: URIRecord
        """
        method = 'dnsrecord_add'

        _args = list()
        _args.append(a_dnszoneidnsname)
        _args.append(a_idnsname)

        _params = dict()
        if o_afsdb_part_hostname:
            _params['afsdb_part_hostname'] = o_afsdb_part_hostname
        if o_cname_part_hostname:
            _params['cname_part_hostname'] = o_cname_part_hostname
        if o_dname_part_target:
            _params['dname_part_target'] = o_dname_part_target
        if o_kx_part_exchanger:
            _params['kx_part_exchanger'] = o_kx_part_exchanger
        if o_mx_part_exchanger:
            _params['mx_part_exchanger'] = o_mx_part_exchanger
        if o_ns_part_hostname:
            _params['ns_part_hostname'] = o_ns_part_hostname
        if o_ptr_part_hostname:
            _params['ptr_part_hostname'] = o_ptr_part_hostname
        if o_srv_part_target:
            _params['srv_part_target'] = o_srv_part_target
        if o_loc_part_altitude:
            _params['loc_part_altitude'] = o_loc_part_altitude
        if o_loc_part_h_precision:
            _params['loc_part_h_precision'] = o_loc_part_h_precision
        if o_loc_part_lat_sec:
            _params['loc_part_lat_sec'] = o_loc_part_lat_sec
        if o_loc_part_lon_sec:
            _params['loc_part_lon_sec'] = o_loc_part_lon_sec
        if o_loc_part_size:
            _params['loc_part_size'] = o_loc_part_size
        if o_loc_part_v_precision:
            _params['loc_part_v_precision'] = o_loc_part_v_precision
        if o_afsdb_part_subtype:
            _params['afsdb_part_subtype'] = o_afsdb_part_subtype
        if o_cert_part_algorithm:
            _params['cert_part_algorithm'] = o_cert_part_algorithm
        if o_cert_part_key_tag:
            _params['cert_part_key_tag'] = o_cert_part_key_tag
        if o_cert_part_type:
            _params['cert_part_type'] = o_cert_part_type
        if o_dlv_part_algorithm:
            _params['dlv_part_algorithm'] = o_dlv_part_algorithm
        if o_dlv_part_digest_type:
            _params['dlv_part_digest_type'] = o_dlv_part_digest_type
        if o_dlv_part_key_tag:
            _params['dlv_part_key_tag'] = o_dlv_part_key_tag
        if o_ds_part_algorithm:
            _params['ds_part_algorithm'] = o_ds_part_algorithm
        if o_ds_part_digest_type:
            _params['ds_part_digest_type'] = o_ds_part_digest_type
        if o_ds_part_key_tag:
            _params['ds_part_key_tag'] = o_ds_part_key_tag
        if o_kx_part_preference:
            _params['kx_part_preference'] = o_kx_part_preference
        if o_loc_part_lat_deg:
            _params['loc_part_lat_deg'] = o_loc_part_lat_deg
        if o_loc_part_lat_min:
            _params['loc_part_lat_min'] = o_loc_part_lat_min
        if o_loc_part_lon_deg:
            _params['loc_part_lon_deg'] = o_loc_part_lon_deg
        if o_loc_part_lon_min:
            _params['loc_part_lon_min'] = o_loc_part_lon_min
        if o_mx_part_preference:
            _params['mx_part_preference'] = o_mx_part_preference
        if o_naptr_part_order:
            _params['naptr_part_order'] = o_naptr_part_order
        if o_naptr_part_preference:
            _params['naptr_part_preference'] = o_naptr_part_preference
        if o_srv_part_port:
            _params['srv_part_port'] = o_srv_part_port
        if o_srv_part_priority:
            _params['srv_part_priority'] = o_srv_part_priority
        if o_srv_part_weight:
            _params['srv_part_weight'] = o_srv_part_weight
        if o_sshfp_part_algorithm:
            _params['sshfp_part_algorithm'] = o_sshfp_part_algorithm
        if o_sshfp_part_fp_type:
            _params['sshfp_part_fp_type'] = o_sshfp_part_fp_type
        if o_tlsa_part_cert_usage:
            _params['tlsa_part_cert_usage'] = o_tlsa_part_cert_usage
        if o_tlsa_part_matching_type:
            _params['tlsa_part_matching_type'] = o_tlsa_part_matching_type
        if o_tlsa_part_selector:
            _params['tlsa_part_selector'] = o_tlsa_part_selector
        if o_uri_part_priority:
            _params['uri_part_priority'] = o_uri_part_priority
        if o_uri_part_weight:
            _params['uri_part_weight'] = o_uri_part_weight
        if o_a6_part_data:
            _params['a6_part_data'] = o_a6_part_data
        if o_a_part_ip_address:
            _params['a_part_ip_address'] = o_a_part_ip_address
        if o_aaaa_part_ip_address:
            _params['aaaa_part_ip_address'] = o_aaaa_part_ip_address
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_cert_part_certificate_or_crl:
            _params['cert_part_certificate_or_crl'] = o_cert_part_certificate_or_crl
        if o_dlv_part_digest:
            _params['dlv_part_digest'] = o_dlv_part_digest
        if o_ds_part_digest:
            _params['ds_part_digest'] = o_ds_part_digest
        if o_naptr_part_flags:
            _params['naptr_part_flags'] = o_naptr_part_flags
        if o_naptr_part_regexp:
            _params['naptr_part_regexp'] = o_naptr_part_regexp
        if o_naptr_part_replacement:
            _params['naptr_part_replacement'] = o_naptr_part_replacement
        if o_naptr_part_service:
            _params['naptr_part_service'] = o_naptr_part_service
        if o_setattr:
            _params['setattr'] = o_setattr
        if o_sshfp_part_fingerprint:
            _params['sshfp_part_fingerprint'] = o_sshfp_part_fingerprint
        if o_tlsa_part_cert_association_data:
            _params['tlsa_part_cert_association_data'] = o_tlsa_part_cert_association_data
        if o_txt_part_data:
            _params['txt_part_data'] = o_txt_part_data
        if o_uri_part_target:
            _params['uri_part_target'] = o_uri_part_target
        if o_loc_part_lon_dir:
            _params['loc_part_lon_dir'] = o_loc_part_lon_dir
        if o_loc_part_lat_dir:
            _params['loc_part_lat_dir'] = o_loc_part_lat_dir
        if o_a_extra_create_reverse:
            _params['a_extra_create_reverse'] = o_a_extra_create_reverse
        if o_aaaa_extra_create_reverse:
            _params['aaaa_extra_create_reverse'] = o_aaaa_extra_create_reverse
        _params['all'] = o_all
        _params['force'] = o_force
        _params['raw'] = o_raw
        _params['structured'] = o_structured
        if o_a6record:
            _params['a6record'] = o_a6record
        if o_aaaarecord:
            _params['aaaarecord'] = o_aaaarecord
        if o_afsdbrecord:
            _params['afsdbrecord'] = o_afsdbrecord
        if o_aplrecord:
            _params['aplrecord'] = o_aplrecord
        if o_arecord:
            _params['arecord'] = o_arecord
        if o_certrecord:
            _params['certrecord'] = o_certrecord
        if o_cnamerecord:
            _params['cnamerecord'] = o_cnamerecord
        if o_dhcidrecord:
            _params['dhcidrecord'] = o_dhcidrecord
        if o_dlvrecord:
            _params['dlvrecord'] = o_dlvrecord
        if o_dnamerecord:
            _params['dnamerecord'] = o_dnamerecord
        if o_dsrecord:
            _params['dsrecord'] = o_dsrecord
        if o_hiprecord:
            _params['hiprecord'] = o_hiprecord
        if o_ipseckeyrecord:
            _params['ipseckeyrecord'] = o_ipseckeyrecord
        if o_dnsttl:
            _params['dnsttl'] = o_dnsttl
        if o_keyrecord:
            _params['keyrecord'] = o_keyrecord
        if o_kxrecord:
            _params['kxrecord'] = o_kxrecord
        if o_locrecord:
            _params['locrecord'] = o_locrecord
        if o_mxrecord:
            _params['mxrecord'] = o_mxrecord
        if o_naptrrecord:
            _params['naptrrecord'] = o_naptrrecord
        if o_nsecrecord:
            _params['nsecrecord'] = o_nsecrecord
        if o_nsrecord:
            _params['nsrecord'] = o_nsrecord
        if o_ptrrecord:
            _params['ptrrecord'] = o_ptrrecord
        if o_rprecord:
            _params['rprecord'] = o_rprecord
        if o_rrsigrecord:
            _params['rrsigrecord'] = o_rrsigrecord
        if o_sigrecord:
            _params['sigrecord'] = o_sigrecord
        if o_spfrecord:
            _params['spfrecord'] = o_spfrecord
        if o_srvrecord:
            _params['srvrecord'] = o_srvrecord
        if o_sshfprecord:
            _params['sshfprecord'] = o_sshfprecord
        if o_dnsclass:
            _params['dnsclass'] = o_dnsclass
        if o_tlsarecord:
            _params['tlsarecord'] = o_tlsarecord
        if o_txtrecord:
            _params['txtrecord'] = o_txtrecord
        if o_urirecord:
            _params['urirecord'] = o_urirecord

        return self._request(method, _args, _params)

    def dnsrecord_del(
            self,
            a_dnszoneidnsname,
            a_idnsname,
            o_del_all=False,
            o_raw=False,
            o_structured=False,
            o_a6record=None,
            o_aaaarecord=None,
            o_afsdbrecord=None,
            o_aplrecord=None,
            o_arecord=None,
            o_certrecord=None,
            o_cnamerecord=None,
            o_dhcidrecord=None,
            o_dlvrecord=None,
            o_dnamerecord=None,
            o_dsrecord=None,
            o_hiprecord=None,
            o_ipseckeyrecord=None,
            o_dnsttl=None,
            o_keyrecord=None,
            o_kxrecord=None,
            o_locrecord=None,
            o_mxrecord=None,
            o_naptrrecord=None,
            o_nsecrecord=None,
            o_nsrecord=None,
            o_ptrrecord=None,
            o_rprecord=None,
            o_rrsigrecord=None,
            o_sigrecord=None,
            o_spfrecord=None,
            o_srvrecord=None,
            o_sshfprecord=None,
            o_dnsclass=None,
            o_tlsarecord=None,
            o_txtrecord=None,
            o_urirecord=None,
    ):
        """Delete DNS resource record.
        :param a_dnszoneidnsname: Zone name (FQDN)
        :type  a_dnszoneidnsname: DNSNameParam
        :param a_idnsname: Record name
        :type  a_idnsname: DNSNameParam
        :param o_del_all: Delete all associated records
        :type  o_del_all: bool
        :param o_raw: <raw>
        :type  o_raw: bool
        :param o_structured: Parse all raw DNS records and return them in a structured way
        :type  o_structured: bool
        :param o_a6record: Raw A6 records
        :type  o_a6record: A6Record
        :param o_aaaarecord: Raw AAAA records
        :type  o_aaaarecord: AAAARecord
        :param o_afsdbrecord: Raw AFSDB records
        :type  o_afsdbrecord: AFSDBRecord
        :param o_aplrecord: Raw APL records
        :type  o_aplrecord: APLRecord
        :param o_arecord: Raw A records
        :type  o_arecord: ARecord
        :param o_certrecord: Raw CERT records
        :type  o_certrecord: CERTRecord
        :param o_cnamerecord: Raw CNAME records
        :type  o_cnamerecord: CNAMERecord
        :param o_dhcidrecord: Raw DHCID records
        :type  o_dhcidrecord: DHCIDRecord
        :param o_dlvrecord: Raw DLV records
        :type  o_dlvrecord: DLVRecord
        :param o_dnamerecord: Raw DNAME records
        :type  o_dnamerecord: DNAMERecord
        :param o_dsrecord: Raw DS records
        :type  o_dsrecord: DSRecord
        :param o_hiprecord: Raw HIP records
        :type  o_hiprecord: HIPRecord
        :param o_ipseckeyrecord: Raw IPSECKEY records
        :type  o_ipseckeyrecord: IPSECKEYRecord
        :param o_dnsttl: Time to live
        :type  o_dnsttl: int, min value -2147483648, max value 2147483647
        :param o_keyrecord: Raw KEY records
        :type  o_keyrecord: KEYRecord
        :param o_kxrecord: Raw KX records
        :type  o_kxrecord: KXRecord
        :param o_locrecord: Raw LOC records
        :type  o_locrecord: LOCRecord
        :param o_mxrecord: Raw MX records
        :type  o_mxrecord: MXRecord
        :param o_naptrrecord: Raw NAPTR records
        :type  o_naptrrecord: NAPTRRecord
        :param o_nsecrecord: Raw NSEC records
        :type  o_nsecrecord: NSECRecord
        :param o_nsrecord: Raw NS records
        :type  o_nsrecord: NSRecord
        :param o_ptrrecord: Raw PTR records
        :type  o_ptrrecord: PTRRecord
        :param o_rprecord: Raw RP records
        :type  o_rprecord: RPRecord
        :param o_rrsigrecord: Raw RRSIG records
        :type  o_rrsigrecord: RRSIGRecord
        :param o_sigrecord: Raw SIG records
        :type  o_sigrecord: SIGRecord
        :param o_spfrecord: Raw SPF records
        :type  o_spfrecord: SPFRecord
        :param o_srvrecord: Raw SRV records
        :type  o_srvrecord: SRVRecord
        :param o_sshfprecord: Raw SSHFP records
        :type  o_sshfprecord: SSHFPRecord
        :param o_dnsclass: <dnsclass>
        :type  o_dnsclass: str, valid values ['IN', 'CS', 'CH', 'HS']
        :param o_tlsarecord: Raw TLSA records
        :type  o_tlsarecord: TLSARecord
        :param o_txtrecord: Raw TXT records
        :type  o_txtrecord: TXTRecord
        :param o_urirecord: Raw URI records
        :type  o_urirecord: URIRecord
        """
        method = 'dnsrecord_del'

        _args = list()
        _args.append(a_dnszoneidnsname)
        _args.append(a_idnsname)

        _params = dict()
        _params['del_all'] = o_del_all
        _params['raw'] = o_raw
        _params['structured'] = o_structured
        if o_a6record:
            _params['a6record'] = o_a6record
        if o_aaaarecord:
            _params['aaaarecord'] = o_aaaarecord
        if o_afsdbrecord:
            _params['afsdbrecord'] = o_afsdbrecord
        if o_aplrecord:
            _params['aplrecord'] = o_aplrecord
        if o_arecord:
            _params['arecord'] = o_arecord
        if o_certrecord:
            _params['certrecord'] = o_certrecord
        if o_cnamerecord:
            _params['cnamerecord'] = o_cnamerecord
        if o_dhcidrecord:
            _params['dhcidrecord'] = o_dhcidrecord
        if o_dlvrecord:
            _params['dlvrecord'] = o_dlvrecord
        if o_dnamerecord:
            _params['dnamerecord'] = o_dnamerecord
        if o_dsrecord:
            _params['dsrecord'] = o_dsrecord
        if o_hiprecord:
            _params['hiprecord'] = o_hiprecord
        if o_ipseckeyrecord:
            _params['ipseckeyrecord'] = o_ipseckeyrecord
        if o_dnsttl:
            _params['dnsttl'] = o_dnsttl
        if o_keyrecord:
            _params['keyrecord'] = o_keyrecord
        if o_kxrecord:
            _params['kxrecord'] = o_kxrecord
        if o_locrecord:
            _params['locrecord'] = o_locrecord
        if o_mxrecord:
            _params['mxrecord'] = o_mxrecord
        if o_naptrrecord:
            _params['naptrrecord'] = o_naptrrecord
        if o_nsecrecord:
            _params['nsecrecord'] = o_nsecrecord
        if o_nsrecord:
            _params['nsrecord'] = o_nsrecord
        if o_ptrrecord:
            _params['ptrrecord'] = o_ptrrecord
        if o_rprecord:
            _params['rprecord'] = o_rprecord
        if o_rrsigrecord:
            _params['rrsigrecord'] = o_rrsigrecord
        if o_sigrecord:
            _params['sigrecord'] = o_sigrecord
        if o_spfrecord:
            _params['spfrecord'] = o_spfrecord
        if o_srvrecord:
            _params['srvrecord'] = o_srvrecord
        if o_sshfprecord:
            _params['sshfprecord'] = o_sshfprecord
        if o_dnsclass:
            _params['dnsclass'] = o_dnsclass
        if o_tlsarecord:
            _params['tlsarecord'] = o_tlsarecord
        if o_txtrecord:
            _params['txtrecord'] = o_txtrecord
        if o_urirecord:
            _params['urirecord'] = o_urirecord

        return self._request(method, _args, _params)

    def dnsrecord_delentry(
            self,
            a_dnszoneidnsname,
            a_idnsname,
            o_continue=False,
    ):
        """
    Delete DNS record entry.
        :param a_dnszoneidnsname: Zone name (FQDN)
        :type  a_dnszoneidnsname: DNSNameParam
        :param a_idnsname: Record name
        :type  a_idnsname: DNSNameParam
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'dnsrecord_delentry'

        _args = list()
        _args.append(a_dnszoneidnsname)
        _args.append(a_idnsname)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def dnsrecord_find(
            self,
            a_dnszoneidnsname,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_structured=False,
            o_a6record=None,
            o_aaaarecord=None,
            o_afsdbrecord=None,
            o_aplrecord=None,
            o_arecord=None,
            o_certrecord=None,
            o_cnamerecord=None,
            o_dhcidrecord=None,
            o_dlvrecord=None,
            o_dnamerecord=None,
            o_idnsname=None,
            o_dsrecord=None,
            o_hiprecord=None,
            o_ipseckeyrecord=None,
            o_dnsttl=None,
            o_keyrecord=None,
            o_kxrecord=None,
            o_locrecord=None,
            o_mxrecord=None,
            o_naptrrecord=None,
            o_nsecrecord=None,
            o_nsrecord=None,
            o_ptrrecord=None,
            o_rprecord=None,
            o_rrsigrecord=None,
            o_sigrecord=None,
            o_spfrecord=None,
            o_srvrecord=None,
            o_sshfprecord=None,
            o_dnsclass=None,
            o_tlsarecord=None,
            o_txtrecord=None,
            o_urirecord=None,
    ):
        """Search for DNS resources.
        :param a_dnszoneidnsname: Zone name (FQDN)
        :type  a_dnszoneidnsname: DNSNameParam
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_structured: Parse all raw DNS records and return them in a structured way
        :type  o_structured: bool
        :param o_a6record: Raw A6 records
        :type  o_a6record: A6Record
        :param o_aaaarecord: Raw AAAA records
        :type  o_aaaarecord: AAAARecord
        :param o_afsdbrecord: Raw AFSDB records
        :type  o_afsdbrecord: AFSDBRecord
        :param o_aplrecord: Raw APL records
        :type  o_aplrecord: APLRecord
        :param o_arecord: Raw A records
        :type  o_arecord: ARecord
        :param o_certrecord: Raw CERT records
        :type  o_certrecord: CERTRecord
        :param o_cnamerecord: Raw CNAME records
        :type  o_cnamerecord: CNAMERecord
        :param o_dhcidrecord: Raw DHCID records
        :type  o_dhcidrecord: DHCIDRecord
        :param o_dlvrecord: Raw DLV records
        :type  o_dlvrecord: DLVRecord
        :param o_dnamerecord: Raw DNAME records
        :type  o_dnamerecord: DNAMERecord
        :param o_idnsname: Record name
        :type  o_idnsname: DNSNameParam
        :param o_dsrecord: Raw DS records
        :type  o_dsrecord: DSRecord
        :param o_hiprecord: Raw HIP records
        :type  o_hiprecord: HIPRecord
        :param o_ipseckeyrecord: Raw IPSECKEY records
        :type  o_ipseckeyrecord: IPSECKEYRecord
        :param o_dnsttl: Time to live
        :type  o_dnsttl: int, min value -2147483648, max value 2147483647
        :param o_keyrecord: Raw KEY records
        :type  o_keyrecord: KEYRecord
        :param o_kxrecord: Raw KX records
        :type  o_kxrecord: KXRecord
        :param o_locrecord: Raw LOC records
        :type  o_locrecord: LOCRecord
        :param o_mxrecord: Raw MX records
        :type  o_mxrecord: MXRecord
        :param o_naptrrecord: Raw NAPTR records
        :type  o_naptrrecord: NAPTRRecord
        :param o_nsecrecord: Raw NSEC records
        :type  o_nsecrecord: NSECRecord
        :param o_nsrecord: Raw NS records
        :type  o_nsrecord: NSRecord
        :param o_ptrrecord: Raw PTR records
        :type  o_ptrrecord: PTRRecord
        :param o_rprecord: Raw RP records
        :type  o_rprecord: RPRecord
        :param o_rrsigrecord: Raw RRSIG records
        :type  o_rrsigrecord: RRSIGRecord
        :param o_sigrecord: Raw SIG records
        :type  o_sigrecord: SIGRecord
        :param o_spfrecord: Raw SPF records
        :type  o_spfrecord: SPFRecord
        :param o_srvrecord: Raw SRV records
        :type  o_srvrecord: SRVRecord
        :param o_sshfprecord: Raw SSHFP records
        :type  o_sshfprecord: SSHFPRecord
        :param o_dnsclass: <dnsclass>
        :type  o_dnsclass: str, valid values ['IN', 'CS', 'CH', 'HS']
        :param o_tlsarecord: Raw TLSA records
        :type  o_tlsarecord: TLSARecord
        :param o_txtrecord: Raw TXT records
        :type  o_txtrecord: TXTRecord
        :param o_urirecord: Raw URI records
        :type  o_urirecord: URIRecord
        """
        method = 'dnsrecord_find'

        _args = list()
        _args.append(a_dnszoneidnsname)
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        _params['structured'] = o_structured
        if o_a6record:
            _params['a6record'] = o_a6record
        if o_aaaarecord:
            _params['aaaarecord'] = o_aaaarecord
        if o_afsdbrecord:
            _params['afsdbrecord'] = o_afsdbrecord
        if o_aplrecord:
            _params['aplrecord'] = o_aplrecord
        if o_arecord:
            _params['arecord'] = o_arecord
        if o_certrecord:
            _params['certrecord'] = o_certrecord
        if o_cnamerecord:
            _params['cnamerecord'] = o_cnamerecord
        if o_dhcidrecord:
            _params['dhcidrecord'] = o_dhcidrecord
        if o_dlvrecord:
            _params['dlvrecord'] = o_dlvrecord
        if o_dnamerecord:
            _params['dnamerecord'] = o_dnamerecord
        if o_idnsname:
            _params['idnsname'] = o_idnsname
        if o_dsrecord:
            _params['dsrecord'] = o_dsrecord
        if o_hiprecord:
            _params['hiprecord'] = o_hiprecord
        if o_ipseckeyrecord:
            _params['ipseckeyrecord'] = o_ipseckeyrecord
        if o_dnsttl:
            _params['dnsttl'] = o_dnsttl
        if o_keyrecord:
            _params['keyrecord'] = o_keyrecord
        if o_kxrecord:
            _params['kxrecord'] = o_kxrecord
        if o_locrecord:
            _params['locrecord'] = o_locrecord
        if o_mxrecord:
            _params['mxrecord'] = o_mxrecord
        if o_naptrrecord:
            _params['naptrrecord'] = o_naptrrecord
        if o_nsecrecord:
            _params['nsecrecord'] = o_nsecrecord
        if o_nsrecord:
            _params['nsrecord'] = o_nsrecord
        if o_ptrrecord:
            _params['ptrrecord'] = o_ptrrecord
        if o_rprecord:
            _params['rprecord'] = o_rprecord
        if o_rrsigrecord:
            _params['rrsigrecord'] = o_rrsigrecord
        if o_sigrecord:
            _params['sigrecord'] = o_sigrecord
        if o_spfrecord:
            _params['spfrecord'] = o_spfrecord
        if o_srvrecord:
            _params['srvrecord'] = o_srvrecord
        if o_sshfprecord:
            _params['sshfprecord'] = o_sshfprecord
        if o_dnsclass:
            _params['dnsclass'] = o_dnsclass
        if o_tlsarecord:
            _params['tlsarecord'] = o_tlsarecord
        if o_txtrecord:
            _params['txtrecord'] = o_txtrecord
        if o_urirecord:
            _params['urirecord'] = o_urirecord

        return self._request(method, _args, _params)

    def dnsrecord_mod(
            self,
            a_dnszoneidnsname,
            a_idnsname,
            o_afsdb_part_hostname=None,
            o_cname_part_hostname=None,
            o_dname_part_target=None,
            o_kx_part_exchanger=None,
            o_mx_part_exchanger=None,
            o_ns_part_hostname=None,
            o_ptr_part_hostname=None,
            o_rename=None,
            o_srv_part_target=None,
            o_loc_part_altitude=None,
            o_loc_part_h_precision=None,
            o_loc_part_lat_sec=None,
            o_loc_part_lon_sec=None,
            o_loc_part_size=None,
            o_loc_part_v_precision=None,
            o_afsdb_part_subtype=None,
            o_cert_part_algorithm=None,
            o_cert_part_key_tag=None,
            o_cert_part_type=None,
            o_dlv_part_algorithm=None,
            o_dlv_part_digest_type=None,
            o_dlv_part_key_tag=None,
            o_ds_part_algorithm=None,
            o_ds_part_digest_type=None,
            o_ds_part_key_tag=None,
            o_kx_part_preference=None,
            o_loc_part_lat_deg=None,
            o_loc_part_lat_min=None,
            o_loc_part_lon_deg=None,
            o_loc_part_lon_min=None,
            o_mx_part_preference=None,
            o_naptr_part_order=None,
            o_naptr_part_preference=None,
            o_srv_part_port=None,
            o_srv_part_priority=None,
            o_srv_part_weight=None,
            o_sshfp_part_algorithm=None,
            o_sshfp_part_fp_type=None,
            o_tlsa_part_cert_usage=None,
            o_tlsa_part_matching_type=None,
            o_tlsa_part_selector=None,
            o_uri_part_priority=None,
            o_uri_part_weight=None,
            o_a6_part_data=None,
            o_a_part_ip_address=None,
            o_aaaa_part_ip_address=None,
            o_addattr=None,
            o_cert_part_certificate_or_crl=None,
            o_delattr=None,
            o_dlv_part_digest=None,
            o_ds_part_digest=None,
            o_naptr_part_flags=None,
            o_naptr_part_regexp=None,
            o_naptr_part_replacement=None,
            o_naptr_part_service=None,
            o_setattr=None,
            o_sshfp_part_fingerprint=None,
            o_tlsa_part_cert_association_data=None,
            o_txt_part_data=None,
            o_uri_part_target=None,
            o_loc_part_lon_dir=None,
            o_loc_part_lat_dir=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_structured=False,
            o_a6record=None,
            o_aaaarecord=None,
            o_afsdbrecord=None,
            o_aplrecord=None,
            o_arecord=None,
            o_certrecord=None,
            o_cnamerecord=None,
            o_dhcidrecord=None,
            o_dlvrecord=None,
            o_dnamerecord=None,
            o_dsrecord=None,
            o_hiprecord=None,
            o_ipseckeyrecord=None,
            o_dnsttl=None,
            o_keyrecord=None,
            o_kxrecord=None,
            o_locrecord=None,
            o_mxrecord=None,
            o_naptrrecord=None,
            o_nsecrecord=None,
            o_nsrecord=None,
            o_ptrrecord=None,
            o_rprecord=None,
            o_rrsigrecord=None,
            o_sigrecord=None,
            o_spfrecord=None,
            o_srvrecord=None,
            o_sshfprecord=None,
            o_dnsclass=None,
            o_tlsarecord=None,
            o_txtrecord=None,
            o_urirecord=None,
    ):
        """Modify a DNS resource record.
        :param a_dnszoneidnsname: Zone name (FQDN)
        :type  a_dnszoneidnsname: DNSNameParam
        :param a_idnsname: Record name
        :type  a_idnsname: DNSNameParam
        :param o_afsdb_part_hostname: AFSDB Hostname
        :type  o_afsdb_part_hostname: DNSNameParam
        :param o_cname_part_hostname: A hostname which this alias hostname points to
        :type  o_cname_part_hostname: DNSNameParam
        :param o_dname_part_target: DNAME Target
        :type  o_dname_part_target: DNSNameParam
        :param o_kx_part_exchanger: A host willing to act as a key exchanger
        :type  o_kx_part_exchanger: DNSNameParam
        :param o_mx_part_exchanger: A host willing to act as a mail exchanger
        :type  o_mx_part_exchanger: DNSNameParam
        :param o_ns_part_hostname: NS Hostname
        :type  o_ns_part_hostname: DNSNameParam
        :param o_ptr_part_hostname: The hostname this reverse record points to
        :type  o_ptr_part_hostname: DNSNameParam
        :param o_rename: Rename the DNS resource record object
        :type  o_rename: DNSNameParam
        :param o_srv_part_target: The domain name of the target host or '.' if the service is decidedly not available at this domain
        :type  o_srv_part_target: DNSNameParam
        :param o_loc_part_altitude: LOC Altitude
        :type  o_loc_part_altitude: Decimal
        :param o_loc_part_h_precision: LOC Horizontal Precision
        :type  o_loc_part_h_precision: Decimal
        :param o_loc_part_lat_sec: LOC Seconds Latitude
        :type  o_loc_part_lat_sec: Decimal
        :param o_loc_part_lon_sec: LOC Seconds Longitude
        :type  o_loc_part_lon_sec: Decimal
        :param o_loc_part_size: LOC Size
        :type  o_loc_part_size: Decimal
        :param o_loc_part_v_precision: LOC Vertical Precision
        :type  o_loc_part_v_precision: Decimal
        :param o_afsdb_part_subtype: AFSDB Subtype
        :type  o_afsdb_part_subtype: int, min value 0, max value 65535
        :param o_cert_part_algorithm: CERT Algorithm
        :type  o_cert_part_algorithm: int, min value 0, max value 255
        :param o_cert_part_key_tag: CERT Key Tag
        :type  o_cert_part_key_tag: int, min value 0, max value 65535
        :param o_cert_part_type: CERT Certificate Type
        :type  o_cert_part_type: int, min value 0, max value 65535
        :param o_dlv_part_algorithm: DLV Algorithm
        :type  o_dlv_part_algorithm: int, min value 0, max value 255
        :param o_dlv_part_digest_type: DLV Digest Type
        :type  o_dlv_part_digest_type: int, min value 0, max value 255
        :param o_dlv_part_key_tag: DLV Key Tag
        :type  o_dlv_part_key_tag: int, min value 0, max value 65535
        :param o_ds_part_algorithm: DS Algorithm
        :type  o_ds_part_algorithm: int, min value 0, max value 255
        :param o_ds_part_digest_type: DS Digest Type
        :type  o_ds_part_digest_type: int, min value 0, max value 255
        :param o_ds_part_key_tag: DS Key Tag
        :type  o_ds_part_key_tag: int, min value 0, max value 65535
        :param o_kx_part_preference: Preference given to this exchanger. Lower values are more preferred
        :type  o_kx_part_preference: int, min value 0, max value 65535
        :param o_loc_part_lat_deg: LOC Degrees Latitude
        :type  o_loc_part_lat_deg: int, min value 0, max value 90
        :param o_loc_part_lat_min: LOC Minutes Latitude
        :type  o_loc_part_lat_min: int, min value 0, max value 59
        :param o_loc_part_lon_deg: LOC Degrees Longitude
        :type  o_loc_part_lon_deg: int, min value 0, max value 180
        :param o_loc_part_lon_min: LOC Minutes Longitude
        :type  o_loc_part_lon_min: int, min value 0, max value 59
        :param o_mx_part_preference: Preference given to this exchanger. Lower values are more preferred
        :type  o_mx_part_preference: int, min value 0, max value 65535
        :param o_naptr_part_order: NAPTR Order
        :type  o_naptr_part_order: int, min value 0, max value 65535
        :param o_naptr_part_preference: NAPTR Preference
        :type  o_naptr_part_preference: int, min value 0, max value 65535
        :param o_srv_part_port: SRV Port
        :type  o_srv_part_port: int, min value 0, max value 65535
        :param o_srv_part_priority: Lower number means higher priority. Clients will attempt to contact the server with the lowest-numbered priority they can reach.
        :type  o_srv_part_priority: int, min value 0, max value 65535
        :param o_srv_part_weight: Relative weight for entries with the same priority.
        :type  o_srv_part_weight: int, min value 0, max value 65535
        :param o_sshfp_part_algorithm: SSHFP Algorithm
        :type  o_sshfp_part_algorithm: int, min value 0, max value 255
        :param o_sshfp_part_fp_type: SSHFP Fingerprint Type
        :type  o_sshfp_part_fp_type: int, min value 0, max value 255
        :param o_tlsa_part_cert_usage: TLSA Certificate Usage
        :type  o_tlsa_part_cert_usage: int, min value 0, max value 255
        :param o_tlsa_part_matching_type: TLSA Matching Type
        :type  o_tlsa_part_matching_type: int, min value 0, max value 255
        :param o_tlsa_part_selector: TLSA Selector
        :type  o_tlsa_part_selector: int, min value 0, max value 255
        :param o_uri_part_priority: Lower number means higher priority. Clients will attempt to contact the URI with the lowest-numbered priority they can reach.
        :type  o_uri_part_priority: int, min value 0, max value 65535
        :param o_uri_part_weight: Relative weight for entries with the same priority.
        :type  o_uri_part_weight: int, min value 0, max value 65535
        :param o_a6_part_data: A6 Record data
        :type  o_a6_part_data: str
        :param o_a_part_ip_address: A IP Address
        :type  o_a_part_ip_address: str
        :param o_aaaa_part_ip_address: AAAA IP Address
        :type  o_aaaa_part_ip_address: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_cert_part_certificate_or_crl: CERT Certificate/CRL
        :type  o_cert_part_certificate_or_crl: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_dlv_part_digest: DLV Digest
        :type  o_dlv_part_digest: str
        :param o_ds_part_digest: DS Digest
        :type  o_ds_part_digest: str
        :param o_naptr_part_flags: NAPTR Flags
        :type  o_naptr_part_flags: str
        :param o_naptr_part_regexp: NAPTR Regular Expression
        :type  o_naptr_part_regexp: str
        :param o_naptr_part_replacement: NAPTR Replacement
        :type  o_naptr_part_replacement: str
        :param o_naptr_part_service: NAPTR Service
        :type  o_naptr_part_service: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_sshfp_part_fingerprint: SSHFP Fingerprint
        :type  o_sshfp_part_fingerprint: str
        :param o_tlsa_part_cert_association_data: TLSA Certificate Association Data
        :type  o_tlsa_part_cert_association_data: str
        :param o_txt_part_data: TXT Text Data
        :type  o_txt_part_data: str
        :param o_uri_part_target: Target Uniform Resource Identifier according to RFC 3986
        :type  o_uri_part_target: str
        :param o_loc_part_lon_dir: LOC Direction Longitude
        :type  o_loc_part_lon_dir: str, valid values ['E', 'W']
        :param o_loc_part_lat_dir: LOC Direction Latitude
        :type  o_loc_part_lat_dir: str, valid values ['N', 'S']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_structured: Parse all raw DNS records and return them in a structured way
        :type  o_structured: bool
        :param o_a6record: Raw A6 records
        :type  o_a6record: A6Record
        :param o_aaaarecord: Raw AAAA records
        :type  o_aaaarecord: AAAARecord
        :param o_afsdbrecord: Raw AFSDB records
        :type  o_afsdbrecord: AFSDBRecord
        :param o_aplrecord: Raw APL records
        :type  o_aplrecord: APLRecord
        :param o_arecord: Raw A records
        :type  o_arecord: ARecord
        :param o_certrecord: Raw CERT records
        :type  o_certrecord: CERTRecord
        :param o_cnamerecord: Raw CNAME records
        :type  o_cnamerecord: CNAMERecord
        :param o_dhcidrecord: Raw DHCID records
        :type  o_dhcidrecord: DHCIDRecord
        :param o_dlvrecord: Raw DLV records
        :type  o_dlvrecord: DLVRecord
        :param o_dnamerecord: Raw DNAME records
        :type  o_dnamerecord: DNAMERecord
        :param o_dsrecord: Raw DS records
        :type  o_dsrecord: DSRecord
        :param o_hiprecord: Raw HIP records
        :type  o_hiprecord: HIPRecord
        :param o_ipseckeyrecord: Raw IPSECKEY records
        :type  o_ipseckeyrecord: IPSECKEYRecord
        :param o_dnsttl: Time to live
        :type  o_dnsttl: int, min value -2147483648, max value 2147483647
        :param o_keyrecord: Raw KEY records
        :type  o_keyrecord: KEYRecord
        :param o_kxrecord: Raw KX records
        :type  o_kxrecord: KXRecord
        :param o_locrecord: Raw LOC records
        :type  o_locrecord: LOCRecord
        :param o_mxrecord: Raw MX records
        :type  o_mxrecord: MXRecord
        :param o_naptrrecord: Raw NAPTR records
        :type  o_naptrrecord: NAPTRRecord
        :param o_nsecrecord: Raw NSEC records
        :type  o_nsecrecord: NSECRecord
        :param o_nsrecord: Raw NS records
        :type  o_nsrecord: NSRecord
        :param o_ptrrecord: Raw PTR records
        :type  o_ptrrecord: PTRRecord
        :param o_rprecord: Raw RP records
        :type  o_rprecord: RPRecord
        :param o_rrsigrecord: Raw RRSIG records
        :type  o_rrsigrecord: RRSIGRecord
        :param o_sigrecord: Raw SIG records
        :type  o_sigrecord: SIGRecord
        :param o_spfrecord: Raw SPF records
        :type  o_spfrecord: SPFRecord
        :param o_srvrecord: Raw SRV records
        :type  o_srvrecord: SRVRecord
        :param o_sshfprecord: Raw SSHFP records
        :type  o_sshfprecord: SSHFPRecord
        :param o_dnsclass: <dnsclass>
        :type  o_dnsclass: str, valid values ['IN', 'CS', 'CH', 'HS']
        :param o_tlsarecord: Raw TLSA records
        :type  o_tlsarecord: TLSARecord
        :param o_txtrecord: Raw TXT records
        :type  o_txtrecord: TXTRecord
        :param o_urirecord: Raw URI records
        :type  o_urirecord: URIRecord
        """
        method = 'dnsrecord_mod'

        _args = list()
        _args.append(a_dnszoneidnsname)
        _args.append(a_idnsname)

        _params = dict()
        if o_afsdb_part_hostname:
            _params['afsdb_part_hostname'] = o_afsdb_part_hostname
        if o_cname_part_hostname:
            _params['cname_part_hostname'] = o_cname_part_hostname
        if o_dname_part_target:
            _params['dname_part_target'] = o_dname_part_target
        if o_kx_part_exchanger:
            _params['kx_part_exchanger'] = o_kx_part_exchanger
        if o_mx_part_exchanger:
            _params['mx_part_exchanger'] = o_mx_part_exchanger
        if o_ns_part_hostname:
            _params['ns_part_hostname'] = o_ns_part_hostname
        if o_ptr_part_hostname:
            _params['ptr_part_hostname'] = o_ptr_part_hostname
        if o_rename:
            _params['rename'] = o_rename
        if o_srv_part_target:
            _params['srv_part_target'] = o_srv_part_target
        if o_loc_part_altitude:
            _params['loc_part_altitude'] = o_loc_part_altitude
        if o_loc_part_h_precision:
            _params['loc_part_h_precision'] = o_loc_part_h_precision
        if o_loc_part_lat_sec:
            _params['loc_part_lat_sec'] = o_loc_part_lat_sec
        if o_loc_part_lon_sec:
            _params['loc_part_lon_sec'] = o_loc_part_lon_sec
        if o_loc_part_size:
            _params['loc_part_size'] = o_loc_part_size
        if o_loc_part_v_precision:
            _params['loc_part_v_precision'] = o_loc_part_v_precision
        if o_afsdb_part_subtype:
            _params['afsdb_part_subtype'] = o_afsdb_part_subtype
        if o_cert_part_algorithm:
            _params['cert_part_algorithm'] = o_cert_part_algorithm
        if o_cert_part_key_tag:
            _params['cert_part_key_tag'] = o_cert_part_key_tag
        if o_cert_part_type:
            _params['cert_part_type'] = o_cert_part_type
        if o_dlv_part_algorithm:
            _params['dlv_part_algorithm'] = o_dlv_part_algorithm
        if o_dlv_part_digest_type:
            _params['dlv_part_digest_type'] = o_dlv_part_digest_type
        if o_dlv_part_key_tag:
            _params['dlv_part_key_tag'] = o_dlv_part_key_tag
        if o_ds_part_algorithm:
            _params['ds_part_algorithm'] = o_ds_part_algorithm
        if o_ds_part_digest_type:
            _params['ds_part_digest_type'] = o_ds_part_digest_type
        if o_ds_part_key_tag:
            _params['ds_part_key_tag'] = o_ds_part_key_tag
        if o_kx_part_preference:
            _params['kx_part_preference'] = o_kx_part_preference
        if o_loc_part_lat_deg:
            _params['loc_part_lat_deg'] = o_loc_part_lat_deg
        if o_loc_part_lat_min:
            _params['loc_part_lat_min'] = o_loc_part_lat_min
        if o_loc_part_lon_deg:
            _params['loc_part_lon_deg'] = o_loc_part_lon_deg
        if o_loc_part_lon_min:
            _params['loc_part_lon_min'] = o_loc_part_lon_min
        if o_mx_part_preference:
            _params['mx_part_preference'] = o_mx_part_preference
        if o_naptr_part_order:
            _params['naptr_part_order'] = o_naptr_part_order
        if o_naptr_part_preference:
            _params['naptr_part_preference'] = o_naptr_part_preference
        if o_srv_part_port:
            _params['srv_part_port'] = o_srv_part_port
        if o_srv_part_priority:
            _params['srv_part_priority'] = o_srv_part_priority
        if o_srv_part_weight:
            _params['srv_part_weight'] = o_srv_part_weight
        if o_sshfp_part_algorithm:
            _params['sshfp_part_algorithm'] = o_sshfp_part_algorithm
        if o_sshfp_part_fp_type:
            _params['sshfp_part_fp_type'] = o_sshfp_part_fp_type
        if o_tlsa_part_cert_usage:
            _params['tlsa_part_cert_usage'] = o_tlsa_part_cert_usage
        if o_tlsa_part_matching_type:
            _params['tlsa_part_matching_type'] = o_tlsa_part_matching_type
        if o_tlsa_part_selector:
            _params['tlsa_part_selector'] = o_tlsa_part_selector
        if o_uri_part_priority:
            _params['uri_part_priority'] = o_uri_part_priority
        if o_uri_part_weight:
            _params['uri_part_weight'] = o_uri_part_weight
        if o_a6_part_data:
            _params['a6_part_data'] = o_a6_part_data
        if o_a_part_ip_address:
            _params['a_part_ip_address'] = o_a_part_ip_address
        if o_aaaa_part_ip_address:
            _params['aaaa_part_ip_address'] = o_aaaa_part_ip_address
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_cert_part_certificate_or_crl:
            _params['cert_part_certificate_or_crl'] = o_cert_part_certificate_or_crl
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_dlv_part_digest:
            _params['dlv_part_digest'] = o_dlv_part_digest
        if o_ds_part_digest:
            _params['ds_part_digest'] = o_ds_part_digest
        if o_naptr_part_flags:
            _params['naptr_part_flags'] = o_naptr_part_flags
        if o_naptr_part_regexp:
            _params['naptr_part_regexp'] = o_naptr_part_regexp
        if o_naptr_part_replacement:
            _params['naptr_part_replacement'] = o_naptr_part_replacement
        if o_naptr_part_service:
            _params['naptr_part_service'] = o_naptr_part_service
        if o_setattr:
            _params['setattr'] = o_setattr
        if o_sshfp_part_fingerprint:
            _params['sshfp_part_fingerprint'] = o_sshfp_part_fingerprint
        if o_tlsa_part_cert_association_data:
            _params['tlsa_part_cert_association_data'] = o_tlsa_part_cert_association_data
        if o_txt_part_data:
            _params['txt_part_data'] = o_txt_part_data
        if o_uri_part_target:
            _params['uri_part_target'] = o_uri_part_target
        if o_loc_part_lon_dir:
            _params['loc_part_lon_dir'] = o_loc_part_lon_dir
        if o_loc_part_lat_dir:
            _params['loc_part_lat_dir'] = o_loc_part_lat_dir
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        _params['structured'] = o_structured
        if o_a6record:
            _params['a6record'] = o_a6record
        if o_aaaarecord:
            _params['aaaarecord'] = o_aaaarecord
        if o_afsdbrecord:
            _params['afsdbrecord'] = o_afsdbrecord
        if o_aplrecord:
            _params['aplrecord'] = o_aplrecord
        if o_arecord:
            _params['arecord'] = o_arecord
        if o_certrecord:
            _params['certrecord'] = o_certrecord
        if o_cnamerecord:
            _params['cnamerecord'] = o_cnamerecord
        if o_dhcidrecord:
            _params['dhcidrecord'] = o_dhcidrecord
        if o_dlvrecord:
            _params['dlvrecord'] = o_dlvrecord
        if o_dnamerecord:
            _params['dnamerecord'] = o_dnamerecord
        if o_dsrecord:
            _params['dsrecord'] = o_dsrecord
        if o_hiprecord:
            _params['hiprecord'] = o_hiprecord
        if o_ipseckeyrecord:
            _params['ipseckeyrecord'] = o_ipseckeyrecord
        if o_dnsttl:
            _params['dnsttl'] = o_dnsttl
        if o_keyrecord:
            _params['keyrecord'] = o_keyrecord
        if o_kxrecord:
            _params['kxrecord'] = o_kxrecord
        if o_locrecord:
            _params['locrecord'] = o_locrecord
        if o_mxrecord:
            _params['mxrecord'] = o_mxrecord
        if o_naptrrecord:
            _params['naptrrecord'] = o_naptrrecord
        if o_nsecrecord:
            _params['nsecrecord'] = o_nsecrecord
        if o_nsrecord:
            _params['nsrecord'] = o_nsrecord
        if o_ptrrecord:
            _params['ptrrecord'] = o_ptrrecord
        if o_rprecord:
            _params['rprecord'] = o_rprecord
        if o_rrsigrecord:
            _params['rrsigrecord'] = o_rrsigrecord
        if o_sigrecord:
            _params['sigrecord'] = o_sigrecord
        if o_spfrecord:
            _params['spfrecord'] = o_spfrecord
        if o_srvrecord:
            _params['srvrecord'] = o_srvrecord
        if o_sshfprecord:
            _params['sshfprecord'] = o_sshfprecord
        if o_dnsclass:
            _params['dnsclass'] = o_dnsclass
        if o_tlsarecord:
            _params['tlsarecord'] = o_tlsarecord
        if o_txtrecord:
            _params['txtrecord'] = o_txtrecord
        if o_urirecord:
            _params['urirecord'] = o_urirecord

        return self._request(method, _args, _params)

    def dnsrecord_show(
            self,
            a_dnszoneidnsname,
            a_idnsname,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_structured=False,
    ):
        """Display DNS resource.
        :param a_dnszoneidnsname: Zone name (FQDN)
        :type  a_dnszoneidnsname: DNSNameParam
        :param a_idnsname: Record name
        :type  a_idnsname: DNSNameParam
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_structured: Parse all raw DNS records and return them in a structured way
        :type  o_structured: bool
        """
        method = 'dnsrecord_show'

        _args = list()
        _args.append(a_dnszoneidnsname)
        _args.append(a_idnsname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        _params['structured'] = o_structured

        return self._request(method, _args, _params)

    def dnsrecord_split_parts(
            self,
            a_name,
            a_value,
    ):
        """None
        :param a_name: <name>
        :type  a_name: str
        :param a_value: <value>
        :type  a_value: str
        """
        method = 'dnsrecord_split_parts'

        _args = list()
        _args.append(a_name)
        _args.append(a_value)

        _params = dict()

        return self._request(method, _args, _params)

    def dnsserver_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_idnssoamname=None,
            o_idnsforwarders=None,
            o_idnsserverid=None,
            o_idnsforwardpolicy=None,
    ):
        """Search for DNS servers.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("hostname")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_idnssoamname: SOA mname (authoritative server) override
        :type  o_idnssoamname: DNSNameParam
        :param o_idnsforwarders: Per-server forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_idnsserverid: DNS Server name
        :type  o_idnsserverid: str
        :param o_idnsforwardpolicy: Per-server conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        """
        method = 'dnsserver_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_idnssoamname:
            _params['idnssoamname'] = o_idnssoamname
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_idnsserverid:
            _params['idnsserverid'] = o_idnsserverid
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy

        return self._request(method, _args, _params)

    def dnsserver_mod(
            self,
            a_idnsserverid,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_idnssoamname=None,
            o_idnsforwarders=None,
            o_idnsforwardpolicy=None,
    ):
        """Modify DNS server configuration
        :param a_idnsserverid: DNS Server name
        :type  a_idnsserverid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_idnssoamname: SOA mname (authoritative server) override
        :type  o_idnssoamname: DNSNameParam
        :param o_idnsforwarders: Per-server forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_idnsforwardpolicy: Per-server conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        """
        method = 'dnsserver_mod'

        _args = list()
        _args.append(a_idnsserverid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_idnssoamname:
            _params['idnssoamname'] = o_idnssoamname
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy

        return self._request(method, _args, _params)

    def dnsserver_show(
            self,
            a_idnsserverid,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display configuration of a DNS server.
        :param a_idnsserverid: DNS Server name
        :type  a_idnsserverid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'dnsserver_show'

        _args = list()
        _args.append(a_idnsserverid)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def dnszone_add(
            self,
            a_idnsname,
            o_idnssoaserial,
            o_addattr=None,
            o_ip_address=None,
            o_name_from_ip=None,
            o_setattr=None,
            o_all=True,
            o_force=False,
            o_raw=False,
            o_skip_nameserver_check=False,
            o_skip_overlap_check=False,
            o_idnsallowsyncptr=None,
            o_idnssecinlinesigning=False,
            o_idnssoamname=None,
            o_dnsdefaultttl=None,
            o_dnsttl=None,
            o_idnsforwarders=None,
            o_nsec3paramrecord=None,
            o_dnsclass=None,
            o_idnsforwardpolicy=None,
            o_idnsallowdynupdate=False,
            o_idnssoarname='',
            o_idnssoaexpire=1209600,
            o_idnssoaminimum=3600,
            o_idnssoarefresh=3600,
            o_idnssoaretry=900,
            o_idnsallowquery='any;',
            o_idnsallowtransfer='none;',
            o_idnsupdatepolicy=None,
    ):
        """Create new DNS zone (SOA record).
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_ip_address: <ip_address>
        :type  o_ip_address: str
        :param o_name_from_ip: IP network to create reverse zone name from
        :type  o_name_from_ip: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_force: Force DNS zone creation even if nameserver is not resolvable. (Deprecated)
        :type  o_force: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_skip_nameserver_check: Force DNS zone creation even if nameserver is not resolvable.
        :type  o_skip_nameserver_check: bool
        :param o_skip_overlap_check: Force DNS zone creation even if it will overlap with an existing zone.
        :type  o_skip_overlap_check: bool
        :param o_idnsallowsyncptr: Allow synchronization of forward (A, AAAA) and reverse (PTR) records in the zone
        :type  o_idnsallowsyncptr: Bool
        :param o_idnssecinlinesigning: Allow inline DNSSEC signing of records in the zone
        :type  o_idnssecinlinesigning: Bool
        :param o_idnssoamname: Authoritative nameserver domain name
        :type  o_idnssoamname: DNSNameParam
        :param o_dnsdefaultttl: Time to live for records without explicit TTL definition
        :type  o_dnsdefaultttl: int, min value 0, max value 2147483647
        :param o_dnsttl: Time to live for records at zone apex
        :type  o_dnsttl: int, min value 0, max value 2147483647
        :param o_idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_nsec3paramrecord: NSEC3PARAM record for zone in format: hash_algorithm flags iterations salt
        :type  o_nsec3paramrecord: str
        :param o_dnsclass: <dnsclass>
        :type  o_dnsclass: str, valid values ['IN', 'CS', 'CH', 'HS']
        :param o_idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        :param o_idnsallowdynupdate: Allow dynamic updates.
        :type  o_idnsallowdynupdate: Bool
        :param o_idnssoarname: Administrator e-mail address
        :type  o_idnssoarname: DNSNameParam
        :param o_idnssoaexpire: SOA record expire time
        :type  o_idnssoaexpire: int, min value 0, max value 2147483647
        :param o_idnssoaminimum: How long should negative responses be cached
        :type  o_idnssoaminimum: int, min value 0, max value 2147483647
        :param o_idnssoarefresh: SOA record refresh time
        :type  o_idnssoarefresh: int, min value 0, max value 2147483647
        :param o_idnssoaretry: SOA record retry time
        :type  o_idnssoaretry: int, min value 0, max value 2147483647
        :param o_idnssoaserial: SOA record serial number
        :type  o_idnssoaserial: int, min value 1, max value 4294967295
        :param o_idnsallowquery: Semicolon separated list of IP addresses or networks which are allowed to issue queries
        :type  o_idnsallowquery: str
        :param o_idnsallowtransfer: Semicolon separated list of IP addresses or networks which are allowed to transfer the zone
        :type  o_idnsallowtransfer: str
        :param o_idnsupdatepolicy: BIND update policy
        :type  o_idnsupdatepolicy: str
        """
        method = 'dnszone_add'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_ip_address:
            _params['ip_address'] = o_ip_address
        if o_name_from_ip:
            _params['name_from_ip'] = o_name_from_ip
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['force'] = o_force
        _params['raw'] = o_raw
        _params['skip_nameserver_check'] = o_skip_nameserver_check
        _params['skip_overlap_check'] = o_skip_overlap_check
        if o_idnsallowsyncptr:
            _params['idnsallowsyncptr'] = o_idnsallowsyncptr
        if o_idnssecinlinesigning:
            _params['idnssecinlinesigning'] = o_idnssecinlinesigning
        if o_idnssoamname:
            _params['idnssoamname'] = o_idnssoamname
        if o_dnsdefaultttl:
            _params['dnsdefaultttl'] = o_dnsdefaultttl
        if o_dnsttl:
            _params['dnsttl'] = o_dnsttl
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_nsec3paramrecord:
            _params['nsec3paramrecord'] = o_nsec3paramrecord
        if o_dnsclass:
            _params['dnsclass'] = o_dnsclass
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy
        if o_idnsallowdynupdate:
            _params['idnsallowdynupdate'] = o_idnsallowdynupdate
        _params['idnssoarname'] = o_idnssoarname
        _params['idnssoaexpire'] = o_idnssoaexpire
        _params['idnssoaminimum'] = o_idnssoaminimum
        _params['idnssoarefresh'] = o_idnssoarefresh
        _params['idnssoaretry'] = o_idnssoaretry
        _params['idnssoaserial'] = o_idnssoaserial
        if o_idnsallowquery:
            _params['idnsallowquery'] = o_idnsallowquery
        if o_idnsallowtransfer:
            _params['idnsallowtransfer'] = o_idnsallowtransfer
        if o_idnsupdatepolicy:
            _params['idnsupdatepolicy'] = o_idnsupdatepolicy

        return self._request(method, _args, _params)

    def dnszone_add_permission(
            self,
            a_idnsname,
    ):
        """Add a permission for per-zone access delegation.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        """
        method = 'dnszone_add_permission'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()

        return self._request(method, _args, _params)

    def dnszone_del(
            self,
            a_idnsname,
            o_continue=False,
    ):
        """Delete DNS zone (SOA record).
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'dnszone_del'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def dnszone_disable(
            self,
            a_idnsname,
    ):
        """Disable DNS Zone.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        """
        method = 'dnszone_disable'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()

        return self._request(method, _args, _params)

    def dnszone_enable(
            self,
            a_idnsname,
    ):
        """Enable DNS Zone.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        """
        method = 'dnszone_enable'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()

        return self._request(method, _args, _params)

    def dnszone_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_name_from_ip=None,
            o_all=True,
            o_forward_only=False,
            o_pkey_only=False,
            o_raw=False,
            o_idnsallowsyncptr=None,
            o_idnssecinlinesigning=False,
            o_idnsallowdynupdate=False,
            o_idnszoneactive=None,
            o_idnssoarname='',
            o_idnsname=None,
            o_idnssoamname=None,
            o_dnsdefaultttl=None,
            o_idnssoaexpire=1209600,
            o_idnssoaminimum=3600,
            o_idnssoarefresh=3600,
            o_idnssoaretry=900,
            o_idnssoaserial=None,
            o_dnsttl=None,
            o_idnsallowquery='any;',
            o_idnsallowtransfer='none;',
            o_idnsforwarders=None,
            o_nsec3paramrecord=None,
            o_idnsupdatepolicy=None,
            o_dnsclass=None,
            o_idnsforwardpolicy=None,
    ):
        """Search for DNS zones (SOA records).
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_name_from_ip: IP network to create reverse zone name from
        :type  o_name_from_ip: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_forward_only: Search for forward zones only
        :type  o_forward_only: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_idnsallowsyncptr: Allow synchronization of forward (A, AAAA) and reverse (PTR) records in the zone
        :type  o_idnsallowsyncptr: Bool
        :param o_idnssecinlinesigning: Allow inline DNSSEC signing of records in the zone
        :type  o_idnssecinlinesigning: Bool
        :param o_idnsallowdynupdate: Allow dynamic updates.
        :type  o_idnsallowdynupdate: Bool
        :param o_idnszoneactive: Is zone active?
        :type  o_idnszoneactive: Bool
        :param o_idnssoarname: Administrator e-mail address
        :type  o_idnssoarname: DNSNameParam
        :param o_idnsname: Zone name (FQDN)
        :type  o_idnsname: DNSNameParam
        :param o_idnssoamname: Authoritative nameserver domain name
        :type  o_idnssoamname: DNSNameParam
        :param o_dnsdefaultttl: Time to live for records without explicit TTL definition
        :type  o_dnsdefaultttl: int, min value 0, max value 2147483647
        :param o_idnssoaexpire: SOA record expire time
        :type  o_idnssoaexpire: int, min value 0, max value 2147483647
        :param o_idnssoaminimum: How long should negative responses be cached
        :type  o_idnssoaminimum: int, min value 0, max value 2147483647
        :param o_idnssoarefresh: SOA record refresh time
        :type  o_idnssoarefresh: int, min value 0, max value 2147483647
        :param o_idnssoaretry: SOA record retry time
        :type  o_idnssoaretry: int, min value 0, max value 2147483647
        :param o_idnssoaserial: SOA record serial number
        :type  o_idnssoaserial: int, min value 1, max value 4294967295
        :param o_dnsttl: Time to live for records at zone apex
        :type  o_dnsttl: int, min value 0, max value 2147483647
        :param o_idnsallowquery: Semicolon separated list of IP addresses or networks which are allowed to issue queries
        :type  o_idnsallowquery: str
        :param o_idnsallowtransfer: Semicolon separated list of IP addresses or networks which are allowed to transfer the zone
        :type  o_idnsallowtransfer: str
        :param o_idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_nsec3paramrecord: NSEC3PARAM record for zone in format: hash_algorithm flags iterations salt
        :type  o_nsec3paramrecord: str
        :param o_idnsupdatepolicy: BIND update policy
        :type  o_idnsupdatepolicy: str
        :param o_dnsclass: <dnsclass>
        :type  o_dnsclass: str, valid values ['IN', 'CS', 'CH', 'HS']
        :param o_idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        """
        method = 'dnszone_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_name_from_ip:
            _params['name_from_ip'] = o_name_from_ip
        _params['all'] = o_all
        _params['forward_only'] = o_forward_only
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_idnsallowsyncptr:
            _params['idnsallowsyncptr'] = o_idnsallowsyncptr
        if o_idnssecinlinesigning:
            _params['idnssecinlinesigning'] = o_idnssecinlinesigning
        if o_idnsallowdynupdate:
            _params['idnsallowdynupdate'] = o_idnsallowdynupdate
        if o_idnszoneactive:
            _params['idnszoneactive'] = o_idnszoneactive
        if o_idnssoarname:
            _params['idnssoarname'] = o_idnssoarname
        if o_idnsname:
            _params['idnsname'] = o_idnsname
        if o_idnssoamname:
            _params['idnssoamname'] = o_idnssoamname
        if o_dnsdefaultttl:
            _params['dnsdefaultttl'] = o_dnsdefaultttl
        if o_idnssoaexpire:
            _params['idnssoaexpire'] = o_idnssoaexpire
        if o_idnssoaminimum:
            _params['idnssoaminimum'] = o_idnssoaminimum
        if o_idnssoarefresh:
            _params['idnssoarefresh'] = o_idnssoarefresh
        if o_idnssoaretry:
            _params['idnssoaretry'] = o_idnssoaretry
        if o_idnssoaserial:
            _params['idnssoaserial'] = o_idnssoaserial
        if o_dnsttl:
            _params['dnsttl'] = o_dnsttl
        if o_idnsallowquery:
            _params['idnsallowquery'] = o_idnsallowquery
        if o_idnsallowtransfer:
            _params['idnsallowtransfer'] = o_idnsallowtransfer
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_nsec3paramrecord:
            _params['nsec3paramrecord'] = o_nsec3paramrecord
        if o_idnsupdatepolicy:
            _params['idnsupdatepolicy'] = o_idnsupdatepolicy
        if o_dnsclass:
            _params['dnsclass'] = o_dnsclass
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy

        return self._request(method, _args, _params)

    def dnszone_mod(
            self,
            a_idnsname,
            o_addattr=None,
            o_delattr=None,
            o_name_from_ip=None,
            o_setattr=None,
            o_all=True,
            o_force=False,
            o_raw=False,
            o_rights=False,
            o_idnsallowsyncptr=None,
            o_idnssecinlinesigning=False,
            o_idnsallowdynupdate=False,
            o_idnssoarname='',
            o_idnssoamname=None,
            o_dnsdefaultttl=None,
            o_idnssoaexpire=1209600,
            o_idnssoaminimum=3600,
            o_idnssoarefresh=3600,
            o_idnssoaretry=900,
            o_idnssoaserial=None,
            o_dnsttl=None,
            o_idnsallowquery='any;',
            o_idnsallowtransfer='none;',
            o_idnsforwarders=None,
            o_nsec3paramrecord=None,
            o_idnsupdatepolicy=None,
            o_dnsclass=None,
            o_idnsforwardpolicy=None,
    ):
        """Modify DNS zone (SOA record).
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_name_from_ip: IP network to create reverse zone name from
        :type  o_name_from_ip: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_force: Force nameserver change even if nameserver not in DNS
        :type  o_force: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_idnsallowsyncptr: Allow synchronization of forward (A, AAAA) and reverse (PTR) records in the zone
        :type  o_idnsallowsyncptr: Bool
        :param o_idnssecinlinesigning: Allow inline DNSSEC signing of records in the zone
        :type  o_idnssecinlinesigning: Bool
        :param o_idnsallowdynupdate: Allow dynamic updates.
        :type  o_idnsallowdynupdate: Bool
        :param o_idnssoarname: Administrator e-mail address
        :type  o_idnssoarname: DNSNameParam
        :param o_idnssoamname: Authoritative nameserver domain name
        :type  o_idnssoamname: DNSNameParam
        :param o_dnsdefaultttl: Time to live for records without explicit TTL definition
        :type  o_dnsdefaultttl: int, min value 0, max value 2147483647
        :param o_idnssoaexpire: SOA record expire time
        :type  o_idnssoaexpire: int, min value 0, max value 2147483647
        :param o_idnssoaminimum: How long should negative responses be cached
        :type  o_idnssoaminimum: int, min value 0, max value 2147483647
        :param o_idnssoarefresh: SOA record refresh time
        :type  o_idnssoarefresh: int, min value 0, max value 2147483647
        :param o_idnssoaretry: SOA record retry time
        :type  o_idnssoaretry: int, min value 0, max value 2147483647
        :param o_idnssoaserial: SOA record serial number
        :type  o_idnssoaserial: int, min value 1, max value 4294967295
        :param o_dnsttl: Time to live for records at zone apex
        :type  o_dnsttl: int, min value 0, max value 2147483647
        :param o_idnsallowquery: Semicolon separated list of IP addresses or networks which are allowed to issue queries
        :type  o_idnsallowquery: str
        :param o_idnsallowtransfer: Semicolon separated list of IP addresses or networks which are allowed to transfer the zone
        :type  o_idnsallowtransfer: str
        :param o_idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type  o_idnsforwarders: str
        :param o_nsec3paramrecord: NSEC3PARAM record for zone in format: hash_algorithm flags iterations salt
        :type  o_nsec3paramrecord: str
        :param o_idnsupdatepolicy: BIND update policy
        :type  o_idnsupdatepolicy: str
        :param o_dnsclass: <dnsclass>
        :type  o_dnsclass: str, valid values ['IN', 'CS', 'CH', 'HS']
        :param o_idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type  o_idnsforwardpolicy: str, valid values ['only', 'first', 'none']
        """
        method = 'dnszone_mod'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_name_from_ip:
            _params['name_from_ip'] = o_name_from_ip
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['force'] = o_force
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_idnsallowsyncptr:
            _params['idnsallowsyncptr'] = o_idnsallowsyncptr
        if o_idnssecinlinesigning:
            _params['idnssecinlinesigning'] = o_idnssecinlinesigning
        if o_idnsallowdynupdate:
            _params['idnsallowdynupdate'] = o_idnsallowdynupdate
        if o_idnssoarname:
            _params['idnssoarname'] = o_idnssoarname
        if o_idnssoamname:
            _params['idnssoamname'] = o_idnssoamname
        if o_dnsdefaultttl:
            _params['dnsdefaultttl'] = o_dnsdefaultttl
        if o_idnssoaexpire:
            _params['idnssoaexpire'] = o_idnssoaexpire
        if o_idnssoaminimum:
            _params['idnssoaminimum'] = o_idnssoaminimum
        if o_idnssoarefresh:
            _params['idnssoarefresh'] = o_idnssoarefresh
        if o_idnssoaretry:
            _params['idnssoaretry'] = o_idnssoaretry
        if o_idnssoaserial:
            _params['idnssoaserial'] = o_idnssoaserial
        if o_dnsttl:
            _params['dnsttl'] = o_dnsttl
        if o_idnsallowquery:
            _params['idnsallowquery'] = o_idnsallowquery
        if o_idnsallowtransfer:
            _params['idnsallowtransfer'] = o_idnsallowtransfer
        if o_idnsforwarders:
            _params['idnsforwarders'] = o_idnsforwarders
        if o_nsec3paramrecord:
            _params['nsec3paramrecord'] = o_nsec3paramrecord
        if o_idnsupdatepolicy:
            _params['idnsupdatepolicy'] = o_idnsupdatepolicy
        if o_dnsclass:
            _params['dnsclass'] = o_dnsclass
        if o_idnsforwardpolicy:
            _params['idnsforwardpolicy'] = o_idnsforwardpolicy

        return self._request(method, _args, _params)

    def dnszone_remove_permission(
            self,
            a_idnsname,
    ):
        """Remove a permission for per-zone access delegation.
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        """
        method = 'dnszone_remove_permission'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()

        return self._request(method, _args, _params)

    def dnszone_show(
            self,
            a_idnsname,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a DNS zone (SOA record).
        :param a_idnsname: Zone name (FQDN)
        :type  a_idnsname: DNSNameParam
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'dnszone_show'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def domainlevel_get(
            self,
    ):
        """Query current Domain Level.
        """
        method = 'domainlevel_get'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def domainlevel_set(
            self,
            a_ipadomainlevel,
    ):
        """Change current Domain Level.
        :param a_ipadomainlevel: Domain Level
        :type  a_ipadomainlevel: int, min value 0, max value 2147483647
        """
        method = 'domainlevel_set'

        _args = list()
        _args.append(a_ipadomainlevel)

        _params = dict()

        return self._request(method, _args, _params)

    def env(
            self,
            o_all=True,
            o_server=False,
    ):
        """Show environment variables.
        :param o_all: retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_server: Forward to server instead of running locally
        :type  o_server: bool
        """
        method = 'env'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        if o_server:
            _params['server'] = o_server

        return self._request(method, _args, _params)

    def group_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_external=False,
            o_no_members=False,
            o_nonposix=False,
            o_raw=False,
            o_gidnumber=None,
            o_description=None,
    ):
        """Create a new group.
        :param a_cn: Group name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_external: Allow adding external non-IPA members from trusted domains
        :type  o_external: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_nonposix: Create as a non-POSIX group
        :type  o_nonposix: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_gidnumber: GID (use this option to set it manually)
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_description: Group description
        :type  o_description: str
        """
        method = 'group_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['external'] = o_external
        _params['no_members'] = o_no_members
        _params['nonposix'] = o_nonposix
        _params['raw'] = o_raw
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def group_add_member(
            self,
            a_cn,
            o_ipaexternalmember=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Add members to a group.
        :param a_cn: Group name
        :type  a_cn: str
        :param o_ipaexternalmember: Members of a trusted domain in DOM\name or name@domain form
        :type  o_ipaexternalmember: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'group_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_ipaexternalmember:
            _params['ipaexternalmember'] = o_ipaexternalmember
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def group_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete group.
        :param a_cn: Group name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'group_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def group_detach(
            self,
            a_cn,
    ):
        """Detach a managed group from a user.
        :param a_cn: Group name
        :type  a_cn: str
        """
        method = 'group_detach'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def group_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_group=None,
            o_in_group=None,
            o_in_hbacrule=None,
            o_in_netgroup=None,
            o_in_role=None,
            o_in_sudorule=None,
            o_no_group=None,
            o_no_user=None,
            o_not_in_group=None,
            o_not_in_hbacrule=None,
            o_not_in_netgroup=None,
            o_not_in_role=None,
            o_not_in_sudorule=None,
            o_user=None,
            o_all=True,
            o_external=False,
            o_no_members=True,
            o_nonposix=False,
            o_pkey_only=False,
            o_posix=False,
            o_private=False,
            o_raw=False,
            o_gidnumber=None,
            o_description=None,
            o_cn=None,
    ):
        """Search for groups.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_group: Search for groups with these member groups.
        :type  o_group: str
        :param o_in_group: Search for groups with these member of groups.
        :type  o_in_group: str
        :param o_in_hbacrule: Search for groups with these member of HBAC rules.
        :type  o_in_hbacrule: str
        :param o_in_netgroup: Search for groups with these member of netgroups.
        :type  o_in_netgroup: str
        :param o_in_role: Search for groups with these member of roles.
        :type  o_in_role: str
        :param o_in_sudorule: Search for groups with these member of sudo rules.
        :type  o_in_sudorule: str
        :param o_no_group: Search for groups without these member groups.
        :type  o_no_group: str
        :param o_no_user: Search for groups without these member users.
        :type  o_no_user: str
        :param o_not_in_group: Search for groups without these member of groups.
        :type  o_not_in_group: str
        :param o_not_in_hbacrule: Search for groups without these member of HBAC rules.
        :type  o_not_in_hbacrule: str
        :param o_not_in_netgroup: Search for groups without these member of netgroups.
        :type  o_not_in_netgroup: str
        :param o_not_in_role: Search for groups without these member of roles.
        :type  o_not_in_role: str
        :param o_not_in_sudorule: Search for groups without these member of sudo rules.
        :type  o_not_in_sudorule: str
        :param o_user: Search for groups with these member users.
        :type  o_user: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_external: search for groups with support of external non-IPA members from trusted domains
        :type  o_external: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_nonposix: search for non-POSIX groups
        :type  o_nonposix: bool
        :param o_pkey_only: Results should contain primary key attribute only ("group-name")
        :type  o_pkey_only: bool
        :param o_posix: search for POSIX groups
        :type  o_posix: bool
        :param o_private: search for private groups
        :type  o_private: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_gidnumber: GID (use this option to set it manually)
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_description: Group description
        :type  o_description: str
        :param o_cn: Group name
        :type  o_cn: str
        """
        method = 'group_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_group:
            _params['group'] = o_group
        if o_in_group:
            _params['in_group'] = o_in_group
        if o_in_hbacrule:
            _params['in_hbacrule'] = o_in_hbacrule
        if o_in_netgroup:
            _params['in_netgroup'] = o_in_netgroup
        if o_in_role:
            _params['in_role'] = o_in_role
        if o_in_sudorule:
            _params['in_sudorule'] = o_in_sudorule
        if o_no_group:
            _params['no_group'] = o_no_group
        if o_no_user:
            _params['no_user'] = o_no_user
        if o_not_in_group:
            _params['not_in_group'] = o_not_in_group
        if o_not_in_hbacrule:
            _params['not_in_hbacrule'] = o_not_in_hbacrule
        if o_not_in_netgroup:
            _params['not_in_netgroup'] = o_not_in_netgroup
        if o_not_in_role:
            _params['not_in_role'] = o_not_in_role
        if o_not_in_sudorule:
            _params['not_in_sudorule'] = o_not_in_sudorule
        if o_user:
            _params['user'] = o_user
        _params['all'] = o_all
        _params['external'] = o_external
        _params['no_members'] = o_no_members
        _params['nonposix'] = o_nonposix
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['posix'] = o_posix
        _params['private'] = o_private
        _params['raw'] = o_raw
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def group_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_external=False,
            o_no_members=False,
            o_posix=False,
            o_raw=False,
            o_rights=False,
            o_gidnumber=None,
            o_description=None,
    ):
        """Modify a group.
        :param a_cn: Group name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the group object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_external: change to support external non-IPA members from trusted domains
        :type  o_external: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_posix: change to a POSIX group
        :type  o_posix: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_gidnumber: GID (use this option to set it manually)
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_description: Group description
        :type  o_description: str
        """
        method = 'group_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['external'] = o_external
        _params['no_members'] = o_no_members
        _params['posix'] = o_posix
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def group_remove_member(
            self,
            a_cn,
            o_ipaexternalmember=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Remove members from a group.
        :param a_cn: Group name
        :type  a_cn: str
        :param o_ipaexternalmember: Members of a trusted domain in DOM\name or name@domain form
        :type  o_ipaexternalmember: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'group_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_ipaexternalmember:
            _params['ipaexternalmember'] = o_ipaexternalmember
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def group_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a named group.
        :param a_cn: Group name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'group_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def hbacrule_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_externalhost=None,
            o_hostcategory=None,
            o_servicecategory=None,
            o_sourcehostcategory=None,
            o_usercategory=None,
            o_accessruletype='allow',
    ):
        """Create a new HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_servicecategory: Service category the rule applies to
        :type  o_servicecategory: str, valid values ['all']
        :param o_sourcehostcategory: Source host category the rule applies to
        :type  o_sourcehostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        :param o_accessruletype: Rule type (allow)
        :type  o_accessruletype: str, valid values ['allow', 'deny']
        """
        method = 'hbacrule_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_servicecategory:
            _params['servicecategory'] = o_servicecategory
        if o_sourcehostcategory:
            _params['sourcehostcategory'] = o_sourcehostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory
        _params['accessruletype'] = o_accessruletype

        return self._request(method, _args, _params)

    def hbacrule_add_host(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Add target hosts and hostgroups to an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        """
        method = 'hbacrule_add_host'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def hbacrule_add_service(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hbacsvcgroup=None,
            o_hbacsvc=None,
    ):
        """Add services to an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hbacsvcgroup: HBAC service groups to add
        :type  o_hbacsvcgroup: str
        :param o_hbacsvc: HBAC services to add
        :type  o_hbacsvc: str
        """
        method = 'hbacrule_add_service'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hbacsvcgroup:
            _params['hbacsvcgroup'] = o_hbacsvcgroup
        if o_hbacsvc:
            _params['hbacsvc'] = o_hbacsvc

        return self._request(method, _args, _params)

    def hbacrule_add_sourcehost(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """None
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        """
        method = 'hbacrule_add_sourcehost'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def hbacrule_add_user(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Add users and groups to an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'hbacrule_add_user'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def hbacrule_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'hbacrule_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def hbacrule_disable(
            self,
            a_cn,
    ):
        """Disable an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        """
        method = 'hbacrule_disable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def hbacrule_enable(
            self,
            a_cn,
    ):
        """Enable an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        """
        method = 'hbacrule_enable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def hbacrule_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_externalhost=None,
            o_cn=None,
            o_hostcategory=None,
            o_servicecategory=None,
            o_sourcehostcategory=None,
            o_usercategory=None,
            o_accessruletype='allow',
    ):
        """Search for HBAC rules.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_cn: Rule name
        :type  o_cn: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_servicecategory: Service category the rule applies to
        :type  o_servicecategory: str, valid values ['all']
        :param o_sourcehostcategory: Source host category the rule applies to
        :type  o_sourcehostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        :param o_accessruletype: Rule type (allow)
        :type  o_accessruletype: str, valid values ['allow', 'deny']
        """
        method = 'hbacrule_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_cn:
            _params['cn'] = o_cn
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_servicecategory:
            _params['servicecategory'] = o_servicecategory
        if o_sourcehostcategory:
            _params['sourcehostcategory'] = o_sourcehostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory
        if o_accessruletype:
            _params['accessruletype'] = o_accessruletype

        return self._request(method, _args, _params)

    def hbacrule_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_externalhost=None,
            o_hostcategory=None,
            o_servicecategory=None,
            o_sourcehostcategory=None,
            o_usercategory=None,
            o_accessruletype='allow',
    ):
        """Modify an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the HBAC rule object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_servicecategory: Service category the rule applies to
        :type  o_servicecategory: str, valid values ['all']
        :param o_sourcehostcategory: Source host category the rule applies to
        :type  o_sourcehostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        :param o_accessruletype: Rule type (allow)
        :type  o_accessruletype: str, valid values ['allow', 'deny']
        """
        method = 'hbacrule_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_servicecategory:
            _params['servicecategory'] = o_servicecategory
        if o_sourcehostcategory:
            _params['sourcehostcategory'] = o_sourcehostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory
        if o_accessruletype:
            _params['accessruletype'] = o_accessruletype

        return self._request(method, _args, _params)

    def hbacrule_remove_host(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Remove target hosts and hostgroups from an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        """
        method = 'hbacrule_remove_host'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def hbacrule_remove_service(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hbacsvcgroup=None,
            o_hbacsvc=None,
    ):
        """Remove service and service groups from an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hbacsvcgroup: HBAC service groups to remove
        :type  o_hbacsvcgroup: str
        :param o_hbacsvc: HBAC services to remove
        :type  o_hbacsvc: str
        """
        method = 'hbacrule_remove_service'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hbacsvcgroup:
            _params['hbacsvcgroup'] = o_hbacsvcgroup
        if o_hbacsvc:
            _params['hbacsvc'] = o_hbacsvc

        return self._request(method, _args, _params)

    def hbacrule_remove_sourcehost(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """None
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        """
        method = 'hbacrule_remove_sourcehost'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def hbacrule_remove_user(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Remove users and groups from an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'hbacrule_remove_user'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def hbacrule_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display the properties of an HBAC rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'hbacrule_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def hbacsvc_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_description=None,
    ):
        """Add a new HBAC service.
        :param a_cn: HBAC service
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: HBAC service description
        :type  o_description: str
        """
        method = 'hbacsvc_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def hbacsvc_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete an existing HBAC service.
        :param a_cn: HBAC service
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'hbacsvc_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def hbacsvc_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_description=None,
            o_cn=None,
    ):
        """Search for HBAC services.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("service")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: HBAC service description
        :type  o_description: str
        :param o_cn: HBAC service
        :type  o_cn: str
        """
        method = 'hbacsvc_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def hbacsvc_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify an HBAC service.
        :param a_cn: HBAC service
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: HBAC service description
        :type  o_description: str
        """
        method = 'hbacsvc_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def hbacsvc_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about an HBAC service.
        :param a_cn: HBAC service
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'hbacsvc_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def hbacsvcgroup_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_description=None,
    ):
        """Add a new HBAC service group.
        :param a_cn: Service group name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: HBAC service group description
        :type  o_description: str
        """
        method = 'hbacsvcgroup_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def hbacsvcgroup_add_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hbacsvc=None,
    ):
        """Add members to an HBAC service group.
        :param a_cn: Service group name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hbacsvc: HBAC services to add
        :type  o_hbacsvc: str
        """
        method = 'hbacsvcgroup_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hbacsvc:
            _params['hbacsvc'] = o_hbacsvc

        return self._request(method, _args, _params)

    def hbacsvcgroup_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete an HBAC service group.
        :param a_cn: Service group name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'hbacsvcgroup_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def hbacsvcgroup_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_description=None,
            o_cn=None,
    ):
        """Search for an HBAC service group.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: HBAC service group description
        :type  o_description: str
        :param o_cn: Service group name
        :type  o_cn: str
        """
        method = 'hbacsvcgroup_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def hbacsvcgroup_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify an HBAC service group.
        :param a_cn: Service group name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: HBAC service group description
        :type  o_description: str
        """
        method = 'hbacsvcgroup_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def hbacsvcgroup_remove_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hbacsvc=None,
    ):
        """Remove members from an HBAC service group.
        :param a_cn: Service group name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hbacsvc: HBAC services to remove
        :type  o_hbacsvc: str
        """
        method = 'hbacsvcgroup_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hbacsvc:
            _params['hbacsvc'] = o_hbacsvc

        return self._request(method, _args, _params)

    def hbacsvcgroup_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about an HBAC service group.
        :param a_cn: Service group name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'hbacsvcgroup_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def hbactest(
            self,
            o_targethost,
            o_service,
            o_user,
            o_sizelimit=None,
            o_rules=None,
            o_sourcehost=None,
            o_disabled=False,
            o_enabled=False,
            o_nodetail=False,
    ):
        """Simulate use of Host-based access controls
        :param o_sizelimit: Maximum number of rules to process when no --rules is specified
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_targethost: Target host
        :type  o_targethost: str
        :param o_rules: Rules to test. If not specified, --enabled is assumed
        :type  o_rules: str
        :param o_service: Service
        :type  o_service: str
        :param o_sourcehost: Source host
        :type  o_sourcehost: str
        :param o_user: User name
        :type  o_user: str
        :param o_disabled: Include all disabled IPA rules into test
        :type  o_disabled: bool
        :param o_enabled: Include all enabled IPA rules into test [default]
        :type  o_enabled: bool
        :param o_nodetail: Hide details which rules are matched, not matched, or invalid
        :type  o_nodetail: bool
        """
        method = 'hbactest'

        _args = list()

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        _params['targethost'] = o_targethost
        if o_rules:
            _params['rules'] = o_rules
        _params['service'] = o_service
        if o_sourcehost:
            _params['sourcehost'] = o_sourcehost
        _params['user'] = o_user
        if o_disabled:
            _params['disabled'] = o_disabled
        if o_enabled:
            _params['enabled'] = o_enabled
        if o_nodetail:
            _params['nodetail'] = o_nodetail

        return self._request(method, _args, _params)

    def host_add(
            self,
            a_fqdn,
            o_ipakrbokasdelegate=None,
            o_ipakrboktoauthasdelegate=None,
            o_ipakrbrequirespreauth=None,
            o_addattr=None,
            o_ip_address=None,
            o_setattr=None,
            o_all=True,
            o_force=False,
            o_no_members=False,
            o_no_reverse=False,
            o_random=False,
            o_raw=False,
            o_usercertificate=None,
            o_krbprincipalauthind=None,
            o_userclass=None,
            o_description=None,
            o_ipaassignedidview=None,
            o_l=None,
            o_nshostlocation=None,
            o_macaddress=None,
            o_nsosversion=None,
            o_userpassword=None,
            o_nshardwareplatform=None,
            o_ipasshpubkey=None,
    ):
        """Add a new host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_ipakrbokasdelegate: Client credentials may be delegated to the service
        :type  o_ipakrbokasdelegate: Bool
        :param o_ipakrboktoauthasdelegate: The service is allowed to authenticate on behalf of a client
        :type  o_ipakrboktoauthasdelegate: Bool
        :param o_ipakrbrequirespreauth: Pre-authentication is required for the service
        :type  o_ipakrbrequirespreauth: Bool
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_ip_address: Add the host to DNS with this IP address
        :type  o_ip_address: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_force: force host name even if not in DNS
        :type  o_force: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_no_reverse: skip reverse DNS detection
        :type  o_no_reverse: bool
        :param o_random: Generate a random password to be used in bulk enrollment
        :type  o_random: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded host certificate
        :type  o_usercertificate: Certificate
        :param o_krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type  o_krbprincipalauthind: str
        :param o_userclass: Host category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_description: A description of this host
        :type  o_description: str
        :param o_ipaassignedidview: Assigned ID View
        :type  o_ipaassignedidview: str
        :param o_l: Host locality (e.g. "Baltimore, MD")
        :type  o_l: str
        :param o_nshostlocation: Host location (e.g. "Lab 2")
        :type  o_nshostlocation: str
        :param o_macaddress: Hardware MAC address(es) on this host
        :type  o_macaddress: str
        :param o_nsosversion: Host operating system and version (e.g. "Fedora 9")
        :type  o_nsosversion: str
        :param o_userpassword: Password used in bulk enrollment
        :type  o_userpassword: str
        :param o_nshardwareplatform: Host hardware platform (e.g. "Lenovo T61")
        :type  o_nshardwareplatform: str
        :param o_ipasshpubkey: SSH public key
        :type  o_ipasshpubkey: str
        """
        method = 'host_add'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        if o_ipakrbokasdelegate:
            _params['ipakrbokasdelegate'] = o_ipakrbokasdelegate
        if o_ipakrboktoauthasdelegate:
            _params['ipakrboktoauthasdelegate'] = o_ipakrboktoauthasdelegate
        if o_ipakrbrequirespreauth:
            _params['ipakrbrequirespreauth'] = o_ipakrbrequirespreauth
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_ip_address:
            _params['ip_address'] = o_ip_address
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['force'] = o_force
        _params['no_members'] = o_no_members
        _params['no_reverse'] = o_no_reverse
        if o_random:
            _params['random'] = o_random
        _params['raw'] = o_raw
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbprincipalauthind:
            _params['krbprincipalauthind'] = o_krbprincipalauthind
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_description:
            _params['description'] = o_description
        if o_ipaassignedidview:
            _params['ipaassignedidview'] = o_ipaassignedidview
        if o_l:
            _params['l'] = o_l
        if o_nshostlocation:
            _params['nshostlocation'] = o_nshostlocation
        if o_macaddress:
            _params['macaddress'] = o_macaddress
        if o_nsosversion:
            _params['nsosversion'] = o_nsosversion
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_nshardwareplatform:
            _params['nshardwareplatform'] = o_nshardwareplatform
        if o_ipasshpubkey:
            _params['ipasshpubkey'] = o_ipasshpubkey

        return self._request(method, _args, _params)

    def host_add_cert(
            self,
            a_fqdn,
            o_usercertificate,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add certificates to host entry
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded host certificate
        :type  o_usercertificate: Certificate
        """
        method = 'host_add_cert'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def host_add_managedby(
            self,
            a_fqdn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_host=None,
    ):
        """Add hosts that can manage this host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_host: hosts to add
        :type  o_host: str
        """
        method = 'host_add_managedby'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def host_add_principal(
            self,
            a_fqdn,
            a_krbprincipalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add new principal alias to host entry
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param a_krbprincipalname: Principal alias
        :type  a_krbprincipalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'host_add_principal'

        _args = list()
        _args.append(a_fqdn)
        _args.append(a_krbprincipalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def host_allow_create_keytab(
            self,
            a_fqdn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_user=None,
    ):
        """Allow users, groups, hosts or host groups to create a keytab of this host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'host_allow_create_keytab'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def host_allow_retrieve_keytab(
            self,
            a_fqdn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_user=None,
    ):
        """Allow users, groups, hosts or host groups to retrieve a keytab of this host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'host_allow_retrieve_keytab'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def host_del(
            self,
            a_fqdn,
            o_continue=False,
            o_updatedns=False,
    ):
        """Delete a host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        :param o_updatedns: Remove A, AAAA, SSHFP and PTR records of the host(s) managed by IPA DNS
        :type  o_updatedns: bool
        """
        method = 'host_del'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['continue'] = o_continue
        if o_updatedns:
            _params['updatedns'] = o_updatedns

        return self._request(method, _args, _params)

    def host_disable(
            self,
            a_fqdn,
    ):
        """Disable the Kerberos key, SSL certificate and all services of a host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        """
        method = 'host_disable'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()

        return self._request(method, _args, _params)

    def host_disallow_create_keytab(
            self,
            a_fqdn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_user=None,
    ):
        """Disallow users, groups, hosts or host groups to create a keytab of this host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'host_disallow_create_keytab'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def host_disallow_retrieve_keytab(
            self,
            a_fqdn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_user=None,
    ):
        """Disallow users, groups, hosts or host groups to retrieve a keytab of this host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'host_disallow_retrieve_keytab'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def host_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_enroll_by_user=None,
            o_in_hbacrule=None,
            o_in_hostgroup=None,
            o_in_netgroup=None,
            o_in_role=None,
            o_in_sudorule=None,
            o_man_by_host=None,
            o_man_host=None,
            o_not_enroll_by_user=None,
            o_not_in_hbacrule=None,
            o_not_in_hostgroup=None,
            o_not_in_netgroup=None,
            o_not_in_role=None,
            o_not_in_sudorule=None,
            o_not_man_by_host=None,
            o_not_man_host=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_usercertificate=None,
            o_krbprincipalauthind=None,
            o_userclass=None,
            o_description=None,
            o_fqdn=None,
            o_ipaassignedidview=None,
            o_l=None,
            o_nshostlocation=None,
            o_macaddress=None,
            o_nsosversion=None,
            o_userpassword=None,
            o_nshardwareplatform=None,
    ):
        """Search for hosts.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_enroll_by_user: Search for hosts with these enrolled by users.
        :type  o_enroll_by_user: str
        :param o_in_hbacrule: Search for hosts with these member of HBAC rules.
        :type  o_in_hbacrule: str
        :param o_in_hostgroup: Search for hosts with these member of host groups.
        :type  o_in_hostgroup: str
        :param o_in_netgroup: Search for hosts with these member of netgroups.
        :type  o_in_netgroup: str
        :param o_in_role: Search for hosts with these member of roles.
        :type  o_in_role: str
        :param o_in_sudorule: Search for hosts with these member of sudo rules.
        :type  o_in_sudorule: str
        :param o_man_by_host: Search for hosts with these managed by hosts.
        :type  o_man_by_host: str
        :param o_man_host: Search for hosts with these managing hosts.
        :type  o_man_host: str
        :param o_not_enroll_by_user: Search for hosts without these enrolled by users.
        :type  o_not_enroll_by_user: str
        :param o_not_in_hbacrule: Search for hosts without these member of HBAC rules.
        :type  o_not_in_hbacrule: str
        :param o_not_in_hostgroup: Search for hosts without these member of host groups.
        :type  o_not_in_hostgroup: str
        :param o_not_in_netgroup: Search for hosts without these member of netgroups.
        :type  o_not_in_netgroup: str
        :param o_not_in_role: Search for hosts without these member of roles.
        :type  o_not_in_role: str
        :param o_not_in_sudorule: Search for hosts without these member of sudo rules.
        :type  o_not_in_sudorule: str
        :param o_not_man_by_host: Search for hosts without these managed by hosts.
        :type  o_not_man_by_host: str
        :param o_not_man_host: Search for hosts without these managing hosts.
        :type  o_not_man_host: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("hostname")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded host certificate
        :type  o_usercertificate: Certificate
        :param o_krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type  o_krbprincipalauthind: str
        :param o_userclass: Host category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_description: A description of this host
        :type  o_description: str
        :param o_fqdn: Host name
        :type  o_fqdn: str
        :param o_ipaassignedidview: Assigned ID View
        :type  o_ipaassignedidview: str
        :param o_l: Host locality (e.g. "Baltimore, MD")
        :type  o_l: str
        :param o_nshostlocation: Host location (e.g. "Lab 2")
        :type  o_nshostlocation: str
        :param o_macaddress: Hardware MAC address(es) on this host
        :type  o_macaddress: str
        :param o_nsosversion: Host operating system and version (e.g. "Fedora 9")
        :type  o_nsosversion: str
        :param o_userpassword: Password used in bulk enrollment
        :type  o_userpassword: str
        :param o_nshardwareplatform: Host hardware platform (e.g. "Lenovo T61")
        :type  o_nshardwareplatform: str
        """
        method = 'host_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_enroll_by_user:
            _params['enroll_by_user'] = o_enroll_by_user
        if o_in_hbacrule:
            _params['in_hbacrule'] = o_in_hbacrule
        if o_in_hostgroup:
            _params['in_hostgroup'] = o_in_hostgroup
        if o_in_netgroup:
            _params['in_netgroup'] = o_in_netgroup
        if o_in_role:
            _params['in_role'] = o_in_role
        if o_in_sudorule:
            _params['in_sudorule'] = o_in_sudorule
        if o_man_by_host:
            _params['man_by_host'] = o_man_by_host
        if o_man_host:
            _params['man_host'] = o_man_host
        if o_not_enroll_by_user:
            _params['not_enroll_by_user'] = o_not_enroll_by_user
        if o_not_in_hbacrule:
            _params['not_in_hbacrule'] = o_not_in_hbacrule
        if o_not_in_hostgroup:
            _params['not_in_hostgroup'] = o_not_in_hostgroup
        if o_not_in_netgroup:
            _params['not_in_netgroup'] = o_not_in_netgroup
        if o_not_in_role:
            _params['not_in_role'] = o_not_in_role
        if o_not_in_sudorule:
            _params['not_in_sudorule'] = o_not_in_sudorule
        if o_not_man_by_host:
            _params['not_man_by_host'] = o_not_man_by_host
        if o_not_man_host:
            _params['not_man_host'] = o_not_man_host
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbprincipalauthind:
            _params['krbprincipalauthind'] = o_krbprincipalauthind
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_description:
            _params['description'] = o_description
        if o_fqdn:
            _params['fqdn'] = o_fqdn
        if o_ipaassignedidview:
            _params['ipaassignedidview'] = o_ipaassignedidview
        if o_l:
            _params['l'] = o_l
        if o_nshostlocation:
            _params['nshostlocation'] = o_nshostlocation
        if o_macaddress:
            _params['macaddress'] = o_macaddress
        if o_nsosversion:
            _params['nsosversion'] = o_nsosversion
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_nshardwareplatform:
            _params['nshardwareplatform'] = o_nshardwareplatform

        return self._request(method, _args, _params)

    def host_mod(
            self,
            a_fqdn,
            o_ipakrbokasdelegate=None,
            o_ipakrboktoauthasdelegate=None,
            o_ipakrbrequirespreauth=None,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_random=False,
            o_raw=False,
            o_rights=False,
            o_updatedns=False,
            o_usercertificate=None,
            o_krbprincipalname=None,
            o_krbprincipalauthind=None,
            o_userclass=None,
            o_description=None,
            o_ipaassignedidview=None,
            o_l=None,
            o_nshostlocation=None,
            o_macaddress=None,
            o_nsosversion=None,
            o_userpassword=None,
            o_nshardwareplatform=None,
            o_ipasshpubkey=None,
    ):
        """Modify information about a host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_ipakrbokasdelegate: Client credentials may be delegated to the service
        :type  o_ipakrbokasdelegate: Bool
        :param o_ipakrboktoauthasdelegate: The service is allowed to authenticate on behalf of a client
        :type  o_ipakrboktoauthasdelegate: Bool
        :param o_ipakrbrequirespreauth: Pre-authentication is required for the service
        :type  o_ipakrbrequirespreauth: Bool
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_random: Generate a random password to be used in bulk enrollment
        :type  o_random: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_updatedns: Update DNS entries
        :type  o_updatedns: bool
        :param o_usercertificate: Base-64 encoded host certificate
        :type  o_usercertificate: Certificate
        :param o_krbprincipalname: Principal alias
        :type  o_krbprincipalname: Principal
        :param o_krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type  o_krbprincipalauthind: str
        :param o_userclass: Host category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_description: A description of this host
        :type  o_description: str
        :param o_ipaassignedidview: Assigned ID View
        :type  o_ipaassignedidview: str
        :param o_l: Host locality (e.g. "Baltimore, MD")
        :type  o_l: str
        :param o_nshostlocation: Host location (e.g. "Lab 2")
        :type  o_nshostlocation: str
        :param o_macaddress: Hardware MAC address(es) on this host
        :type  o_macaddress: str
        :param o_nsosversion: Host operating system and version (e.g. "Fedora 9")
        :type  o_nsosversion: str
        :param o_userpassword: Password used in bulk enrollment
        :type  o_userpassword: str
        :param o_nshardwareplatform: Host hardware platform (e.g. "Lenovo T61")
        :type  o_nshardwareplatform: str
        :param o_ipasshpubkey: SSH public key
        :type  o_ipasshpubkey: str
        """
        method = 'host_mod'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        if o_ipakrbokasdelegate:
            _params['ipakrbokasdelegate'] = o_ipakrbokasdelegate
        if o_ipakrboktoauthasdelegate:
            _params['ipakrboktoauthasdelegate'] = o_ipakrboktoauthasdelegate
        if o_ipakrbrequirespreauth:
            _params['ipakrbrequirespreauth'] = o_ipakrbrequirespreauth
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_random:
            _params['random'] = o_random
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_updatedns:
            _params['updatedns'] = o_updatedns
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        if o_krbprincipalauthind:
            _params['krbprincipalauthind'] = o_krbprincipalauthind
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_description:
            _params['description'] = o_description
        if o_ipaassignedidview:
            _params['ipaassignedidview'] = o_ipaassignedidview
        if o_l:
            _params['l'] = o_l
        if o_nshostlocation:
            _params['nshostlocation'] = o_nshostlocation
        if o_macaddress:
            _params['macaddress'] = o_macaddress
        if o_nsosversion:
            _params['nsosversion'] = o_nsosversion
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_nshardwareplatform:
            _params['nshardwareplatform'] = o_nshardwareplatform
        if o_ipasshpubkey:
            _params['ipasshpubkey'] = o_ipasshpubkey

        return self._request(method, _args, _params)

    def host_remove_cert(
            self,
            a_fqdn,
            o_usercertificate,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove certificates from host entry
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded host certificate
        :type  o_usercertificate: Certificate
        """
        method = 'host_remove_cert'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def host_remove_managedby(
            self,
            a_fqdn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_host=None,
    ):
        """Remove hosts that can manage this host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_host: hosts to remove
        :type  o_host: str
        """
        method = 'host_remove_managedby'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def host_remove_principal(
            self,
            a_fqdn,
            a_krbprincipalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove principal alias from a host entry
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param a_krbprincipalname: Principal alias
        :type  a_krbprincipalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'host_remove_principal'

        _args = list()
        _args.append(a_fqdn)
        _args.append(a_krbprincipalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def host_show(
            self,
            a_fqdn,
            o_out=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a host.
        :param a_fqdn: Host name
        :type  a_fqdn: str
        :param o_out: file to store certificate in
        :type  o_out: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'host_show'

        _args = list()
        _args.append(a_fqdn)

        _params = dict()
        if o_out:
            _params['out'] = o_out
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def hostgroup_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_description=None,
    ):
        """Add a new hostgroup.
        :param a_cn: Name of host-group
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this host-group
        :type  o_description: str
        """
        method = 'hostgroup_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def hostgroup_add_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Add members to a hostgroup.
        :param a_cn: Name of host-group
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        """
        method = 'hostgroup_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def hostgroup_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a hostgroup.
        :param a_cn: Name of host-group
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'hostgroup_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def hostgroup_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_hostgroup=None,
            o_host=None,
            o_in_hbacrule=None,
            o_in_hostgroup=None,
            o_in_netgroup=None,
            o_in_sudorule=None,
            o_no_hostgroup=None,
            o_no_host=None,
            o_not_in_hbacrule=None,
            o_not_in_hostgroup=None,
            o_not_in_netgroup=None,
            o_not_in_sudorule=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_description=None,
            o_cn=None,
    ):
        """Search for hostgroups.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_hostgroup: Search for host groups with these member host groups.
        :type  o_hostgroup: str
        :param o_host: Search for host groups with these member hosts.
        :type  o_host: str
        :param o_in_hbacrule: Search for host groups with these member of HBAC rules.
        :type  o_in_hbacrule: str
        :param o_in_hostgroup: Search for host groups with these member of host groups.
        :type  o_in_hostgroup: str
        :param o_in_netgroup: Search for host groups with these member of netgroups.
        :type  o_in_netgroup: str
        :param o_in_sudorule: Search for host groups with these member of sudo rules.
        :type  o_in_sudorule: str
        :param o_no_hostgroup: Search for host groups without these member host groups.
        :type  o_no_hostgroup: str
        :param o_no_host: Search for host groups without these member hosts.
        :type  o_no_host: str
        :param o_not_in_hbacrule: Search for host groups without these member of HBAC rules.
        :type  o_not_in_hbacrule: str
        :param o_not_in_hostgroup: Search for host groups without these member of host groups.
        :type  o_not_in_hostgroup: str
        :param o_not_in_netgroup: Search for host groups without these member of netgroups.
        :type  o_not_in_netgroup: str
        :param o_not_in_sudorule: Search for host groups without these member of sudo rules.
        :type  o_not_in_sudorule: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("hostgroup-name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this host-group
        :type  o_description: str
        :param o_cn: Name of host-group
        :type  o_cn: str
        """
        method = 'hostgroup_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_in_hbacrule:
            _params['in_hbacrule'] = o_in_hbacrule
        if o_in_hostgroup:
            _params['in_hostgroup'] = o_in_hostgroup
        if o_in_netgroup:
            _params['in_netgroup'] = o_in_netgroup
        if o_in_sudorule:
            _params['in_sudorule'] = o_in_sudorule
        if o_no_hostgroup:
            _params['no_hostgroup'] = o_no_hostgroup
        if o_no_host:
            _params['no_host'] = o_no_host
        if o_not_in_hbacrule:
            _params['not_in_hbacrule'] = o_not_in_hbacrule
        if o_not_in_hostgroup:
            _params['not_in_hostgroup'] = o_not_in_hostgroup
        if o_not_in_netgroup:
            _params['not_in_netgroup'] = o_not_in_netgroup
        if o_not_in_sudorule:
            _params['not_in_sudorule'] = o_not_in_sudorule
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def hostgroup_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify a hostgroup.
        :param a_cn: Name of host-group
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: A description of this host-group
        :type  o_description: str
        """
        method = 'hostgroup_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def hostgroup_remove_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Remove members from a hostgroup.
        :param a_cn: Name of host-group
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        """
        method = 'hostgroup_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def hostgroup_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a hostgroup.
        :param a_cn: Name of host-group
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'hostgroup_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def i18n_messages(
            self,
    ):
        """None
        """
        method = 'i18n_messages'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def idoverridegroup_add(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_fallback_to_ldap=False,
            o_raw=False,
            o_gidnumber=None,
            o_description=None,
            o_cn=None,
    ):
        """Add a new Group ID override.
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_description: Description
        :type  o_description: str
        :param o_cn: Group name
        :type  o_cn: str
        """
        method = 'idoverridegroup_add'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        _params['raw'] = o_raw
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def idoverridegroup_del(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_continue=False,
            o_fallback_to_ldap=False,
    ):
        """Delete an Group ID override.
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        """
        method = 'idoverridegroup_del'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        _params['continue'] = o_continue
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap

        return self._request(method, _args, _params)

    def idoverridegroup_find(
            self,
            a_idviewcn,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_fallback_to_ldap=False,
            o_pkey_only=False,
            o_raw=False,
            o_gidnumber=None,
            o_ipaanchoruuid=None,
            o_description=None,
            o_cn=None,
    ):
        """Search for an Group ID override.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_pkey_only: Results should contain primary key attribute only ("anchor")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_ipaanchoruuid: Anchor to override
        :type  o_ipaanchoruuid: str
        :param o_description: Description
        :type  o_description: str
        :param o_cn: Group name
        :type  o_cn: str
        """
        method = 'idoverridegroup_find'

        _args = list()
        _args.append(a_criteria)
        _args.append(a_idviewcn)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_ipaanchoruuid:
            _params['ipaanchoruuid'] = o_ipaanchoruuid
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def idoverridegroup_mod(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_fallback_to_ldap=False,
            o_raw=False,
            o_rights=False,
            o_gidnumber=None,
            o_description=None,
            o_cn=None,
    ):
        """Modify an Group ID override.
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the Group ID override object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_description: Description
        :type  o_description: str
        :param o_cn: Group name
        :type  o_cn: str
        """
        method = 'idoverridegroup_mod'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def idoverridegroup_show(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_all=True,
            o_fallback_to_ldap=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about an Group ID override.
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'idoverridegroup_show'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def idoverrideuser_add(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_fallback_to_ldap=False,
            o_raw=False,
            o_usercertificate=None,
            o_gidnumber=None,
            o_uidnumber=None,
            o_description=None,
            o_gecos=None,
            o_homedirectory=None,
            o_ipaoriginaluid=None,
            o_uid=None,
            o_loginshell=None,
            o_ipasshpubkey=None,
    ):
        """Add a new User ID override.
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_description: Description
        :type  o_description: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_ipaoriginaluid: <ipaoriginaluid>
        :type  o_ipaoriginaluid: str
        :param o_uid: User login
        :type  o_uid: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        :param o_ipasshpubkey: SSH public key
        :type  o_ipasshpubkey: str
        """
        method = 'idoverrideuser_add'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        _params['raw'] = o_raw
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_description:
            _params['description'] = o_description
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        if o_ipaoriginaluid:
            _params['ipaoriginaluid'] = o_ipaoriginaluid
        if o_uid:
            _params['uid'] = o_uid
        if o_loginshell:
            _params['loginshell'] = o_loginshell
        if o_ipasshpubkey:
            _params['ipasshpubkey'] = o_ipasshpubkey

        return self._request(method, _args, _params)

    def idoverrideuser_add_cert(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_usercertificate,
            o_all=True,
            o_fallback_to_ldap=False,
            o_raw=False,
    ):
        """Add one or more certificates to the idoverrideuser entry
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        """
        method = 'idoverrideuser_add_cert'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def idoverrideuser_del(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_continue=False,
            o_fallback_to_ldap=False,
    ):
        """Delete an User ID override.
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        """
        method = 'idoverrideuser_del'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        _params['continue'] = o_continue
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap

        return self._request(method, _args, _params)

    def idoverrideuser_find(
            self,
            a_idviewcn,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_fallback_to_ldap=False,
            o_pkey_only=False,
            o_raw=False,
            o_gidnumber=None,
            o_uidnumber=None,
            o_ipaanchoruuid=None,
            o_description=None,
            o_gecos=None,
            o_homedirectory=None,
            o_ipaoriginaluid=None,
            o_uid=None,
            o_loginshell=None,
    ):
        """Search for an User ID override.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_pkey_only: Results should contain primary key attribute only ("anchor")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_ipaanchoruuid: Anchor to override
        :type  o_ipaanchoruuid: str
        :param o_description: Description
        :type  o_description: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_ipaoriginaluid: <ipaoriginaluid>
        :type  o_ipaoriginaluid: str
        :param o_uid: User login
        :type  o_uid: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        """
        method = 'idoverrideuser_find'

        _args = list()
        _args.append(a_criteria)
        _args.append(a_idviewcn)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_ipaanchoruuid:
            _params['ipaanchoruuid'] = o_ipaanchoruuid
        if o_description:
            _params['description'] = o_description
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        if o_ipaoriginaluid:
            _params['ipaoriginaluid'] = o_ipaoriginaluid
        if o_uid:
            _params['uid'] = o_uid
        if o_loginshell:
            _params['loginshell'] = o_loginshell

        return self._request(method, _args, _params)

    def idoverrideuser_mod(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_fallback_to_ldap=False,
            o_raw=False,
            o_rights=False,
            o_usercertificate=None,
            o_gidnumber=None,
            o_uidnumber=None,
            o_description=None,
            o_gecos=None,
            o_homedirectory=None,
            o_ipaoriginaluid=None,
            o_uid=None,
            o_loginshell=None,
            o_ipasshpubkey=None,
    ):
        """Modify an User ID override.
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the User ID override object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_description: Description
        :type  o_description: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_ipaoriginaluid: <ipaoriginaluid>
        :type  o_ipaoriginaluid: str
        :param o_uid: User login
        :type  o_uid: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        :param o_ipasshpubkey: SSH public key
        :type  o_ipasshpubkey: str
        """
        method = 'idoverrideuser_mod'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_description:
            _params['description'] = o_description
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        if o_ipaoriginaluid:
            _params['ipaoriginaluid'] = o_ipaoriginaluid
        if o_uid:
            _params['uid'] = o_uid
        if o_loginshell:
            _params['loginshell'] = o_loginshell
        if o_ipasshpubkey:
            _params['ipasshpubkey'] = o_ipasshpubkey

        return self._request(method, _args, _params)

    def idoverrideuser_remove_cert(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_usercertificate,
            o_all=True,
            o_fallback_to_ldap=False,
            o_raw=False,
    ):
        """Remove one or more certificates to the idoverrideuser entry
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        """
        method = 'idoverrideuser_remove_cert'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def idoverrideuser_show(
            self,
            a_idviewcn,
            a_ipaanchoruuid,
            o_all=True,
            o_fallback_to_ldap=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about an User ID override.
        :param a_idviewcn: ID View Name
        :type  a_idviewcn: str
        :param a_ipaanchoruuid: Anchor to override
        :type  a_ipaanchoruuid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type  o_fallback_to_ldap: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'idoverrideuser_show'

        _args = list()
        _args.append(a_idviewcn)
        _args.append(a_ipaanchoruuid)

        _params = dict()
        _params['all'] = o_all
        if o_fallback_to_ldap:
            _params['fallback_to_ldap'] = o_fallback_to_ldap
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def idrange_add(
            self,
            a_cn,
            o_ipabaseid,
            o_ipaidrangesize,
            o_addattr=None,
            o_ipanttrusteddomainname=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_ipabaserid=None,
            o_ipasecondarybaserid=None,
            o_ipanttrusteddomainsid=None,
            o_iparangetype=None,
    ):
        """
    Add new ID range.

    To add a new ID range you always have to specify

        --base-id
        --range-size

    Additionally

        --rid-base
        --secondary-rid-base

    may be given for a new ID range for the local domain while

        --rid-base
        --dom-sid

    must be given to add a new range for a trusted AD domain.

=======
WARNING:

DNA plugin in 389-ds will allocate IDs based on the ranges configured for the
local domain. Currently the DNA plugin *cannot* be reconfigured itself based
on the local ranges set via this family of commands.

Manual configuration change has to be done in the DNA plugin configuration for
the new local range. Specifically, The dnaNextRange attribute of 'cn=Posix
IDs,cn=Distributed Numeric Assignment Plugin,cn=plugins,cn=config' has to be
modified to match the new range.
=======
        :param a_cn: Range name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_ipanttrusteddomainname: Name of the trusted domain
        :type  o_ipanttrusteddomainname: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipabaseid: First Posix ID of the range
        :type  o_ipabaseid: int, min value -2147483648, max value 2147483647
        :param o_ipaidrangesize: Number of IDs in the range
        :type  o_ipaidrangesize: int, min value -2147483648, max value 2147483647
        :param o_ipabaserid: First RID of the corresponding RID range
        :type  o_ipabaserid: int, min value -2147483648, max value 2147483647
        :param o_ipasecondarybaserid: First RID of the secondary RID range
        :type  o_ipasecondarybaserid: int, min value -2147483648, max value 2147483647
        :param o_ipanttrusteddomainsid: Domain SID of the trusted domain
        :type  o_ipanttrusteddomainsid: str
        :param o_iparangetype: ID range type, one of ipa-ad-trust, ipa-ad-trust-posix, ipa-local
        :type  o_iparangetype: str, valid values ['ipa-ad-trust', 'ipa-ad-trust-posix', 'ipa-local']
        """
        method = 'idrange_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_ipanttrusteddomainname:
            _params['ipanttrusteddomainname'] = o_ipanttrusteddomainname
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['ipabaseid'] = o_ipabaseid
        _params['ipaidrangesize'] = o_ipaidrangesize
        if o_ipabaserid:
            _params['ipabaserid'] = o_ipabaserid
        if o_ipasecondarybaserid:
            _params['ipasecondarybaserid'] = o_ipasecondarybaserid
        if o_ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = o_ipanttrusteddomainsid
        if o_iparangetype:
            _params['iparangetype'] = o_iparangetype

        return self._request(method, _args, _params)

    def idrange_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete an ID range.
        :param a_cn: Range name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'idrange_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def idrange_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipabaseid=None,
            o_ipaidrangesize=None,
            o_ipabaserid=None,
            o_ipasecondarybaserid=None,
            o_ipanttrusteddomainsid=None,
            o_cn=None,
            o_iparangetype=None,
    ):
        """Search for ranges.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipabaseid: First Posix ID of the range
        :type  o_ipabaseid: int, min value -2147483648, max value 2147483647
        :param o_ipaidrangesize: Number of IDs in the range
        :type  o_ipaidrangesize: int, min value -2147483648, max value 2147483647
        :param o_ipabaserid: First RID of the corresponding RID range
        :type  o_ipabaserid: int, min value -2147483648, max value 2147483647
        :param o_ipasecondarybaserid: First RID of the secondary RID range
        :type  o_ipasecondarybaserid: int, min value -2147483648, max value 2147483647
        :param o_ipanttrusteddomainsid: Domain SID of the trusted domain
        :type  o_ipanttrusteddomainsid: str
        :param o_cn: Range name
        :type  o_cn: str
        :param o_iparangetype: ID range type, one of ipa-ad-trust, ipa-ad-trust-posix, ipa-local
        :type  o_iparangetype: str, valid values ['ipa-ad-trust', 'ipa-ad-trust-posix', 'ipa-local']
        """
        method = 'idrange_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipabaseid:
            _params['ipabaseid'] = o_ipabaseid
        if o_ipaidrangesize:
            _params['ipaidrangesize'] = o_ipaidrangesize
        if o_ipabaserid:
            _params['ipabaserid'] = o_ipabaserid
        if o_ipasecondarybaserid:
            _params['ipasecondarybaserid'] = o_ipasecondarybaserid
        if o_ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = o_ipanttrusteddomainsid
        if o_cn:
            _params['cn'] = o_cn
        if o_iparangetype:
            _params['iparangetype'] = o_iparangetype

        return self._request(method, _args, _params)

    def idrange_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_ipanttrusteddomainname=None,
            o_ipanttrusteddomainsid=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_ipabaseid=None,
            o_ipaidrangesize=None,
            o_ipabaserid=None,
            o_ipasecondarybaserid=None,
    ):
        """Modify ID range.

=======
WARNING:

DNA plugin in 389-ds will allocate IDs based on the ranges configured for the
local domain. Currently the DNA plugin *cannot* be reconfigured itself based
on the local ranges set via this family of commands.

Manual configuration change has to be done in the DNA plugin configuration for
the new local range. Specifically, The dnaNextRange attribute of 'cn=Posix
IDs,cn=Distributed Numeric Assignment Plugin,cn=plugins,cn=config' has to be
modified to match the new range.
=======
        :param a_cn: Range name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_ipanttrusteddomainname: Name of the trusted domain
        :type  o_ipanttrusteddomainname: str
        :param o_ipanttrusteddomainsid: Domain SID of the trusted domain
        :type  o_ipanttrusteddomainsid: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipabaseid: First Posix ID of the range
        :type  o_ipabaseid: int, min value -2147483648, max value 2147483647
        :param o_ipaidrangesize: Number of IDs in the range
        :type  o_ipaidrangesize: int, min value -2147483648, max value 2147483647
        :param o_ipabaserid: First RID of the corresponding RID range
        :type  o_ipabaserid: int, min value -2147483648, max value 2147483647
        :param o_ipasecondarybaserid: First RID of the secondary RID range
        :type  o_ipasecondarybaserid: int, min value -2147483648, max value 2147483647
        """
        method = 'idrange_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_ipanttrusteddomainname:
            _params['ipanttrusteddomainname'] = o_ipanttrusteddomainname
        if o_ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = o_ipanttrusteddomainsid
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipabaseid:
            _params['ipabaseid'] = o_ipabaseid
        if o_ipaidrangesize:
            _params['ipaidrangesize'] = o_ipaidrangesize
        if o_ipabaserid:
            _params['ipabaserid'] = o_ipabaserid
        if o_ipasecondarybaserid:
            _params['ipasecondarybaserid'] = o_ipasecondarybaserid

        return self._request(method, _args, _params)

    def idrange_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a range.
        :param a_cn: Range name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'idrange_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def idview_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_description=None,
            o_ipadomainresolutionorder=None,
    ):
        """Add a new ID View.
        :param a_cn: ID View Name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Description
        :type  o_description: str
        :param o_ipadomainresolutionorder: colon-separated list of domains used for short name qualification
        :type  o_ipadomainresolutionorder: str
        """
        method = 'idview_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_ipadomainresolutionorder:
            _params['ipadomainresolutionorder'] = o_ipadomainresolutionorder

        return self._request(method, _args, _params)

    def idview_apply(
            self,
            a_cn,
            o_hostgroup=None,
            o_host=None,
    ):
        """Applies ID View to specified hosts or current members of specified hostgroups. If any other ID View is applied to the host, it is overridden.
        :param a_cn: ID View Name
        :type  a_cn: str
        :param o_hostgroup: Hostgroups to whose hosts apply the ID View to. Please note that view is not applied automatically to any hosts added to the hostgroup after running the idview-apply command.
        :type  o_hostgroup: str
        :param o_host: Hosts to apply the ID View to
        :type  o_host: str
        """
        method = 'idview_apply'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def idview_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete an ID View.
        :param a_cn: ID View Name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'idview_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def idview_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_description=None,
            o_cn=None,
    ):
        """Search for an ID View.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Description
        :type  o_description: str
        :param o_cn: ID View Name
        :type  o_cn: str
        """
        method = 'idview_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def idview_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_description=None,
            o_ipadomainresolutionorder=None,
    ):
        """Modify an ID View.
        :param a_cn: ID View Name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the ID View object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: Description
        :type  o_description: str
        :param o_ipadomainresolutionorder: colon-separated list of domains used for short name qualification
        :type  o_ipadomainresolutionorder: str
        """
        method = 'idview_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description
        if o_ipadomainresolutionorder:
            _params['ipadomainresolutionorder'] = o_ipadomainresolutionorder

        return self._request(method, _args, _params)

    def idview_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_show_hosts=False,
    ):
        """Display information about an ID View.
        :param a_cn: ID View Name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_show_hosts: Enumerate all the hosts the view applies to.
        :type  o_show_hosts: bool
        """
        method = 'idview_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_show_hosts:
            _params['show_hosts'] = o_show_hosts

        return self._request(method, _args, _params)

    def idview_unapply(
            self,
            o_hostgroup=None,
            o_host=None,
    ):
        """Clears ID View from specified hosts or current members of specified hostgroups.
        :param o_hostgroup: Hostgroups whose hosts should have ID Views cleared. Note that view is not cleared automatically from any host added to the hostgroup after running idview-unapply command.
        :type  o_hostgroup: str
        :param o_host: Hosts to clear (any) ID View from.
        :type  o_host: str
        """
        method = 'idview_unapply'

        _args = list()

        _params = dict()
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def join(
            self,
            a_cn,
            o_realm,
            o_nsosversion=None,
            o_nshardwareplatform=None,
    ):
        """Join an IPA domain
        :param a_cn: The hostname to register as
        :type  a_cn: str
        :param o_nsosversion: Operating System and version of the host (e.g. Fedora 9)
        :type  o_nsosversion: str
        :param o_nshardwareplatform: Hardware platform of the host (e.g. Lenovo T61)
        :type  o_nshardwareplatform: str
        :param o_realm: The IPA realm
        :type  o_realm: str
        """
        method = 'join'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_nsosversion:
            _params['nsosversion'] = o_nsosversion
        if o_nshardwareplatform:
            _params['nshardwareplatform'] = o_nshardwareplatform
        _params['realm'] = o_realm

        return self._request(method, _args, _params)

    def json_metadata(
            self,
            a_methodname=None,
            a_objname=None,
            o_command=None,
            o_method=None,
            o_object=None,
    ):
        """
    Export plugin meta-data for the webUI.
        :param a_methodname: Name of method to export
        :type  a_methodname: str
        :param a_objname: Name of object to export
        :type  a_objname: str
        :param o_command: Name of command to export
        :type  o_command: str
        :param o_method: Name of method to export
        :type  o_method: str
        :param o_object: Name of object to export
        :type  o_object: str
        """
        method = 'json_metadata'

        _args = list()
        _args.append(a_methodname)
        _args.append(a_objname)

        _params = dict()
        if o_command:
            _params['command'] = o_command
        if o_method:
            _params['method'] = o_method
        if o_object:
            _params['object'] = o_object

        return self._request(method, _args, _params)

    def kra_is_enabled(
            self,
    ):
        """None
        """
        method = 'kra_is_enabled'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def krbtpolicy_mod(
            self,
            a_uid=None,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_krbmaxticketlife=None,
            o_krbmaxrenewableage=None,
    ):
        """Modify Kerberos ticket policy.
        :param a_uid: Manage ticket policy for specific user
        :type  a_uid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_krbmaxticketlife: Maximum ticket life (seconds)
        :type  o_krbmaxticketlife: int, min value 1, max value 2147483647
        :param o_krbmaxrenewableage: Maximum renewable age (seconds)
        :type  o_krbmaxrenewableage: int, min value 1, max value 2147483647
        """
        method = 'krbtpolicy_mod'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_krbmaxticketlife:
            _params['krbmaxticketlife'] = o_krbmaxticketlife
        if o_krbmaxrenewableage:
            _params['krbmaxrenewableage'] = o_krbmaxrenewableage

        return self._request(method, _args, _params)

    def krbtpolicy_reset(
            self,
            a_uid=None,
            o_all=True,
            o_raw=False,
    ):
        """Reset Kerberos ticket policy to the default values.
        :param a_uid: Manage ticket policy for specific user
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'krbtpolicy_reset'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def krbtpolicy_show(
            self,
            a_uid=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display the current Kerberos ticket policy.
        :param a_uid: Manage ticket policy for specific user
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'krbtpolicy_show'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def location_add(
            self,
            a_idnsname,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_description=None,
    ):
        """Add a new IPA location.
        :param a_idnsname: IPA location name
        :type  a_idnsname: DNSNameParam
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: IPA Location description
        :type  o_description: str
        """
        method = 'location_add'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def location_del(
            self,
            a_idnsname,
            o_continue=False,
    ):
        """Delete an IPA location.
        :param a_idnsname: IPA location name
        :type  a_idnsname: DNSNameParam
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'location_del'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def location_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_idnsname=None,
            o_description=None,
    ):
        """Search for IPA locations.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_idnsname: IPA location name
        :type  o_idnsname: DNSNameParam
        :param o_description: IPA Location description
        :type  o_description: str
        """
        method = 'location_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_idnsname:
            _params['idnsname'] = o_idnsname
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def location_mod(
            self,
            a_idnsname,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify information about an IPA location.
        :param a_idnsname: IPA location name
        :type  a_idnsname: DNSNameParam
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: IPA Location description
        :type  o_description: str
        """
        method = 'location_mod'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def location_show(
            self,
            a_idnsname,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about an IPA location.
        :param a_idnsname: IPA location name
        :type  a_idnsname: DNSNameParam
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'location_show'

        _args = list()
        _args.append(a_idnsname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def migrate_ds(
            self,
            a_bindpw,
            a_ldapuri,
            o_basedn=None,
            o_cacertfile=None,
            o_use_def_group=True,
            o_binddn='cn=directory manager',
            o_groupcontainer='ou=groups',
            o_usercontainer='ou=people',
            o_continue=False,
            o_groupoverwritegid=False,
            o_compat=False,
            o_exclude_groups=None,
            o_exclude_users=None,
            o_groupignoreattribute=None,
            o_groupignoreobjectclass=None,
            o_groupobjectclass=None,
            o_userignoreattribute=None,
            o_userignoreobjectclass=None,
            o_userobjectclass=None,
            o_schema='RFC2307bis',
            o_scope='onelevel',
    ):
        """Migrate users and groups from DS to IPA.
        :param a_bindpw: bind password
        :type  a_bindpw: Password
        :param a_ldapuri: LDAP URI of DS server to migrate from
        :type  a_ldapuri: str
        :param o_basedn: Base DN on remote LDAP server
        :type  o_basedn: DNParam
        :param o_cacertfile: Load CA certificate of LDAP server from FILE
        :type  o_cacertfile: str
        :param o_use_def_group: Add migrated users without a group to a default group (default: true)
        :type  o_use_def_group: Bool
        :param o_binddn: Bind DN
        :type  o_binddn: DNParam
        :param o_groupcontainer: DN of container for groups in DS relative to base DN
        :type  o_groupcontainer: DNParam
        :param o_usercontainer: DN of container for users in DS relative to base DN
        :type  o_usercontainer: DNParam
        :param o_continue: Continuous operation mode. Errors are reported but the process continues
        :type  o_continue: bool
        :param o_groupoverwritegid: When migrating a group already existing in IPA domain overwrite the group GID and report as success
        :type  o_groupoverwritegid: bool
        :param o_compat: Allows migration despite the usage of compat plugin
        :type  o_compat: bool
        :param o_exclude_groups: groups to exclude from migration
        :type  o_exclude_groups: str
        :param o_exclude_users: users to exclude from migration
        :type  o_exclude_users: str
        :param o_groupignoreattribute: Attributes to be ignored for group entries in DS
        :type  o_groupignoreattribute: str
        :param o_groupignoreobjectclass: Objectclasses to be ignored for group entries in DS
        :type  o_groupignoreobjectclass: str
        :param o_groupobjectclass: Objectclasses used to search for group entries in DS
        :type  o_groupobjectclass: str
        :param o_userignoreattribute: Attributes to be ignored for user entries in DS
        :type  o_userignoreattribute: str
        :param o_userignoreobjectclass: Objectclasses to be ignored for user entries in DS
        :type  o_userignoreobjectclass: str
        :param o_userobjectclass: Objectclasses used to search for user entries in DS
        :type  o_userobjectclass: str
        :param o_schema: The schema used on the LDAP server. Supported values are RFC2307 and RFC2307bis. The default is RFC2307bis
        :type  o_schema: str, valid values ['RFC2307bis', 'RFC2307']
        :param o_scope: LDAP search scope for users and groups: base, onelevel, or subtree. Defaults to onelevel
        :type  o_scope: str, valid values ['base', 'onelevel', 'subtree']
        """
        method = 'migrate_ds'

        _args = list()
        _args.append(a_bindpw)
        _args.append(a_ldapuri)

        _params = dict()
        if o_basedn:
            _params['basedn'] = o_basedn
        if o_cacertfile:
            _params['cacertfile'] = o_cacertfile
        if o_use_def_group:
            _params['use_def_group'] = o_use_def_group
        if o_binddn:
            _params['binddn'] = o_binddn
        _params['groupcontainer'] = o_groupcontainer
        _params['usercontainer'] = o_usercontainer
        if o_continue:
            _params['continue'] = o_continue
        _params['groupoverwritegid'] = o_groupoverwritegid
        if o_compat:
            _params['compat'] = o_compat
        if o_exclude_groups:
            _params['exclude_groups'] = o_exclude_groups
        if o_exclude_users:
            _params['exclude_users'] = o_exclude_users
        if o_groupignoreattribute:
            _params['groupignoreattribute'] = o_groupignoreattribute
        if o_groupignoreobjectclass:
            _params['groupignoreobjectclass'] = o_groupignoreobjectclass
        _params['groupobjectclass'] = o_groupobjectclass
        if o_userignoreattribute:
            _params['userignoreattribute'] = o_userignoreattribute
        if o_userignoreobjectclass:
            _params['userignoreobjectclass'] = o_userignoreobjectclass
        _params['userobjectclass'] = o_userobjectclass
        if o_schema:
            _params['schema'] = o_schema
        _params['scope'] = o_scope

        return self._request(method, _args, _params)

    def netgroup_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_description=None,
            o_externalhost=None,
            o_nisdomainname=None,
            o_hostcategory=None,
            o_usercategory=None,
    ):
        """Add a new netgroup.
        :param a_cn: Netgroup name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Netgroup description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_nisdomainname: NIS domain name
        :type  o_nisdomainname: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'netgroup_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_nisdomainname:
            _params['nisdomainname'] = o_nisdomainname
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def netgroup_add_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_netgroup=None,
            o_user=None,
    ):
        """Add members to a netgroup.
        :param a_cn: Netgroup name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        :param o_netgroup: netgroups to add
        :type  o_netgroup: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'netgroup_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_netgroup:
            _params['netgroup'] = o_netgroup
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def netgroup_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a netgroup.
        :param a_cn: Netgroup name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'netgroup_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def netgroup_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_in_netgroup=None,
            o_netgroup=None,
            o_no_group=None,
            o_no_hostgroup=None,
            o_no_host=None,
            o_no_netgroup=None,
            o_no_user=None,
            o_not_in_netgroup=None,
            o_user=None,
            o_all=True,
            o_managed=False,
            o_no_members=True,
            o_pkey_only=False,
            o_private=False,
            o_raw=False,
            o_description=None,
            o_externalhost=None,
            o_cn=None,
            o_nisdomainname=None,
            o_ipauniqueid=None,
            o_hostcategory=None,
            o_usercategory=None,
    ):
        """Search for a netgroup.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_group: Search for netgroups with these member groups.
        :type  o_group: str
        :param o_hostgroup: Search for netgroups with these member host groups.
        :type  o_hostgroup: str
        :param o_host: Search for netgroups with these member hosts.
        :type  o_host: str
        :param o_in_netgroup: Search for netgroups with these member of netgroups.
        :type  o_in_netgroup: str
        :param o_netgroup: Search for netgroups with these member netgroups.
        :type  o_netgroup: str
        :param o_no_group: Search for netgroups without these member groups.
        :type  o_no_group: str
        :param o_no_hostgroup: Search for netgroups without these member host groups.
        :type  o_no_hostgroup: str
        :param o_no_host: Search for netgroups without these member hosts.
        :type  o_no_host: str
        :param o_no_netgroup: Search for netgroups without these member netgroups.
        :type  o_no_netgroup: str
        :param o_no_user: Search for netgroups without these member users.
        :type  o_no_user: str
        :param o_not_in_netgroup: Search for netgroups without these member of netgroups.
        :type  o_not_in_netgroup: str
        :param o_user: Search for netgroups with these member users.
        :type  o_user: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_managed: search for managed groups
        :type  o_managed: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_private: <private>
        :type  o_private: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Netgroup description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_cn: Netgroup name
        :type  o_cn: str
        :param o_nisdomainname: NIS domain name
        :type  o_nisdomainname: str
        :param o_ipauniqueid: IPA unique ID
        :type  o_ipauniqueid: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'netgroup_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_in_netgroup:
            _params['in_netgroup'] = o_in_netgroup
        if o_netgroup:
            _params['netgroup'] = o_netgroup
        if o_no_group:
            _params['no_group'] = o_no_group
        if o_no_hostgroup:
            _params['no_hostgroup'] = o_no_hostgroup
        if o_no_host:
            _params['no_host'] = o_no_host
        if o_no_netgroup:
            _params['no_netgroup'] = o_no_netgroup
        if o_no_user:
            _params['no_user'] = o_no_user
        if o_not_in_netgroup:
            _params['not_in_netgroup'] = o_not_in_netgroup
        if o_user:
            _params['user'] = o_user
        _params['all'] = o_all
        _params['managed'] = o_managed
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['private'] = o_private
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_cn:
            _params['cn'] = o_cn
        if o_nisdomainname:
            _params['nisdomainname'] = o_nisdomainname
        if o_ipauniqueid:
            _params['ipauniqueid'] = o_ipauniqueid
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def netgroup_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_description=None,
            o_externalhost=None,
            o_nisdomainname=None,
            o_hostcategory=None,
            o_usercategory=None,
    ):
        """Modify a netgroup.
        :param a_cn: Netgroup name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: Netgroup description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_nisdomainname: NIS domain name
        :type  o_nisdomainname: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'netgroup_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_nisdomainname:
            _params['nisdomainname'] = o_nisdomainname
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def netgroup_remove_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_netgroup=None,
            o_user=None,
    ):
        """Remove members from a netgroup.
        :param a_cn: Netgroup name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        :param o_netgroup: netgroups to remove
        :type  o_netgroup: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'netgroup_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_netgroup:
            _params['netgroup'] = o_netgroup
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def netgroup_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a netgroup.
        :param a_cn: Netgroup name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'netgroup_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def otpconfig_mod(
            self,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_ipatokenhotpauthwindow=None,
            o_ipatokenhotpsyncwindow=None,
            o_ipatokentotpauthwindow=None,
            o_ipatokentotpsyncwindow=None,
    ):
        """Modify OTP configuration options.
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipatokenhotpauthwindow: HOTP authentication skip-ahead
        :type  o_ipatokenhotpauthwindow: int, min value 1, max value 2147483647
        :param o_ipatokenhotpsyncwindow: HOTP synchronization skip-ahead
        :type  o_ipatokenhotpsyncwindow: int, min value 1, max value 2147483647
        :param o_ipatokentotpauthwindow: TOTP authentication time variance (seconds)
        :type  o_ipatokentotpauthwindow: int, min value 5, max value 2147483647
        :param o_ipatokentotpsyncwindow: TOTP synchronization time variance (seconds)
        :type  o_ipatokentotpsyncwindow: int, min value 5, max value 2147483647
        """
        method = 'otpconfig_mod'

        _args = list()

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipatokenhotpauthwindow:
            _params['ipatokenhotpauthwindow'] = o_ipatokenhotpauthwindow
        if o_ipatokenhotpsyncwindow:
            _params['ipatokenhotpsyncwindow'] = o_ipatokenhotpsyncwindow
        if o_ipatokentotpauthwindow:
            _params['ipatokentotpauthwindow'] = o_ipatokentotpauthwindow
        if o_ipatokentotpsyncwindow:
            _params['ipatokentotpsyncwindow'] = o_ipatokentotpsyncwindow

        return self._request(method, _args, _params)

    def otpconfig_show(
            self,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Show the current OTP configuration.
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'otpconfig_show'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def otptoken_add(
            self,
            a_ipatokenuniqueid=None,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_no_qrcode=False,
            o_qrcode=False,
            o_raw=False,
            o_type='totp',
            o_ipatokendisabled=None,
            o_ipatokennotafter=None,
            o_ipatokennotbefore=None,
            o_description=None,
            o_ipatokenmodel=None,
            o_ipatokenowner=None,
            o_ipatokenserial=None,
            o_ipatokenvendor=None,
            o_ipatokenhotpcounter=0,
            o_ipatokentotptimestep=30,
            o_ipatokentotpclockoffset=0,
            o_ipatokenotpdigits=6,
            o_ipatokenotpkey=None,
            o_ipatokenotpalgorithm='sha1',
    ):
        """Add a new OTP token.
        :param a_ipatokenuniqueid: Unique ID
        :type  a_ipatokenuniqueid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_no_qrcode: Do not display QR code
        :type  o_no_qrcode: bool
        :param o_qrcode: (deprecated)
        :type  o_qrcode: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_type: Type of the token
        :type  o_type: str, valid values ['totp', 'hotp', 'TOTP', 'HOTP']
        :param o_ipatokendisabled: Mark the token as disabled (default: false)
        :type  o_ipatokendisabled: Bool
        :param o_ipatokennotafter: Last date/time the token can be used
        :type  o_ipatokennotafter: DateTime
        :param o_ipatokennotbefore: First date/time the token can be used
        :type  o_ipatokennotbefore: DateTime
        :param o_description: Token description (informational only)
        :type  o_description: str
        :param o_ipatokenmodel: Token model (informational only)
        :type  o_ipatokenmodel: str
        :param o_ipatokenowner: Assigned user of the token (default: self)
        :type  o_ipatokenowner: str
        :param o_ipatokenserial: Token serial (informational only)
        :type  o_ipatokenserial: str
        :param o_ipatokenvendor: Token vendor name (informational only)
        :type  o_ipatokenvendor: str
        :param o_ipatokenhotpcounter: Initial counter for the HOTP token
        :type  o_ipatokenhotpcounter: int, min value 0, max value 2147483647
        :param o_ipatokentotptimestep: Length of TOTP token code validity
        :type  o_ipatokentotptimestep: int, min value 5, max value 2147483647
        :param o_ipatokentotpclockoffset: TOTP token / FreeIPA server time difference
        :type  o_ipatokentotpclockoffset: int, min value -2147483648, max value 2147483647
        :param o_ipatokenotpdigits: Number of digits each token code will have
        :type  o_ipatokenotpdigits: int, valid values ['6', '8']
        :param o_ipatokenotpkey: Token secret (Base32; default: random)
        :type  o_ipatokenotpkey: OTPTokenKey
        :param o_ipatokenotpalgorithm: Token hash algorithm
        :type  o_ipatokenotpalgorithm: str, valid values ['sha1', 'sha256', 'sha384', 'sha512']
        """
        method = 'otptoken_add'

        _args = list()
        _args.append(a_ipatokenuniqueid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['no_qrcode'] = o_no_qrcode
        if o_qrcode:
            _params['qrcode'] = o_qrcode
        _params['raw'] = o_raw
        if o_type:
            _params['type'] = o_type
        if o_ipatokendisabled:
            _params['ipatokendisabled'] = o_ipatokendisabled
        if o_ipatokennotafter:
            _params['ipatokennotafter'] = o_ipatokennotafter
        if o_ipatokennotbefore:
            _params['ipatokennotbefore'] = o_ipatokennotbefore
        if o_description:
            _params['description'] = o_description
        if o_ipatokenmodel:
            _params['ipatokenmodel'] = o_ipatokenmodel
        if o_ipatokenowner:
            _params['ipatokenowner'] = o_ipatokenowner
        if o_ipatokenserial:
            _params['ipatokenserial'] = o_ipatokenserial
        if o_ipatokenvendor:
            _params['ipatokenvendor'] = o_ipatokenvendor
        if o_ipatokenhotpcounter:
            _params['ipatokenhotpcounter'] = o_ipatokenhotpcounter
        if o_ipatokentotptimestep:
            _params['ipatokentotptimestep'] = o_ipatokentotptimestep
        if o_ipatokentotpclockoffset:
            _params['ipatokentotpclockoffset'] = o_ipatokentotpclockoffset
        if o_ipatokenotpdigits:
            _params['ipatokenotpdigits'] = o_ipatokenotpdigits
        if o_ipatokenotpkey:
            _params['ipatokenotpkey'] = o_ipatokenotpkey
        if o_ipatokenotpalgorithm:
            _params['ipatokenotpalgorithm'] = o_ipatokenotpalgorithm

        return self._request(method, _args, _params)

    def otptoken_add_managedby(
            self,
            a_ipatokenuniqueid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_user=None,
    ):
        """Add users that can manage this token.
        :param a_ipatokenuniqueid: Unique ID
        :type  a_ipatokenuniqueid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'otptoken_add_managedby'

        _args = list()
        _args.append(a_ipatokenuniqueid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def otptoken_del(
            self,
            a_ipatokenuniqueid,
            o_continue=False,
    ):
        """Delete an OTP token.
        :param a_ipatokenuniqueid: Unique ID
        :type  a_ipatokenuniqueid: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'otptoken_del'

        _args = list()
        _args.append(a_ipatokenuniqueid)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def otptoken_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_type='totp',
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipatokendisabled=None,
            o_ipatokennotafter=None,
            o_ipatokennotbefore=None,
            o_ipatokenhotpcounter=0,
            o_ipatokentotptimestep=30,
            o_ipatokentotpclockoffset=0,
            o_ipatokenotpdigits=6,
            o_description=None,
            o_ipatokenuniqueid=None,
            o_ipatokenmodel=None,
            o_ipatokenowner=None,
            o_ipatokenserial=None,
            o_ipatokenvendor=None,
            o_ipatokenotpalgorithm='sha1',
    ):
        """Search for OTP token.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_type: Type of the token
        :type  o_type: str, valid values ['totp', 'hotp', 'TOTP', 'HOTP']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("id")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipatokendisabled: Mark the token as disabled (default: false)
        :type  o_ipatokendisabled: Bool
        :param o_ipatokennotafter: Last date/time the token can be used
        :type  o_ipatokennotafter: DateTime
        :param o_ipatokennotbefore: First date/time the token can be used
        :type  o_ipatokennotbefore: DateTime
        :param o_ipatokenhotpcounter: Initial counter for the HOTP token
        :type  o_ipatokenhotpcounter: int, min value 0, max value 2147483647
        :param o_ipatokentotptimestep: Length of TOTP token code validity
        :type  o_ipatokentotptimestep: int, min value 5, max value 2147483647
        :param o_ipatokentotpclockoffset: TOTP token / FreeIPA server time difference
        :type  o_ipatokentotpclockoffset: int, min value -2147483648, max value 2147483647
        :param o_ipatokenotpdigits: Number of digits each token code will have
        :type  o_ipatokenotpdigits: int, valid values ['6', '8']
        :param o_description: Token description (informational only)
        :type  o_description: str
        :param o_ipatokenuniqueid: Unique ID
        :type  o_ipatokenuniqueid: str
        :param o_ipatokenmodel: Token model (informational only)
        :type  o_ipatokenmodel: str
        :param o_ipatokenowner: Assigned user of the token (default: self)
        :type  o_ipatokenowner: str
        :param o_ipatokenserial: Token serial (informational only)
        :type  o_ipatokenserial: str
        :param o_ipatokenvendor: Token vendor name (informational only)
        :type  o_ipatokenvendor: str
        :param o_ipatokenotpalgorithm: Token hash algorithm
        :type  o_ipatokenotpalgorithm: str, valid values ['sha1', 'sha256', 'sha384', 'sha512']
        """
        method = 'otptoken_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_type:
            _params['type'] = o_type
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipatokendisabled:
            _params['ipatokendisabled'] = o_ipatokendisabled
        if o_ipatokennotafter:
            _params['ipatokennotafter'] = o_ipatokennotafter
        if o_ipatokennotbefore:
            _params['ipatokennotbefore'] = o_ipatokennotbefore
        if o_ipatokenhotpcounter:
            _params['ipatokenhotpcounter'] = o_ipatokenhotpcounter
        if o_ipatokentotptimestep:
            _params['ipatokentotptimestep'] = o_ipatokentotptimestep
        if o_ipatokentotpclockoffset:
            _params['ipatokentotpclockoffset'] = o_ipatokentotpclockoffset
        if o_ipatokenotpdigits:
            _params['ipatokenotpdigits'] = o_ipatokenotpdigits
        if o_description:
            _params['description'] = o_description
        if o_ipatokenuniqueid:
            _params['ipatokenuniqueid'] = o_ipatokenuniqueid
        if o_ipatokenmodel:
            _params['ipatokenmodel'] = o_ipatokenmodel
        if o_ipatokenowner:
            _params['ipatokenowner'] = o_ipatokenowner
        if o_ipatokenserial:
            _params['ipatokenserial'] = o_ipatokenserial
        if o_ipatokenvendor:
            _params['ipatokenvendor'] = o_ipatokenvendor
        if o_ipatokenotpalgorithm:
            _params['ipatokenotpalgorithm'] = o_ipatokenotpalgorithm

        return self._request(method, _args, _params)

    def otptoken_mod(
            self,
            a_ipatokenuniqueid,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_ipatokendisabled=None,
            o_ipatokennotafter=None,
            o_ipatokennotbefore=None,
            o_description=None,
            o_ipatokenmodel=None,
            o_ipatokenowner=None,
            o_ipatokenserial=None,
            o_ipatokenvendor=None,
    ):
        """Modify a OTP token.
        :param a_ipatokenuniqueid: Unique ID
        :type  a_ipatokenuniqueid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the OTP token object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipatokendisabled: Mark the token as disabled (default: false)
        :type  o_ipatokendisabled: Bool
        :param o_ipatokennotafter: Last date/time the token can be used
        :type  o_ipatokennotafter: DateTime
        :param o_ipatokennotbefore: First date/time the token can be used
        :type  o_ipatokennotbefore: DateTime
        :param o_description: Token description (informational only)
        :type  o_description: str
        :param o_ipatokenmodel: Token model (informational only)
        :type  o_ipatokenmodel: str
        :param o_ipatokenowner: Assigned user of the token (default: self)
        :type  o_ipatokenowner: str
        :param o_ipatokenserial: Token serial (informational only)
        :type  o_ipatokenserial: str
        :param o_ipatokenvendor: Token vendor name (informational only)
        :type  o_ipatokenvendor: str
        """
        method = 'otptoken_mod'

        _args = list()
        _args.append(a_ipatokenuniqueid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipatokendisabled:
            _params['ipatokendisabled'] = o_ipatokendisabled
        if o_ipatokennotafter:
            _params['ipatokennotafter'] = o_ipatokennotafter
        if o_ipatokennotbefore:
            _params['ipatokennotbefore'] = o_ipatokennotbefore
        if o_description:
            _params['description'] = o_description
        if o_ipatokenmodel:
            _params['ipatokenmodel'] = o_ipatokenmodel
        if o_ipatokenowner:
            _params['ipatokenowner'] = o_ipatokenowner
        if o_ipatokenserial:
            _params['ipatokenserial'] = o_ipatokenserial
        if o_ipatokenvendor:
            _params['ipatokenvendor'] = o_ipatokenvendor

        return self._request(method, _args, _params)

    def otptoken_remove_managedby(
            self,
            a_ipatokenuniqueid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_user=None,
    ):
        """Remove users that can manage this token.
        :param a_ipatokenuniqueid: Unique ID
        :type  a_ipatokenuniqueid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'otptoken_remove_managedby'

        _args = list()
        _args.append(a_ipatokenuniqueid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def otptoken_show(
            self,
            a_ipatokenuniqueid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about an OTP token.
        :param a_ipatokenuniqueid: Unique ID
        :type  a_ipatokenuniqueid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'otptoken_show'

        _args = list()
        _args.append(a_ipatokenuniqueid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def output_find(
            self,
            a_commandfull_name,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
    ):
        """Search for command outputs.
        :param a_commandfull_name: Full name
        :type  a_commandfull_name: str
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'output_find'

        _args = list()
        _args.append(a_commandfull_name)
        _args.append(a_criteria)

        _params = dict()
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def output_show(
            self,
            a_commandfull_name,
            a_name,
            o_all=True,
            o_raw=False,
    ):
        """Display information about a command output.
        :param a_commandfull_name: Full name
        :type  a_commandfull_name: str
        :param a_name: Name
        :type  a_name: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'output_show'

        _args = list()
        _args.append(a_commandfull_name)
        _args.append(a_name)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def param_find(
            self,
            a_metaobjectfull_name,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
    ):
        """Search command parameters.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param a_metaobjectfull_name: Full name
        :type  a_metaobjectfull_name: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'param_find'

        _args = list()
        _args.append(a_criteria)
        _args.append(a_metaobjectfull_name)

        _params = dict()
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def param_show(
            self,
            a_metaobjectfull_name,
            a_name,
            o_all=True,
            o_raw=False,
    ):
        """Display information about a command parameter.
        :param a_metaobjectfull_name: Full name
        :type  a_metaobjectfull_name: str
        :param a_name: Name
        :type  a_name: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'param_show'

        _args = list()
        _args.append(a_metaobjectfull_name)
        _args.append(a_name)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def passwd(
            self,
            a_password,
            a_current_password,
            a_principal,
            o_otp=None,
    ):
        """Set a user's password.
        :param a_password: New Password
        :type  a_password: Password
        :param a_current_password: Current Password
        :type  a_current_password: Password
        :param a_principal: User name
        :type  a_principal: Principal
        :param o_otp: One Time Password
        :type  o_otp: Password
        """
        method = 'passwd'

        _args = list()
        _args.append(a_password)
        _args.append(a_current_password)
        _args.append(a_principal)

        _params = dict()
        if o_otp:
            _params['otp'] = o_otp

        return self._request(method, _args, _params)

    def permission_add(
            self,
            a_cn,
            o_addattr=None,
            o_attrs=None,
            o_filter=None,
            o_extratargetfilter=None,
            o_permissions=None,
            o_setattr=None,
            o_subtree=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_ipapermtarget=None,
            o_ipapermtargetfrom=None,
            o_ipapermtargetto=None,
            o_ipapermtargetfilter=None,
            o_ipapermbindruletype='permission',
            o_memberof=None,
            o_targetgroup=None,
            o_type=None,
            o_ipapermlocation=None,
            o_ipapermright=None,
    ):
        """Add a new permission.
        :param a_cn: Permission name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_attrs: All attributes to which the permission applies
        :type  o_attrs: str
        :param o_filter: Deprecated; use extratargetfilter
        :type  o_filter: str
        :param o_extratargetfilter: Extra target filter
        :type  o_extratargetfilter: str
        :param o_permissions: Deprecated; use ipapermright
        :type  o_permissions: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_subtree: Deprecated; use ipapermlocation
        :type  o_subtree: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipapermtarget: Optional DN to apply the permission to (must be in the subtree, but may not yet exist)
        :type  o_ipapermtarget: DNParam
        :param o_ipapermtargetfrom: Optional DN subtree from where an entry can be moved (must be in the subtree, but may not yet exist)
        :type  o_ipapermtargetfrom: DNParam
        :param o_ipapermtargetto: Optional DN subtree where an entry can be moved to (must be in the subtree, but may not yet exist)
        :type  o_ipapermtargetto: DNParam
        :param o_ipapermtargetfilter: All target filters, including those implied by type and memberof
        :type  o_ipapermtargetfilter: str
        :param o_ipapermbindruletype: Bind rule type
        :type  o_ipapermbindruletype: str, valid values ['permission', 'all', 'anonymous']
        :param o_memberof: Target members of a group (sets memberOf targetfilter)
        :type  o_memberof: str
        :param o_targetgroup: User group to apply permissions to (sets target)
        :type  o_targetgroup: str
        :param o_type: Type of IPA object (sets subtree and objectClass targetfilter)
        :type  o_type: str
        :param o_ipapermlocation: Subtree to apply permissions to
        :type  o_ipapermlocation: DNOrURL
        :param o_ipapermright: Rights to grant (read, search, compare, write, add, delete, all)
        :type  o_ipapermright: str, valid values ['read', 'search', 'compare', 'write', 'add', 'delete', 'all']
        """
        method = 'permission_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_filter:
            _params['filter'] = o_filter
        if o_extratargetfilter:
            _params['extratargetfilter'] = o_extratargetfilter
        if o_permissions:
            _params['permissions'] = o_permissions
        if o_setattr:
            _params['setattr'] = o_setattr
        if o_subtree:
            _params['subtree'] = o_subtree
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_ipapermtarget:
            _params['ipapermtarget'] = o_ipapermtarget
        if o_ipapermtargetfrom:
            _params['ipapermtargetfrom'] = o_ipapermtargetfrom
        if o_ipapermtargetto:
            _params['ipapermtargetto'] = o_ipapermtargetto
        if o_ipapermtargetfilter:
            _params['ipapermtargetfilter'] = o_ipapermtargetfilter
        _params['ipapermbindruletype'] = o_ipapermbindruletype
        if o_memberof:
            _params['memberof'] = o_memberof
        if o_targetgroup:
            _params['targetgroup'] = o_targetgroup
        if o_type:
            _params['type'] = o_type
        if o_ipapermlocation:
            _params['ipapermlocation'] = o_ipapermlocation
        if o_ipapermright:
            _params['ipapermright'] = o_ipapermright

        return self._request(method, _args, _params)

    def permission_add_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_privilege=None,
    ):
        """Add members to a permission.
        :param a_cn: Permission name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_privilege: privileges to add
        :type  o_privilege: str
        """
        method = 'permission_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_privilege:
            _params['privilege'] = o_privilege

        return self._request(method, _args, _params)

    def permission_add_noaci(
            self,
            a_cn,
            o_ipapermissiontype,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add a system permission without an ACI (internal command)
        :param a_cn: Permission name
        :type  a_cn: str
        :param o_ipapermissiontype: Permission flags
        :type  o_ipapermissiontype: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'permission_add_noaci'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['ipapermissiontype'] = o_ipapermissiontype
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def permission_del(
            self,
            a_cn,
            o_continue=False,
            o_force=False,
    ):
        """Delete a permission.
        :param a_cn: Permission name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        :param o_force: force delete of SYSTEM permissions
        :type  o_force: bool
        """
        method = 'permission_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue
        _params['force'] = o_force

        return self._request(method, _args, _params)

    def permission_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_attrs=None,
            o_filter=None,
            o_extratargetfilter=None,
            o_memberof=None,
            o_permissions=None,
            o_subtree=None,
            o_targetgroup=None,
            o_type=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipapermlocation=None,
            o_ipapermtarget=None,
            o_ipapermtargetfrom=None,
            o_ipapermtargetto=None,
            o_ipapermdefaultattr=None,
            o_ipapermexcludedattr=None,
            o_ipapermincludedattr=None,
            o_cn=None,
            o_ipapermtargetfilter=None,
            o_ipapermbindruletype='permission',
            o_ipapermright=None,
    ):
        """Search for permissions.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_attrs: All attributes to which the permission applies
        :type  o_attrs: str
        :param o_filter: Deprecated; use extratargetfilter
        :type  o_filter: str
        :param o_extratargetfilter: Extra target filter
        :type  o_extratargetfilter: str
        :param o_memberof: Target members of a group (sets memberOf targetfilter)
        :type  o_memberof: str
        :param o_permissions: Deprecated; use ipapermright
        :type  o_permissions: str
        :param o_subtree: Deprecated; use ipapermlocation
        :type  o_subtree: str
        :param o_targetgroup: User group to apply permissions to (sets target)
        :type  o_targetgroup: str
        :param o_type: Type of IPA object (sets subtree and objectClass targetfilter)
        :type  o_type: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipapermlocation: Subtree to apply permissions to
        :type  o_ipapermlocation: DNOrURL
        :param o_ipapermtarget: Optional DN to apply the permission to (must be in the subtree, but may not yet exist)
        :type  o_ipapermtarget: DNParam
        :param o_ipapermtargetfrom: Optional DN subtree from where an entry can be moved (must be in the subtree, but may not yet exist)
        :type  o_ipapermtargetfrom: DNParam
        :param o_ipapermtargetto: Optional DN subtree where an entry can be moved to (must be in the subtree, but may not yet exist)
        :type  o_ipapermtargetto: DNParam
        :param o_ipapermdefaultattr: Attributes to which the permission applies by default
        :type  o_ipapermdefaultattr: str
        :param o_ipapermexcludedattr: User-specified attributes to which the permission explicitly does not apply
        :type  o_ipapermexcludedattr: str
        :param o_ipapermincludedattr: User-specified attributes to which the permission applies
        :type  o_ipapermincludedattr: str
        :param o_cn: Permission name
        :type  o_cn: str
        :param o_ipapermtargetfilter: All target filters, including those implied by type and memberof
        :type  o_ipapermtargetfilter: str
        :param o_ipapermbindruletype: Bind rule type
        :type  o_ipapermbindruletype: str, valid values ['permission', 'all', 'anonymous']
        :param o_ipapermright: Rights to grant (read, search, compare, write, add, delete, all)
        :type  o_ipapermright: str, valid values ['read', 'search', 'compare', 'write', 'add', 'delete', 'all']
        """
        method = 'permission_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_filter:
            _params['filter'] = o_filter
        if o_extratargetfilter:
            _params['extratargetfilter'] = o_extratargetfilter
        if o_memberof:
            _params['memberof'] = o_memberof
        if o_permissions:
            _params['permissions'] = o_permissions
        if o_subtree:
            _params['subtree'] = o_subtree
        if o_targetgroup:
            _params['targetgroup'] = o_targetgroup
        if o_type:
            _params['type'] = o_type
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipapermlocation:
            _params['ipapermlocation'] = o_ipapermlocation
        if o_ipapermtarget:
            _params['ipapermtarget'] = o_ipapermtarget
        if o_ipapermtargetfrom:
            _params['ipapermtargetfrom'] = o_ipapermtargetfrom
        if o_ipapermtargetto:
            _params['ipapermtargetto'] = o_ipapermtargetto
        if o_ipapermdefaultattr:
            _params['ipapermdefaultattr'] = o_ipapermdefaultattr
        if o_ipapermexcludedattr:
            _params['ipapermexcludedattr'] = o_ipapermexcludedattr
        if o_ipapermincludedattr:
            _params['ipapermincludedattr'] = o_ipapermincludedattr
        if o_cn:
            _params['cn'] = o_cn
        if o_ipapermtargetfilter:
            _params['ipapermtargetfilter'] = o_ipapermtargetfilter
        if o_ipapermbindruletype:
            _params['ipapermbindruletype'] = o_ipapermbindruletype
        if o_ipapermright:
            _params['ipapermright'] = o_ipapermright

        return self._request(method, _args, _params)

    def permission_mod(
            self,
            a_cn,
            o_addattr=None,
            o_attrs=None,
            o_delattr=None,
            o_filter=None,
            o_extratargetfilter=None,
            o_memberof=None,
            o_permissions=None,
            o_rename=None,
            o_setattr=None,
            o_subtree=None,
            o_targetgroup=None,
            o_type=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_ipapermlocation=None,
            o_ipapermtarget=None,
            o_ipapermtargetfrom=None,
            o_ipapermtargetto=None,
            o_ipapermexcludedattr=None,
            o_ipapermincludedattr=None,
            o_ipapermtargetfilter=None,
            o_ipapermbindruletype='permission',
            o_ipapermright=None,
    ):
        """Modify a permission.
        :param a_cn: Permission name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_attrs: All attributes to which the permission applies
        :type  o_attrs: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_filter: Deprecated; use extratargetfilter
        :type  o_filter: str
        :param o_extratargetfilter: Extra target filter
        :type  o_extratargetfilter: str
        :param o_memberof: Target members of a group (sets memberOf targetfilter)
        :type  o_memberof: str
        :param o_permissions: Deprecated; use ipapermright
        :type  o_permissions: str
        :param o_rename: Rename the permission object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_subtree: Deprecated; use ipapermlocation
        :type  o_subtree: str
        :param o_targetgroup: User group to apply permissions to (sets target)
        :type  o_targetgroup: str
        :param o_type: Type of IPA object (sets subtree and objectClass targetfilter)
        :type  o_type: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipapermlocation: Subtree to apply permissions to
        :type  o_ipapermlocation: DNOrURL
        :param o_ipapermtarget: Optional DN to apply the permission to (must be in the subtree, but may not yet exist)
        :type  o_ipapermtarget: DNParam
        :param o_ipapermtargetfrom: Optional DN subtree from where an entry can be moved (must be in the subtree, but may not yet exist)
        :type  o_ipapermtargetfrom: DNParam
        :param o_ipapermtargetto: Optional DN subtree where an entry can be moved to (must be in the subtree, but may not yet exist)
        :type  o_ipapermtargetto: DNParam
        :param o_ipapermexcludedattr: User-specified attributes to which the permission explicitly does not apply
        :type  o_ipapermexcludedattr: str
        :param o_ipapermincludedattr: User-specified attributes to which the permission applies
        :type  o_ipapermincludedattr: str
        :param o_ipapermtargetfilter: All target filters, including those implied by type and memberof
        :type  o_ipapermtargetfilter: str
        :param o_ipapermbindruletype: Bind rule type
        :type  o_ipapermbindruletype: str, valid values ['permission', 'all', 'anonymous']
        :param o_ipapermright: Rights to grant (read, search, compare, write, add, delete, all)
        :type  o_ipapermright: str, valid values ['read', 'search', 'compare', 'write', 'add', 'delete', 'all']
        """
        method = 'permission_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_filter:
            _params['filter'] = o_filter
        if o_extratargetfilter:
            _params['extratargetfilter'] = o_extratargetfilter
        if o_memberof:
            _params['memberof'] = o_memberof
        if o_permissions:
            _params['permissions'] = o_permissions
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        if o_subtree:
            _params['subtree'] = o_subtree
        if o_targetgroup:
            _params['targetgroup'] = o_targetgroup
        if o_type:
            _params['type'] = o_type
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipapermlocation:
            _params['ipapermlocation'] = o_ipapermlocation
        if o_ipapermtarget:
            _params['ipapermtarget'] = o_ipapermtarget
        if o_ipapermtargetfrom:
            _params['ipapermtargetfrom'] = o_ipapermtargetfrom
        if o_ipapermtargetto:
            _params['ipapermtargetto'] = o_ipapermtargetto
        if o_ipapermexcludedattr:
            _params['ipapermexcludedattr'] = o_ipapermexcludedattr
        if o_ipapermincludedattr:
            _params['ipapermincludedattr'] = o_ipapermincludedattr
        if o_ipapermtargetfilter:
            _params['ipapermtargetfilter'] = o_ipapermtargetfilter
        if o_ipapermbindruletype:
            _params['ipapermbindruletype'] = o_ipapermbindruletype
        if o_ipapermright:
            _params['ipapermright'] = o_ipapermright

        return self._request(method, _args, _params)

    def permission_remove_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_privilege=None,
    ):
        """Remove members from a permission.
        :param a_cn: Permission name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_privilege: privileges to remove
        :type  o_privilege: str
        """
        method = 'permission_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_privilege:
            _params['privilege'] = o_privilege

        return self._request(method, _args, _params)

    def permission_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a permission.
        :param a_cn: Permission name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'permission_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def ping(
            self,
    ):
        """Ping a remote server.
        """
        method = 'ping'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def pkinit_status(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_status=None,
            o_all=True,
            o_raw=False,
            o_server_server=None,
    ):
        """Report PKINIT status on the IPA masters
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_status: Whether PKINIT is enabled or disabled
        :type  o_status: str, valid values ['enabled', 'disabled']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_server_server: IPA server hostname
        :type  o_server_server: str
        """
        method = 'pkinit_status'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_status:
            _params['status'] = o_status
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_server_server:
            _params['server_server'] = o_server_server

        return self._request(method, _args, _params)

    def plugins(
            self,
            o_all=True,
            o_server=False,
    ):
        """Show all loaded plugins.
        :param o_all: retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_server: Forward to server instead of running locally
        :type  o_server: bool
        """
        method = 'plugins'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        if o_server:
            _params['server'] = o_server

        return self._request(method, _args, _params)

    def privilege_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_description=None,
    ):
        """Add a new privilege.
        :param a_cn: Privilege name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Privilege description
        :type  o_description: str
        """
        method = 'privilege_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def privilege_add_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_role=None,
    ):
        """Add members to a privilege.
        :param a_cn: Privilege name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_role: roles to add
        :type  o_role: str
        """
        method = 'privilege_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_role:
            _params['role'] = o_role

        return self._request(method, _args, _params)

    def privilege_add_permission(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_permission=None,
    ):
        """Add permissions to a privilege.
        :param a_cn: Privilege name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_permission: permissions
        :type  o_permission: str
        """
        method = 'privilege_add_permission'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_permission:
            _params['permission'] = o_permission

        return self._request(method, _args, _params)

    def privilege_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a privilege.
        :param a_cn: Privilege name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'privilege_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def privilege_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_description=None,
            o_cn=None,
    ):
        """Search for privileges.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Privilege description
        :type  o_description: str
        :param o_cn: Privilege name
        :type  o_cn: str
        """
        method = 'privilege_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def privilege_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify a privilege.
        :param a_cn: Privilege name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the privilege object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: Privilege description
        :type  o_description: str
        """
        method = 'privilege_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def privilege_remove_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_role=None,
    ):
        """
    Remove members from a privilege
        :param a_cn: Privilege name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_role: roles to remove
        :type  o_role: str
        """
        method = 'privilege_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_role:
            _params['role'] = o_role

        return self._request(method, _args, _params)

    def privilege_remove_permission(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_permission=None,
    ):
        """Remove permissions from a privilege.
        :param a_cn: Privilege name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_permission: permissions
        :type  o_permission: str
        """
        method = 'privilege_remove_permission'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_permission:
            _params['permission'] = o_permission

        return self._request(method, _args, _params)

    def privilege_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a privilege.
        :param a_cn: Privilege name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'privilege_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def pwpolicy_add(
            self,
            a_cn,
            o_cospriority,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_krbpwdfailurecountinterval=None,
            o_krbpwdhistorylength=None,
            o_krbpwdlockoutduration=None,
            o_krbpwdmaxfailure=None,
            o_krbmaxpwdlife=None,
            o_krbpwdmindiffchars=None,
            o_krbpwdminlength=None,
            o_krbminpwdlife=None,
    ):
        """Add a new group password policy.
        :param a_cn: Manage password policy for specific group
        :type  a_cn: str
        :param o_cospriority: Priority of the policy (higher number means lower priority
        :type  o_cospriority: int, min value 0, max value 2147483647
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_krbpwdfailurecountinterval: Period after which failure count will be reset (seconds)
        :type  o_krbpwdfailurecountinterval: int, min value 0, max value 2147483647
        :param o_krbpwdhistorylength: Password history size
        :type  o_krbpwdhistorylength: int, min value 0, max value 2147483647
        :param o_krbpwdlockoutduration: Period for which lockout is enforced (seconds)
        :type  o_krbpwdlockoutduration: int, min value 0, max value 2147483647
        :param o_krbpwdmaxfailure: Consecutive failures before lockout
        :type  o_krbpwdmaxfailure: int, min value 0, max value 2147483647
        :param o_krbmaxpwdlife: Maximum password lifetime (in days)
        :type  o_krbmaxpwdlife: int, min value 0, max value 20000
        :param o_krbpwdmindiffchars: Minimum number of character classes
        :type  o_krbpwdmindiffchars: int, min value 0, max value 5
        :param o_krbpwdminlength: Minimum length of password
        :type  o_krbpwdminlength: int, min value 0, max value 2147483647
        :param o_krbminpwdlife: Minimum password lifetime (in hours)
        :type  o_krbminpwdlife: int, min value 0, max value 2147483647
        """
        method = 'pwpolicy_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['cospriority'] = o_cospriority
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_krbpwdfailurecountinterval:
            _params['krbpwdfailurecountinterval'] = o_krbpwdfailurecountinterval
        if o_krbpwdhistorylength:
            _params['krbpwdhistorylength'] = o_krbpwdhistorylength
        if o_krbpwdlockoutduration:
            _params['krbpwdlockoutduration'] = o_krbpwdlockoutduration
        if o_krbpwdmaxfailure:
            _params['krbpwdmaxfailure'] = o_krbpwdmaxfailure
        if o_krbmaxpwdlife:
            _params['krbmaxpwdlife'] = o_krbmaxpwdlife
        if o_krbpwdmindiffchars:
            _params['krbpwdmindiffchars'] = o_krbpwdmindiffchars
        if o_krbpwdminlength:
            _params['krbpwdminlength'] = o_krbpwdminlength
        if o_krbminpwdlife:
            _params['krbminpwdlife'] = o_krbminpwdlife

        return self._request(method, _args, _params)

    def pwpolicy_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a group password policy.
        :param a_cn: Manage password policy for specific group
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'pwpolicy_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def pwpolicy_find(
            self,
            a_criteria=None,
            o_cospriority=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_krbpwdfailurecountinterval=None,
            o_krbpwdhistorylength=None,
            o_krbpwdlockoutduration=None,
            o_krbpwdmaxfailure=None,
            o_krbmaxpwdlife=None,
            o_krbpwdmindiffchars=None,
            o_krbpwdminlength=None,
            o_krbminpwdlife=None,
            o_cn=None,
    ):
        """Search for group password policies.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_cospriority: Priority of the policy (higher number means lower priority
        :type  o_cospriority: int, min value 0, max value 2147483647
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("group")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_krbpwdfailurecountinterval: Period after which failure count will be reset (seconds)
        :type  o_krbpwdfailurecountinterval: int, min value 0, max value 2147483647
        :param o_krbpwdhistorylength: Password history size
        :type  o_krbpwdhistorylength: int, min value 0, max value 2147483647
        :param o_krbpwdlockoutduration: Period for which lockout is enforced (seconds)
        :type  o_krbpwdlockoutduration: int, min value 0, max value 2147483647
        :param o_krbpwdmaxfailure: Consecutive failures before lockout
        :type  o_krbpwdmaxfailure: int, min value 0, max value 2147483647
        :param o_krbmaxpwdlife: Maximum password lifetime (in days)
        :type  o_krbmaxpwdlife: int, min value 0, max value 20000
        :param o_krbpwdmindiffchars: Minimum number of character classes
        :type  o_krbpwdmindiffchars: int, min value 0, max value 5
        :param o_krbpwdminlength: Minimum length of password
        :type  o_krbpwdminlength: int, min value 0, max value 2147483647
        :param o_krbminpwdlife: Minimum password lifetime (in hours)
        :type  o_krbminpwdlife: int, min value 0, max value 2147483647
        :param o_cn: Manage password policy for specific group
        :type  o_cn: str
        """
        method = 'pwpolicy_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_cospriority:
            _params['cospriority'] = o_cospriority
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_krbpwdfailurecountinterval:
            _params['krbpwdfailurecountinterval'] = o_krbpwdfailurecountinterval
        if o_krbpwdhistorylength:
            _params['krbpwdhistorylength'] = o_krbpwdhistorylength
        if o_krbpwdlockoutduration:
            _params['krbpwdlockoutduration'] = o_krbpwdlockoutduration
        if o_krbpwdmaxfailure:
            _params['krbpwdmaxfailure'] = o_krbpwdmaxfailure
        if o_krbmaxpwdlife:
            _params['krbmaxpwdlife'] = o_krbmaxpwdlife
        if o_krbpwdmindiffchars:
            _params['krbpwdmindiffchars'] = o_krbpwdmindiffchars
        if o_krbpwdminlength:
            _params['krbpwdminlength'] = o_krbpwdminlength
        if o_krbminpwdlife:
            _params['krbminpwdlife'] = o_krbminpwdlife
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def pwpolicy_mod(
            self,
            a_cn=None,
            o_cospriority=None,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_krbpwdfailurecountinterval=None,
            o_krbpwdhistorylength=None,
            o_krbpwdlockoutduration=None,
            o_krbpwdmaxfailure=None,
            o_krbmaxpwdlife=None,
            o_krbpwdmindiffchars=None,
            o_krbpwdminlength=None,
            o_krbminpwdlife=None,
    ):
        """Modify a group password policy.
        :param a_cn: Manage password policy for specific group
        :type  a_cn: str
        :param o_cospriority: Priority of the policy (higher number means lower priority
        :type  o_cospriority: int, min value 0, max value 2147483647
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_krbpwdfailurecountinterval: Period after which failure count will be reset (seconds)
        :type  o_krbpwdfailurecountinterval: int, min value 0, max value 2147483647
        :param o_krbpwdhistorylength: Password history size
        :type  o_krbpwdhistorylength: int, min value 0, max value 2147483647
        :param o_krbpwdlockoutduration: Period for which lockout is enforced (seconds)
        :type  o_krbpwdlockoutduration: int, min value 0, max value 2147483647
        :param o_krbpwdmaxfailure: Consecutive failures before lockout
        :type  o_krbpwdmaxfailure: int, min value 0, max value 2147483647
        :param o_krbmaxpwdlife: Maximum password lifetime (in days)
        :type  o_krbmaxpwdlife: int, min value 0, max value 20000
        :param o_krbpwdmindiffchars: Minimum number of character classes
        :type  o_krbpwdmindiffchars: int, min value 0, max value 5
        :param o_krbpwdminlength: Minimum length of password
        :type  o_krbpwdminlength: int, min value 0, max value 2147483647
        :param o_krbminpwdlife: Minimum password lifetime (in hours)
        :type  o_krbminpwdlife: int, min value 0, max value 2147483647
        """
        method = 'pwpolicy_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_cospriority:
            _params['cospriority'] = o_cospriority
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_krbpwdfailurecountinterval:
            _params['krbpwdfailurecountinterval'] = o_krbpwdfailurecountinterval
        if o_krbpwdhistorylength:
            _params['krbpwdhistorylength'] = o_krbpwdhistorylength
        if o_krbpwdlockoutduration:
            _params['krbpwdlockoutduration'] = o_krbpwdlockoutduration
        if o_krbpwdmaxfailure:
            _params['krbpwdmaxfailure'] = o_krbpwdmaxfailure
        if o_krbmaxpwdlife:
            _params['krbmaxpwdlife'] = o_krbmaxpwdlife
        if o_krbpwdmindiffchars:
            _params['krbpwdmindiffchars'] = o_krbpwdmindiffchars
        if o_krbpwdminlength:
            _params['krbpwdminlength'] = o_krbpwdminlength
        if o_krbminpwdlife:
            _params['krbminpwdlife'] = o_krbminpwdlife

        return self._request(method, _args, _params)

    def pwpolicy_show(
            self,
            a_cn=None,
            o_user=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about password policy.
        :param a_cn: Manage password policy for specific group
        :type  a_cn: str
        :param o_user: Display effective policy for a specific user
        :type  o_user: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'pwpolicy_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_user:
            _params['user'] = o_user
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def radiusproxy_add(
            self,
            a_cn,
            o_ipatokenradiussecret,
            o_ipatokenradiusserver,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_ipatokenradiusretries=None,
            o_ipatokenradiustimeout=None,
            o_description=None,
            o_ipatokenusermapattribute=None,
    ):
        """Add a new RADIUS proxy server.
        :param a_cn: RADIUS proxy server name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipatokenradiusretries: The number of times to retry authentication
        :type  o_ipatokenradiusretries: int, min value 0, max value 10
        :param o_ipatokenradiustimeout: The total timeout across all retries (in seconds)
        :type  o_ipatokenradiustimeout: int, min value 1, max value 2147483647
        :param o_ipatokenradiussecret: The secret used to encrypt data
        :type  o_ipatokenradiussecret: Password
        :param o_description: A description of this RADIUS proxy server
        :type  o_description: str
        :param o_ipatokenradiusserver: The hostname or IP (with or without port)
        :type  o_ipatokenradiusserver: str
        :param o_ipatokenusermapattribute: The username attribute on the user object
        :type  o_ipatokenusermapattribute: str
        """
        method = 'radiusproxy_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_ipatokenradiusretries:
            _params['ipatokenradiusretries'] = o_ipatokenradiusretries
        if o_ipatokenradiustimeout:
            _params['ipatokenradiustimeout'] = o_ipatokenradiustimeout
        _params['ipatokenradiussecret'] = o_ipatokenradiussecret
        if o_description:
            _params['description'] = o_description
        _params['ipatokenradiusserver'] = o_ipatokenradiusserver
        if o_ipatokenusermapattribute:
            _params['ipatokenusermapattribute'] = o_ipatokenusermapattribute

        return self._request(method, _args, _params)

    def radiusproxy_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a RADIUS proxy server.
        :param a_cn: RADIUS proxy server name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'radiusproxy_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def radiusproxy_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipatokenradiusretries=None,
            o_ipatokenradiustimeout=None,
            o_ipatokenradiussecret=None,
            o_description=None,
            o_cn=None,
            o_ipatokenradiusserver=None,
            o_ipatokenusermapattribute=None,
    ):
        """Search for RADIUS proxy servers.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipatokenradiusretries: The number of times to retry authentication
        :type  o_ipatokenradiusretries: int, min value 0, max value 10
        :param o_ipatokenradiustimeout: The total timeout across all retries (in seconds)
        :type  o_ipatokenradiustimeout: int, min value 1, max value 2147483647
        :param o_ipatokenradiussecret: The secret used to encrypt data
        :type  o_ipatokenradiussecret: Password
        :param o_description: A description of this RADIUS proxy server
        :type  o_description: str
        :param o_cn: RADIUS proxy server name
        :type  o_cn: str
        :param o_ipatokenradiusserver: The hostname or IP (with or without port)
        :type  o_ipatokenradiusserver: str
        :param o_ipatokenusermapattribute: The username attribute on the user object
        :type  o_ipatokenusermapattribute: str
        """
        method = 'radiusproxy_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipatokenradiusretries:
            _params['ipatokenradiusretries'] = o_ipatokenradiusretries
        if o_ipatokenradiustimeout:
            _params['ipatokenradiustimeout'] = o_ipatokenradiustimeout
        if o_ipatokenradiussecret:
            _params['ipatokenradiussecret'] = o_ipatokenradiussecret
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn
        if o_ipatokenradiusserver:
            _params['ipatokenradiusserver'] = o_ipatokenradiusserver
        if o_ipatokenusermapattribute:
            _params['ipatokenusermapattribute'] = o_ipatokenusermapattribute

        return self._request(method, _args, _params)

    def radiusproxy_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_ipatokenradiusretries=None,
            o_ipatokenradiustimeout=None,
            o_ipatokenradiussecret=None,
            o_description=None,
            o_ipatokenradiusserver=None,
            o_ipatokenusermapattribute=None,
    ):
        """Modify a RADIUS proxy server.
        :param a_cn: RADIUS proxy server name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the RADIUS proxy server object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipatokenradiusretries: The number of times to retry authentication
        :type  o_ipatokenradiusretries: int, min value 0, max value 10
        :param o_ipatokenradiustimeout: The total timeout across all retries (in seconds)
        :type  o_ipatokenradiustimeout: int, min value 1, max value 2147483647
        :param o_ipatokenradiussecret: The secret used to encrypt data
        :type  o_ipatokenradiussecret: Password
        :param o_description: A description of this RADIUS proxy server
        :type  o_description: str
        :param o_ipatokenradiusserver: The hostname or IP (with or without port)
        :type  o_ipatokenradiusserver: str
        :param o_ipatokenusermapattribute: The username attribute on the user object
        :type  o_ipatokenusermapattribute: str
        """
        method = 'radiusproxy_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipatokenradiusretries:
            _params['ipatokenradiusretries'] = o_ipatokenradiusretries
        if o_ipatokenradiustimeout:
            _params['ipatokenradiustimeout'] = o_ipatokenradiustimeout
        if o_ipatokenradiussecret:
            _params['ipatokenradiussecret'] = o_ipatokenradiussecret
        if o_description:
            _params['description'] = o_description
        if o_ipatokenradiusserver:
            _params['ipatokenradiusserver'] = o_ipatokenradiusserver
        if o_ipatokenusermapattribute:
            _params['ipatokenusermapattribute'] = o_ipatokenusermapattribute

        return self._request(method, _args, _params)

    def radiusproxy_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a RADIUS proxy server.
        :param a_cn: RADIUS proxy server name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'radiusproxy_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def realmdomains_mod(
            self,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_force=False,
            o_raw=False,
            o_rights=False,
            o_add_domain=None,
            o_del_domain=None,
            o_associateddomain=None,
    ):
        """Modify realm domains.
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_force: Force adding domain even if not in DNS
        :type  o_force: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_add_domain: Add domain
        :type  o_add_domain: str
        :param o_del_domain: Delete domain
        :type  o_del_domain: str
        :param o_associateddomain: Domain
        :type  o_associateddomain: str
        """
        method = 'realmdomains_mod'

        _args = list()

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['force'] = o_force
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_add_domain:
            _params['add_domain'] = o_add_domain
        if o_del_domain:
            _params['del_domain'] = o_del_domain
        if o_associateddomain:
            _params['associateddomain'] = o_associateddomain

        return self._request(method, _args, _params)

    def realmdomains_show(
            self,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display the list of realm domains.
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'realmdomains_show'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def role_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_description=None,
    ):
        """Add a new role.
        :param a_cn: Role name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this role-group
        :type  o_description: str
        """
        method = 'role_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def role_add_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_service=None,
            o_user=None,
    ):
        """Add members to a role.
        :param a_cn: Role name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        :param o_service: services to add
        :type  o_service: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'role_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_service:
            _params['service'] = o_service
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def role_add_privilege(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_privilege=None,
    ):
        """Add privileges to a role.
        :param a_cn: Role name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_privilege: privileges
        :type  o_privilege: str
        """
        method = 'role_add_privilege'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_privilege:
            _params['privilege'] = o_privilege

        return self._request(method, _args, _params)

    def role_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a role.
        :param a_cn: Role name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'role_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def role_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_description=None,
            o_cn=None,
    ):
        """Search for roles.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this role-group
        :type  o_description: str
        :param o_cn: Role name
        :type  o_cn: str
        """
        method = 'role_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def role_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify a role.
        :param a_cn: Role name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the role object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: A description of this role-group
        :type  o_description: str
        """
        method = 'role_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def role_remove_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_service=None,
            o_user=None,
    ):
        """Remove members from a role.
        :param a_cn: Role name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        :param o_service: services to remove
        :type  o_service: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'role_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_service:
            _params['service'] = o_service
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def role_remove_privilege(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_privilege=None,
    ):
        """Remove privileges from a role.
        :param a_cn: Role name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_privilege: privileges
        :type  o_privilege: str
        """
        method = 'role_remove_privilege'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_privilege:
            _params['privilege'] = o_privilege

        return self._request(method, _args, _params)

    def role_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a role.
        :param a_cn: Role name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'role_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def schema(
            self,
            o_known_fingerprints=None,
    ):
        """None
        :param o_known_fingerprints: Fingerprint of schema cached by client
        :type  o_known_fingerprints: str
        """
        method = 'schema'

        _args = list()

        _params = dict()
        if o_known_fingerprints:
            _params['known_fingerprints'] = o_known_fingerprints

        return self._request(method, _args, _params)

    def selfservice_add(
            self,
            a_aciname,
            o_attrs,
            o_all=True,
            o_raw=False,
            o_permissions=None,
    ):
        """Add a new self-service permission.
        :param a_aciname: Self-service name
        :type  a_aciname: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_attrs: Attributes to which the permission applies.
        :type  o_attrs: str
        :param o_permissions: Permissions to grant (read, write). Default is write.
        :type  o_permissions: str
        """
        method = 'selfservice_add'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['attrs'] = o_attrs
        if o_permissions:
            _params['permissions'] = o_permissions

        return self._request(method, _args, _params)

    def selfservice_del(
            self,
            a_aciname,
    ):
        """Delete a self-service permission.
        :param a_aciname: Self-service name
        :type  a_aciname: str
        """
        method = 'selfservice_del'

        _args = list()
        _args.append(a_aciname)

        _params = dict()

        return self._request(method, _args, _params)

    def selfservice_find(
            self,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_attrs=None,
            o_aciname=None,
            o_permissions=None,
    ):
        """Search for a self-service permission.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_attrs: Attributes to which the permission applies.
        :type  o_attrs: str
        :param o_aciname: Self-service name
        :type  o_aciname: str
        :param o_permissions: Permissions to grant (read, write). Default is write.
        :type  o_permissions: str
        """
        method = 'selfservice_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_aciname:
            _params['aciname'] = o_aciname
        if o_permissions:
            _params['permissions'] = o_permissions

        return self._request(method, _args, _params)

    def selfservice_mod(
            self,
            a_aciname,
            o_all=True,
            o_raw=False,
            o_attrs=None,
            o_permissions=None,
    ):
        """Modify a self-service permission.
        :param a_aciname: Self-service name
        :type  a_aciname: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_attrs: Attributes to which the permission applies.
        :type  o_attrs: str
        :param o_permissions: Permissions to grant (read, write). Default is write.
        :type  o_permissions: str
        """
        method = 'selfservice_mod'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_attrs:
            _params['attrs'] = o_attrs
        if o_permissions:
            _params['permissions'] = o_permissions

        return self._request(method, _args, _params)

    def selfservice_show(
            self,
            a_aciname,
            o_all=True,
            o_raw=False,
    ):
        """Display information about a self-service permission.
        :param a_aciname: Self-service name
        :type  a_aciname: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'selfservice_show'

        _args = list()
        _args.append(a_aciname)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def selinuxusermap_add(
            self,
            a_cn,
            o_ipaselinuxuser,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_seealso=None,
            o_hostcategory=None,
            o_usercategory=None,
    ):
        """Create a new SELinux User Map.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_seealso: HBAC Rule that defines the users, groups and hostgroups
        :type  o_seealso: str
        :param o_ipaselinuxuser: SELinux User
        :type  o_ipaselinuxuser: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'selinuxusermap_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_seealso:
            _params['seealso'] = o_seealso
        _params['ipaselinuxuser'] = o_ipaselinuxuser
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def selinuxusermap_add_host(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Add target hosts and hostgroups to an SELinux User Map rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        """
        method = 'selinuxusermap_add_host'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def selinuxusermap_add_user(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Add users and groups to an SELinux User Map rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'selinuxusermap_add_user'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def selinuxusermap_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a SELinux User Map.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'selinuxusermap_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def selinuxusermap_disable(
            self,
            a_cn,
    ):
        """Disable an SELinux User Map rule.
        :param a_cn: Rule name
        :type  a_cn: str
        """
        method = 'selinuxusermap_disable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def selinuxusermap_enable(
            self,
            a_cn,
    ):
        """Enable an SELinux User Map rule.
        :param a_cn: Rule name
        :type  a_cn: str
        """
        method = 'selinuxusermap_enable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def selinuxusermap_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_seealso=None,
            o_cn=None,
            o_ipaselinuxuser=None,
            o_hostcategory=None,
            o_usercategory=None,
    ):
        """Search for SELinux User Maps.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_seealso: HBAC Rule that defines the users, groups and hostgroups
        :type  o_seealso: str
        :param o_cn: Rule name
        :type  o_cn: str
        :param o_ipaselinuxuser: SELinux User
        :type  o_ipaselinuxuser: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'selinuxusermap_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_seealso:
            _params['seealso'] = o_seealso
        if o_cn:
            _params['cn'] = o_cn
        if o_ipaselinuxuser:
            _params['ipaselinuxuser'] = o_ipaselinuxuser
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def selinuxusermap_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_ipaenabledflag=None,
            o_description=None,
            o_seealso=None,
            o_ipaselinuxuser=None,
            o_hostcategory=None,
            o_usercategory=None,
    ):
        """Modify a SELinux User Map.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_description: Description
        :type  o_description: str
        :param o_seealso: HBAC Rule that defines the users, groups and hostgroups
        :type  o_seealso: str
        :param o_ipaselinuxuser: SELinux User
        :type  o_ipaselinuxuser: str
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'selinuxusermap_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_description:
            _params['description'] = o_description
        if o_seealso:
            _params['seealso'] = o_seealso
        if o_ipaselinuxuser:
            _params['ipaselinuxuser'] = o_ipaselinuxuser
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def selinuxusermap_remove_host(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Remove target hosts and hostgroups from an SELinux User Map rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        """
        method = 'selinuxusermap_remove_host'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def selinuxusermap_remove_user(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Remove users and groups from an SELinux User Map rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'selinuxusermap_remove_user'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def selinuxusermap_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display the properties of a SELinux User Map rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'selinuxusermap_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def server_conncheck(
            self,
            a_remote_cn,
            a_cn,
    ):
        """Check connection to remote IPA server.
        :param a_remote_cn: Remote IPA server hostname
        :type  a_remote_cn: str
        :param a_cn: IPA server hostname
        :type  a_cn: str
        """
        method = 'server_conncheck'

        _args = list()
        _args.append(a_remote_cn)
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def server_del(
            self,
            a_cn,
            o_continue=False,
            o_force=False,
            o_ignore_last_of_role=False,
            o_ignore_topology_disconnect=False,
    ):
        """Delete IPA server.
        :param a_cn: IPA server hostname
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        :param o_force: Force server removal even if it does not exist
        :type  o_force: bool
        :param o_ignore_last_of_role: Skip a check whether the last CA master or DNS server is removed
        :type  o_ignore_last_of_role: bool
        :param o_ignore_topology_disconnect: Ignore topology connectivity problems after removal
        :type  o_ignore_topology_disconnect: bool
        """
        method = 'server_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue
        if o_force:
            _params['force'] = o_force
        if o_ignore_last_of_role:
            _params['ignore_last_of_role'] = o_ignore_last_of_role
        if o_ignore_topology_disconnect:
            _params['ignore_topology_disconnect'] = o_ignore_topology_disconnect

        return self._request(method, _args, _params)

    def server_find(
            self,
            a_criteria=None,
            o_in_location=None,
            o_not_in_location=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_no_topologysuffix=None,
            o_servrole=None,
            o_topologysuffix=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipamaxdomainlevel=None,
            o_ipamindomainlevel=None,
            o_cn=None,
    ):
        """Search for IPA servers.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_in_location: Search for servers with these ipa locations.
        :type  o_in_location: DNSNameParam
        :param o_not_in_location: Search for servers without these ipa locations.
        :type  o_not_in_location: DNSNameParam
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_no_topologysuffix: Search for servers without these managed suffixes.
        :type  o_no_topologysuffix: str
        :param o_servrole: Search for servers with these enabled roles.
        :type  o_servrole: str
        :param o_topologysuffix: Search for servers with these managed suffixes.
        :type  o_topologysuffix: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipamaxdomainlevel: Maximum domain level
        :type  o_ipamaxdomainlevel: int, min value -2147483648, max value 2147483647
        :param o_ipamindomainlevel: Minimum domain level
        :type  o_ipamindomainlevel: int, min value -2147483648, max value 2147483647
        :param o_cn: IPA server hostname
        :type  o_cn: str
        """
        method = 'server_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_in_location:
            _params['in_location'] = o_in_location
        if o_not_in_location:
            _params['not_in_location'] = o_not_in_location
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_no_topologysuffix:
            _params['no_topologysuffix'] = o_no_topologysuffix
        if o_servrole:
            _params['servrole'] = o_servrole
        if o_topologysuffix:
            _params['topologysuffix'] = o_topologysuffix
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipamaxdomainlevel:
            _params['ipamaxdomainlevel'] = o_ipamaxdomainlevel
        if o_ipamindomainlevel:
            _params['ipamindomainlevel'] = o_ipamindomainlevel
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def server_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_ipalocation_location=None,
            o_ipaserviceweight=None,
    ):
        """Modify information about an IPA server.
        :param a_cn: IPA server hostname
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipalocation_location: Server location
        :type  o_ipalocation_location: DNSNameParam
        :param o_ipaserviceweight: Weight for server services
        :type  o_ipaserviceweight: int, min value 0, max value 65535
        """
        method = 'server_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipalocation_location:
            _params['ipalocation_location'] = o_ipalocation_location
        if o_ipaserviceweight:
            _params['ipaserviceweight'] = o_ipaserviceweight

        return self._request(method, _args, _params)

    def server_role_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_role_servrole=None,
            o_status='enabled',
            o_all=True,
            o_include_master=False,
            o_raw=False,
            o_server_server=None,
    ):
        """Find a server role on a server(s)
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_role_servrole: IPA server role name
        :type  o_role_servrole: str
        :param o_status: Status of the role
        :type  o_status: str, valid values ['enabled', 'configured', 'hidden', 'absent']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_include_master: Include IPA master entries
        :type  o_include_master: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_server_server: IPA server hostname
        :type  o_server_server: str
        """
        method = 'server_role_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_role_servrole:
            _params['role_servrole'] = o_role_servrole
        if o_status:
            _params['status'] = o_status
        _params['all'] = o_all
        _params['include_master'] = o_include_master
        _params['raw'] = o_raw
        if o_server_server:
            _params['server_server'] = o_server_server

        return self._request(method, _args, _params)

    def server_role_show(
            self,
            a_role_servrole,
            a_server_server,
            o_all=True,
            o_raw=False,
    ):
        """Show role status on a server
        :param a_role_servrole: IPA server role name
        :type  a_role_servrole: str
        :param a_server_server: IPA server hostname
        :type  a_server_server: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'server_role_show'

        _args = list()
        _args.append(a_role_servrole)
        _args.append(a_server_server)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def server_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Show IPA server.
        :param a_cn: IPA server hostname
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'server_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def server_state(
            self,
            a_cn,
            o_state,
    ):
        """Set enabled/hidden state of a server.
        :param a_cn: IPA server hostname
        :type  a_cn: str
        :param o_state: Server state
        :type  o_state: str, valid values ['enabled', 'hidden']
        """
        method = 'server_state'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['state'] = o_state

        return self._request(method, _args, _params)

    def service_add(
            self,
            a_krbcanonicalname,
            o_ipakrbokasdelegate=None,
            o_ipakrboktoauthasdelegate=None,
            o_ipakrbrequirespreauth=None,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_force=False,
            o_no_members=False,
            o_raw=False,
            o_usercertificate=None,
            o_krbprincipalauthind=None,
            o_ipakrbauthzdata=None,
    ):
        """Add a new IPA service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_ipakrbokasdelegate: Client credentials may be delegated to the service
        :type  o_ipakrbokasdelegate: Bool
        :param o_ipakrboktoauthasdelegate: The service is allowed to authenticate on behalf of a client
        :type  o_ipakrboktoauthasdelegate: Bool
        :param o_ipakrbrequirespreauth: Pre-authentication is required for the service
        :type  o_ipakrbrequirespreauth: Bool
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_force: force principal name even if not in DNS
        :type  o_force: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded service certificate
        :type  o_usercertificate: Certificate
        :param o_krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type  o_krbprincipalauthind: str
        :param o_ipakrbauthzdata: Override default list of supported PAC types. Use 'NONE' to disable PAC support for this service, e.g. this might be necessary for NFS services.
        :type  o_ipakrbauthzdata: str, valid values ['MS-PAC', 'PAD', 'NONE']
        """
        method = 'service_add'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        if o_ipakrbokasdelegate:
            _params['ipakrbokasdelegate'] = o_ipakrbokasdelegate
        if o_ipakrboktoauthasdelegate:
            _params['ipakrboktoauthasdelegate'] = o_ipakrboktoauthasdelegate
        if o_ipakrbrequirespreauth:
            _params['ipakrbrequirespreauth'] = o_ipakrbrequirespreauth
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['force'] = o_force
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbprincipalauthind:
            _params['krbprincipalauthind'] = o_krbprincipalauthind
        if o_ipakrbauthzdata:
            _params['ipakrbauthzdata'] = o_ipakrbauthzdata

        return self._request(method, _args, _params)

    def service_add_cert(
            self,
            a_krbcanonicalname,
            o_usercertificate,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add new certificates to a service
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded service certificate
        :type  o_usercertificate: Certificate
        """
        method = 'service_add_cert'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def service_add_host(
            self,
            a_krbcanonicalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_host=None,
    ):
        """Add hosts that can manage this service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_host: hosts to add
        :type  o_host: str
        """
        method = 'service_add_host'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def service_add_principal(
            self,
            a_krbcanonicalname,
            a_krbprincipalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add new principal alias to a service
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param a_krbprincipalname: Service principal alias
        :type  a_krbprincipalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'service_add_principal'

        _args = list()
        _args.append(a_krbcanonicalname)
        _args.append(a_krbprincipalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def service_allow_create_keytab(
            self,
            a_krbcanonicalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_user=None,
    ):
        """Allow users, groups, hosts or host groups to create a keytab of this service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'service_allow_create_keytab'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def service_allow_retrieve_keytab(
            self,
            a_krbcanonicalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_user=None,
    ):
        """Allow users, groups, hosts or host groups to retrieve a keytab of this service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'service_allow_retrieve_keytab'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def service_del(
            self,
            a_krbcanonicalname,
            o_continue=False,
    ):
        """Delete an IPA service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'service_del'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def service_disable(
            self,
            a_krbcanonicalname,
    ):
        """Disable the Kerberos key and SSL certificate of a service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        """
        method = 'service_disable'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()

        return self._request(method, _args, _params)

    def service_disallow_create_keytab(
            self,
            a_krbcanonicalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_user=None,
    ):
        """Disallow users, groups, hosts or host groups to create a keytab of this service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'service_disallow_create_keytab'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def service_disallow_retrieve_keytab(
            self,
            a_krbcanonicalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_hostgroup=None,
            o_host=None,
            o_user=None,
    ):
        """Disallow users, groups, hosts or host groups to retrieve a keytab of this service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'service_disallow_retrieve_keytab'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def service_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_man_by_host=None,
            o_not_man_by_host=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_krbcanonicalname=None,
            o_krbprincipalname=None,
            o_krbprincipalauthind=None,
            o_ipakrbauthzdata=None,
    ):
        """Search for IPA services.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_man_by_host: Search for services with these managed by hosts.
        :type  o_man_by_host: str
        :param o_not_man_by_host: Search for services without these managed by hosts.
        :type  o_not_man_by_host: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("canonical-principal")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_krbcanonicalname: Service principal
        :type  o_krbcanonicalname: Principal
        :param o_krbprincipalname: Service principal alias
        :type  o_krbprincipalname: Principal
        :param o_krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type  o_krbprincipalauthind: str
        :param o_ipakrbauthzdata: Override default list of supported PAC types. Use 'NONE' to disable PAC support for this service, e.g. this might be necessary for NFS services.
        :type  o_ipakrbauthzdata: str, valid values ['MS-PAC', 'PAD', 'NONE']
        """
        method = 'service_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_man_by_host:
            _params['man_by_host'] = o_man_by_host
        if o_not_man_by_host:
            _params['not_man_by_host'] = o_not_man_by_host
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_krbcanonicalname:
            _params['krbcanonicalname'] = o_krbcanonicalname
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        if o_krbprincipalauthind:
            _params['krbprincipalauthind'] = o_krbprincipalauthind
        if o_ipakrbauthzdata:
            _params['ipakrbauthzdata'] = o_ipakrbauthzdata

        return self._request(method, _args, _params)

    def service_mod(
            self,
            a_krbcanonicalname,
            o_ipakrbokasdelegate=None,
            o_ipakrboktoauthasdelegate=None,
            o_ipakrbrequirespreauth=None,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_usercertificate=None,
            o_krbprincipalname=None,
            o_krbprincipalauthind=None,
            o_ipakrbauthzdata=None,
    ):
        """Modify an existing IPA service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_ipakrbokasdelegate: Client credentials may be delegated to the service
        :type  o_ipakrbokasdelegate: Bool
        :param o_ipakrboktoauthasdelegate: The service is allowed to authenticate on behalf of a client
        :type  o_ipakrboktoauthasdelegate: Bool
        :param o_ipakrbrequirespreauth: Pre-authentication is required for the service
        :type  o_ipakrbrequirespreauth: Bool
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_usercertificate: Base-64 encoded service certificate
        :type  o_usercertificate: Certificate
        :param o_krbprincipalname: Service principal alias
        :type  o_krbprincipalname: Principal
        :param o_krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type  o_krbprincipalauthind: str
        :param o_ipakrbauthzdata: Override default list of supported PAC types. Use 'NONE' to disable PAC support for this service, e.g. this might be necessary for NFS services.
        :type  o_ipakrbauthzdata: str, valid values ['MS-PAC', 'PAD', 'NONE']
        """
        method = 'service_mod'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        if o_ipakrbokasdelegate:
            _params['ipakrbokasdelegate'] = o_ipakrbokasdelegate
        if o_ipakrboktoauthasdelegate:
            _params['ipakrboktoauthasdelegate'] = o_ipakrboktoauthasdelegate
        if o_ipakrbrequirespreauth:
            _params['ipakrbrequirespreauth'] = o_ipakrbrequirespreauth
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        if o_krbprincipalauthind:
            _params['krbprincipalauthind'] = o_krbprincipalauthind
        if o_ipakrbauthzdata:
            _params['ipakrbauthzdata'] = o_ipakrbauthzdata

        return self._request(method, _args, _params)

    def service_remove_cert(
            self,
            a_krbcanonicalname,
            o_usercertificate,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove certificates from a service
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded service certificate
        :type  o_usercertificate: Certificate
        """
        method = 'service_remove_cert'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def service_remove_host(
            self,
            a_krbcanonicalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_host=None,
    ):
        """Remove hosts that can manage this service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_host: hosts to remove
        :type  o_host: str
        """
        method = 'service_remove_host'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def service_remove_principal(
            self,
            a_krbcanonicalname,
            a_krbprincipalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove principal alias from a service
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param a_krbprincipalname: Service principal alias
        :type  a_krbprincipalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'service_remove_principal'

        _args = list()
        _args.append(a_krbcanonicalname)
        _args.append(a_krbprincipalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def service_show(
            self,
            a_krbcanonicalname,
            o_out=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about an IPA service.
        :param a_krbcanonicalname: Service principal
        :type  a_krbcanonicalname: Principal
        :param o_out: file to store certificate in
        :type  o_out: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'service_show'

        _args = list()
        _args.append(a_krbcanonicalname)

        _params = dict()
        if o_out:
            _params['out'] = o_out
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def servicedelegationrule_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Create a new service delegation rule.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'servicedelegationrule_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def servicedelegationrule_add_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_principal=None,
    ):
        """Add member to a named service delegation rule.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_principal: principal to add
        :type  o_principal: str
        """
        method = 'servicedelegationrule_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_principal:
            _params['principal'] = o_principal

        return self._request(method, _args, _params)

    def servicedelegationrule_add_target(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_servicedelegationtarget=None,
    ):
        """Add target to a named service delegation rule.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_servicedelegationtarget: service delegation targets to add
        :type  o_servicedelegationtarget: str
        """
        method = 'servicedelegationrule_add_target'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_servicedelegationtarget:
            _params['servicedelegationtarget'] = o_servicedelegationtarget

        return self._request(method, _args, _params)

    def servicedelegationrule_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete service delegation.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'servicedelegationrule_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def servicedelegationrule_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_cn=None,
    ):
        """Search for service delegations rule.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("delegation-name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_cn: Delegation name
        :type  o_cn: str
        """
        method = 'servicedelegationrule_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def servicedelegationrule_remove_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_principal=None,
    ):
        """Remove member from a named service delegation rule.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_principal: principal to remove
        :type  o_principal: str
        """
        method = 'servicedelegationrule_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_principal:
            _params['principal'] = o_principal

        return self._request(method, _args, _params)

    def servicedelegationrule_remove_target(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_servicedelegationtarget=None,
    ):
        """Remove target from a named service delegation rule.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_servicedelegationtarget: service delegation targets to remove
        :type  o_servicedelegationtarget: str
        """
        method = 'servicedelegationrule_remove_target'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_servicedelegationtarget:
            _params['servicedelegationtarget'] = o_servicedelegationtarget

        return self._request(method, _args, _params)

    def servicedelegationrule_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a named service delegation rule.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'servicedelegationrule_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def servicedelegationtarget_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
    ):
        """Create a new service delegation target.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'servicedelegationtarget_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def servicedelegationtarget_add_member(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_principal=None,
    ):
        """Add member to a named service delegation target.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_principal: principal to add
        :type  o_principal: str
        """
        method = 'servicedelegationtarget_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_principal:
            _params['principal'] = o_principal

        return self._request(method, _args, _params)

    def servicedelegationtarget_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete service delegation target.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'servicedelegationtarget_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def servicedelegationtarget_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_cn=None,
    ):
        """Search for service delegation target.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("delegation-name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_cn: Delegation name
        :type  o_cn: str
        """
        method = 'servicedelegationtarget_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def servicedelegationtarget_remove_member(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_principal=None,
    ):
        """Remove member from a named service delegation target.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_principal: principal to remove
        :type  o_principal: str
        """
        method = 'servicedelegationtarget_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_principal:
            _params['principal'] = o_principal

        return self._request(method, _args, _params)

    def servicedelegationtarget_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a named service delegation target.
        :param a_cn: Delegation name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'servicedelegationtarget_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def session_logout(
            self,
    ):
        """
    RPC command used to log the current user out of their session.
        """
        method = 'session_logout'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def sidgen_was_run(
            self,
    ):
        """Determine whether ipa-adtrust-install has been run with sidgen task
        """
        method = 'sidgen_was_run'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)

    def stageuser_activate(
            self,
            a_uid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Activate a stage user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'stageuser_activate'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def stageuser_add(
            self,
            a_uid,
            o_givenname,
            o_sn,
            o_cn,
            o_from_delete=None,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_random=False,
            o_raw=False,
            o_usercertificate=None,
            o_krbpasswordexpiration=None,
            o_krbprincipalexpiration=None,
            o_gidnumber=None,
            o_uidnumber=None,
            o_userpassword=None,
            o_carlicense=None,
            o_l=None,
            o_userclass=None,
            o_departmentnumber=None,
            o_mail=None,
            o_employeenumber=None,
            o_employeetype=None,
            o_facsimiletelephonenumber=None,
            o_homedirectory=None,
            o_manager=None,
            o_mobile=None,
            o_ou=None,
            o_pager=None,
            o_telephonenumber=None,
            o_postalcode=None,
            o_preferredlanguage=None,
            o_ipatokenradiusconfiglink=None,
            o_ipatokenradiususername=None,
            o_loginshell=None,
            o_ipasshpubkey=None,
            o_st=None,
            o_street=None,
            o_title=None,
            o_ipauserauthtype=None,
            o_krbprincipalname=None,
            o_displayname=None,
            o_gecos=None,
            o_initials=None,
    ):
        """Add a new stage user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_from_delete: Create Stage user in from a delete user
        :type  o_from_delete: Bool
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_random: Generate a random user password
        :type  o_random: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        :param o_krbpasswordexpiration: User password expiration
        :type  o_krbpasswordexpiration: DateTime
        :param o_krbprincipalexpiration: Kerberos principal expiration
        :type  o_krbprincipalexpiration: DateTime
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number (system will assign one if not provided)
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_userpassword: Prompt to set the user password
        :type  o_userpassword: Password
        :param o_carlicense: Car License
        :type  o_carlicense: str
        :param o_l: City
        :type  o_l: str
        :param o_userclass: User category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_departmentnumber: Department Number
        :type  o_departmentnumber: str
        :param o_mail: Email address
        :type  o_mail: str
        :param o_employeenumber: Employee Number
        :type  o_employeenumber: str
        :param o_employeetype: Employee Type
        :type  o_employeetype: str
        :param o_facsimiletelephonenumber: Fax Number
        :type  o_facsimiletelephonenumber: str
        :param o_givenname: First name
        :type  o_givenname: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_sn: Last name
        :type  o_sn: str
        :param o_manager: Manager
        :type  o_manager: str
        :param o_mobile: Mobile Telephone Number
        :type  o_mobile: str
        :param o_ou: Org. Unit
        :type  o_ou: str
        :param o_pager: Pager Number
        :type  o_pager: str
        :param o_telephonenumber: Telephone Number
        :type  o_telephonenumber: str
        :param o_postalcode: ZIP
        :type  o_postalcode: str
        :param o_preferredlanguage: Preferred Language
        :type  o_preferredlanguage: str
        :param o_ipatokenradiusconfiglink: RADIUS proxy configuration
        :type  o_ipatokenradiusconfiglink: str
        :param o_ipatokenradiususername: RADIUS proxy username
        :type  o_ipatokenradiususername: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        :param o_ipasshpubkey: SSH public key
        :type  o_ipasshpubkey: str
        :param o_st: State/Province
        :type  o_st: str
        :param o_street: Street address
        :type  o_street: str
        :param o_title: Job Title
        :type  o_title: str
        :param o_ipauserauthtype: Types of supported user authentication
        :type  o_ipauserauthtype: str, valid values ['password', 'radius', 'otp']
        :param o_krbprincipalname: Principal alias
        :type  o_krbprincipalname: Principal
        :param o_cn: Full name
        :type  o_cn: str
        :param o_displayname: Display name
        :type  o_displayname: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_initials: Initials
        :type  o_initials: str
        """
        method = 'stageuser_add'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        if o_from_delete:
            _params['from_delete'] = o_from_delete
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_random:
            _params['random'] = o_random
        _params['raw'] = o_raw
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbpasswordexpiration:
            _params['krbpasswordexpiration'] = o_krbpasswordexpiration
        if o_krbprincipalexpiration:
            _params['krbprincipalexpiration'] = o_krbprincipalexpiration
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_carlicense:
            _params['carlicense'] = o_carlicense
        if o_l:
            _params['l'] = o_l
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_departmentnumber:
            _params['departmentnumber'] = o_departmentnumber
        if o_mail:
            _params['mail'] = o_mail
        if o_employeenumber:
            _params['employeenumber'] = o_employeenumber
        if o_employeetype:
            _params['employeetype'] = o_employeetype
        if o_facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = o_facsimiletelephonenumber
        _params['givenname'] = o_givenname
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        _params['sn'] = o_sn
        if o_manager:
            _params['manager'] = o_manager
        if o_mobile:
            _params['mobile'] = o_mobile
        if o_ou:
            _params['ou'] = o_ou
        if o_pager:
            _params['pager'] = o_pager
        if o_telephonenumber:
            _params['telephonenumber'] = o_telephonenumber
        if o_postalcode:
            _params['postalcode'] = o_postalcode
        if o_preferredlanguage:
            _params['preferredlanguage'] = o_preferredlanguage
        if o_ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = o_ipatokenradiusconfiglink
        if o_ipatokenradiususername:
            _params['ipatokenradiususername'] = o_ipatokenradiususername
        if o_loginshell:
            _params['loginshell'] = o_loginshell
        if o_ipasshpubkey:
            _params['ipasshpubkey'] = o_ipasshpubkey
        if o_st:
            _params['st'] = o_st
        if o_street:
            _params['street'] = o_street
        if o_title:
            _params['title'] = o_title
        if o_ipauserauthtype:
            _params['ipauserauthtype'] = o_ipauserauthtype
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        _params['cn'] = o_cn
        if o_displayname:
            _params['displayname'] = o_displayname
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_initials:
            _params['initials'] = o_initials

        return self._request(method, _args, _params)

    def stageuser_add_cert(
            self,
            a_uid,
            o_usercertificate,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add one or more certificates to the stageuser entry
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        """
        method = 'stageuser_add_cert'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def stageuser_add_certmapdata(
            self,
            a_uid,
            a_ipacertmapdata=None,
            o_certificate=None,
            o_issuer=None,
            o_subject=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add one or more certificate mappings to the stage user entry.
        :param a_ipacertmapdata: Certificate mapping data
        :type  a_ipacertmapdata: str
        :param a_uid: User login
        :type  a_uid: str
        :param o_certificate: Base-64 encoded user certificate
        :type  o_certificate: Certificate
        :param o_issuer: Issuer of the certificate
        :type  o_issuer: DNParam
        :param o_subject: Subject of the certificate
        :type  o_subject: DNParam
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'stageuser_add_certmapdata'

        _args = list()
        _args.append(a_ipacertmapdata)
        _args.append(a_uid)

        _params = dict()
        if o_certificate:
            _params['certificate'] = o_certificate
        if o_issuer:
            _params['issuer'] = o_issuer
        if o_subject:
            _params['subject'] = o_subject
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def stageuser_add_manager(
            self,
            a_uid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_user=None,
    ):
        """Add a manager to the stage user entry
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'stageuser_add_manager'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def stageuser_add_principal(
            self,
            a_uid,
            a_krbprincipalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add new principal alias to the stageuser entry
        :param a_uid: User login
        :type  a_uid: str
        :param a_krbprincipalname: Principal alias
        :type  a_krbprincipalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'stageuser_add_principal'

        _args = list()
        _args.append(a_uid)
        _args.append(a_krbprincipalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def stageuser_del(
            self,
            a_uid,
            o_continue=False,
    ):
        """Delete a stage user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'stageuser_del'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def stageuser_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_in_group=None,
            o_in_hbacrule=None,
            o_in_netgroup=None,
            o_in_role=None,
            o_in_sudorule=None,
            o_not_in_group=None,
            o_not_in_hbacrule=None,
            o_not_in_netgroup=None,
            o_not_in_role=None,
            o_not_in_sudorule=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_usercertificate=None,
            o_krbpasswordexpiration=None,
            o_krbprincipalexpiration=None,
            o_gidnumber=None,
            o_uidnumber=None,
            o_userpassword=None,
            o_krbprincipalname=None,
            o_carlicense=None,
            o_l=None,
            o_userclass=None,
            o_cn=None,
            o_departmentnumber=None,
            o_displayname=None,
            o_mail=None,
            o_employeenumber=None,
            o_employeetype=None,
            o_facsimiletelephonenumber=None,
            o_givenname=None,
            o_gecos=None,
            o_homedirectory=None,
            o_initials=None,
            o_sn=None,
            o_uid=None,
            o_manager=None,
            o_mobile=None,
            o_ou=None,
            o_pager=None,
            o_telephonenumber=None,
            o_postalcode=None,
            o_preferredlanguage=None,
            o_ipatokenradiusconfiglink=None,
            o_ipatokenradiususername=None,
            o_loginshell=None,
            o_st=None,
            o_street=None,
            o_title=None,
            o_ipauserauthtype=None,
    ):
        """Search for stage users.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_in_group: Search for stage users with these member of groups.
        :type  o_in_group: str
        :param o_in_hbacrule: Search for stage users with these member of HBAC rules.
        :type  o_in_hbacrule: str
        :param o_in_netgroup: Search for stage users with these member of netgroups.
        :type  o_in_netgroup: str
        :param o_in_role: Search for stage users with these member of roles.
        :type  o_in_role: str
        :param o_in_sudorule: Search for stage users with these member of sudo rules.
        :type  o_in_sudorule: str
        :param o_not_in_group: Search for stage users without these member of groups.
        :type  o_not_in_group: str
        :param o_not_in_hbacrule: Search for stage users without these member of HBAC rules.
        :type  o_not_in_hbacrule: str
        :param o_not_in_netgroup: Search for stage users without these member of netgroups.
        :type  o_not_in_netgroup: str
        :param o_not_in_role: Search for stage users without these member of roles.
        :type  o_not_in_role: str
        :param o_not_in_sudorule: Search for stage users without these member of sudo rules.
        :type  o_not_in_sudorule: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("login")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        :param o_krbpasswordexpiration: User password expiration
        :type  o_krbpasswordexpiration: DateTime
        :param o_krbprincipalexpiration: Kerberos principal expiration
        :type  o_krbprincipalexpiration: DateTime
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number (system will assign one if not provided)
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_userpassword: Prompt to set the user password
        :type  o_userpassword: Password
        :param o_krbprincipalname: Principal alias
        :type  o_krbprincipalname: Principal
        :param o_carlicense: Car License
        :type  o_carlicense: str
        :param o_l: City
        :type  o_l: str
        :param o_userclass: User category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_cn: Full name
        :type  o_cn: str
        :param o_departmentnumber: Department Number
        :type  o_departmentnumber: str
        :param o_displayname: Display name
        :type  o_displayname: str
        :param o_mail: Email address
        :type  o_mail: str
        :param o_employeenumber: Employee Number
        :type  o_employeenumber: str
        :param o_employeetype: Employee Type
        :type  o_employeetype: str
        :param o_facsimiletelephonenumber: Fax Number
        :type  o_facsimiletelephonenumber: str
        :param o_givenname: First name
        :type  o_givenname: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_initials: Initials
        :type  o_initials: str
        :param o_sn: Last name
        :type  o_sn: str
        :param o_uid: User login
        :type  o_uid: str
        :param o_manager: Manager
        :type  o_manager: str
        :param o_mobile: Mobile Telephone Number
        :type  o_mobile: str
        :param o_ou: Org. Unit
        :type  o_ou: str
        :param o_pager: Pager Number
        :type  o_pager: str
        :param o_telephonenumber: Telephone Number
        :type  o_telephonenumber: str
        :param o_postalcode: ZIP
        :type  o_postalcode: str
        :param o_preferredlanguage: Preferred Language
        :type  o_preferredlanguage: str
        :param o_ipatokenradiusconfiglink: RADIUS proxy configuration
        :type  o_ipatokenradiusconfiglink: str
        :param o_ipatokenradiususername: RADIUS proxy username
        :type  o_ipatokenradiususername: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        :param o_st: State/Province
        :type  o_st: str
        :param o_street: Street address
        :type  o_street: str
        :param o_title: Job Title
        :type  o_title: str
        :param o_ipauserauthtype: Types of supported user authentication
        :type  o_ipauserauthtype: str, valid values ['password', 'radius', 'otp']
        """
        method = 'stageuser_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_in_group:
            _params['in_group'] = o_in_group
        if o_in_hbacrule:
            _params['in_hbacrule'] = o_in_hbacrule
        if o_in_netgroup:
            _params['in_netgroup'] = o_in_netgroup
        if o_in_role:
            _params['in_role'] = o_in_role
        if o_in_sudorule:
            _params['in_sudorule'] = o_in_sudorule
        if o_not_in_group:
            _params['not_in_group'] = o_not_in_group
        if o_not_in_hbacrule:
            _params['not_in_hbacrule'] = o_not_in_hbacrule
        if o_not_in_netgroup:
            _params['not_in_netgroup'] = o_not_in_netgroup
        if o_not_in_role:
            _params['not_in_role'] = o_not_in_role
        if o_not_in_sudorule:
            _params['not_in_sudorule'] = o_not_in_sudorule
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbpasswordexpiration:
            _params['krbpasswordexpiration'] = o_krbpasswordexpiration
        if o_krbprincipalexpiration:
            _params['krbprincipalexpiration'] = o_krbprincipalexpiration
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        if o_carlicense:
            _params['carlicense'] = o_carlicense
        if o_l:
            _params['l'] = o_l
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_cn:
            _params['cn'] = o_cn
        if o_departmentnumber:
            _params['departmentnumber'] = o_departmentnumber
        if o_displayname:
            _params['displayname'] = o_displayname
        if o_mail:
            _params['mail'] = o_mail
        if o_employeenumber:
            _params['employeenumber'] = o_employeenumber
        if o_employeetype:
            _params['employeetype'] = o_employeetype
        if o_facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = o_facsimiletelephonenumber
        if o_givenname:
            _params['givenname'] = o_givenname
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        if o_initials:
            _params['initials'] = o_initials
        if o_sn:
            _params['sn'] = o_sn
        if o_uid:
            _params['uid'] = o_uid
        if o_manager:
            _params['manager'] = o_manager
        if o_mobile:
            _params['mobile'] = o_mobile
        if o_ou:
            _params['ou'] = o_ou
        if o_pager:
            _params['pager'] = o_pager
        if o_telephonenumber:
            _params['telephonenumber'] = o_telephonenumber
        if o_postalcode:
            _params['postalcode'] = o_postalcode
        if o_preferredlanguage:
            _params['preferredlanguage'] = o_preferredlanguage
        if o_ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = o_ipatokenradiusconfiglink
        if o_ipatokenradiususername:
            _params['ipatokenradiususername'] = o_ipatokenradiususername
        if o_loginshell:
            _params['loginshell'] = o_loginshell
        if o_st:
            _params['st'] = o_st
        if o_street:
            _params['street'] = o_street
        if o_title:
            _params['title'] = o_title
        if o_ipauserauthtype:
            _params['ipauserauthtype'] = o_ipauserauthtype

        return self._request(method, _args, _params)

    def stageuser_mod(
            self,
            a_uid,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_random=False,
            o_raw=False,
            o_rights=False,
            o_usercertificate=None,
            o_krbpasswordexpiration=None,
            o_krbprincipalexpiration=None,
            o_gidnumber=None,
            o_uidnumber=None,
            o_userpassword=None,
            o_krbprincipalname=None,
            o_carlicense=None,
            o_l=None,
            o_userclass=None,
            o_cn=None,
            o_departmentnumber=None,
            o_displayname=None,
            o_mail=None,
            o_employeenumber=None,
            o_employeetype=None,
            o_facsimiletelephonenumber=None,
            o_givenname=None,
            o_gecos=None,
            o_homedirectory=None,
            o_initials=None,
            o_sn=None,
            o_manager=None,
            o_mobile=None,
            o_ou=None,
            o_pager=None,
            o_telephonenumber=None,
            o_postalcode=None,
            o_preferredlanguage=None,
            o_ipatokenradiusconfiglink=None,
            o_ipatokenradiususername=None,
            o_loginshell=None,
            o_ipasshpubkey=None,
            o_st=None,
            o_street=None,
            o_title=None,
            o_ipauserauthtype=None,
    ):
        """Modify a stage user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the stage user object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_random: Generate a random user password
        :type  o_random: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        :param o_krbpasswordexpiration: User password expiration
        :type  o_krbpasswordexpiration: DateTime
        :param o_krbprincipalexpiration: Kerberos principal expiration
        :type  o_krbprincipalexpiration: DateTime
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number (system will assign one if not provided)
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_userpassword: Prompt to set the user password
        :type  o_userpassword: Password
        :param o_krbprincipalname: Principal alias
        :type  o_krbprincipalname: Principal
        :param o_carlicense: Car License
        :type  o_carlicense: str
        :param o_l: City
        :type  o_l: str
        :param o_userclass: User category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_cn: Full name
        :type  o_cn: str
        :param o_departmentnumber: Department Number
        :type  o_departmentnumber: str
        :param o_displayname: Display name
        :type  o_displayname: str
        :param o_mail: Email address
        :type  o_mail: str
        :param o_employeenumber: Employee Number
        :type  o_employeenumber: str
        :param o_employeetype: Employee Type
        :type  o_employeetype: str
        :param o_facsimiletelephonenumber: Fax Number
        :type  o_facsimiletelephonenumber: str
        :param o_givenname: First name
        :type  o_givenname: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_initials: Initials
        :type  o_initials: str
        :param o_sn: Last name
        :type  o_sn: str
        :param o_manager: Manager
        :type  o_manager: str
        :param o_mobile: Mobile Telephone Number
        :type  o_mobile: str
        :param o_ou: Org. Unit
        :type  o_ou: str
        :param o_pager: Pager Number
        :type  o_pager: str
        :param o_telephonenumber: Telephone Number
        :type  o_telephonenumber: str
        :param o_postalcode: ZIP
        :type  o_postalcode: str
        :param o_preferredlanguage: Preferred Language
        :type  o_preferredlanguage: str
        :param o_ipatokenradiusconfiglink: RADIUS proxy configuration
        :type  o_ipatokenradiusconfiglink: str
        :param o_ipatokenradiususername: RADIUS proxy username
        :type  o_ipatokenradiususername: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        :param o_ipasshpubkey: SSH public key
        :type  o_ipasshpubkey: str
        :param o_st: State/Province
        :type  o_st: str
        :param o_street: Street address
        :type  o_street: str
        :param o_title: Job Title
        :type  o_title: str
        :param o_ipauserauthtype: Types of supported user authentication
        :type  o_ipauserauthtype: str, valid values ['password', 'radius', 'otp']
        """
        method = 'stageuser_mod'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_random:
            _params['random'] = o_random
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbpasswordexpiration:
            _params['krbpasswordexpiration'] = o_krbpasswordexpiration
        if o_krbprincipalexpiration:
            _params['krbprincipalexpiration'] = o_krbprincipalexpiration
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        if o_carlicense:
            _params['carlicense'] = o_carlicense
        if o_l:
            _params['l'] = o_l
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_cn:
            _params['cn'] = o_cn
        if o_departmentnumber:
            _params['departmentnumber'] = o_departmentnumber
        if o_displayname:
            _params['displayname'] = o_displayname
        if o_mail:
            _params['mail'] = o_mail
        if o_employeenumber:
            _params['employeenumber'] = o_employeenumber
        if o_employeetype:
            _params['employeetype'] = o_employeetype
        if o_facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = o_facsimiletelephonenumber
        if o_givenname:
            _params['givenname'] = o_givenname
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        if o_initials:
            _params['initials'] = o_initials
        if o_sn:
            _params['sn'] = o_sn
        if o_manager:
            _params['manager'] = o_manager
        if o_mobile:
            _params['mobile'] = o_mobile
        if o_ou:
            _params['ou'] = o_ou
        if o_pager:
            _params['pager'] = o_pager
        if o_telephonenumber:
            _params['telephonenumber'] = o_telephonenumber
        if o_postalcode:
            _params['postalcode'] = o_postalcode
        if o_preferredlanguage:
            _params['preferredlanguage'] = o_preferredlanguage
        if o_ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = o_ipatokenradiusconfiglink
        if o_ipatokenradiususername:
            _params['ipatokenradiususername'] = o_ipatokenradiususername
        if o_loginshell:
            _params['loginshell'] = o_loginshell
        if o_ipasshpubkey:
            _params['ipasshpubkey'] = o_ipasshpubkey
        if o_st:
            _params['st'] = o_st
        if o_street:
            _params['street'] = o_street
        if o_title:
            _params['title'] = o_title
        if o_ipauserauthtype:
            _params['ipauserauthtype'] = o_ipauserauthtype

        return self._request(method, _args, _params)

    def stageuser_remove_cert(
            self,
            a_uid,
            o_usercertificate,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove one or more certificates to the stageuser entry
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        """
        method = 'stageuser_remove_cert'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def stageuser_remove_certmapdata(
            self,
            a_uid,
            a_ipacertmapdata=None,
            o_certificate=None,
            o_issuer=None,
            o_subject=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove one or more certificate mappings from the stage user entry.
        :param a_ipacertmapdata: Certificate mapping data
        :type  a_ipacertmapdata: str
        :param a_uid: User login
        :type  a_uid: str
        :param o_certificate: Base-64 encoded user certificate
        :type  o_certificate: Certificate
        :param o_issuer: Issuer of the certificate
        :type  o_issuer: DNParam
        :param o_subject: Subject of the certificate
        :type  o_subject: DNParam
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'stageuser_remove_certmapdata'

        _args = list()
        _args.append(a_ipacertmapdata)
        _args.append(a_uid)

        _params = dict()
        if o_certificate:
            _params['certificate'] = o_certificate
        if o_issuer:
            _params['issuer'] = o_issuer
        if o_subject:
            _params['subject'] = o_subject
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def stageuser_remove_manager(
            self,
            a_uid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_user=None,
    ):
        """Remove a manager to the stage user entry
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'stageuser_remove_manager'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def stageuser_remove_principal(
            self,
            a_uid,
            a_krbprincipalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove principal alias from the stageuser entry
        :param a_uid: User login
        :type  a_uid: str
        :param a_krbprincipalname: Principal alias
        :type  a_krbprincipalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'stageuser_remove_principal'

        _args = list()
        _args.append(a_uid)
        _args.append(a_krbprincipalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def stageuser_show(
            self,
            a_uid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a stage user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'stageuser_show'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def sudocmd_add(
            self,
            a_sudocmd,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_description=None,
    ):
        """Create new Sudo Command.
        :param a_sudocmd: Sudo Command
        :type  a_sudocmd: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: A description of this command
        :type  o_description: str
        """
        method = 'sudocmd_add'

        _args = list()
        _args.append(a_sudocmd)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def sudocmd_del(
            self,
            a_sudocmd,
            o_continue=False,
    ):
        """Delete Sudo Command.
        :param a_sudocmd: Sudo Command
        :type  a_sudocmd: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'sudocmd_del'

        _args = list()
        _args.append(a_sudocmd)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def sudocmd_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_sudocmd=None,
            o_description=None,
    ):
        """Search for Sudo Commands.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("command")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_sudocmd: Sudo Command
        :type  o_sudocmd: str
        :param o_description: A description of this command
        :type  o_description: str
        """
        method = 'sudocmd_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_sudocmd:
            _params['sudocmd'] = o_sudocmd
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def sudocmd_mod(
            self,
            a_sudocmd,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify Sudo Command.
        :param a_sudocmd: Sudo Command
        :type  a_sudocmd: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: A description of this command
        :type  o_description: str
        """
        method = 'sudocmd_mod'

        _args = list()
        _args.append(a_sudocmd)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def sudocmd_show(
            self,
            a_sudocmd,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display Sudo Command.
        :param a_sudocmd: Sudo Command
        :type  a_sudocmd: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'sudocmd_show'

        _args = list()
        _args.append(a_sudocmd)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def sudocmdgroup_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_description=None,
    ):
        """Create new Sudo Command Group.
        :param a_cn: Sudo Command Group
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Group description
        :type  o_description: str
        """
        method = 'sudocmdgroup_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def sudocmdgroup_add_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_sudocmd=None,
    ):
        """Add members to Sudo Command Group.
        :param a_cn: Sudo Command Group
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_sudocmd: sudo commands to add
        :type  o_sudocmd: str
        """
        method = 'sudocmdgroup_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_sudocmd:
            _params['sudocmd'] = o_sudocmd

        return self._request(method, _args, _params)

    def sudocmdgroup_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete Sudo Command Group.
        :param a_cn: Sudo Command Group
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'sudocmdgroup_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def sudocmdgroup_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_description=None,
            o_cn=None,
    ):
        """Search for Sudo Command Groups.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("sudocmdgroup-name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_description: Group description
        :type  o_description: str
        :param o_cn: Sudo Command Group
        :type  o_cn: str
        """
        method = 'sudocmdgroup_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def sudocmdgroup_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_description=None,
    ):
        """Modify Sudo Command Group.
        :param a_cn: Sudo Command Group
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_description: Group description
        :type  o_description: str
        """
        method = 'sudocmdgroup_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_description:
            _params['description'] = o_description

        return self._request(method, _args, _params)

    def sudocmdgroup_remove_member(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_sudocmd=None,
    ):
        """Remove members from Sudo Command Group.
        :param a_cn: Sudo Command Group
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_sudocmd: sudo commands to remove
        :type  o_sudocmd: str
        """
        method = 'sudocmdgroup_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_sudocmd:
            _params['sudocmd'] = o_sudocmd

        return self._request(method, _args, _params)

    def sudocmdgroup_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display Sudo Command Group.
        :param a_cn: Sudo Command Group
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'sudocmdgroup_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def sudorule_add(
            self,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_ipaenabledflag=None,
            o_sudoorder=0,
            o_description=None,
            o_externalhost=None,
            o_externaluser=None,
            o_ipasudorunasextgroup=None,
            o_ipasudorunasextuser=None,
            o_cmdcategory=None,
            o_hostcategory=None,
            o_ipasudorunasgroupcategory=None,
            o_ipasudorunasusercategory=None,
            o_usercategory=None,
    ):
        """Create new Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_sudoorder: integer to order the Sudo rules
        :type  o_sudoorder: int, min value 0, max value 2147483647
        :param o_description: Description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_externaluser: External User the rule applies to (sudorule-find only)
        :type  o_externaluser: str
        :param o_ipasudorunasextgroup: External Group the commands can run as (sudorule-find only)
        :type  o_ipasudorunasextgroup: str
        :param o_ipasudorunasextuser: External User the commands can run as (sudorule-find only)
        :type  o_ipasudorunasextuser: str
        :param o_cmdcategory: Command category the rule applies to
        :type  o_cmdcategory: str, valid values ['all']
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_ipasudorunasgroupcategory: RunAs Group category the rule applies to
        :type  o_ipasudorunasgroupcategory: str, valid values ['all']
        :param o_ipasudorunasusercategory: RunAs User category the rule applies to
        :type  o_ipasudorunasusercategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'sudorule_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_sudoorder:
            _params['sudoorder'] = o_sudoorder
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_externaluser:
            _params['externaluser'] = o_externaluser
        if o_ipasudorunasextgroup:
            _params['ipasudorunasextgroup'] = o_ipasudorunasextgroup
        if o_ipasudorunasextuser:
            _params['ipasudorunasextuser'] = o_ipasudorunasextuser
        if o_cmdcategory:
            _params['cmdcategory'] = o_cmdcategory
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_ipasudorunasgroupcategory:
            _params['ipasudorunasgroupcategory'] = o_ipasudorunasgroupcategory
        if o_ipasudorunasusercategory:
            _params['ipasudorunasusercategory'] = o_ipasudorunasusercategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def sudorule_add_allow_command(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_sudocmdgroup=None,
            o_sudocmd=None,
    ):
        """Add commands and sudo command groups affected by Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_sudocmdgroup: sudo command groups to add
        :type  o_sudocmdgroup: str
        :param o_sudocmd: sudo commands to add
        :type  o_sudocmd: str
        """
        method = 'sudorule_add_allow_command'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_sudocmdgroup:
            _params['sudocmdgroup'] = o_sudocmdgroup
        if o_sudocmd:
            _params['sudocmd'] = o_sudocmd

        return self._request(method, _args, _params)

    def sudorule_add_deny_command(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_sudocmdgroup=None,
            o_sudocmd=None,
    ):
        """Add commands and sudo command groups affected by Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_sudocmdgroup: sudo command groups to add
        :type  o_sudocmdgroup: str
        :param o_sudocmd: sudo commands to add
        :type  o_sudocmd: str
        """
        method = 'sudorule_add_deny_command'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_sudocmdgroup:
            _params['sudocmdgroup'] = o_sudocmdgroup
        if o_sudocmd:
            _params['sudocmd'] = o_sudocmd

        return self._request(method, _args, _params)

    def sudorule_add_host(
            self,
            a_cn,
            o_hostmask=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Add hosts and hostgroups affected by Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_hostmask: host masks of allowed hosts
        :type  o_hostmask: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to add
        :type  o_hostgroup: str
        :param o_host: hosts to add
        :type  o_host: str
        """
        method = 'sudorule_add_host'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_hostmask:
            _params['hostmask'] = o_hostmask
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def sudorule_add_option(
            self,
            a_cn,
            o_ipasudoopt,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add an option to the Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_ipasudoopt: Sudo Option
        :type  o_ipasudoopt: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'sudorule_add_option'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['ipasudoopt'] = o_ipasudoopt
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def sudorule_add_runasgroup(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
    ):
        """Add group for Sudo to execute as.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        """
        method = 'sudorule_add_runasgroup'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group

        return self._request(method, _args, _params)

    def sudorule_add_runasuser(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Add users and groups for Sudo to execute as.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'sudorule_add_runasuser'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def sudorule_add_user(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Add users and groups affected by Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'sudorule_add_user'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def sudorule_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'sudorule_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def sudorule_disable(
            self,
            a_cn,
    ):
        """Disable a Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        """
        method = 'sudorule_disable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def sudorule_enable(
            self,
            a_cn,
    ):
        """Enable a Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        """
        method = 'sudorule_enable'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def sudorule_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipaenabledflag=None,
            o_sudoorder=0,
            o_description=None,
            o_externalhost=None,
            o_externaluser=None,
            o_ipasudorunasextgroup=None,
            o_ipasudorunasextuser=None,
            o_cn=None,
            o_cmdcategory=None,
            o_hostcategory=None,
            o_ipasudorunasgroupcategory=None,
            o_ipasudorunasusercategory=None,
            o_usercategory=None,
    ):
        """Search for Sudo Rule.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("sudorule-name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_sudoorder: integer to order the Sudo rules
        :type  o_sudoorder: int, min value 0, max value 2147483647
        :param o_description: Description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_externaluser: External User the rule applies to (sudorule-find only)
        :type  o_externaluser: str
        :param o_ipasudorunasextgroup: External Group the commands can run as (sudorule-find only)
        :type  o_ipasudorunasextgroup: str
        :param o_ipasudorunasextuser: External User the commands can run as (sudorule-find only)
        :type  o_ipasudorunasextuser: str
        :param o_cn: Rule name
        :type  o_cn: str
        :param o_cmdcategory: Command category the rule applies to
        :type  o_cmdcategory: str, valid values ['all']
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_ipasudorunasgroupcategory: RunAs Group category the rule applies to
        :type  o_ipasudorunasgroupcategory: str, valid values ['all']
        :param o_ipasudorunasusercategory: RunAs User category the rule applies to
        :type  o_ipasudorunasusercategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'sudorule_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_sudoorder:
            _params['sudoorder'] = o_sudoorder
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_externaluser:
            _params['externaluser'] = o_externaluser
        if o_ipasudorunasextgroup:
            _params['ipasudorunasextgroup'] = o_ipasudorunasextgroup
        if o_ipasudorunasextuser:
            _params['ipasudorunasextuser'] = o_ipasudorunasextuser
        if o_cn:
            _params['cn'] = o_cn
        if o_cmdcategory:
            _params['cmdcategory'] = o_cmdcategory
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_ipasudorunasgroupcategory:
            _params['ipasudorunasgroupcategory'] = o_ipasudorunasgroupcategory
        if o_ipasudorunasusercategory:
            _params['ipasudorunasusercategory'] = o_ipasudorunasusercategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def sudorule_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_ipaenabledflag=None,
            o_sudoorder=0,
            o_description=None,
            o_externalhost=None,
            o_externaluser=None,
            o_ipasudorunasextgroup=None,
            o_ipasudorunasextuser=None,
            o_cmdcategory=None,
            o_hostcategory=None,
            o_ipasudorunasgroupcategory=None,
            o_ipasudorunasusercategory=None,
            o_usercategory=None,
    ):
        """Modify Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the sudo rule object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipaenabledflag: Enabled
        :type  o_ipaenabledflag: Bool
        :param o_sudoorder: integer to order the Sudo rules
        :type  o_sudoorder: int, min value 0, max value 2147483647
        :param o_description: Description
        :type  o_description: str
        :param o_externalhost: External host
        :type  o_externalhost: str
        :param o_externaluser: External User the rule applies to (sudorule-find only)
        :type  o_externaluser: str
        :param o_ipasudorunasextgroup: External Group the commands can run as (sudorule-find only)
        :type  o_ipasudorunasextgroup: str
        :param o_ipasudorunasextuser: External User the commands can run as (sudorule-find only)
        :type  o_ipasudorunasextuser: str
        :param o_cmdcategory: Command category the rule applies to
        :type  o_cmdcategory: str, valid values ['all']
        :param o_hostcategory: Host category the rule applies to
        :type  o_hostcategory: str, valid values ['all']
        :param o_ipasudorunasgroupcategory: RunAs Group category the rule applies to
        :type  o_ipasudorunasgroupcategory: str, valid values ['all']
        :param o_ipasudorunasusercategory: RunAs User category the rule applies to
        :type  o_ipasudorunasusercategory: str, valid values ['all']
        :param o_usercategory: User category the rule applies to
        :type  o_usercategory: str, valid values ['all']
        """
        method = 'sudorule_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipaenabledflag:
            _params['ipaenabledflag'] = o_ipaenabledflag
        if o_sudoorder:
            _params['sudoorder'] = o_sudoorder
        if o_description:
            _params['description'] = o_description
        if o_externalhost:
            _params['externalhost'] = o_externalhost
        if o_externaluser:
            _params['externaluser'] = o_externaluser
        if o_ipasudorunasextgroup:
            _params['ipasudorunasextgroup'] = o_ipasudorunasextgroup
        if o_ipasudorunasextuser:
            _params['ipasudorunasextuser'] = o_ipasudorunasextuser
        if o_cmdcategory:
            _params['cmdcategory'] = o_cmdcategory
        if o_hostcategory:
            _params['hostcategory'] = o_hostcategory
        if o_ipasudorunasgroupcategory:
            _params['ipasudorunasgroupcategory'] = o_ipasudorunasgroupcategory
        if o_ipasudorunasusercategory:
            _params['ipasudorunasusercategory'] = o_ipasudorunasusercategory
        if o_usercategory:
            _params['usercategory'] = o_usercategory

        return self._request(method, _args, _params)

    def sudorule_remove_allow_command(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_sudocmdgroup=None,
            o_sudocmd=None,
    ):
        """Remove commands and sudo command groups affected by Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_sudocmdgroup: sudo command groups to remove
        :type  o_sudocmdgroup: str
        :param o_sudocmd: sudo commands to remove
        :type  o_sudocmd: str
        """
        method = 'sudorule_remove_allow_command'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_sudocmdgroup:
            _params['sudocmdgroup'] = o_sudocmdgroup
        if o_sudocmd:
            _params['sudocmd'] = o_sudocmd

        return self._request(method, _args, _params)

    def sudorule_remove_deny_command(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_sudocmdgroup=None,
            o_sudocmd=None,
    ):
        """Remove commands and sudo command groups affected by Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_sudocmdgroup: sudo command groups to remove
        :type  o_sudocmdgroup: str
        :param o_sudocmd: sudo commands to remove
        :type  o_sudocmd: str
        """
        method = 'sudorule_remove_deny_command'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_sudocmdgroup:
            _params['sudocmdgroup'] = o_sudocmdgroup
        if o_sudocmd:
            _params['sudocmd'] = o_sudocmd

        return self._request(method, _args, _params)

    def sudorule_remove_host(
            self,
            a_cn,
            o_hostmask=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_hostgroup=None,
            o_host=None,
    ):
        """Remove hosts and hostgroups affected by Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_hostmask: host masks of allowed hosts
        :type  o_hostmask: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_hostgroup: host groups to remove
        :type  o_hostgroup: str
        :param o_host: hosts to remove
        :type  o_host: str
        """
        method = 'sudorule_remove_host'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_hostmask:
            _params['hostmask'] = o_hostmask
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_hostgroup:
            _params['hostgroup'] = o_hostgroup
        if o_host:
            _params['host'] = o_host

        return self._request(method, _args, _params)

    def sudorule_remove_option(
            self,
            a_cn,
            o_ipasudoopt,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove an option from Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_ipasudoopt: Sudo Option
        :type  o_ipasudoopt: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'sudorule_remove_option'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['ipasudoopt'] = o_ipasudoopt
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def sudorule_remove_runasgroup(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
    ):
        """Remove group for Sudo to execute as.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        """
        method = 'sudorule_remove_runasgroup'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group

        return self._request(method, _args, _params)

    def sudorule_remove_runasuser(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Remove users and groups for Sudo to execute as.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'sudorule_remove_runasuser'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def sudorule_remove_user(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_group=None,
            o_user=None,
    ):
        """Remove users and groups affected by Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'sudorule_remove_user'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_group:
            _params['group'] = o_group
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def sudorule_show(
            self,
            a_cn,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display Sudo Rule.
        :param a_cn: Rule name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'sudorule_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def topic_find(
            self,
            a_criteria=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
    ):
        """Search for help topics.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'topic_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def topic_show(
            self,
            a_full_name,
            o_all=True,
            o_raw=False,
    ):
        """Display information about a help topic.
        :param a_full_name: Full name
        :type  a_full_name: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'topic_show'

        _args = list()
        _args.append(a_full_name)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def topologysegment_add(
            self,
            a_topologysuffixcn,
            a_cn,
            o_iparepltoposegmentleftnode,
            o_iparepltoposegmentrightnode,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_nsds5replicatimeout=None,
            o_nsds5replicatedattributelist=None,
            o_nsds5replicatedattributelisttotal=None,
            o_nsds5replicastripattrs=None,
            o_nsds5replicaenabled=None,
            o_iparepltoposegmentdirection='both',
    ):
        """Add a new segment.
        :param a_topologysuffixcn: Suffix name
        :type  a_topologysuffixcn: str
        :param a_cn: Arbitrary string identifying the segment
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_nsds5replicatimeout: Number of seconds outbound LDAP operations waits for a response from the remote replica before timing out and failing
        :type  o_nsds5replicatimeout: int, min value 0, max value 2147483647
        :param o_iparepltoposegmentleftnode: Left replication node - an IPA server
        :type  o_iparepltoposegmentleftnode: str
        :param o_nsds5replicatedattributelist: Attributes that are not replicated to a consumer server during a fractional update. E.g., `(objectclass=*) $ EXCLUDE accountlockout memberof
        :type  o_nsds5replicatedattributelist: str
        :param o_nsds5replicatedattributelisttotal: Attributes that are not replicated to a consumer server during a total update. E.g. (objectclass=*) $ EXCLUDE accountlockout
        :type  o_nsds5replicatedattributelisttotal: str
        :param o_iparepltoposegmentrightnode: Right replication node - an IPA server
        :type  o_iparepltoposegmentrightnode: str
        :param o_nsds5replicastripattrs: A space separated list of attributes which are removed from replication updates.
        :type  o_nsds5replicastripattrs: str
        :param o_nsds5replicaenabled: Whether a replication agreement is active, meaning whether replication is occurring per that agreement
        :type  o_nsds5replicaenabled: str, valid values ['on', 'off']
        :param o_iparepltoposegmentdirection: Direction of replication between left and right replication node
        :type  o_iparepltoposegmentdirection: str, valid values ['both', 'left-right', 'right-left']
        """
        method = 'topologysegment_add'

        _args = list()
        _args.append(a_topologysuffixcn)
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_nsds5replicatimeout:
            _params['nsds5replicatimeout'] = o_nsds5replicatimeout
        _params['iparepltoposegmentleftnode'] = o_iparepltoposegmentleftnode
        if o_nsds5replicatedattributelist:
            _params['nsds5replicatedattributelist'] = o_nsds5replicatedattributelist
        if o_nsds5replicatedattributelisttotal:
            _params['nsds5replicatedattributelisttotal'] = o_nsds5replicatedattributelisttotal
        _params['iparepltoposegmentrightnode'] = o_iparepltoposegmentrightnode
        if o_nsds5replicastripattrs:
            _params['nsds5replicastripattrs'] = o_nsds5replicastripattrs
        if o_nsds5replicaenabled:
            _params['nsds5replicaenabled'] = o_nsds5replicaenabled
        _params['iparepltoposegmentdirection'] = o_iparepltoposegmentdirection

        return self._request(method, _args, _params)

    def topologysegment_del(
            self,
            a_topologysuffixcn,
            a_cn,
            o_continue=False,
    ):
        """Delete a segment.
        :param a_topologysuffixcn: Suffix name
        :type  a_topologysuffixcn: str
        :param a_cn: Arbitrary string identifying the segment
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'topologysegment_del'

        _args = list()
        _args.append(a_topologysuffixcn)
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def topologysegment_find(
            self,
            a_topologysuffixcn,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_nsds5replicatimeout=None,
            o_iparepltoposegmentleftnode=None,
            o_cn=None,
            o_nsds5replicatedattributelist=None,
            o_nsds5replicatedattributelisttotal=None,
            o_iparepltoposegmentrightnode=None,
            o_nsds5replicastripattrs=None,
            o_iparepltoposegmentdirection='both',
            o_nsds5replicaenabled=None,
    ):
        """Search for topology segments.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param a_topologysuffixcn: Suffix name
        :type  a_topologysuffixcn: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_nsds5replicatimeout: Number of seconds outbound LDAP operations waits for a response from the remote replica before timing out and failing
        :type  o_nsds5replicatimeout: int, min value 0, max value 2147483647
        :param o_iparepltoposegmentleftnode: Left replication node - an IPA server
        :type  o_iparepltoposegmentleftnode: str
        :param o_cn: Arbitrary string identifying the segment
        :type  o_cn: str
        :param o_nsds5replicatedattributelist: Attributes that are not replicated to a consumer server during a fractional update. E.g., `(objectclass=*) $ EXCLUDE accountlockout memberof
        :type  o_nsds5replicatedattributelist: str
        :param o_nsds5replicatedattributelisttotal: Attributes that are not replicated to a consumer server during a total update. E.g. (objectclass=*) $ EXCLUDE accountlockout
        :type  o_nsds5replicatedattributelisttotal: str
        :param o_iparepltoposegmentrightnode: Right replication node - an IPA server
        :type  o_iparepltoposegmentrightnode: str
        :param o_nsds5replicastripattrs: A space separated list of attributes which are removed from replication updates.
        :type  o_nsds5replicastripattrs: str
        :param o_iparepltoposegmentdirection: Direction of replication between left and right replication node
        :type  o_iparepltoposegmentdirection: str, valid values ['both', 'left-right', 'right-left']
        :param o_nsds5replicaenabled: Whether a replication agreement is active, meaning whether replication is occurring per that agreement
        :type  o_nsds5replicaenabled: str, valid values ['on', 'off']
        """
        method = 'topologysegment_find'

        _args = list()
        _args.append(a_criteria)
        _args.append(a_topologysuffixcn)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_nsds5replicatimeout:
            _params['nsds5replicatimeout'] = o_nsds5replicatimeout
        if o_iparepltoposegmentleftnode:
            _params['iparepltoposegmentleftnode'] = o_iparepltoposegmentleftnode
        if o_cn:
            _params['cn'] = o_cn
        if o_nsds5replicatedattributelist:
            _params['nsds5replicatedattributelist'] = o_nsds5replicatedattributelist
        if o_nsds5replicatedattributelisttotal:
            _params['nsds5replicatedattributelisttotal'] = o_nsds5replicatedattributelisttotal
        if o_iparepltoposegmentrightnode:
            _params['iparepltoposegmentrightnode'] = o_iparepltoposegmentrightnode
        if o_nsds5replicastripattrs:
            _params['nsds5replicastripattrs'] = o_nsds5replicastripattrs
        if o_iparepltoposegmentdirection:
            _params['iparepltoposegmentdirection'] = o_iparepltoposegmentdirection
        if o_nsds5replicaenabled:
            _params['nsds5replicaenabled'] = o_nsds5replicaenabled

        return self._request(method, _args, _params)

    def topologysegment_mod(
            self,
            a_topologysuffixcn,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_nsds5replicatimeout=None,
            o_nsds5replicatedattributelist=None,
            o_nsds5replicatedattributelisttotal=None,
            o_nsds5replicastripattrs=None,
            o_nsds5replicaenabled=None,
    ):
        """Modify a segment.
        :param a_topologysuffixcn: Suffix name
        :type  a_topologysuffixcn: str
        :param a_cn: Arbitrary string identifying the segment
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_nsds5replicatimeout: Number of seconds outbound LDAP operations waits for a response from the remote replica before timing out and failing
        :type  o_nsds5replicatimeout: int, min value 0, max value 2147483647
        :param o_nsds5replicatedattributelist: Attributes that are not replicated to a consumer server during a fractional update. E.g., `(objectclass=*) $ EXCLUDE accountlockout memberof
        :type  o_nsds5replicatedattributelist: str
        :param o_nsds5replicatedattributelisttotal: Attributes that are not replicated to a consumer server during a total update. E.g. (objectclass=*) $ EXCLUDE accountlockout
        :type  o_nsds5replicatedattributelisttotal: str
        :param o_nsds5replicastripattrs: A space separated list of attributes which are removed from replication updates.
        :type  o_nsds5replicastripattrs: str
        :param o_nsds5replicaenabled: Whether a replication agreement is active, meaning whether replication is occurring per that agreement
        :type  o_nsds5replicaenabled: str, valid values ['on', 'off']
        """
        method = 'topologysegment_mod'

        _args = list()
        _args.append(a_topologysuffixcn)
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_nsds5replicatimeout:
            _params['nsds5replicatimeout'] = o_nsds5replicatimeout
        if o_nsds5replicatedattributelist:
            _params['nsds5replicatedattributelist'] = o_nsds5replicatedattributelist
        if o_nsds5replicatedattributelisttotal:
            _params['nsds5replicatedattributelisttotal'] = o_nsds5replicatedattributelisttotal
        if o_nsds5replicastripattrs:
            _params['nsds5replicastripattrs'] = o_nsds5replicastripattrs
        if o_nsds5replicaenabled:
            _params['nsds5replicaenabled'] = o_nsds5replicaenabled

        return self._request(method, _args, _params)

    def topologysegment_reinitialize(
            self,
            a_topologysuffixcn,
            a_cn,
            o_left=False,
            o_right=False,
            o_stop=False,
    ):
        """Request a full re-initialization of the node retrieving data from the other node.
        :param a_topologysuffixcn: Suffix name
        :type  a_topologysuffixcn: str
        :param a_cn: Arbitrary string identifying the segment
        :type  a_cn: str
        :param o_left: Initialize left node
        :type  o_left: bool
        :param o_right: Initialize right node
        :type  o_right: bool
        :param o_stop: Stop already started refresh of chosen node(s)
        :type  o_stop: bool
        """
        method = 'topologysegment_reinitialize'

        _args = list()
        _args.append(a_topologysuffixcn)
        _args.append(a_cn)

        _params = dict()
        if o_left:
            _params['left'] = o_left
        if o_right:
            _params['right'] = o_right
        if o_stop:
            _params['stop'] = o_stop

        return self._request(method, _args, _params)

    def topologysegment_show(
            self,
            a_topologysuffixcn,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display a segment.
        :param a_topologysuffixcn: Suffix name
        :type  a_topologysuffixcn: str
        :param a_cn: Arbitrary string identifying the segment
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'topologysegment_show'

        _args = list()
        _args.append(a_topologysuffixcn)
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def topologysuffix_add(
            self,
            a_cn,
            o_iparepltopoconfroot,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
    ):
        """Add a new topology suffix to be managed.
        :param a_cn: Suffix name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_iparepltopoconfroot: Managed LDAP suffix DN
        :type  o_iparepltopoconfroot: DNParam
        """
        method = 'topologysuffix_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['iparepltopoconfroot'] = o_iparepltopoconfroot

        return self._request(method, _args, _params)

    def topologysuffix_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a topology suffix.
        :param a_cn: Suffix name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'topologysuffix_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def topologysuffix_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_iparepltopoconfroot=None,
            o_cn=None,
    ):
        """Search for topology suffixes.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_iparepltopoconfroot: Managed LDAP suffix DN
        :type  o_iparepltopoconfroot: DNParam
        :param o_cn: Suffix name
        :type  o_cn: str
        """
        method = 'topologysuffix_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_iparepltopoconfroot:
            _params['iparepltopoconfroot'] = o_iparepltopoconfroot
        if o_cn:
            _params['cn'] = o_cn

        return self._request(method, _args, _params)

    def topologysuffix_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_iparepltopoconfroot=None,
    ):
        """Modify a topology suffix.
        :param a_cn: Suffix name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_iparepltopoconfroot: Managed LDAP suffix DN
        :type  o_iparepltopoconfroot: DNParam
        """
        method = 'topologysuffix_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_iparepltopoconfroot:
            _params['iparepltopoconfroot'] = o_iparepltopoconfroot

        return self._request(method, _args, _params)

    def topologysuffix_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Show managed suffix.
        :param a_cn: Suffix name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'topologysuffix_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def topologysuffix_verify(
            self,
            a_cn,
    ):
        """
Verify replication topology for suffix.

Checks done:
  1. check if a topology is not disconnected. In other words if there are
     replication paths between all servers.
  2. check if servers don't have more than the recommended number of
     replication agreements
        :param a_cn: Suffix name
        :type  a_cn: str
        """
        method = 'topologysuffix_verify'

        _args = list()
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def trust_add(
            self,
            a_cn,
            o_external=False,
            o_bidirectional=False,
            o_base_id=None,
            o_range_size=None,
            o_realm_passwd=None,
            o_trust_secret=None,
            o_addattr=None,
            o_realm_admin=None,
            o_realm_server=None,
            o_setattr=None,
            o_range_type=None,
            o_all=True,
            o_raw=False,
            o_trust_type='ad',
    ):
        """
Add new trust to use.

This command establishes trust relationship to another domain
which becomes 'trusted'. As result, users of the trusted domain
may access resources of this domain.

Only trusts to Active Directory domains are supported right now.

The command can be safely run multiple times against the same domain,
this will cause change to trust relationship credentials on both
sides.

Note that if the command was previously run with a specific range type,
or with automatic detection of the range type, and you want to configure a
different range type, you may need to delete first the ID range using
ipa idrange-del before retrying the command with the desired range type.
        :param a_cn: Realm name
        :type  a_cn: str
        :param o_external: Establish external trust to a domain in another forest. The trust is not transitive beyond the domain.
        :type  o_external: Bool
        :param o_bidirectional: Establish bi-directional trust. By default trust is inbound one-way only.
        :type  o_bidirectional: Bool
        :param o_base_id: First Posix ID of the range reserved for the trusted domain
        :type  o_base_id: int, min value -2147483648, max value 2147483647
        :param o_range_size: Size of the ID range reserved for the trusted domain
        :type  o_range_size: int, min value -2147483648, max value 2147483647
        :param o_realm_passwd: Active Directory domain administrator's password
        :type  o_realm_passwd: Password
        :param o_trust_secret: Shared secret for the trust
        :type  o_trust_secret: Password
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_realm_admin: Active Directory domain administrator
        :type  o_realm_admin: str
        :param o_realm_server: Domain controller for the Active Directory domain (optional)
        :type  o_realm_server: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_range_type: Type of trusted domain ID range, one of ipa-ad-trust, ipa-ad-trust-posix
        :type  o_range_type: str, valid values ['ipa-ad-trust', 'ipa-ad-trust-posix']
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_trust_type: Trust type (ad for Active Directory, default)
        :type  o_trust_type: str, valid values ['ad']
        """
        method = 'trust_add'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_external:
            _params['external'] = o_external
        if o_bidirectional:
            _params['bidirectional'] = o_bidirectional
        if o_base_id:
            _params['base_id'] = o_base_id
        if o_range_size:
            _params['range_size'] = o_range_size
        if o_realm_passwd:
            _params['realm_passwd'] = o_realm_passwd
        if o_trust_secret:
            _params['trust_secret'] = o_trust_secret
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_realm_admin:
            _params['realm_admin'] = o_realm_admin
        if o_realm_server:
            _params['realm_server'] = o_realm_server
        if o_setattr:
            _params['setattr'] = o_setattr
        if o_range_type:
            _params['range_type'] = o_range_type
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['trust_type'] = o_trust_type

        return self._request(method, _args, _params)

    def trust_del(
            self,
            a_cn,
            o_continue=False,
    ):
        """Delete a trust.
        :param a_cn: Realm name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'trust_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def trust_fetch_domains(
            self,
            a_cn,
            o_realm_passwd=None,
            o_realm_admin=None,
            o_realm_server=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Refresh list of the domains associated with the trust
        :param a_cn: Realm name
        :type  a_cn: str
        :param o_realm_passwd: Active Directory domain administrator's password
        :type  o_realm_passwd: Password
        :param o_realm_admin: Active Directory domain administrator
        :type  o_realm_admin: str
        :param o_realm_server: Domain controller for the Active Directory domain (optional)
        :type  o_realm_server: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'trust_fetch_domains'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_realm_passwd:
            _params['realm_passwd'] = o_realm_passwd
        if o_realm_admin:
            _params['realm_admin'] = o_realm_admin
        if o_realm_server:
            _params['realm_server'] = o_realm_server
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def trust_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_ipantflatname=None,
            o_cn=None,
            o_ipanttrusteddomainsid=None,
            o_ipantsidblacklistincoming=None,
            o_ipantsidblacklistoutgoing=None,
    ):
        """Search for trusts.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("realm")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_ipantflatname: Domain NetBIOS name
        :type  o_ipantflatname: str
        :param o_cn: Realm name
        :type  o_cn: str
        :param o_ipanttrusteddomainsid: Domain Security Identifier
        :type  o_ipanttrusteddomainsid: str
        :param o_ipantsidblacklistincoming: SID blacklist incoming
        :type  o_ipantsidblacklistincoming: str
        :param o_ipantsidblacklistoutgoing: SID blacklist outgoing
        :type  o_ipantsidblacklistoutgoing: str
        """
        method = 'trust_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_ipantflatname:
            _params['ipantflatname'] = o_ipantflatname
        if o_cn:
            _params['cn'] = o_cn
        if o_ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = o_ipanttrusteddomainsid
        if o_ipantsidblacklistincoming:
            _params['ipantsidblacklistincoming'] = o_ipantsidblacklistincoming
        if o_ipantsidblacklistoutgoing:
            _params['ipantsidblacklistoutgoing'] = o_ipantsidblacklistoutgoing

        return self._request(method, _args, _params)

    def trust_mod(
            self,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_ipantsidblacklistincoming=None,
            o_ipantsidblacklistoutgoing=None,
            o_ipantadditionalsuffixes=None,
    ):
        """
    Modify a trust (for future use).

    Currently only the default option to modify the LDAP attributes is
    available. More specific options will be added in coming releases.
        :param a_cn: Realm name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_ipantsidblacklistincoming: SID blacklist incoming
        :type  o_ipantsidblacklistincoming: str
        :param o_ipantsidblacklistoutgoing: SID blacklist outgoing
        :type  o_ipantsidblacklistoutgoing: str
        :param o_ipantadditionalsuffixes: UPN suffixes
        :type  o_ipantadditionalsuffixes: str
        """
        method = 'trust_mod'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_ipantsidblacklistincoming:
            _params['ipantsidblacklistincoming'] = o_ipantsidblacklistincoming
        if o_ipantsidblacklistoutgoing:
            _params['ipantsidblacklistoutgoing'] = o_ipantsidblacklistoutgoing
        if o_ipantadditionalsuffixes:
            _params['ipantadditionalsuffixes'] = o_ipantadditionalsuffixes

        return self._request(method, _args, _params)

    def trust_resolve(
            self,
            o_sids,
            o_all=True,
            o_raw=False,
    ):
        """Resolve security identifiers of users and groups in trusted domains
        :param o_sids: Security Identifiers (SIDs)
        :type  o_sids: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'trust_resolve'

        _args = list()

        _params = dict()
        _params['sids'] = o_sids
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def trust_show(
            self,
            a_cn,
            o_all=True,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a trust.
        :param a_cn: Realm name
        :type  a_cn: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'trust_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def trustconfig_mod(
            self,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_trust_type='ad',
            o_ipantfallbackprimarygroup=None,
    ):
        """Modify global trust configuration.
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_trust_type: Trust type (ad for Active Directory, default)
        :type  o_trust_type: str, valid values ['ad']
        :param o_ipantfallbackprimarygroup: Fallback primary group
        :type  o_ipantfallbackprimarygroup: str
        """
        method = 'trustconfig_mod'

        _args = list()

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        _params['trust_type'] = o_trust_type
        if o_ipantfallbackprimarygroup:
            _params['ipantfallbackprimarygroup'] = o_ipantfallbackprimarygroup

        return self._request(method, _args, _params)

    def trustconfig_show(
            self,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_trust_type='ad',
    ):
        """Show global trust configuration.
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_trust_type: Trust type (ad for Active Directory, default)
        :type  o_trust_type: str, valid values ['ad']
        """
        method = 'trustconfig_show'

        _args = list()

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        _params['trust_type'] = o_trust_type

        return self._request(method, _args, _params)

    def trustdomain_add(
            self,
            a_trustcn,
            a_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_trust_type='ad',
            o_ipantflatname=None,
            o_ipanttrusteddomainsid=None,
    ):
        """Allow access from the trusted domain
        :param a_trustcn: Realm name
        :type  a_trustcn: str
        :param a_cn: Domain name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_trust_type: Trust type (ad for Active Directory, default)
        :type  o_trust_type: str, valid values ['ad']
        :param o_ipantflatname: Domain NetBIOS name
        :type  o_ipantflatname: str
        :param o_ipanttrusteddomainsid: Domain Security Identifier
        :type  o_ipanttrusteddomainsid: str
        """
        method = 'trustdomain_add'

        _args = list()
        _args.append(a_trustcn)
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['trust_type'] = o_trust_type
        if o_ipantflatname:
            _params['ipantflatname'] = o_ipantflatname
        if o_ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = o_ipanttrusteddomainsid

        return self._request(method, _args, _params)

    def trustdomain_del(
            self,
            a_trustcn,
            a_cn,
            o_continue=False,
    ):
        """Remove information about the domain associated with the trust.
        :param a_trustcn: Realm name
        :type  a_trustcn: str
        :param a_cn: Domain name
        :type  a_cn: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'trustdomain_del'

        _args = list()
        _args.append(a_trustcn)
        _args.append(a_cn)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def trustdomain_disable(
            self,
            a_trustcn,
            a_cn,
    ):
        """Disable use of IPA resources by the domain of the trust
        :param a_trustcn: Realm name
        :type  a_trustcn: str
        :param a_cn: Domain name
        :type  a_cn: str
        """
        method = 'trustdomain_disable'

        _args = list()
        _args.append(a_trustcn)
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def trustdomain_enable(
            self,
            a_trustcn,
            a_cn,
    ):
        """Allow use of IPA resources by the domain of the trust
        :param a_trustcn: Realm name
        :type  a_trustcn: str
        :param a_cn: Domain name
        :type  a_cn: str
        """
        method = 'trustdomain_enable'

        _args = list()
        _args.append(a_trustcn)
        _args.append(a_cn)

        _params = dict()

        return self._request(method, _args, _params)

    def trustdomain_find(
            self,
            a_trustcn,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_all=True,
            o_pkey_only=False,
            o_raw=False,
            o_cn=None,
            o_ipantflatname=None,
            o_ipanttrusteddomainsid=None,
    ):
        """Search domains of the trust
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param a_trustcn: Realm name
        :type  a_trustcn: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_pkey_only: Results should contain primary key attribute only ("domain")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_cn: Domain name
        :type  o_cn: str
        :param o_ipantflatname: Domain NetBIOS name
        :type  o_ipantflatname: str
        :param o_ipanttrusteddomainsid: Domain Security Identifier
        :type  o_ipanttrusteddomainsid: str
        """
        method = 'trustdomain_find'

        _args = list()
        _args.append(a_criteria)
        _args.append(a_trustcn)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        _params['all'] = o_all
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_cn:
            _params['cn'] = o_cn
        if o_ipantflatname:
            _params['ipantflatname'] = o_ipantflatname
        if o_ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = o_ipanttrusteddomainsid

        return self._request(method, _args, _params)

    def trustdomain_mod(
            self,
            a_trustcn,
            a_cn,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_all=True,
            o_raw=False,
            o_rights=False,
            o_trust_type='ad',
            o_ipantflatname=None,
            o_ipanttrusteddomainsid=None,
    ):
        """Modify trustdomain of the trust
        :param a_trustcn: Realm name
        :type  a_trustcn: str
        :param a_cn: Domain name
        :type  a_cn: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_trust_type: Trust type (ad for Active Directory, default)
        :type  o_trust_type: str, valid values ['ad']
        :param o_ipantflatname: Domain NetBIOS name
        :type  o_ipantflatname: str
        :param o_ipanttrusteddomainsid: Domain Security Identifier
        :type  o_ipanttrusteddomainsid: str
        """
        method = 'trustdomain_mod'

        _args = list()
        _args.append(a_trustcn)
        _args.append(a_cn)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        _params['trust_type'] = o_trust_type
        if o_ipantflatname:
            _params['ipantflatname'] = o_ipantflatname
        if o_ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = o_ipanttrusteddomainsid

        return self._request(method, _args, _params)

    def user_add(
            self,
            a_uid,
            o_givenname,
            o_sn,
            o_cn,
            o_addattr=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_noprivate=False,
            o_random=False,
            o_raw=False,
            o_nsaccountlock=False,
            o_usercertificate=None,
            o_krbpasswordexpiration=None,
            o_krbprincipalexpiration=None,
            o_gidnumber=None,
            o_uidnumber=None,
            o_userpassword=None,
            o_carlicense=None,
            o_l=None,
            o_userclass=None,
            o_departmentnumber=None,
            o_mail=None,
            o_employeenumber=None,
            o_employeetype=None,
            o_facsimiletelephonenumber=None,
            o_homedirectory=None,
            o_manager=None,
            o_mobile=None,
            o_ou=None,
            o_pager=None,
            o_telephonenumber=None,
            o_postalcode=None,
            o_preferredlanguage=None,
            o_ipatokenradiusconfiglink=None,
            o_ipatokenradiususername=None,
            o_loginshell=None,
            o_ipasshpubkey=None,
            o_st=None,
            o_street=None,
            o_title=None,
            o_ipauserauthtype=None,
            o_krbprincipalname=None,
            o_displayname=None,
            o_gecos=None,
            o_initials=None,
    ):
        """Add a new user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_noprivate: Don't create user private group
        :type  o_noprivate: bool
        :param o_random: Generate a random user password
        :type  o_random: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_nsaccountlock: Account disabled
        :type  o_nsaccountlock: Bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        :param o_krbpasswordexpiration: User password expiration
        :type  o_krbpasswordexpiration: DateTime
        :param o_krbprincipalexpiration: Kerberos principal expiration
        :type  o_krbprincipalexpiration: DateTime
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number (system will assign one if not provided)
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_userpassword: Prompt to set the user password
        :type  o_userpassword: Password
        :param o_carlicense: Car License
        :type  o_carlicense: str
        :param o_l: City
        :type  o_l: str
        :param o_userclass: User category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_departmentnumber: Department Number
        :type  o_departmentnumber: str
        :param o_mail: Email address
        :type  o_mail: str
        :param o_employeenumber: Employee Number
        :type  o_employeenumber: str
        :param o_employeetype: Employee Type
        :type  o_employeetype: str
        :param o_facsimiletelephonenumber: Fax Number
        :type  o_facsimiletelephonenumber: str
        :param o_givenname: First name
        :type  o_givenname: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_sn: Last name
        :type  o_sn: str
        :param o_manager: Manager
        :type  o_manager: str
        :param o_mobile: Mobile Telephone Number
        :type  o_mobile: str
        :param o_ou: Org. Unit
        :type  o_ou: str
        :param o_pager: Pager Number
        :type  o_pager: str
        :param o_telephonenumber: Telephone Number
        :type  o_telephonenumber: str
        :param o_postalcode: ZIP
        :type  o_postalcode: str
        :param o_preferredlanguage: Preferred Language
        :type  o_preferredlanguage: str
        :param o_ipatokenradiusconfiglink: RADIUS proxy configuration
        :type  o_ipatokenradiusconfiglink: str
        :param o_ipatokenradiususername: RADIUS proxy username
        :type  o_ipatokenradiususername: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        :param o_ipasshpubkey: SSH public key
        :type  o_ipasshpubkey: str
        :param o_st: State/Province
        :type  o_st: str
        :param o_street: Street address
        :type  o_street: str
        :param o_title: Job Title
        :type  o_title: str
        :param o_ipauserauthtype: Types of supported user authentication
        :type  o_ipauserauthtype: str, valid values ['password', 'radius', 'otp']
        :param o_krbprincipalname: Principal alias
        :type  o_krbprincipalname: Principal
        :param o_cn: Full name
        :type  o_cn: str
        :param o_displayname: Display name
        :type  o_displayname: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_initials: Initials
        :type  o_initials: str
        """
        method = 'user_add'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['noprivate'] = o_noprivate
        if o_random:
            _params['random'] = o_random
        _params['raw'] = o_raw
        if o_nsaccountlock:
            _params['nsaccountlock'] = o_nsaccountlock
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbpasswordexpiration:
            _params['krbpasswordexpiration'] = o_krbpasswordexpiration
        if o_krbprincipalexpiration:
            _params['krbprincipalexpiration'] = o_krbprincipalexpiration
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_carlicense:
            _params['carlicense'] = o_carlicense
        if o_l:
            _params['l'] = o_l
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_departmentnumber:
            _params['departmentnumber'] = o_departmentnumber
        if o_mail:
            _params['mail'] = o_mail
        if o_employeenumber:
            _params['employeenumber'] = o_employeenumber
        if o_employeetype:
            _params['employeetype'] = o_employeetype
        if o_facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = o_facsimiletelephonenumber
        _params['givenname'] = o_givenname
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        _params['sn'] = o_sn
        if o_manager:
            _params['manager'] = o_manager
        if o_mobile:
            _params['mobile'] = o_mobile
        if o_ou:
            _params['ou'] = o_ou
        if o_pager:
            _params['pager'] = o_pager
        if o_telephonenumber:
            _params['telephonenumber'] = o_telephonenumber
        if o_postalcode:
            _params['postalcode'] = o_postalcode
        if o_preferredlanguage:
            _params['preferredlanguage'] = o_preferredlanguage
        if o_ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = o_ipatokenradiusconfiglink
        if o_ipatokenradiususername:
            _params['ipatokenradiususername'] = o_ipatokenradiususername
        if o_loginshell:
            _params['loginshell'] = o_loginshell
        if o_ipasshpubkey:
            _params['ipasshpubkey'] = o_ipasshpubkey
        if o_st:
            _params['st'] = o_st
        if o_street:
            _params['street'] = o_street
        if o_title:
            _params['title'] = o_title
        if o_ipauserauthtype:
            _params['ipauserauthtype'] = o_ipauserauthtype
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        _params['cn'] = o_cn
        if o_displayname:
            _params['displayname'] = o_displayname
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_initials:
            _params['initials'] = o_initials

        return self._request(method, _args, _params)

    def user_add_cert(
            self,
            a_uid,
            o_usercertificate,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add one or more certificates to the user entry
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        """
        method = 'user_add_cert'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def user_add_certmapdata(
            self,
            a_uid,
            a_ipacertmapdata=None,
            o_certificate=None,
            o_issuer=None,
            o_subject=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add one or more certificate mappings to the user entry.
        :param a_ipacertmapdata: Certificate mapping data
        :type  a_ipacertmapdata: str
        :param a_uid: User login
        :type  a_uid: str
        :param o_certificate: Base-64 encoded user certificate
        :type  o_certificate: Certificate
        :param o_issuer: Issuer of the certificate
        :type  o_issuer: DNParam
        :param o_subject: Subject of the certificate
        :type  o_subject: DNParam
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'user_add_certmapdata'

        _args = list()
        _args.append(a_ipacertmapdata)
        _args.append(a_uid)

        _params = dict()
        if o_certificate:
            _params['certificate'] = o_certificate
        if o_issuer:
            _params['issuer'] = o_issuer
        if o_subject:
            _params['subject'] = o_subject
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def user_add_manager(
            self,
            a_uid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_user=None,
    ):
        """Add a manager to the user entry
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'user_add_manager'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def user_add_principal(
            self,
            a_uid,
            a_krbprincipalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Add new principal alias to the user entry
        :param a_uid: User login
        :type  a_uid: str
        :param a_krbprincipalname: Principal alias
        :type  a_krbprincipalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'user_add_principal'

        _args = list()
        _args.append(a_uid)
        _args.append(a_krbprincipalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def user_del(
            self,
            a_uid,
            o_preserve=None,
            o_continue=False,
    ):
        """Delete a user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_preserve: <preserve>
        :type  o_preserve: Bool
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'user_del'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        if o_preserve:
            _params['preserve'] = o_preserve
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def user_disable(
            self,
            a_uid,
    ):
        """Disable a user account.
        :param a_uid: User login
        :type  a_uid: str
        """
        method = 'user_disable'

        _args = list()
        _args.append(a_uid)

        _params = dict()

        return self._request(method, _args, _params)

    def user_enable(
            self,
            a_uid,
    ):
        """Enable a user account.
        :param a_uid: User login
        :type  a_uid: str
        """
        method = 'user_enable'

        _args = list()
        _args.append(a_uid)

        _params = dict()

        return self._request(method, _args, _params)

    def user_find(
            self,
            a_criteria=None,
            o_preserved=False,
            o_sizelimit=None,
            o_timelimit=None,
            o_in_group=None,
            o_in_hbacrule=None,
            o_in_netgroup=None,
            o_in_role=None,
            o_in_sudorule=None,
            o_not_in_group=None,
            o_not_in_hbacrule=None,
            o_not_in_netgroup=None,
            o_not_in_role=None,
            o_not_in_sudorule=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_whoami=False,
            o_nsaccountlock=False,
            o_usercertificate=None,
            o_krbpasswordexpiration=None,
            o_krbprincipalexpiration=None,
            o_gidnumber=None,
            o_uidnumber=None,
            o_userpassword=None,
            o_krbprincipalname=None,
            o_carlicense=None,
            o_l=None,
            o_userclass=None,
            o_cn=None,
            o_departmentnumber=None,
            o_displayname=None,
            o_mail=None,
            o_employeenumber=None,
            o_employeetype=None,
            o_facsimiletelephonenumber=None,
            o_givenname=None,
            o_gecos=None,
            o_homedirectory=None,
            o_initials=None,
            o_sn=None,
            o_uid=None,
            o_manager=None,
            o_mobile=None,
            o_ou=None,
            o_pager=None,
            o_telephonenumber=None,
            o_postalcode=None,
            o_preferredlanguage=None,
            o_ipatokenradiusconfiglink=None,
            o_ipatokenradiususername=None,
            o_loginshell=None,
            o_st=None,
            o_street=None,
            o_title=None,
            o_ipauserauthtype=None,
    ):
        """Search for users.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_preserved: Preserved user
        :type  o_preserved: Bool
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_in_group: Search for users with these member of groups.
        :type  o_in_group: str
        :param o_in_hbacrule: Search for users with these member of HBAC rules.
        :type  o_in_hbacrule: str
        :param o_in_netgroup: Search for users with these member of netgroups.
        :type  o_in_netgroup: str
        :param o_in_role: Search for users with these member of roles.
        :type  o_in_role: str
        :param o_in_sudorule: Search for users with these member of sudo rules.
        :type  o_in_sudorule: str
        :param o_not_in_group: Search for users without these member of groups.
        :type  o_not_in_group: str
        :param o_not_in_hbacrule: Search for users without these member of HBAC rules.
        :type  o_not_in_hbacrule: str
        :param o_not_in_netgroup: Search for users without these member of netgroups.
        :type  o_not_in_netgroup: str
        :param o_not_in_role: Search for users without these member of roles.
        :type  o_not_in_role: str
        :param o_not_in_sudorule: Search for users without these member of sudo rules.
        :type  o_not_in_sudorule: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("login")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_whoami: Display user record for current Kerberos principal
        :type  o_whoami: bool
        :param o_nsaccountlock: Account disabled
        :type  o_nsaccountlock: Bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        :param o_krbpasswordexpiration: User password expiration
        :type  o_krbpasswordexpiration: DateTime
        :param o_krbprincipalexpiration: Kerberos principal expiration
        :type  o_krbprincipalexpiration: DateTime
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number (system will assign one if not provided)
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_userpassword: Prompt to set the user password
        :type  o_userpassword: Password
        :param o_krbprincipalname: Principal alias
        :type  o_krbprincipalname: Principal
        :param o_carlicense: Car License
        :type  o_carlicense: str
        :param o_l: City
        :type  o_l: str
        :param o_userclass: User category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_cn: Full name
        :type  o_cn: str
        :param o_departmentnumber: Department Number
        :type  o_departmentnumber: str
        :param o_displayname: Display name
        :type  o_displayname: str
        :param o_mail: Email address
        :type  o_mail: str
        :param o_employeenumber: Employee Number
        :type  o_employeenumber: str
        :param o_employeetype: Employee Type
        :type  o_employeetype: str
        :param o_facsimiletelephonenumber: Fax Number
        :type  o_facsimiletelephonenumber: str
        :param o_givenname: First name
        :type  o_givenname: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_initials: Initials
        :type  o_initials: str
        :param o_sn: Last name
        :type  o_sn: str
        :param o_uid: User login
        :type  o_uid: str
        :param o_manager: Manager
        :type  o_manager: str
        :param o_mobile: Mobile Telephone Number
        :type  o_mobile: str
        :param o_ou: Org. Unit
        :type  o_ou: str
        :param o_pager: Pager Number
        :type  o_pager: str
        :param o_telephonenumber: Telephone Number
        :type  o_telephonenumber: str
        :param o_postalcode: ZIP
        :type  o_postalcode: str
        :param o_preferredlanguage: Preferred Language
        :type  o_preferredlanguage: str
        :param o_ipatokenradiusconfiglink: RADIUS proxy configuration
        :type  o_ipatokenradiusconfiglink: str
        :param o_ipatokenradiususername: RADIUS proxy username
        :type  o_ipatokenradiususername: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        :param o_st: State/Province
        :type  o_st: str
        :param o_street: Street address
        :type  o_street: str
        :param o_title: Job Title
        :type  o_title: str
        :param o_ipauserauthtype: Types of supported user authentication
        :type  o_ipauserauthtype: str, valid values ['password', 'radius', 'otp']
        """
        method = 'user_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_preserved:
            _params['preserved'] = o_preserved
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_in_group:
            _params['in_group'] = o_in_group
        if o_in_hbacrule:
            _params['in_hbacrule'] = o_in_hbacrule
        if o_in_netgroup:
            _params['in_netgroup'] = o_in_netgroup
        if o_in_role:
            _params['in_role'] = o_in_role
        if o_in_sudorule:
            _params['in_sudorule'] = o_in_sudorule
        if o_not_in_group:
            _params['not_in_group'] = o_not_in_group
        if o_not_in_hbacrule:
            _params['not_in_hbacrule'] = o_not_in_hbacrule
        if o_not_in_netgroup:
            _params['not_in_netgroup'] = o_not_in_netgroup
        if o_not_in_role:
            _params['not_in_role'] = o_not_in_role
        if o_not_in_sudorule:
            _params['not_in_sudorule'] = o_not_in_sudorule
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        _params['whoami'] = o_whoami
        if o_nsaccountlock:
            _params['nsaccountlock'] = o_nsaccountlock
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbpasswordexpiration:
            _params['krbpasswordexpiration'] = o_krbpasswordexpiration
        if o_krbprincipalexpiration:
            _params['krbprincipalexpiration'] = o_krbprincipalexpiration
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        if o_carlicense:
            _params['carlicense'] = o_carlicense
        if o_l:
            _params['l'] = o_l
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_cn:
            _params['cn'] = o_cn
        if o_departmentnumber:
            _params['departmentnumber'] = o_departmentnumber
        if o_displayname:
            _params['displayname'] = o_displayname
        if o_mail:
            _params['mail'] = o_mail
        if o_employeenumber:
            _params['employeenumber'] = o_employeenumber
        if o_employeetype:
            _params['employeetype'] = o_employeetype
        if o_facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = o_facsimiletelephonenumber
        if o_givenname:
            _params['givenname'] = o_givenname
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        if o_initials:
            _params['initials'] = o_initials
        if o_sn:
            _params['sn'] = o_sn
        if o_uid:
            _params['uid'] = o_uid
        if o_manager:
            _params['manager'] = o_manager
        if o_mobile:
            _params['mobile'] = o_mobile
        if o_ou:
            _params['ou'] = o_ou
        if o_pager:
            _params['pager'] = o_pager
        if o_telephonenumber:
            _params['telephonenumber'] = o_telephonenumber
        if o_postalcode:
            _params['postalcode'] = o_postalcode
        if o_preferredlanguage:
            _params['preferredlanguage'] = o_preferredlanguage
        if o_ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = o_ipatokenradiusconfiglink
        if o_ipatokenradiususername:
            _params['ipatokenradiususername'] = o_ipatokenradiususername
        if o_loginshell:
            _params['loginshell'] = o_loginshell
        if o_st:
            _params['st'] = o_st
        if o_street:
            _params['street'] = o_street
        if o_title:
            _params['title'] = o_title
        if o_ipauserauthtype:
            _params['ipauserauthtype'] = o_ipauserauthtype

        return self._request(method, _args, _params)

    def user_mod(
            self,
            a_uid,
            o_addattr=None,
            o_delattr=None,
            o_rename=None,
            o_setattr=None,
            o_all=True,
            o_no_members=False,
            o_random=False,
            o_raw=False,
            o_rights=False,
            o_nsaccountlock=False,
            o_usercertificate=None,
            o_krbpasswordexpiration=None,
            o_krbprincipalexpiration=None,
            o_gidnumber=None,
            o_uidnumber=None,
            o_userpassword=None,
            o_krbprincipalname=None,
            o_carlicense=None,
            o_l=None,
            o_userclass=None,
            o_cn=None,
            o_departmentnumber=None,
            o_displayname=None,
            o_mail=None,
            o_employeenumber=None,
            o_employeetype=None,
            o_facsimiletelephonenumber=None,
            o_givenname=None,
            o_gecos=None,
            o_homedirectory=None,
            o_initials=None,
            o_sn=None,
            o_manager=None,
            o_mobile=None,
            o_ou=None,
            o_pager=None,
            o_telephonenumber=None,
            o_postalcode=None,
            o_preferredlanguage=None,
            o_ipatokenradiusconfiglink=None,
            o_ipatokenradiususername=None,
            o_loginshell=None,
            o_ipasshpubkey=None,
            o_st=None,
            o_street=None,
            o_title=None,
            o_ipauserauthtype=None,
    ):
        """Modify a user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_rename: Rename the user object
        :type  o_rename: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_random: Generate a random user password
        :type  o_random: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_nsaccountlock: Account disabled
        :type  o_nsaccountlock: Bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        :param o_krbpasswordexpiration: User password expiration
        :type  o_krbpasswordexpiration: DateTime
        :param o_krbprincipalexpiration: Kerberos principal expiration
        :type  o_krbprincipalexpiration: DateTime
        :param o_gidnumber: Group ID Number
        :type  o_gidnumber: int, min value 1, max value 2147483647
        :param o_uidnumber: User ID Number (system will assign one if not provided)
        :type  o_uidnumber: int, min value 1, max value 2147483647
        :param o_userpassword: Prompt to set the user password
        :type  o_userpassword: Password
        :param o_krbprincipalname: Principal alias
        :type  o_krbprincipalname: Principal
        :param o_carlicense: Car License
        :type  o_carlicense: str
        :param o_l: City
        :type  o_l: str
        :param o_userclass: User category (semantics placed on this attribute are for local interpretation)
        :type  o_userclass: str
        :param o_cn: Full name
        :type  o_cn: str
        :param o_departmentnumber: Department Number
        :type  o_departmentnumber: str
        :param o_displayname: Display name
        :type  o_displayname: str
        :param o_mail: Email address
        :type  o_mail: str
        :param o_employeenumber: Employee Number
        :type  o_employeenumber: str
        :param o_employeetype: Employee Type
        :type  o_employeetype: str
        :param o_facsimiletelephonenumber: Fax Number
        :type  o_facsimiletelephonenumber: str
        :param o_givenname: First name
        :type  o_givenname: str
        :param o_gecos: GECOS
        :type  o_gecos: str
        :param o_homedirectory: Home directory
        :type  o_homedirectory: str
        :param o_initials: Initials
        :type  o_initials: str
        :param o_sn: Last name
        :type  o_sn: str
        :param o_manager: Manager
        :type  o_manager: str
        :param o_mobile: Mobile Telephone Number
        :type  o_mobile: str
        :param o_ou: Org. Unit
        :type  o_ou: str
        :param o_pager: Pager Number
        :type  o_pager: str
        :param o_telephonenumber: Telephone Number
        :type  o_telephonenumber: str
        :param o_postalcode: ZIP
        :type  o_postalcode: str
        :param o_preferredlanguage: Preferred Language
        :type  o_preferredlanguage: str
        :param o_ipatokenradiusconfiglink: RADIUS proxy configuration
        :type  o_ipatokenradiusconfiglink: str
        :param o_ipatokenradiususername: RADIUS proxy username
        :type  o_ipatokenradiususername: str
        :param o_loginshell: Login shell
        :type  o_loginshell: str
        :param o_ipasshpubkey: SSH public key
        :type  o_ipasshpubkey: str
        :param o_st: State/Province
        :type  o_st: str
        :param o_street: Street address
        :type  o_street: str
        :param o_title: Job Title
        :type  o_title: str
        :param o_ipauserauthtype: Types of supported user authentication
        :type  o_ipauserauthtype: str, valid values ['password', 'radius', 'otp']
        """
        method = 'user_mod'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_rename:
            _params['rename'] = o_rename
        if o_setattr:
            _params['setattr'] = o_setattr
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_random:
            _params['random'] = o_random
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_nsaccountlock:
            _params['nsaccountlock'] = o_nsaccountlock
        if o_usercertificate:
            _params['usercertificate'] = o_usercertificate
        if o_krbpasswordexpiration:
            _params['krbpasswordexpiration'] = o_krbpasswordexpiration
        if o_krbprincipalexpiration:
            _params['krbprincipalexpiration'] = o_krbprincipalexpiration
        if o_gidnumber:
            _params['gidnumber'] = o_gidnumber
        if o_uidnumber:
            _params['uidnumber'] = o_uidnumber
        if o_userpassword:
            _params['userpassword'] = o_userpassword
        if o_krbprincipalname:
            _params['krbprincipalname'] = o_krbprincipalname
        if o_carlicense:
            _params['carlicense'] = o_carlicense
        if o_l:
            _params['l'] = o_l
        if o_userclass:
            _params['userclass'] = o_userclass
        if o_cn:
            _params['cn'] = o_cn
        if o_departmentnumber:
            _params['departmentnumber'] = o_departmentnumber
        if o_displayname:
            _params['displayname'] = o_displayname
        if o_mail:
            _params['mail'] = o_mail
        if o_employeenumber:
            _params['employeenumber'] = o_employeenumber
        if o_employeetype:
            _params['employeetype'] = o_employeetype
        if o_facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = o_facsimiletelephonenumber
        if o_givenname:
            _params['givenname'] = o_givenname
        if o_gecos:
            _params['gecos'] = o_gecos
        if o_homedirectory:
            _params['homedirectory'] = o_homedirectory
        if o_initials:
            _params['initials'] = o_initials
        if o_sn:
            _params['sn'] = o_sn
        if o_manager:
            _params['manager'] = o_manager
        if o_mobile:
            _params['mobile'] = o_mobile
        if o_ou:
            _params['ou'] = o_ou
        if o_pager:
            _params['pager'] = o_pager
        if o_telephonenumber:
            _params['telephonenumber'] = o_telephonenumber
        if o_postalcode:
            _params['postalcode'] = o_postalcode
        if o_preferredlanguage:
            _params['preferredlanguage'] = o_preferredlanguage
        if o_ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = o_ipatokenradiusconfiglink
        if o_ipatokenradiususername:
            _params['ipatokenradiususername'] = o_ipatokenradiususername
        if o_loginshell:
            _params['loginshell'] = o_loginshell
        if o_ipasshpubkey:
            _params['ipasshpubkey'] = o_ipasshpubkey
        if o_st:
            _params['st'] = o_st
        if o_street:
            _params['street'] = o_street
        if o_title:
            _params['title'] = o_title
        if o_ipauserauthtype:
            _params['ipauserauthtype'] = o_ipauserauthtype

        return self._request(method, _args, _params)

    def user_remove_cert(
            self,
            a_uid,
            o_usercertificate,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove one or more certificates to the user entry
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_usercertificate: Base-64 encoded user certificate
        :type  o_usercertificate: Certificate
        """
        method = 'user_remove_cert'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['usercertificate'] = o_usercertificate

        return self._request(method, _args, _params)

    def user_remove_certmapdata(
            self,
            a_uid,
            a_ipacertmapdata=None,
            o_certificate=None,
            o_issuer=None,
            o_subject=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove one or more certificate mappings from the user entry.
        :param a_ipacertmapdata: Certificate mapping data
        :type  a_ipacertmapdata: str
        :param a_uid: User login
        :type  a_uid: str
        :param o_certificate: Base-64 encoded user certificate
        :type  o_certificate: Certificate
        :param o_issuer: Issuer of the certificate
        :type  o_issuer: DNParam
        :param o_subject: Subject of the certificate
        :type  o_subject: DNParam
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'user_remove_certmapdata'

        _args = list()
        _args.append(a_ipacertmapdata)
        _args.append(a_uid)

        _params = dict()
        if o_certificate:
            _params['certificate'] = o_certificate
        if o_issuer:
            _params['issuer'] = o_issuer
        if o_subject:
            _params['subject'] = o_subject
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def user_remove_manager(
            self,
            a_uid,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_user=None,
    ):
        """Remove a manager to the user entry
        :param a_uid: User login
        :type  a_uid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'user_remove_manager'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def user_remove_principal(
            self,
            a_uid,
            a_krbprincipalname,
            o_all=True,
            o_no_members=False,
            o_raw=False,
    ):
        """Remove principal alias from the user entry
        :param a_uid: User login
        :type  a_uid: str
        :param a_krbprincipalname: Principal alias
        :type  a_krbprincipalname: Principal
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'user_remove_principal'

        _args = list()
        _args.append(a_uid)
        _args.append(a_krbprincipalname)

        _params = dict()
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def user_show(
            self,
            a_uid,
            o_out=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
    ):
        """Display information about a user.
        :param a_uid: User login
        :type  a_uid: str
        :param o_out: file to store certificate in
        :type  o_out: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        """
        method = 'user_show'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        if o_out:
            _params['out'] = o_out
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights

        return self._request(method, _args, _params)

    def user_stage(
            self,
            a_uid,
            o_continue=False,
    ):
        """Move deleted user into staged area
        :param a_uid: User login
        :type  a_uid: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        """
        method = 'user_stage'

        _args = list()
        _args.append(a_uid)

        _params = dict()
        _params['continue'] = o_continue

        return self._request(method, _args, _params)

    def user_status(
            self,
            a_useruid,
            o_all=True,
            o_raw=False,
    ):
        """
    Lockout status of a user account

    An account may become locked if the password is entered incorrectly too
    many times within a specific time period as controlled by password
    policy. A locked account is a temporary condition and may be unlocked by
    an administrator.

    This connects to each IPA master and displays the lockout status on
    each one.

    To determine whether an account is locked on a given server you need
    to compare the number of failed logins and the time of the last failure.
    For an account to be locked it must exceed the maxfail failures within
    the failinterval duration as specified in the password policy associated
    with the user.

    The failed login counter is modified only when a user attempts a log in
    so it is possible that an account may appear locked but the last failed
    login attempt is older than the lockouttime of the password policy. This
    means that the user may attempt a login again.
        :param a_useruid: User login
        :type  a_useruid: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'user_status'

        _args = list()
        _args.append(a_useruid)

        _params = dict()
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def user_undel(
            self,
            a_uid,
    ):
        """Undelete a delete user account.
        :param a_uid: User login
        :type  a_uid: str
        """
        method = 'user_undel'

        _args = list()
        _args.append(a_uid)

        _params = dict()

        return self._request(method, _args, _params)

    def user_unlock(
            self,
            a_uid,
    ):
        """
    Unlock a user account

    An account may become locked if the password is entered incorrectly too
    many times within a specific time period as controlled by password
    policy. A locked account is a temporary condition and may be unlocked by
    an administrator.
        :param a_uid: User login
        :type  a_uid: str
        """
        method = 'user_unlock'

        _args = list()
        _args.append(a_uid)

        _params = dict()

        return self._request(method, _args, _params)

    def vault_add_internal(
            self,
            a_cn,
            o_service=None,
            o_addattr=None,
            o_setattr=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_shared=False,
            o_ipavaultpublickey=None,
            o_ipavaultsalt=None,
            o_description=None,
            o_ipavaulttype='symmetric',
    ):
        """None
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_ipavaultpublickey: Vault public key
        :type  o_ipavaultpublickey: Bytes
        :param o_ipavaultsalt: Vault salt
        :type  o_ipavaultsalt: Bytes
        :param o_description: Vault description
        :type  o_description: str
        :param o_ipavaulttype: Vault type
        :type  o_ipavaulttype: str, valid values ['standard', 'symmetric', 'asymmetric']
        """
        method = 'vault_add_internal'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_setattr:
            _params['setattr'] = o_setattr
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared
        if o_ipavaultpublickey:
            _params['ipavaultpublickey'] = o_ipavaultpublickey
        if o_ipavaultsalt:
            _params['ipavaultsalt'] = o_ipavaultsalt
        if o_description:
            _params['description'] = o_description
        if o_ipavaulttype:
            _params['ipavaulttype'] = o_ipavaulttype

        return self._request(method, _args, _params)

    def vault_add_member(
            self,
            a_cn,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_shared=False,
            o_group=None,
            o_services=None,
            o_user=None,
    ):
        """Add members to a vault.
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_services: services to add
        :type  o_services: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'vault_add_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared
        if o_group:
            _params['group'] = o_group
        if o_services:
            _params['services'] = o_services
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def vault_add_owner(
            self,
            a_cn,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_shared=False,
            o_group=None,
            o_services=None,
            o_user=None,
    ):
        """Add owners to a vault.
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_services: services to add
        :type  o_services: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'vault_add_owner'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared
        if o_group:
            _params['group'] = o_group
        if o_services:
            _params['services'] = o_services
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def vault_archive_internal(
            self,
            a_cn,
            o_nonce,
            o_session_key,
            o_vault_data,
            o_service=None,
            o_username=None,
            o_all=True,
            o_raw=False,
            o_shared=False,
    ):
        """None
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_nonce: Nonce
        :type  o_nonce: Bytes
        :param o_session_key: Session key wrapped with transport certificate
        :type  o_session_key: Bytes
        :param o_vault_data: Vault data encrypted with session key
        :type  o_vault_data: Bytes
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        """
        method = 'vault_archive_internal'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['nonce'] = o_nonce
        _params['session_key'] = o_session_key
        _params['vault_data'] = o_vault_data
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared

        return self._request(method, _args, _params)

    def vault_del(
            self,
            a_cn,
            o_service=None,
            o_username=None,
            o_continue=False,
            o_shared=False,
    ):
        """Delete a vault.
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        """
        method = 'vault_del'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['continue'] = o_continue
        if o_shared:
            _params['shared'] = o_shared

        return self._request(method, _args, _params)

    def vault_find(
            self,
            a_criteria=None,
            o_sizelimit=None,
            o_timelimit=None,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=True,
            o_pkey_only=False,
            o_raw=False,
            o_services=False,
            o_shared=False,
            o_users=False,
            o_description=None,
            o_cn=None,
            o_ipavaulttype='symmetric',
    ):
        """Search for vaults.
        :param a_criteria: A string searched in all relevant object attributes
        :type  a_criteria: str
        :param o_sizelimit: Maximum number of entries returned (0 is unlimited)
        :type  o_sizelimit: int, min value 0, max value 2147483647
        :param o_timelimit: Time limit of search in seconds (0 is unlimited)
        :type  o_timelimit: int, min value 0, max value 2147483647
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_pkey_only: Results should contain primary key attribute only ("name")
        :type  o_pkey_only: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_services: List all service vaults
        :type  o_services: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_users: List all user vaults
        :type  o_users: bool
        :param o_description: Vault description
        :type  o_description: str
        :param o_cn: Vault name
        :type  o_cn: str
        :param o_ipavaulttype: Vault type
        :type  o_ipavaulttype: str, valid values ['standard', 'symmetric', 'asymmetric']
        """
        method = 'vault_find'

        _args = list()
        _args.append(a_criteria)

        _params = dict()
        if o_sizelimit:
            _params['sizelimit'] = o_sizelimit
        if o_timelimit:
            _params['timelimit'] = o_timelimit
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        if o_pkey_only:
            _params['pkey_only'] = o_pkey_only
        _params['raw'] = o_raw
        if o_services:
            _params['services'] = o_services
        if o_shared:
            _params['shared'] = o_shared
        if o_users:
            _params['users'] = o_users
        if o_description:
            _params['description'] = o_description
        if o_cn:
            _params['cn'] = o_cn
        if o_ipavaulttype:
            _params['ipavaulttype'] = o_ipavaulttype

        return self._request(method, _args, _params)

    def vault_mod_internal(
            self,
            a_cn,
            o_service=None,
            o_addattr=None,
            o_delattr=None,
            o_setattr=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_shared=False,
            o_ipavaultpublickey=None,
            o_ipavaultsalt=None,
            o_description=None,
            o_ipavaulttype='symmetric',
    ):
        """None
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type  o_addattr: str
        :param o_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type  o_delattr: str
        :param o_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type  o_setattr: str
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_ipavaultpublickey: Vault public key
        :type  o_ipavaultpublickey: Bytes
        :param o_ipavaultsalt: Vault salt
        :type  o_ipavaultsalt: Bytes
        :param o_description: Vault description
        :type  o_description: str
        :param o_ipavaulttype: Vault type
        :type  o_ipavaulttype: str, valid values ['standard', 'symmetric', 'asymmetric']
        """
        method = 'vault_mod_internal'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_addattr:
            _params['addattr'] = o_addattr
        if o_delattr:
            _params['delattr'] = o_delattr
        if o_setattr:
            _params['setattr'] = o_setattr
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_shared:
            _params['shared'] = o_shared
        if o_ipavaultpublickey:
            _params['ipavaultpublickey'] = o_ipavaultpublickey
        if o_ipavaultsalt:
            _params['ipavaultsalt'] = o_ipavaultsalt
        if o_description:
            _params['description'] = o_description
        if o_ipavaulttype:
            _params['ipavaulttype'] = o_ipavaulttype

        return self._request(method, _args, _params)

    def vault_remove_member(
            self,
            a_cn,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_shared=False,
            o_group=None,
            o_services=None,
            o_user=None,
    ):
        """Remove members from a vault.
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_services: services to remove
        :type  o_services: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'vault_remove_member'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared
        if o_group:
            _params['group'] = o_group
        if o_services:
            _params['services'] = o_services
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def vault_remove_owner(
            self,
            a_cn,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_shared=False,
            o_group=None,
            o_services=None,
            o_user=None,
    ):
        """Remove owners from a vault.
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_services: services to remove
        :type  o_services: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'vault_remove_owner'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared
        if o_group:
            _params['group'] = o_group
        if o_services:
            _params['services'] = o_services
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def vault_retrieve_internal(
            self,
            a_cn,
            o_session_key,
            o_service=None,
            o_username=None,
            o_all=True,
            o_raw=False,
            o_shared=False,
    ):
        """None
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_session_key: Session key wrapped with transport certificate
        :type  o_session_key: Bytes
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        """
        method = 'vault_retrieve_internal'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        _params['session_key'] = o_session_key
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared

        return self._request(method, _args, _params)

    def vault_show(
            self,
            a_cn,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_shared=False,
    ):
        """Display information about a vault.
        :param a_cn: Vault name
        :type  a_cn: str
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        """
        method = 'vault_show'

        _args = list()
        _args.append(a_cn)

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_shared:
            _params['shared'] = o_shared

        return self._request(method, _args, _params)

    def vaultconfig_show(
            self,
            o_transport_out=None,
            o_all=True,
            o_raw=False,
    ):
        """Show vault configuration.
        :param o_transport_out: Output file to store the transport certificate
        :type  o_transport_out: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        """
        method = 'vaultconfig_show'

        _args = list()

        _params = dict()
        if o_transport_out:
            _params['transport_out'] = o_transport_out
        _params['all'] = o_all
        _params['raw'] = o_raw

        return self._request(method, _args, _params)

    def vaultcontainer_add_owner(
            self,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_shared=False,
            o_group=None,
            o_services=None,
            o_user=None,
    ):
        """Add owners to a vault container.
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_group: groups to add
        :type  o_group: str
        :param o_services: services to add
        :type  o_services: str
        :param o_user: users to add
        :type  o_user: str
        """
        method = 'vaultcontainer_add_owner'

        _args = list()

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared
        if o_group:
            _params['group'] = o_group
        if o_services:
            _params['services'] = o_services
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def vaultcontainer_del(
            self,
            o_service=None,
            o_username=None,
            o_continue=False,
            o_shared=False,
    ):
        """Delete a vault container.
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_continue: Continuous mode: Don't stop on errors.
        :type  o_continue: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        """
        method = 'vaultcontainer_del'

        _args = list()

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['continue'] = o_continue
        if o_shared:
            _params['shared'] = o_shared

        return self._request(method, _args, _params)

    def vaultcontainer_remove_owner(
            self,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_shared=False,
            o_group=None,
            o_services=None,
            o_user=None,
    ):
        """Remove owners from a vault container.
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        :param o_group: groups to remove
        :type  o_group: str
        :param o_services: services to remove
        :type  o_services: str
        :param o_user: users to remove
        :type  o_user: str
        """
        method = 'vaultcontainer_remove_owner'

        _args = list()

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        if o_shared:
            _params['shared'] = o_shared
        if o_group:
            _params['group'] = o_group
        if o_services:
            _params['services'] = o_services
        if o_user:
            _params['user'] = o_user

        return self._request(method, _args, _params)

    def vaultcontainer_show(
            self,
            o_service=None,
            o_username=None,
            o_all=True,
            o_no_members=False,
            o_raw=False,
            o_rights=False,
            o_shared=False,
    ):
        """Display information about a vault container.
        :param o_service: Service name of the service vault
        :type  o_service: Principal
        :param o_username: Username of the user vault
        :type  o_username: str
        :param o_all: Retrieve and print all attributes from the server. Affects command output.
        :type  o_all: bool
        :param o_no_members: Suppress processing of membership attributes.
        :type  o_no_members: bool
        :param o_raw: Print entries as stored on the server. Only affects output format.
        :type  o_raw: bool
        :param o_rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type  o_rights: bool
        :param o_shared: Shared vault
        :type  o_shared: bool
        """
        method = 'vaultcontainer_show'

        _args = list()

        _params = dict()
        if o_service:
            _params['service'] = o_service
        if o_username:
            _params['username'] = o_username
        _params['all'] = o_all
        _params['no_members'] = o_no_members
        _params['raw'] = o_raw
        _params['rights'] = o_rights
        if o_shared:
            _params['shared'] = o_shared

        return self._request(method, _args, _params)

    def whoami(
            self,
    ):
        """Describe currently authenticated identity.
        """
        method = 'whoami'

        _args = list()

        _params = dict()

        return self._request(method, _args, _params)
