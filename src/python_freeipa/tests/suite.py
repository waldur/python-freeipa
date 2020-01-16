import json
import responses
import unittest

from python_freeipa import ClientLegacy as Client


class UsersTest(unittest.TestCase):
    def setUp(self):
        self.client = Client('ipa.demo1.freeipa.org', version='2.215')
        self.url = 'https://ipa.demo1.freeipa.org/ipa/session/json'
        self.maxDiff = None

    @responses.activate
    def test_user_add(self):
        request_json = {
            'method': 'user_add',
            'params': [
                ['alice'],
                {
                    'all': True,
                    'givenname': 'Alice',
                    'sn': 'Lebowski',
                    'cn': 'Alice Lebowski',
                    'preferredlanguage': 'EN',
                    'version': '2.215'
                }
            ]
        }

        response_json = {
            'error': None,
            'id': None,
            'principal': 'admin@DEMO1.FREEIPA.ORG',
            'result': {
                'result': {
                    'cn': [
                        'Alice Lebowski'
                    ],
                    'displayname': [
                        'Alice Lebowski'
                    ],
                    'dn': 'uid=alice,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org',
                    'gecos': [
                        'Alice Lebowski'
                    ],
                    'gidnumber': [
                        '1120000017'
                    ],
                    'givenname': [
                        'Alice'
                    ],
                    'has_keytab': False,
                    'has_password': False,
                    'homedirectory': [
                        '/home/alice'
                    ],
                    'initials': [
                        'AL'
                    ],
                    'ipauniqueid': [
                        'e413c980-409e-11e7-b15d-fa163e0a8415'
                    ],
                    'krbcanonicalname': [
                        'alice@DEMO1.FREEIPA.ORG'
                    ],
                    'krbprincipalname': [
                        'alice@DEMO1.FREEIPA.ORG'
                    ],
                    'loginshell': [
                        '/bin/sh'
                    ],
                    'mail': [
                        'alice@demo1.freeipa.org'
                    ],
                    'memberof_group': [
                        'ipausers'
                    ],
                    'mepmanagedentry': [
                        'cn=alice,cn=groups,cn=accounts,dc=demo1,dc=freeipa,dc=org'
                    ],
                    'objectclass': [
                        'ipaSshGroupOfPubKeys',
                        'ipaobject',
                        'mepOriginEntry',
                        'person',
                        'top',
                        'ipasshuser',
                        'inetorgperson',
                        'organizationalperson',
                        'krbticketpolicyaux',
                        'krbprincipalaux',
                        'inetuser',
                        'posixaccount'
                    ],
                    'sn': [
                        'Lebowski'
                    ],
                    'uid': [
                        'alice'
                    ],
                    'uidnumber': [
                        '1120000017'
                    ]
                },
                'summary': 'Added user \'alice\'',
                'value': 'alice'
            },
            'version': '4.4.2'
        }

        responses.add(responses.POST, self.url, json=response_json, status=200)
        self.client.user_add('alice', 'Alice', 'Lebowski', 'Alice Lebowski', preferred_language='EN')
        self.assertEqual(1, len(responses.calls))
        self.assertEqual(json.loads(responses.calls[0].request.body), request_json)

    @responses.activate
    def test_user_disable(self):
        request_json = {
            'method': 'user_disable',
            'params': [
                ['test1'],
                {'version': '2.215'}
            ]
        }

        response_json = {
            'error': None,
            'id': None,
            'principal': 'admin@DEMO1.FREEIPA.ORG',
            'result': {
                'result': True,
                'summary': 'Disabled user account \'test1\'',
                'value': 'test1'
            },
            'version': '4.4.2'
        }

        responses.add(responses.POST, self.url, json=response_json, status=200)
        self.client.user_disable('test1')

        self.assertEqual(1, len(responses.calls))
        self.assertEqual(json.loads(responses.calls[0].request.body), request_json)
