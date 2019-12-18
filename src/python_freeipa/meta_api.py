class MetaAPI:
    def __init__(self):
        pass

    def _request(self, method, args=None, params=None):
        raise NotImplementedError

    def aci_add(
        self,
        aciname,
        permissions,
        aciprefix,
        attrs=None,
        opt_filter=None,
        group=None,
        memberof=None,
        permission=None,
        subtree=None,
        targetgroup=None,
        opt_type=None,
        opt_all=True,
        raw=False,
        selfaci=False,
        test=False,
    ):
        """
    Create new ACI.
    
        :param aciname: ACI name
        :type aciname: Str
        :param attrs: Attributes
        :type attrs: Str
        :param opt_filter: Legal LDAP filter (e.g. ou=Engineering)
        :type opt_filter: Str
        :param group: User group ACI grants access to
        :type group: Str
        :param memberof: Member of a group
        :type memberof: Str
        :param permission: Permission ACI grants access to
        :type permission: Str
        :param permissions: Permissions to grant(read, write, add, delete, all)
        :type permissions: Str
        :param subtree: Subtree to apply ACI to
        :type subtree: Str
        :param targetgroup: Group to apply ACI to
        :type targetgroup: Str
        :param aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type aciprefix: StrEnum
        :param opt_type: type of IPA object (user, group, host, hostgroup, service, netgroup)
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param selfaci: Apply ACI to your own entry (self)
        :type selfaci: Flag
        :param test: Test the ACI syntax but don't write anything
        :type test: Flag
        """
        method = 'aci_add'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        if attrs:
            _params['attrs'] = attrs
        if opt_filter:
            _params['filter'] = opt_filter
        if group:
            _params['group'] = group
        if memberof:
            _params['memberof'] = memberof
        if permission:
            _params['permission'] = permission
        _params['permissions'] = permissions
        if subtree:
            _params['subtree'] = subtree
        if targetgroup:
            _params['targetgroup'] = targetgroup
        _params['aciprefix'] = aciprefix
        if opt_type:
            _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        if selfaci:
            _params['selfaci'] = selfaci
        if test:
            _params['test'] = test
        
        return self._request(method, _args, _params)

    def aci_del(
        self,
        aciname,
        aciprefix,
    ):
        """
    Delete ACI.
    
        :param aciname: ACI name
        :type aciname: Str
        :param aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type aciprefix: StrEnum
        """
        method = 'aci_del'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        _params['aciprefix'] = aciprefix
        
        return self._request(method, _args, _params)

    def aci_find(
        self,
        criteria=None,
        selfaci=False,
        attrs=None,
        opt_filter=None,
        group=None,
        memberof=None,
        aciname=None,
        permission=None,
        permissions=None,
        subtree=None,
        targetgroup=None,
        aciprefix=None,
        opt_type=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
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
    
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param selfaci: Apply ACI to your own entry (self)
        :type selfaci: Bool
        :param attrs: Attributes
        :type attrs: Str
        :param opt_filter: Legal LDAP filter (e.g. ou=Engineering)
        :type opt_filter: Str
        :param group: User group ACI grants access to
        :type group: Str
        :param memberof: Member of a group
        :type memberof: Str
        :param aciname: ACI name
        :type aciname: Str
        :param permission: Permission ACI grants access to
        :type permission: Str
        :param permissions: Permissions to grant(read, write, add, delete, all)
        :type permissions: Str
        :param subtree: Subtree to apply ACI to
        :type subtree: Str
        :param targetgroup: Group to apply ACI to
        :type targetgroup: Str
        :param aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type aciprefix: StrEnum
        :param opt_type: type of IPA object (user, group, host, hostgroup, service, netgroup)
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'aci_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if selfaci:
            _params['selfaci'] = selfaci
        if attrs:
            _params['attrs'] = attrs
        if opt_filter:
            _params['filter'] = opt_filter
        if group:
            _params['group'] = group
        if memberof:
            _params['memberof'] = memberof
        if aciname:
            _params['aciname'] = aciname
        if permission:
            _params['permission'] = permission
        if permissions:
            _params['permissions'] = permissions
        if subtree:
            _params['subtree'] = subtree
        if targetgroup:
            _params['targetgroup'] = targetgroup
        if aciprefix:
            _params['aciprefix'] = aciprefix
        if opt_type:
            _params['type'] = opt_type
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def aci_mod(
        self,
        aciname,
        aciprefix,
        attrs=None,
        opt_filter=None,
        group=None,
        memberof=None,
        permission=None,
        permissions=None,
        subtree=None,
        targetgroup=None,
        opt_type=None,
        opt_all=True,
        raw=False,
        selfaci=False,
    ):
        """
    Modify ACI.
    
        :param aciname: ACI name
        :type aciname: Str
        :param attrs: Attributes
        :type attrs: Str
        :param opt_filter: Legal LDAP filter (e.g. ou=Engineering)
        :type opt_filter: Str
        :param group: User group ACI grants access to
        :type group: Str
        :param memberof: Member of a group
        :type memberof: Str
        :param permission: Permission ACI grants access to
        :type permission: Str
        :param permissions: Permissions to grant(read, write, add, delete, all)
        :type permissions: Str
        :param subtree: Subtree to apply ACI to
        :type subtree: Str
        :param targetgroup: Group to apply ACI to
        :type targetgroup: Str
        :param aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type aciprefix: StrEnum
        :param opt_type: type of IPA object (user, group, host, hostgroup, service, netgroup)
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param selfaci: Apply ACI to your own entry (self)
        :type selfaci: Flag
        """
        method = 'aci_mod'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        if attrs:
            _params['attrs'] = attrs
        if opt_filter:
            _params['filter'] = opt_filter
        if group:
            _params['group'] = group
        if memberof:
            _params['memberof'] = memberof
        if permission:
            _params['permission'] = permission
        if permissions:
            _params['permissions'] = permissions
        if subtree:
            _params['subtree'] = subtree
        if targetgroup:
            _params['targetgroup'] = targetgroup
        _params['aciprefix'] = aciprefix
        if opt_type:
            _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        if selfaci:
            _params['selfaci'] = selfaci
        
        return self._request(method, _args, _params)

    def aci_rename(
        self,
        aciname,
        newname,
        aciprefix,
        attrs=None,
        opt_filter=None,
        group=None,
        memberof=None,
        permission=None,
        permissions=None,
        subtree=None,
        targetgroup=None,
        opt_type=None,
        opt_all=True,
        raw=False,
        selfaci=False,
    ):
        """
    Rename an ACI.
    
        :param aciname: ACI name
        :type aciname: Str
        :param attrs: Attributes
        :type attrs: Str
        :param opt_filter: Legal LDAP filter (e.g. ou=Engineering)
        :type opt_filter: Str
        :param group: User group ACI grants access to
        :type group: Str
        :param memberof: Member of a group
        :type memberof: Str
        :param newname: New ACI name
        :type newname: Str
        :param permission: Permission ACI grants access to
        :type permission: Str
        :param permissions: Permissions to grant(read, write, add, delete, all)
        :type permissions: Str
        :param subtree: Subtree to apply ACI to
        :type subtree: Str
        :param targetgroup: Group to apply ACI to
        :type targetgroup: Str
        :param aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type aciprefix: StrEnum
        :param opt_type: type of IPA object (user, group, host, hostgroup, service, netgroup)
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param selfaci: Apply ACI to your own entry (self)
        :type selfaci: Flag
        """
        method = 'aci_rename'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        if attrs:
            _params['attrs'] = attrs
        if opt_filter:
            _params['filter'] = opt_filter
        if group:
            _params['group'] = group
        if memberof:
            _params['memberof'] = memberof
        _params['newname'] = newname
        if permission:
            _params['permission'] = permission
        if permissions:
            _params['permissions'] = permissions
        if subtree:
            _params['subtree'] = subtree
        if targetgroup:
            _params['targetgroup'] = targetgroup
        _params['aciprefix'] = aciprefix
        if opt_type:
            _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        if selfaci:
            _params['selfaci'] = selfaci
        
        return self._request(method, _args, _params)

    def aci_show(
        self,
        aciname,
        aciprefix,
        location=None,
        opt_all=True,
        raw=False,
    ):
        """
    Display a single ACI given an ACI name.
    
        :param aciname: ACI name
        :type aciname: Str
        :param location: Location of the ACI
        :type location: DNParam
        :param aciprefix: Prefix used to distinguish ACI types (permission, delegation, selfservice, none)
        :type aciprefix: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'aci_show'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        if location:
            _params['location'] = location
        _params['aciprefix'] = aciprefix
        _params['all'] = opt_all
        _params['raw'] = raw
        
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
        cn,
        opt_type,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        description=None,
    ):
        """
    Add an automember rule.
    
        :param cn: Automember Rule
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this auto member rule
        :type description: Str
        """
        method = 'automember_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automember_add_condition(
        self,
        cn,
        key,
        opt_type,
        opt_all=True,
        raw=False,
        description=None,
        automemberexclusiveregex=None,
        automemberinclusiveregex=None,
    ):
        """
    Add conditions to an automember rule.
    
        :param cn: Automember Rule
        :type cn: Str
        :param key: Attribute to filter via regex. For example fqdn for a host, or manager for a user
        :type key: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this auto member rule
        :type description: Str
        :param automemberexclusiveregex: Exclusive Regex
        :type automemberexclusiveregex: Str
        :param automemberinclusiveregex: Inclusive Regex
        :type automemberinclusiveregex: Str
        """
        method = 'automember_add_condition'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['key'] = key
        _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if automemberexclusiveregex:
            _params['automemberexclusiveregex'] = automemberexclusiveregex
        if automemberinclusiveregex:
            _params['automemberinclusiveregex'] = automemberinclusiveregex
        
        return self._request(method, _args, _params)

    def automember_default_group_remove(
        self,
        opt_type,
        opt_all=True,
        raw=False,
        description=None,
    ):
        """
    Remove default (fallback) group for all unmatched entries.
    
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this auto member rule
        :type description: Str
        """
        method = 'automember_default_group_remove'
        
        _args = list()
        
        _params = dict()
        _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automember_default_group_set(
        self,
        automemberdefaultgroup,
        opt_type,
        opt_all=True,
        raw=False,
        description=None,
    ):
        """
    Set default (fallback) group for all unmatched entries.
    
        :param automemberdefaultgroup: Default (fallback) group for entries to land
        :type automemberdefaultgroup: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this auto member rule
        :type description: Str
        """
        method = 'automember_default_group_set'
        
        _args = list()
        
        _params = dict()
        _params['automemberdefaultgroup'] = automemberdefaultgroup
        _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automember_default_group_show(
        self,
        opt_type,
        opt_all=True,
        raw=False,
    ):
        """
    Display information about the default (fallback) automember groups.
    
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'automember_default_group_show'
        
        _args = list()
        
        _params = dict()
        _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def automember_del(
        self,
        cn,
        opt_type,
    ):
        """
    Delete an automember rule.
    
        :param cn: Automember Rule
        :type cn: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        """
        method = 'automember_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['type'] = opt_type
        
        return self._request(method, _args, _params)

    def automember_find(
        self,
        opt_type,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        description=None,
    ):
        """
    Search for automember rules.
    
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("automember-rule")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this auto member rule
        :type description: Str
        """
        method = 'automember_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        _params['type'] = opt_type
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automember_find_orphans(
        self,
        opt_type,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        remove=False,
        description=None,
    ):
        """
    Search for orphan automember rules. The command might need to be run as
    a privileged user user to get all orphan rules.
    
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("automember-rule")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param remove: Remove orphan automember rules
        :type remove: Flag
        :param description: A description of this auto member rule
        :type description: Str
        """
        method = 'automember_find_orphans'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        _params['type'] = opt_type
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if remove:
            _params['remove'] = remove
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automember_mod(
        self,
        cn,
        opt_type,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        description=None,
    ):
        """
    Modify an automember rule.
    
        :param cn: Automember Rule
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: A description of this auto member rule
        :type description: Str
        """
        method = 'automember_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automember_rebuild(
        self,
        hosts=None,
        users=None,
        opt_type=None,
        opt_all=True,
        no_wait=False,
        raw=False,
    ):
        """Rebuild auto membership.
        :param hosts: Rebuild membership for specified hosts
        :type hosts: Str
        :param users: Rebuild membership for specified users
        :type users: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_wait: Don't wait for rebuilding membership
        :type no_wait: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'automember_rebuild'
        
        _args = list()
        
        _params = dict()
        if hosts:
            _params['hosts'] = hosts
        if users:
            _params['users'] = users
        if opt_type:
            _params['type'] = opt_type
        _params['all'] = opt_all
        if no_wait:
            _params['no_wait'] = no_wait
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def automember_remove_condition(
        self,
        cn,
        key,
        opt_type,
        opt_all=True,
        raw=False,
        description=None,
        automemberexclusiveregex=None,
        automemberinclusiveregex=None,
    ):
        """
    Remove conditions from an automember rule.
    
        :param cn: Automember Rule
        :type cn: Str
        :param key: Attribute to filter via regex. For example fqdn for a host, or manager for a user
        :type key: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this auto member rule
        :type description: Str
        :param automemberexclusiveregex: Exclusive Regex
        :type automemberexclusiveregex: Str
        :param automemberinclusiveregex: Inclusive Regex
        :type automemberinclusiveregex: Str
        """
        method = 'automember_remove_condition'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['key'] = key
        _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if automemberexclusiveregex:
            _params['automemberexclusiveregex'] = automemberexclusiveregex
        if automemberinclusiveregex:
            _params['automemberinclusiveregex'] = automemberinclusiveregex
        
        return self._request(method, _args, _params)

    def automember_show(
        self,
        cn,
        opt_type,
        opt_all=True,
        raw=False,
    ):
        """
    Display information about an automember rule.
    
        :param cn: Automember Rule
        :type cn: Str
        :param opt_type: Grouping to which the rule applies
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'automember_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['type'] = opt_type
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def automountkey_add(
        self,
        automountmapautomountmapname,
        automountlocationcn,
        automountinformation,
        automountkey,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
    ):
        """Create a new automount key.
        :param automountmapautomountmapname: Automount map name.
        :type automountmapautomountmapname: IA5Str
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param automountinformation: Mount information
        :type automountinformation: IA5Str
        :param automountkey: Automount key name.
        :type automountkey: IA5Str
        """
        method = 'automountkey_add'
        
        _args = list()
        _args.append(automountmapautomountmapname)
        _args.append(automountlocationcn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['automountinformation'] = automountinformation
        _params['automountkey'] = automountkey
        
        return self._request(method, _args, _params)

    def automountkey_del(
        self,
        automountmapautomountmapname,
        automountlocationcn,
        automountkey,
        automountinformation=None,
        opt_continue=False,
    ):
        """Delete an automount key.
        :param automountmapautomountmapname: Automount map name.
        :type automountmapautomountmapname: IA5Str
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param automountinformation: Mount information
        :type automountinformation: IA5Str
        :param automountkey: Automount key name.
        :type automountkey: IA5Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'automountkey_del'
        
        _args = list()
        _args.append(automountmapautomountmapname)
        _args.append(automountlocationcn)
        
        _params = dict()
        if automountinformation:
            _params['automountinformation'] = automountinformation
        _params['automountkey'] = automountkey
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def automountkey_find(
        self,
        automountmapautomountmapname,
        automountlocationcn,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        raw=False,
        automountinformation=None,
        automountkey=None,
    ):
        """Search for an automount key.
        :param automountmapautomountmapname: Automount map name.
        :type automountmapautomountmapname: IA5Str
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param automountinformation: Mount information
        :type automountinformation: IA5Str
        :param automountkey: Automount key name.
        :type automountkey: IA5Str
        """
        method = 'automountkey_find'
        
        _args = list()
        _args.append(automountmapautomountmapname)
        _args.append(automountlocationcn)
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['raw'] = raw
        if automountinformation:
            _params['automountinformation'] = automountinformation
        if automountkey:
            _params['automountkey'] = automountkey
        
        return self._request(method, _args, _params)

    def automountkey_mod(
        self,
        automountmapautomountmapname,
        automountlocationcn,
        automountkey,
        newautomountinformation=None,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        automountinformation=None,
    ):
        """Modify an automount key.
        :param automountmapautomountmapname: Automount map name.
        :type automountmapautomountmapname: IA5Str
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param newautomountinformation: New mount information
        :type newautomountinformation: IA5Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the automount key object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param automountinformation: Mount information
        :type automountinformation: IA5Str
        :param automountkey: Automount key name.
        :type automountkey: IA5Str
        """
        method = 'automountkey_mod'
        
        _args = list()
        _args.append(automountmapautomountmapname)
        _args.append(automountlocationcn)
        
        _params = dict()
        if newautomountinformation:
            _params['newautomountinformation'] = newautomountinformation
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if automountinformation:
            _params['automountinformation'] = automountinformation
        _params['automountkey'] = automountkey
        
        return self._request(method, _args, _params)

    def automountkey_show(
        self,
        automountmapautomountmapname,
        automountlocationcn,
        automountkey,
        automountinformation=None,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display an automount key.
        :param automountmapautomountmapname: Automount map name.
        :type automountmapautomountmapname: IA5Str
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param automountinformation: Mount information
        :type automountinformation: IA5Str
        :param automountkey: Automount key name.
        :type automountkey: IA5Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'automountkey_show'
        
        _args = list()
        _args.append(automountmapautomountmapname)
        _args.append(automountlocationcn)
        
        _params = dict()
        if automountinformation:
            _params['automountinformation'] = automountinformation
        _params['automountkey'] = automountkey
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def automountlocation_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
    ):
        """Create a new automount location.
        :param cn: Automount location name.
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'automountlocation_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def automountlocation_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete an automount location.
        :param cn: Automount location name.
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'automountlocation_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def automountlocation_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        cn=None,
    ):
        """Search for an automount location.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("location")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param cn: Automount location name.
        :type cn: Str
        """
        method = 'automountlocation_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def automountlocation_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display an automount location.
        :param cn: Automount location name.
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'automountlocation_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def automountlocation_tofiles(
        self,
        cn,
    ):
        """Generate automount files for a specific location.
        :param cn: Automount location name.
        :type cn: Str
        """
        method = 'automountlocation_tofiles'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def automountmap_add(
        self,
        automountlocationcn,
        automountmapname,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        description=None,
    ):
        """Create a new automount map.
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param automountmapname: Automount map name.
        :type automountmapname: IA5Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Description
        :type description: Str
        """
        method = 'automountmap_add'
        
        _args = list()
        _args.append(automountlocationcn)
        _args.append(automountmapname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automountmap_add_indirect(
        self,
        automountlocationcn,
        automountmapname,
        key,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        parentmap='auto.master',
        description=None,
    ):
        """Create a new indirect mount point.
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param automountmapname: Automount map name.
        :type automountmapname: IA5Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param key: Mount point
        :type key: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param parentmap: Name of parent automount map (default: auto.master).
        :type parentmap: Str
        :param description: Description
        :type description: Str
        """
        method = 'automountmap_add_indirect'
        
        _args = list()
        _args.append(automountlocationcn)
        _args.append(automountmapname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        _params['key'] = key
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        if parentmap:
            _params['parentmap'] = parentmap
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automountmap_del(
        self,
        automountlocationcn,
        automountmapname,
        opt_continue=False,
    ):
        """Delete an automount map.
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param automountmapname: Automount map name.
        :type automountmapname: IA5Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'automountmap_del'
        
        _args = list()
        _args.append(automountlocationcn)
        _args.append(automountmapname)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def automountmap_find(
        self,
        automountlocationcn,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        automountmapname=None,
        description=None,
    ):
        """Search for an automount map.
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("map")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param automountmapname: Automount map name.
        :type automountmapname: IA5Str
        :param description: Description
        :type description: Str
        """
        method = 'automountmap_find'
        
        _args = list()
        _args.append(automountlocationcn)
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if automountmapname:
            _params['automountmapname'] = automountmapname
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automountmap_mod(
        self,
        automountlocationcn,
        automountmapname,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify an automount map.
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param automountmapname: Automount map name.
        :type automountmapname: IA5Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: Description
        :type description: Str
        """
        method = 'automountmap_mod'
        
        _args = list()
        _args.append(automountlocationcn)
        _args.append(automountmapname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def automountmap_show(
        self,
        automountlocationcn,
        automountmapname,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display an automount map.
        :param automountlocationcn: Automount location name.
        :type automountlocationcn: Str
        :param automountmapname: Automount map name.
        :type automountmapname: IA5Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'automountmap_show'
        
        _args = list()
        _args.append(automountlocationcn)
        _args.append(automountmapname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def batch(
        self,
        methods=None,
    ):
        """None
        :param methods: Nested Methods to execute
        :type methods: Dict
        """
        method = 'batch'
        
        _args = list()
        _args.append(methods)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def ca_add(
        self,
        cn,
        ipacasubjectdn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        chain=False,
        raw=False,
        description=None,
    ):
        """Create a CA.
        :param cn: Name for referencing the CA
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param chain: Include certificate chain in output
        :type chain: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipacasubjectdn: Subject Distinguished Name
        :type ipacasubjectdn: DNParam
        :param description: Description of the purpose of the CA
        :type description: Str
        """
        method = 'ca_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['chain'] = chain
        _params['raw'] = raw
        _params['ipacasubjectdn'] = ipacasubjectdn
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def ca_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a CA.
        :param cn: Name for referencing the CA
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'ca_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def ca_disable(
        self,
        cn,
    ):
        """Disable a CA.
        :param cn: Name for referencing the CA
        :type cn: Str
        """
        method = 'ca_disable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def ca_enable(
        self,
        cn,
    ):
        """Enable a CA.
        :param cn: Name for referencing the CA
        :type cn: Str
        """
        method = 'ca_enable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def ca_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        ipacaissuerdn=None,
        ipacasubjectdn=None,
        description=None,
        ipacaid=None,
        cn=None,
    ):
        """Search for CAs.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipacaissuerdn: Issuer Distinguished Name
        :type ipacaissuerdn: DNParam
        :param ipacasubjectdn: Subject Distinguished Name
        :type ipacasubjectdn: DNParam
        :param description: Description of the purpose of the CA
        :type description: Str
        :param ipacaid: Dogtag Authority ID
        :type ipacaid: Str
        :param cn: Name for referencing the CA
        :type cn: Str
        """
        method = 'ca_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipacaissuerdn:
            _params['ipacaissuerdn'] = ipacaissuerdn
        if ipacasubjectdn:
            _params['ipacasubjectdn'] = ipacasubjectdn
        if description:
            _params['description'] = description
        if ipacaid:
            _params['ipacaid'] = ipacaid
        if cn:
            _params['cn'] = cn
        
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
        cn,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify CA configuration.
        :param cn: Name for referencing the CA
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the Certificate Authority object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: Description of the purpose of the CA
        :type description: Str
        """
        method = 'ca_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def ca_show(
        self,
        cn,
        opt_all=True,
        chain=False,
        raw=False,
        rights=False,
    ):
        """Display the properties of a CA.
        :param cn: Name for referencing the CA
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param chain: Include certificate chain in output
        :type chain: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'ca_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['chain'] = chain
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def caacl_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        ipaenabledflag=None,
        description=None,
        ipacacategory=None,
        hostcategory=None,
        ipacertprofilecategory=None,
        servicecategory=None,
        usercategory=None,
    ):
        """Create a new CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param ipacacategory: CA category the ACL applies to
        :type ipacacategory: StrEnum
        :param hostcategory: Host category the ACL applies to
        :type hostcategory: StrEnum
        :param ipacertprofilecategory: Profile category the ACL applies to
        :type ipacertprofilecategory: StrEnum
        :param servicecategory: Service category the ACL applies to
        :type servicecategory: StrEnum
        :param usercategory: User category the ACL applies to
        :type usercategory: StrEnum
        """
        method = 'caacl_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if ipacacategory:
            _params['ipacacategory'] = ipacacategory
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if ipacertprofilecategory:
            _params['ipacertprofilecategory'] = ipacertprofilecategory
        if servicecategory:
            _params['servicecategory'] = servicecategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def caacl_add_ca(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        ca=None,
    ):
        """Add CAs to a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ca: Certificate Authorities to add
        :type ca: Str
        """
        method = 'caacl_add_ca'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if ca:
            _params['ca'] = ca
        
        return self._request(method, _args, _params)

    def caacl_add_host(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Add target hosts and hostgroups to a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        """
        method = 'caacl_add_host'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def caacl_add_profile(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        certprofile=None,
    ):
        """Add profiles to a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param certprofile: Certificate Profiles to add
        :type certprofile: Str
        """
        method = 'caacl_add_profile'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if certprofile:
            _params['certprofile'] = certprofile
        
        return self._request(method, _args, _params)

    def caacl_add_service(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        service=None,
    ):
        """Add services to a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param service: services to add
        :type service: Str
        """
        method = 'caacl_add_service'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if service:
            _params['service'] = service
        
        return self._request(method, _args, _params)

    def caacl_add_user(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Add users and groups to a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param user: users to add
        :type user: Str
        """
        method = 'caacl_add_user'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def caacl_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'caacl_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def caacl_disable(
        self,
        cn,
    ):
        """Disable a CA ACL.
        :param cn: ACL name
        :type cn: Str
        """
        method = 'caacl_disable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def caacl_enable(
        self,
        cn,
    ):
        """Enable a CA ACL.
        :param cn: ACL name
        :type cn: Str
        """
        method = 'caacl_enable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def caacl_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        ipaenabledflag=None,
        description=None,
        cn=None,
        ipacacategory=None,
        hostcategory=None,
        ipacertprofilecategory=None,
        servicecategory=None,
        usercategory=None,
    ):
        """Search for CA ACLs.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param cn: ACL name
        :type cn: Str
        :param ipacacategory: CA category the ACL applies to
        :type ipacacategory: StrEnum
        :param hostcategory: Host category the ACL applies to
        :type hostcategory: StrEnum
        :param ipacertprofilecategory: Profile category the ACL applies to
        :type ipacertprofilecategory: StrEnum
        :param servicecategory: Service category the ACL applies to
        :type servicecategory: StrEnum
        :param usercategory: User category the ACL applies to
        :type usercategory: StrEnum
        """
        method = 'caacl_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        if ipacacategory:
            _params['ipacacategory'] = ipacacategory
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if ipacertprofilecategory:
            _params['ipacertprofilecategory'] = ipacertprofilecategory
        if servicecategory:
            _params['servicecategory'] = servicecategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def caacl_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        ipaenabledflag=None,
        description=None,
        ipacacategory=None,
        hostcategory=None,
        ipacertprofilecategory=None,
        servicecategory=None,
        usercategory=None,
    ):
        """Modify a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param ipacacategory: CA category the ACL applies to
        :type ipacacategory: StrEnum
        :param hostcategory: Host category the ACL applies to
        :type hostcategory: StrEnum
        :param ipacertprofilecategory: Profile category the ACL applies to
        :type ipacertprofilecategory: StrEnum
        :param servicecategory: Service category the ACL applies to
        :type servicecategory: StrEnum
        :param usercategory: User category the ACL applies to
        :type usercategory: StrEnum
        """
        method = 'caacl_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if ipacacategory:
            _params['ipacacategory'] = ipacacategory
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if ipacertprofilecategory:
            _params['ipacertprofilecategory'] = ipacertprofilecategory
        if servicecategory:
            _params['servicecategory'] = servicecategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def caacl_remove_ca(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        ca=None,
    ):
        """Remove CAs from a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ca: Certificate Authorities to remove
        :type ca: Str
        """
        method = 'caacl_remove_ca'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if ca:
            _params['ca'] = ca
        
        return self._request(method, _args, _params)

    def caacl_remove_host(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Remove target hosts and hostgroups from a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        """
        method = 'caacl_remove_host'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def caacl_remove_profile(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        certprofile=None,
    ):
        """Remove profiles from a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param certprofile: Certificate Profiles to remove
        :type certprofile: Str
        """
        method = 'caacl_remove_profile'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if certprofile:
            _params['certprofile'] = certprofile
        
        return self._request(method, _args, _params)

    def caacl_remove_service(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        service=None,
    ):
        """Remove services from a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param service: services to remove
        :type service: Str
        """
        method = 'caacl_remove_service'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if service:
            _params['service'] = service
        
        return self._request(method, _args, _params)

    def caacl_remove_user(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Remove users and groups from a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'caacl_remove_user'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def caacl_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display the properties of a CA ACL.
        :param cn: ACL name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'caacl_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def cert_find(
        self,
        criteria=None,
        issuedon_from=None,
        issuedon_to=None,
        revokedon_from=None,
        revokedon_to=None,
        validnotafter_from=None,
        validnotafter_to=None,
        validnotbefore_from=None,
        validnotbefore_to=None,
        max_serial_number=None,
        min_serial_number=None,
        sizelimit=None,
        timelimit=None,
        no_service=None,
        service=None,
        cacn=None,
        host=None,
        no_host=None,
        no_user=None,
        subject=None,
        user=None,
        opt_all=True,
        exactly=False,
        no_members=True,
        pkey_only=False,
        raw=False,
        certificate=None,
        issuer=None,
        revocation_reason=None,
    ):
        """Search for existing certificates.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param issuedon_from: Issued on from this date (YYYY-mm-dd)
        :type issuedon_from: DateTime
        :param issuedon_to: Issued on to this date (YYYY-mm-dd)
        :type issuedon_to: DateTime
        :param revokedon_from: Revoked on from this date (YYYY-mm-dd)
        :type revokedon_from: DateTime
        :param revokedon_to: Revoked on to this date (YYYY-mm-dd)
        :type revokedon_to: DateTime
        :param validnotafter_from: Valid not after from this date (YYYY-mm-dd)
        :type validnotafter_from: DateTime
        :param validnotafter_to: Valid not after to this date (YYYY-mm-dd)
        :type validnotafter_to: DateTime
        :param validnotbefore_from: Valid not before from this date (YYYY-mm-dd)
        :type validnotbefore_from: DateTime
        :param validnotbefore_to: Valid not before to this date (YYYY-mm-dd)
        :type validnotbefore_to: DateTime
        :param max_serial_number: maximum serial number
        :type max_serial_number: Int
        :param min_serial_number: minimum serial number
        :type min_serial_number: Int
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param no_service: Search for certificates without these owner services.
        :type no_service: Principal
        :param service: Search for certificates with these owner services.
        :type service: Principal
        :param cacn: Name of issuing CA
        :type cacn: Str
        :param host: Search for certificates with these owner hosts.
        :type host: Str
        :param no_host: Search for certificates without these owner hosts.
        :type no_host: Str
        :param no_user: Search for certificates without these owner users.
        :type no_user: Str
        :param subject: Subject
        :type subject: Str
        :param user: Search for certificates with these owner users.
        :type user: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param exactly: match the common name exactly
        :type exactly: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("certificate")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param certificate: Base-64 encoded certificate.
        :type certificate: Certificate
        :param issuer: Issuer DN
        :type issuer: DNParam
        :param revocation_reason: Reason for revoking the certificate (0-10). Type "ipa help cert" for revocation reason details. 
        :type revocation_reason: Int
        """
        method = 'cert_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if issuedon_from:
            _params['issuedon_from'] = issuedon_from
        if issuedon_to:
            _params['issuedon_to'] = issuedon_to
        if revokedon_from:
            _params['revokedon_from'] = revokedon_from
        if revokedon_to:
            _params['revokedon_to'] = revokedon_to
        if validnotafter_from:
            _params['validnotafter_from'] = validnotafter_from
        if validnotafter_to:
            _params['validnotafter_to'] = validnotafter_to
        if validnotbefore_from:
            _params['validnotbefore_from'] = validnotbefore_from
        if validnotbefore_to:
            _params['validnotbefore_to'] = validnotbefore_to
        if max_serial_number:
            _params['max_serial_number'] = max_serial_number
        if min_serial_number:
            _params['min_serial_number'] = min_serial_number
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if no_service:
            _params['no_service'] = no_service
        if service:
            _params['service'] = service
        if cacn:
            _params['cacn'] = cacn
        if host:
            _params['host'] = host
        if no_host:
            _params['no_host'] = no_host
        if no_user:
            _params['no_user'] = no_user
        if subject:
            _params['subject'] = subject
        if user:
            _params['user'] = user
        _params['all'] = opt_all
        if exactly:
            _params['exactly'] = exactly
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if certificate:
            _params['certificate'] = certificate
        if issuer:
            _params['issuer'] = issuer
        if revocation_reason:
            _params['revocation_reason'] = revocation_reason
        
        return self._request(method, _args, _params)

    def cert_remove_hold(
        self,
        serial_number,
        cacn='ipa',
    ):
        """Take a revoked certificate off hold.
        :param serial_number: Serial number in decimal or if prefixed with 0x in hexadecimal
        :type serial_number: Int
        :param cacn: Name of issuing CA
        :type cacn: Str
        """
        method = 'cert_remove_hold'
        
        _args = list()
        _args.append(serial_number)
        
        _params = dict()
        if cacn:
            _params['cacn'] = cacn
        
        return self._request(method, _args, _params)

    def cert_request(
        self,
        csr,
        principal,
        add=False,
        opt_all=True,
        chain=False,
        raw=False,
        cacn='ipa',
        profile_id=None,
        request_type='pkcs10',
    ):
        """Submit a certificate signing request.
        :param csr: CSR
        :type csr: CertificateSigningRequest
        :param principal: Principal for this certificate (e.g. HTTP/test.example.com)
        :type principal: Principal
        :param add: automatically add the principal if it doesn't exist (service principals only)
        :type add: Flag
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param chain: Include certificate chain in output
        :type chain: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param cacn: Name of issuing CA
        :type cacn: Str
        :param profile_id: Certificate Profile to use
        :type profile_id: Str
        :param request_type: <request_type>
        :type request_type: Str
        """
        method = 'cert_request'
        
        _args = list()
        _args.append(csr)
        
        _params = dict()
        _params['principal'] = principal
        _params['add'] = add
        _params['all'] = opt_all
        _params['chain'] = chain
        _params['raw'] = raw
        if cacn:
            _params['cacn'] = cacn
        if profile_id:
            _params['profile_id'] = profile_id
        _params['request_type'] = request_type
        
        return self._request(method, _args, _params)

    def cert_revoke(
        self,
        serial_number,
        revocation_reason=0,
        cacn='ipa',
    ):
        """Revoke a certificate.
        :param serial_number: Serial number in decimal or if prefixed with 0x in hexadecimal
        :type serial_number: Int
        :param revocation_reason: Reason for revoking the certificate (0-10). Type "ipa help cert" for revocation reason details. 
        :type revocation_reason: Int
        :param cacn: Name of issuing CA
        :type cacn: Str
        """
        method = 'cert_revoke'
        
        _args = list()
        _args.append(serial_number)
        
        _params = dict()
        _params['revocation_reason'] = revocation_reason
        if cacn:
            _params['cacn'] = cacn
        
        return self._request(method, _args, _params)

    def cert_show(
        self,
        serial_number,
        out=None,
        opt_all=True,
        chain=False,
        no_members=False,
        raw=False,
        cacn='ipa',
    ):
        """Retrieve an existing certificate.
        :param serial_number: Serial number in decimal or if prefixed with 0x in hexadecimal
        :type serial_number: Int
        :param out: File to store the certificate in.
        :type out: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param chain: Include certificate chain in output
        :type chain: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param cacn: Name of issuing CA
        :type cacn: Str
        """
        method = 'cert_show'
        
        _args = list()
        _args.append(serial_number)
        
        _params = dict()
        if out:
            _params['out'] = out
        _params['all'] = opt_all
        _params['chain'] = chain
        _params['no_members'] = no_members
        _params['raw'] = raw
        if cacn:
            _params['cacn'] = cacn
        
        return self._request(method, _args, _params)

    def cert_status(
        self,
        request_id,
        opt_all=True,
        raw=False,
        cacn='ipa',
    ):
        """Check the status of a certificate signing request.
        :param request_id: Request id
        :type request_id: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param cacn: Name of issuing CA
        :type cacn: Str
        """
        method = 'cert_status'
        
        _args = list()
        _args.append(request_id)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        if cacn:
            _params['cacn'] = cacn
        
        return self._request(method, _args, _params)

    def certmap_match(
        self,
        certificate,
        opt_all=True,
        raw=False,
    ):
        """
    Search for users matching the provided certificate.

    This command relies on SSSD to retrieve the list of matching users and
    may return cached data. For more information on purging SSSD cache,
    please refer to sss_cache documentation.
    
        :param certificate: Base-64 encoded user certificate
        :type certificate: Certificate
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'certmap_match'
        
        _args = list()
        _args.append(certificate)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def certmapconfig_mod(
        self,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        ipacertmappromptusername=None,
    ):
        """Modify Certificate Identity Mapping configuration.
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipacertmappromptusername: Prompt for the username when multiple identities are mapped to a certificate
        :type ipacertmappromptusername: Bool
        """
        method = 'certmapconfig_mod'
        
        _args = list()
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if ipacertmappromptusername:
            _params['ipacertmappromptusername'] = ipacertmappromptusername
        
        return self._request(method, _args, _params)

    def certmapconfig_show(
        self,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Show the current Certificate Identity Mapping configuration.
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'certmapconfig_show'
        
        _args = list()
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def certmaprule_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        associateddomain=None,
        ipacertmappriority=None,
        description=None,
        ipacertmapmaprule=None,
        ipacertmapmatchrule=None,
        ipaenabledflag=True,
    ):
        """Create a new Certificate Identity Mapping Rule.
        :param cn: Certificate Identity Mapping Rule name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param associateddomain: Domain where the user entry will be searched
        :type associateddomain: DNSNameParam
        :param ipacertmappriority: Priority of the rule (higher number means lower priority
        :type ipacertmappriority: Int
        :param description: Certificate Identity Mapping Rule description
        :type description: Str
        :param ipacertmapmaprule: Rule used to map the certificate with a user entry
        :type ipacertmapmaprule: Str
        :param ipacertmapmatchrule: Rule used to check if a certificate can be used for authentication
        :type ipacertmapmatchrule: Str
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Flag
        """
        method = 'certmaprule_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        if associateddomain:
            _params['associateddomain'] = associateddomain
        if ipacertmappriority:
            _params['ipacertmappriority'] = ipacertmappriority
        if description:
            _params['description'] = description
        if ipacertmapmaprule:
            _params['ipacertmapmaprule'] = ipacertmapmaprule
        if ipacertmapmatchrule:
            _params['ipacertmapmatchrule'] = ipacertmapmatchrule
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        
        return self._request(method, _args, _params)

    def certmaprule_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a Certificate Identity Mapping Rule.
        :param cn: Certificate Identity Mapping Rule name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'certmaprule_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def certmaprule_disable(
        self,
        cn,
    ):
        """Disable a Certificate Identity Mapping Rule.
        :param cn: Certificate Identity Mapping Rule name
        :type cn: Str
        """
        method = 'certmaprule_disable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def certmaprule_enable(
        self,
        cn,
    ):
        """Enable a Certificate Identity Mapping Rule.
        :param cn: Certificate Identity Mapping Rule name
        :type cn: Str
        """
        method = 'certmaprule_enable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def certmaprule_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        ipaenabledflag=True,
        associateddomain=None,
        ipacertmappriority=None,
        description=None,
        ipacertmapmaprule=None,
        ipacertmapmatchrule=None,
        cn=None,
    ):
        """Search for Certificate Identity Mapping Rules.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("rulename")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param associateddomain: Domain where the user entry will be searched
        :type associateddomain: DNSNameParam
        :param ipacertmappriority: Priority of the rule (higher number means lower priority
        :type ipacertmappriority: Int
        :param description: Certificate Identity Mapping Rule description
        :type description: Str
        :param ipacertmapmaprule: Rule used to map the certificate with a user entry
        :type ipacertmapmaprule: Str
        :param ipacertmapmatchrule: Rule used to check if a certificate can be used for authentication
        :type ipacertmapmatchrule: Str
        :param cn: Certificate Identity Mapping Rule name
        :type cn: Str
        """
        method = 'certmaprule_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if associateddomain:
            _params['associateddomain'] = associateddomain
        if ipacertmappriority:
            _params['ipacertmappriority'] = ipacertmappriority
        if description:
            _params['description'] = description
        if ipacertmapmaprule:
            _params['ipacertmapmaprule'] = ipacertmapmaprule
        if ipacertmapmatchrule:
            _params['ipacertmapmatchrule'] = ipacertmapmatchrule
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def certmaprule_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        associateddomain=None,
        ipacertmappriority=None,
        description=None,
        ipacertmapmaprule=None,
        ipacertmapmatchrule=None,
        ipaenabledflag=True,
    ):
        """Modify a Certificate Identity Mapping Rule.
        :param cn: Certificate Identity Mapping Rule name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param associateddomain: Domain where the user entry will be searched
        :type associateddomain: DNSNameParam
        :param ipacertmappriority: Priority of the rule (higher number means lower priority
        :type ipacertmappriority: Int
        :param description: Certificate Identity Mapping Rule description
        :type description: Str
        :param ipacertmapmaprule: Rule used to map the certificate with a user entry
        :type ipacertmapmaprule: Str
        :param ipacertmapmatchrule: Rule used to check if a certificate can be used for authentication
        :type ipacertmapmatchrule: Str
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Flag
        """
        method = 'certmaprule_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if associateddomain:
            _params['associateddomain'] = associateddomain
        if ipacertmappriority:
            _params['ipacertmappriority'] = ipacertmappriority
        if description:
            _params['description'] = description
        if ipacertmapmaprule:
            _params['ipacertmapmaprule'] = ipacertmapmaprule
        if ipacertmapmatchrule:
            _params['ipacertmapmatchrule'] = ipacertmapmatchrule
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        
        return self._request(method, _args, _params)

    def certmaprule_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about a Certificate Identity Mapping Rule.
        :param cn: Certificate Identity Mapping Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'certmaprule_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def certprofile_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a Certificate Profile.
        :param cn: Profile ID for referring to this profile
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'certprofile_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def certprofile_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        ipacertprofilestoreissued=True,
        description=None,
        cn=None,
    ):
        """Search for Certificate Profiles.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("id")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipacertprofilestoreissued: Whether to store certs issued using this profile
        :type ipacertprofilestoreissued: Bool
        :param description: Brief description of this profile
        :type description: Str
        :param cn: Profile ID for referring to this profile
        :type cn: Str
        """
        method = 'certprofile_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipacertprofilestoreissued:
            _params['ipacertprofilestoreissued'] = ipacertprofilestoreissued
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def certprofile_import(
        self,
        cn,
        file,
        description,
        opt_all=True,
        raw=False,
        ipacertprofilestoreissued=True,
    ):
        """Import a Certificate Profile.
        :param cn: Profile ID for referring to this profile
        :type cn: Str
        :param file: Filename of a raw profile. The XML format is not supported.
        :type file: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipacertprofilestoreissued: Whether to store certs issued using this profile
        :type ipacertprofilestoreissued: Bool
        :param description: Brief description of this profile
        :type description: Str
        """
        method = 'certprofile_import'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['file'] = file
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['ipacertprofilestoreissued'] = ipacertprofilestoreissued
        _params['description'] = description
        
        return self._request(method, _args, _params)

    def certprofile_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        file=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        ipacertprofilestoreissued=True,
        description=None,
    ):
        """Modify Certificate Profile configuration.
        :param cn: Profile ID for referring to this profile
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param file: File containing profile configuration
        :type file: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipacertprofilestoreissued: Whether to store certs issued using this profile
        :type ipacertprofilestoreissued: Bool
        :param description: Brief description of this profile
        :type description: Str
        """
        method = 'certprofile_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if file:
            _params['file'] = file
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if ipacertprofilestoreissued:
            _params['ipacertprofilestoreissued'] = ipacertprofilestoreissued
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def certprofile_show(
        self,
        cn,
        out=None,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display the properties of a Certificate Profile.
        :param cn: Profile ID for referring to this profile
        :type cn: Str
        :param out: Write profile configuration to file
        :type out: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'certprofile_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if out:
            _params['out'] = out
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def class_find(
        self,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
    ):
        """Search for classes.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'class_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def class_show(
        self,
        full_name,
        opt_all=True,
        raw=False,
    ):
        """Display information about a class.
        :param full_name: Full name
        :type full_name: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'class_show'
        
        _args = list()
        _args.append(full_name)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def command_defaults(
        self,
        full_name,
        kw=None,
        params=None,
    ):
        """None
        :param full_name: Full name
        :type full_name: Str
        :param kw: <kw>
        :type kw: Dict
        :param params: <params>
        :type params: Str
        """
        method = 'command_defaults'
        
        _args = list()
        _args.append(full_name)
        
        _params = dict()
        if kw:
            _params['kw'] = kw
        if params:
            _params['params'] = params
        
        return self._request(method, _args, _params)

    def command_find(
        self,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
    ):
        """Search for commands.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'command_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def command_show(
        self,
        full_name,
        opt_all=True,
        raw=False,
    ):
        """Display information about a command.
        :param full_name: Full name
        :type full_name: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'command_show'
        
        _args = list()
        _args.append(full_name)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
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
        addattr=None,
        ca_renewal_master_server=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        ipamigrationenabled=None,
        ipagroupsearchfields=None,
        ipahomesrootdir=None,
        ipausersearchfields=None,
        ipamaxusernamelength=None,
        ipapwdexpadvnotify=None,
        ipasearchrecordslimit=None,
        ipasearchtimelimit=None,
        ipadefaultprimarygroup=None,
        ipadefaultloginshell=None,
        ipadomainresolutionorder=None,
        ipadefaultemaildomain=None,
        ipagroupobjectclasses=None,
        ipaselinuxusermapdefault=None,
        ipaselinuxusermaporder=None,
        ipauserobjectclasses=None,
        ipaconfigstring=None,
        ipakrbauthzdata=None,
        ipauserauthtype=None,
    ):
        """Modify configuration options.
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param ca_renewal_master_server: Renewal master for IPA certificate authority
        :type ca_renewal_master_server: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipamigrationenabled: Enable migration mode
        :type ipamigrationenabled: Bool
        :param ipagroupsearchfields: A comma-separated list of fields to search in when searching for groups
        :type ipagroupsearchfields: IA5Str
        :param ipahomesrootdir: Default location of home directories
        :type ipahomesrootdir: IA5Str
        :param ipausersearchfields: A comma-separated list of fields to search in when searching for users
        :type ipausersearchfields: IA5Str
        :param ipamaxusernamelength: Maximum username length
        :type ipamaxusernamelength: Int
        :param ipapwdexpadvnotify: Number of days's notice of impending password expiration
        :type ipapwdexpadvnotify: Int
        :param ipasearchrecordslimit: Maximum number of records to search (-1 or 0 is unlimited)
        :type ipasearchrecordslimit: Int
        :param ipasearchtimelimit: Maximum amount of time (seconds) for a search (-1 or 0 is unlimited)
        :type ipasearchtimelimit: Int
        :param ipadefaultprimarygroup: Default group for new users
        :type ipadefaultprimarygroup: Str
        :param ipadefaultloginshell: Default shell for new users
        :type ipadefaultloginshell: Str
        :param ipadomainresolutionorder: colon-separated list of domains used for short name qualification
        :type ipadomainresolutionorder: Str
        :param ipadefaultemaildomain: Default e-mail domain
        :type ipadefaultemaildomain: Str
        :param ipagroupobjectclasses: Default group objectclasses (comma-separated list)
        :type ipagroupobjectclasses: Str
        :param ipaselinuxusermapdefault: Default SELinux user when no match is found in SELinux map rule
        :type ipaselinuxusermapdefault: Str
        :param ipaselinuxusermaporder: Order in increasing priority of SELinux users, delimited by $
        :type ipaselinuxusermaporder: Str
        :param ipauserobjectclasses: Default user objectclasses (comma-separated list)
        :type ipauserobjectclasses: Str
        :param ipaconfigstring: Extra hashes to generate in password plug-in
        :type ipaconfigstring: StrEnum
        :param ipakrbauthzdata: Default types of PAC supported for services
        :type ipakrbauthzdata: StrEnum
        :param ipauserauthtype: Default types of supported user authentication
        :type ipauserauthtype: StrEnum
        """
        method = 'config_mod'
        
        _args = list()
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if ca_renewal_master_server:
            _params['ca_renewal_master_server'] = ca_renewal_master_server
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if ipamigrationenabled:
            _params['ipamigrationenabled'] = ipamigrationenabled
        if ipagroupsearchfields:
            _params['ipagroupsearchfields'] = ipagroupsearchfields
        if ipahomesrootdir:
            _params['ipahomesrootdir'] = ipahomesrootdir
        if ipausersearchfields:
            _params['ipausersearchfields'] = ipausersearchfields
        if ipamaxusernamelength:
            _params['ipamaxusernamelength'] = ipamaxusernamelength
        if ipapwdexpadvnotify:
            _params['ipapwdexpadvnotify'] = ipapwdexpadvnotify
        if ipasearchrecordslimit:
            _params['ipasearchrecordslimit'] = ipasearchrecordslimit
        if ipasearchtimelimit:
            _params['ipasearchtimelimit'] = ipasearchtimelimit
        if ipadefaultprimarygroup:
            _params['ipadefaultprimarygroup'] = ipadefaultprimarygroup
        if ipadefaultloginshell:
            _params['ipadefaultloginshell'] = ipadefaultloginshell
        if ipadomainresolutionorder:
            _params['ipadomainresolutionorder'] = ipadomainresolutionorder
        if ipadefaultemaildomain:
            _params['ipadefaultemaildomain'] = ipadefaultemaildomain
        if ipagroupobjectclasses:
            _params['ipagroupobjectclasses'] = ipagroupobjectclasses
        if ipaselinuxusermapdefault:
            _params['ipaselinuxusermapdefault'] = ipaselinuxusermapdefault
        if ipaselinuxusermaporder:
            _params['ipaselinuxusermaporder'] = ipaselinuxusermaporder
        if ipauserobjectclasses:
            _params['ipauserobjectclasses'] = ipauserobjectclasses
        if ipaconfigstring:
            _params['ipaconfigstring'] = ipaconfigstring
        if ipakrbauthzdata:
            _params['ipakrbauthzdata'] = ipakrbauthzdata
        if ipauserauthtype:
            _params['ipauserauthtype'] = ipauserauthtype
        
        return self._request(method, _args, _params)

    def config_show(
        self,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Show the current configuration.
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'config_show'
        
        _args = list()
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def cosentry_add(
        self,
        cn,
        krbpwdpolicyreference,
        cospriority,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
    ):
        """None
        :param cn: <cn>
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param krbpwdpolicyreference: <krbpwdpolicyreference>
        :type krbpwdpolicyreference: DNParam
        :param cospriority: <cospriority>
        :type cospriority: Int
        """
        method = 'cosentry_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['krbpwdpolicyreference'] = krbpwdpolicyreference
        _params['cospriority'] = cospriority
        
        return self._request(method, _args, _params)

    def cosentry_del(
        self,
        cn,
        opt_continue=False,
    ):
        """None
        :param cn: <cn>
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'cosentry_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def cosentry_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        krbpwdpolicyreference=None,
        cospriority=None,
        cn=None,
    ):
        """None
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("cn")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param krbpwdpolicyreference: <krbpwdpolicyreference>
        :type krbpwdpolicyreference: DNParam
        :param cospriority: <cospriority>
        :type cospriority: Int
        :param cn: <cn>
        :type cn: Str
        """
        method = 'cosentry_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if krbpwdpolicyreference:
            _params['krbpwdpolicyreference'] = krbpwdpolicyreference
        if cospriority:
            _params['cospriority'] = cospriority
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def cosentry_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        krbpwdpolicyreference=None,
        cospriority=None,
    ):
        """None
        :param cn: <cn>
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param krbpwdpolicyreference: <krbpwdpolicyreference>
        :type krbpwdpolicyreference: DNParam
        :param cospriority: <cospriority>
        :type cospriority: Int
        """
        method = 'cosentry_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if krbpwdpolicyreference:
            _params['krbpwdpolicyreference'] = krbpwdpolicyreference
        if cospriority:
            _params['cospriority'] = cospriority
        
        return self._request(method, _args, _params)

    def cosentry_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """None
        :param cn: <cn>
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'cosentry_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def delegation_add(
        self,
        aciname,
        attrs,
        group,
        memberof,
        opt_all=True,
        raw=False,
        permissions=None,
    ):
        """Add a new delegation.
        :param aciname: Delegation name
        :type aciname: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param attrs: Attributes to which the delegation applies
        :type attrs: Str
        :param group: User group ACI grants access to
        :type group: Str
        :param memberof: User group to apply delegation to
        :type memberof: Str
        :param permissions: Permissions to grant (read, write). Default is write.
        :type permissions: Str
        """
        method = 'delegation_add'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['attrs'] = attrs
        _params['group'] = group
        _params['memberof'] = memberof
        if permissions:
            _params['permissions'] = permissions
        
        return self._request(method, _args, _params)

    def delegation_del(
        self,
        aciname,
    ):
        """Delete a delegation.
        :param aciname: Delegation name
        :type aciname: Str
        """
        method = 'delegation_del'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def delegation_find(
        self,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        attrs=None,
        group=None,
        memberof=None,
        aciname=None,
        permissions=None,
    ):
        """Search for delegations.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param attrs: Attributes to which the delegation applies
        :type attrs: Str
        :param group: User group ACI grants access to
        :type group: Str
        :param memberof: User group to apply delegation to
        :type memberof: Str
        :param aciname: Delegation name
        :type aciname: Str
        :param permissions: Permissions to grant (read, write). Default is write.
        :type permissions: Str
        """
        method = 'delegation_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if attrs:
            _params['attrs'] = attrs
        if group:
            _params['group'] = group
        if memberof:
            _params['memberof'] = memberof
        if aciname:
            _params['aciname'] = aciname
        if permissions:
            _params['permissions'] = permissions
        
        return self._request(method, _args, _params)

    def delegation_mod(
        self,
        aciname,
        opt_all=True,
        raw=False,
        attrs=None,
        group=None,
        memberof=None,
        permissions=None,
    ):
        """Modify a delegation.
        :param aciname: Delegation name
        :type aciname: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param attrs: Attributes to which the delegation applies
        :type attrs: Str
        :param group: User group ACI grants access to
        :type group: Str
        :param memberof: User group to apply delegation to
        :type memberof: Str
        :param permissions: Permissions to grant (read, write). Default is write.
        :type permissions: Str
        """
        method = 'delegation_mod'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        if attrs:
            _params['attrs'] = attrs
        if group:
            _params['group'] = group
        if memberof:
            _params['memberof'] = memberof
        if permissions:
            _params['permissions'] = permissions
        
        return self._request(method, _args, _params)

    def delegation_show(
        self,
        aciname,
        opt_all=True,
        raw=False,
    ):
        """Display information about a delegation.
        :param aciname: Delegation name
        :type aciname: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'delegation_show'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
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
        hostname,
    ):
        """Resolve a host name in DNS. (Deprecated)
        :param hostname: Hostname (FQDN)
        :type hostname: Str
        """
        method = 'dns_resolve'
        
        _args = list()
        _args.append(hostname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dns_update_system_records(
        self,
        opt_all=True,
        dry_run=False,
        raw=False,
    ):
        """Update location and IPA server DNS records
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param dry_run: Do not update records only return expected records
        :type dry_run: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'dns_update_system_records'
        
        _args = list()
        
        _params = dict()
        _params['all'] = opt_all
        _params['dry_run'] = dry_run
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def dnsconfig_mod(
        self,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        idnsallowsyncptr=None,
        ipadnsversion=None,
        idnszonerefresh=None,
        idnsforwarders=None,
        idnsforwardpolicy=None,
    ):
        """Modify global DNS configuration.
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param idnsallowsyncptr: Allow synchronization of forward (A, AAAA) and reverse (PTR) records
        :type idnsallowsyncptr: Bool
        :param ipadnsversion: IPA DNS version
        :type ipadnsversion: Int
        :param idnszonerefresh: An interval between regular polls of the name server for new DNS zones
        :type idnszonerefresh: Int
        :param idnsforwarders: Global forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param idnsforwardpolicy: Global forwarding policy. Set to "none" to disable any configured global forwarders.
        :type idnsforwardpolicy: StrEnum
        """
        method = 'dnsconfig_mod'
        
        _args = list()
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if idnsallowsyncptr:
            _params['idnsallowsyncptr'] = idnsallowsyncptr
        if ipadnsversion:
            _params['ipadnsversion'] = ipadnsversion
        if idnszonerefresh:
            _params['idnszonerefresh'] = idnszonerefresh
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        
        return self._request(method, _args, _params)

    def dnsconfig_show(
        self,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Show the current global DNS configuration.
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'dnsconfig_show'
        
        _args = list()
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def dnsforwardzone_add(
        self,
        idnsname,
        addattr=None,
        name_from_ip=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        skip_overlap_check=False,
        idnsforwarders=None,
        idnsforwardpolicy=None,
    ):
        """Create new DNS forward zone.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param name_from_ip: IP network to create reverse zone name from
        :type name_from_ip: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param skip_overlap_check: Force DNS zone creation even if it will overlap with an existing zone.
        :type skip_overlap_check: Flag
        :param idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type idnsforwardpolicy: StrEnum
        """
        method = 'dnsforwardzone_add'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if name_from_ip:
            _params['name_from_ip'] = name_from_ip
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['skip_overlap_check'] = skip_overlap_check
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        
        return self._request(method, _args, _params)

    def dnsforwardzone_add_permission(
        self,
        idnsname,
    ):
        """Add a permission for per-forward zone access delegation.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        """
        method = 'dnsforwardzone_add_permission'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnsforwardzone_del(
        self,
        idnsname,
        opt_continue=False,
    ):
        """Delete DNS forward zone.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'dnsforwardzone_del'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def dnsforwardzone_disable(
        self,
        idnsname,
    ):
        """Disable DNS Forward Zone.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        """
        method = 'dnsforwardzone_disable'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnsforwardzone_enable(
        self,
        idnsname,
    ):
        """Enable DNS Forward Zone.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        """
        method = 'dnsforwardzone_enable'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnsforwardzone_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        name_from_ip=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        idnszoneactive=None,
        idnsname=None,
        idnsforwarders=None,
        idnsforwardpolicy=None,
    ):
        """Search for DNS forward zones.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param name_from_ip: IP network to create reverse zone name from
        :type name_from_ip: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param idnszoneactive: Is zone active?
        :type idnszoneactive: Bool
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type idnsforwardpolicy: StrEnum
        """
        method = 'dnsforwardzone_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if name_from_ip:
            _params['name_from_ip'] = name_from_ip
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if idnszoneactive:
            _params['idnszoneactive'] = idnszoneactive
        if idnsname:
            _params['idnsname'] = idnsname
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        
        return self._request(method, _args, _params)

    def dnsforwardzone_mod(
        self,
        idnsname,
        addattr=None,
        opt_delattr=None,
        name_from_ip=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        idnsforwarders=None,
        idnsforwardpolicy=None,
    ):
        """Modify DNS forward zone.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param name_from_ip: IP network to create reverse zone name from
        :type name_from_ip: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type idnsforwardpolicy: StrEnum
        """
        method = 'dnsforwardzone_mod'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if name_from_ip:
            _params['name_from_ip'] = name_from_ip
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        
        return self._request(method, _args, _params)

    def dnsforwardzone_remove_permission(
        self,
        idnsname,
    ):
        """Remove a permission for per-forward zone access delegation.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        """
        method = 'dnsforwardzone_remove_permission'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnsforwardzone_show(
        self,
        idnsname,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about a DNS forward zone.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'dnsforwardzone_show'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def dnsrecord_add(
        self,
        dnszoneidnsname,
        idnsname,
        afsdb_part_hostname=None,
        cname_part_hostname=None,
        dname_part_target=None,
        kx_part_exchanger=None,
        mx_part_exchanger=None,
        ns_part_hostname=None,
        ptr_part_hostname=None,
        srv_part_target=None,
        loc_part_altitude=None,
        loc_part_h_precision=None,
        loc_part_lat_sec=None,
        loc_part_lon_sec=None,
        loc_part_size=None,
        loc_part_v_precision=None,
        afsdb_part_subtype=None,
        cert_part_algorithm=None,
        cert_part_key_tag=None,
        cert_part_type=None,
        dlv_part_algorithm=None,
        dlv_part_digest_type=None,
        dlv_part_key_tag=None,
        ds_part_algorithm=None,
        ds_part_digest_type=None,
        ds_part_key_tag=None,
        kx_part_preference=None,
        loc_part_lat_deg=None,
        loc_part_lat_min=None,
        loc_part_lon_deg=None,
        loc_part_lon_min=None,
        mx_part_preference=None,
        naptr_part_order=None,
        naptr_part_preference=None,
        srv_part_port=None,
        srv_part_priority=None,
        srv_part_weight=None,
        sshfp_part_algorithm=None,
        sshfp_part_fp_type=None,
        tlsa_part_cert_usage=None,
        tlsa_part_matching_type=None,
        tlsa_part_selector=None,
        uri_part_priority=None,
        uri_part_weight=None,
        a6_part_data=None,
        a_part_ip_address=None,
        aaaa_part_ip_address=None,
        addattr=None,
        cert_part_certificate_or_crl=None,
        dlv_part_digest=None,
        ds_part_digest=None,
        naptr_part_flags=None,
        naptr_part_regexp=None,
        naptr_part_replacement=None,
        naptr_part_service=None,
        opt_setattr=None,
        sshfp_part_fingerprint=None,
        tlsa_part_cert_association_data=None,
        txt_part_data=None,
        uri_part_target=None,
        loc_part_lon_dir=None,
        loc_part_lat_dir=None,
        a_extra_create_reverse=False,
        aaaa_extra_create_reverse=False,
        opt_all=True,
        force=False,
        raw=False,
        structured=False,
        a6record=None,
        aaaarecord=None,
        afsdbrecord=None,
        aplrecord=None,
        arecord=None,
        certrecord=None,
        cnamerecord=None,
        dhcidrecord=None,
        dlvrecord=None,
        dnamerecord=None,
        dsrecord=None,
        hiprecord=None,
        ipseckeyrecord=None,
        dnsttl=None,
        keyrecord=None,
        kxrecord=None,
        locrecord=None,
        mxrecord=None,
        naptrrecord=None,
        nsecrecord=None,
        nsrecord=None,
        ptrrecord=None,
        rprecord=None,
        rrsigrecord=None,
        sigrecord=None,
        spfrecord=None,
        srvrecord=None,
        sshfprecord=None,
        dnsclass=None,
        tlsarecord=None,
        txtrecord=None,
        urirecord=None,
    ):
        """Add new DNS resource record.
        :param dnszoneidnsname: Zone name (FQDN)
        :type dnszoneidnsname: DNSNameParam
        :param idnsname: Record name
        :type idnsname: DNSNameParam
        :param afsdb_part_hostname: AFSDB Hostname
        :type afsdb_part_hostname: DNSNameParam
        :param cname_part_hostname: A hostname which this alias hostname points to
        :type cname_part_hostname: DNSNameParam
        :param dname_part_target: DNAME Target
        :type dname_part_target: DNSNameParam
        :param kx_part_exchanger: A host willing to act as a key exchanger
        :type kx_part_exchanger: DNSNameParam
        :param mx_part_exchanger: A host willing to act as a mail exchanger
        :type mx_part_exchanger: DNSNameParam
        :param ns_part_hostname: NS Hostname
        :type ns_part_hostname: DNSNameParam
        :param ptr_part_hostname: The hostname this reverse record points to
        :type ptr_part_hostname: DNSNameParam
        :param srv_part_target: The domain name of the target host or '.' if the service is decidedly not available at this domain
        :type srv_part_target: DNSNameParam
        :param loc_part_altitude: LOC Altitude
        :type loc_part_altitude: Decimal
        :param loc_part_h_precision: LOC Horizontal Precision
        :type loc_part_h_precision: Decimal
        :param loc_part_lat_sec: LOC Seconds Latitude
        :type loc_part_lat_sec: Decimal
        :param loc_part_lon_sec: LOC Seconds Longitude
        :type loc_part_lon_sec: Decimal
        :param loc_part_size: LOC Size
        :type loc_part_size: Decimal
        :param loc_part_v_precision: LOC Vertical Precision
        :type loc_part_v_precision: Decimal
        :param afsdb_part_subtype: AFSDB Subtype
        :type afsdb_part_subtype: Int
        :param cert_part_algorithm: CERT Algorithm
        :type cert_part_algorithm: Int
        :param cert_part_key_tag: CERT Key Tag
        :type cert_part_key_tag: Int
        :param cert_part_type: CERT Certificate Type
        :type cert_part_type: Int
        :param dlv_part_algorithm: DLV Algorithm
        :type dlv_part_algorithm: Int
        :param dlv_part_digest_type: DLV Digest Type
        :type dlv_part_digest_type: Int
        :param dlv_part_key_tag: DLV Key Tag
        :type dlv_part_key_tag: Int
        :param ds_part_algorithm: DS Algorithm
        :type ds_part_algorithm: Int
        :param ds_part_digest_type: DS Digest Type
        :type ds_part_digest_type: Int
        :param ds_part_key_tag: DS Key Tag
        :type ds_part_key_tag: Int
        :param kx_part_preference: Preference given to this exchanger. Lower values are more preferred
        :type kx_part_preference: Int
        :param loc_part_lat_deg: LOC Degrees Latitude
        :type loc_part_lat_deg: Int
        :param loc_part_lat_min: LOC Minutes Latitude
        :type loc_part_lat_min: Int
        :param loc_part_lon_deg: LOC Degrees Longitude
        :type loc_part_lon_deg: Int
        :param loc_part_lon_min: LOC Minutes Longitude
        :type loc_part_lon_min: Int
        :param mx_part_preference: Preference given to this exchanger. Lower values are more preferred
        :type mx_part_preference: Int
        :param naptr_part_order: NAPTR Order
        :type naptr_part_order: Int
        :param naptr_part_preference: NAPTR Preference
        :type naptr_part_preference: Int
        :param srv_part_port: SRV Port
        :type srv_part_port: Int
        :param srv_part_priority: Lower number means higher priority. Clients will attempt to contact the server with the lowest-numbered priority they can reach.
        :type srv_part_priority: Int
        :param srv_part_weight: Relative weight for entries with the same priority.
        :type srv_part_weight: Int
        :param sshfp_part_algorithm: SSHFP Algorithm
        :type sshfp_part_algorithm: Int
        :param sshfp_part_fp_type: SSHFP Fingerprint Type
        :type sshfp_part_fp_type: Int
        :param tlsa_part_cert_usage: TLSA Certificate Usage
        :type tlsa_part_cert_usage: Int
        :param tlsa_part_matching_type: TLSA Matching Type
        :type tlsa_part_matching_type: Int
        :param tlsa_part_selector: TLSA Selector
        :type tlsa_part_selector: Int
        :param uri_part_priority: Lower number means higher priority. Clients will attempt to contact the URI with the lowest-numbered priority they can reach.
        :type uri_part_priority: Int
        :param uri_part_weight: Relative weight for entries with the same priority.
        :type uri_part_weight: Int
        :param a6_part_data: A6 Record data
        :type a6_part_data: Str
        :param a_part_ip_address: A IP Address
        :type a_part_ip_address: Str
        :param aaaa_part_ip_address: AAAA IP Address
        :type aaaa_part_ip_address: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param cert_part_certificate_or_crl: CERT Certificate/CRL
        :type cert_part_certificate_or_crl: Str
        :param dlv_part_digest: DLV Digest
        :type dlv_part_digest: Str
        :param ds_part_digest: DS Digest
        :type ds_part_digest: Str
        :param naptr_part_flags: NAPTR Flags
        :type naptr_part_flags: Str
        :param naptr_part_regexp: NAPTR Regular Expression
        :type naptr_part_regexp: Str
        :param naptr_part_replacement: NAPTR Replacement
        :type naptr_part_replacement: Str
        :param naptr_part_service: NAPTR Service
        :type naptr_part_service: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param sshfp_part_fingerprint: SSHFP Fingerprint
        :type sshfp_part_fingerprint: Str
        :param tlsa_part_cert_association_data: TLSA Certificate Association Data
        :type tlsa_part_cert_association_data: Str
        :param txt_part_data: TXT Text Data
        :type txt_part_data: Str
        :param uri_part_target: Target Uniform Resource Identifier according to RFC 3986
        :type uri_part_target: Str
        :param loc_part_lon_dir: LOC Direction Longitude
        :type loc_part_lon_dir: StrEnum
        :param loc_part_lat_dir: LOC Direction Latitude
        :type loc_part_lat_dir: StrEnum
        :param a_extra_create_reverse: Create reverse record for this IP Address
        :type a_extra_create_reverse: Flag
        :param aaaa_extra_create_reverse: Create reverse record for this IP Address
        :type aaaa_extra_create_reverse: Flag
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param force: force NS record creation even if its hostname is not in DNS
        :type force: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param structured: Parse all raw DNS records and return them in a structured way
        :type structured: Flag
        :param a6record: Raw A6 records
        :type a6record: A6Record
        :param aaaarecord: Raw AAAA records
        :type aaaarecord: AAAARecord
        :param afsdbrecord: Raw AFSDB records
        :type afsdbrecord: AFSDBRecord
        :param aplrecord: Raw APL records
        :type aplrecord: APLRecord
        :param arecord: Raw A records
        :type arecord: ARecord
        :param certrecord: Raw CERT records
        :type certrecord: CERTRecord
        :param cnamerecord: Raw CNAME records
        :type cnamerecord: CNAMERecord
        :param dhcidrecord: Raw DHCID records
        :type dhcidrecord: DHCIDRecord
        :param dlvrecord: Raw DLV records
        :type dlvrecord: DLVRecord
        :param dnamerecord: Raw DNAME records
        :type dnamerecord: DNAMERecord
        :param dsrecord: Raw DS records
        :type dsrecord: DSRecord
        :param hiprecord: Raw HIP records
        :type hiprecord: HIPRecord
        :param ipseckeyrecord: Raw IPSECKEY records
        :type ipseckeyrecord: IPSECKEYRecord
        :param dnsttl: Time to live
        :type dnsttl: Int
        :param keyrecord: Raw KEY records
        :type keyrecord: KEYRecord
        :param kxrecord: Raw KX records
        :type kxrecord: KXRecord
        :param locrecord: Raw LOC records
        :type locrecord: LOCRecord
        :param mxrecord: Raw MX records
        :type mxrecord: MXRecord
        :param naptrrecord: Raw NAPTR records
        :type naptrrecord: NAPTRRecord
        :param nsecrecord: Raw NSEC records
        :type nsecrecord: NSECRecord
        :param nsrecord: Raw NS records
        :type nsrecord: NSRecord
        :param ptrrecord: Raw PTR records
        :type ptrrecord: PTRRecord
        :param rprecord: Raw RP records
        :type rprecord: RPRecord
        :param rrsigrecord: Raw RRSIG records
        :type rrsigrecord: RRSIGRecord
        :param sigrecord: Raw SIG records
        :type sigrecord: SIGRecord
        :param spfrecord: Raw SPF records
        :type spfrecord: SPFRecord
        :param srvrecord: Raw SRV records
        :type srvrecord: SRVRecord
        :param sshfprecord: Raw SSHFP records
        :type sshfprecord: SSHFPRecord
        :param dnsclass: <dnsclass>
        :type dnsclass: StrEnum
        :param tlsarecord: Raw TLSA records
        :type tlsarecord: TLSARecord
        :param txtrecord: Raw TXT records
        :type txtrecord: TXTRecord
        :param urirecord: Raw URI records
        :type urirecord: URIRecord
        """
        method = 'dnsrecord_add'
        
        _args = list()
        _args.append(dnszoneidnsname)
        _args.append(idnsname)
        
        _params = dict()
        if afsdb_part_hostname:
            _params['afsdb_part_hostname'] = afsdb_part_hostname
        if cname_part_hostname:
            _params['cname_part_hostname'] = cname_part_hostname
        if dname_part_target:
            _params['dname_part_target'] = dname_part_target
        if kx_part_exchanger:
            _params['kx_part_exchanger'] = kx_part_exchanger
        if mx_part_exchanger:
            _params['mx_part_exchanger'] = mx_part_exchanger
        if ns_part_hostname:
            _params['ns_part_hostname'] = ns_part_hostname
        if ptr_part_hostname:
            _params['ptr_part_hostname'] = ptr_part_hostname
        if srv_part_target:
            _params['srv_part_target'] = srv_part_target
        if loc_part_altitude:
            _params['loc_part_altitude'] = loc_part_altitude
        if loc_part_h_precision:
            _params['loc_part_h_precision'] = loc_part_h_precision
        if loc_part_lat_sec:
            _params['loc_part_lat_sec'] = loc_part_lat_sec
        if loc_part_lon_sec:
            _params['loc_part_lon_sec'] = loc_part_lon_sec
        if loc_part_size:
            _params['loc_part_size'] = loc_part_size
        if loc_part_v_precision:
            _params['loc_part_v_precision'] = loc_part_v_precision
        if afsdb_part_subtype:
            _params['afsdb_part_subtype'] = afsdb_part_subtype
        if cert_part_algorithm:
            _params['cert_part_algorithm'] = cert_part_algorithm
        if cert_part_key_tag:
            _params['cert_part_key_tag'] = cert_part_key_tag
        if cert_part_type:
            _params['cert_part_type'] = cert_part_type
        if dlv_part_algorithm:
            _params['dlv_part_algorithm'] = dlv_part_algorithm
        if dlv_part_digest_type:
            _params['dlv_part_digest_type'] = dlv_part_digest_type
        if dlv_part_key_tag:
            _params['dlv_part_key_tag'] = dlv_part_key_tag
        if ds_part_algorithm:
            _params['ds_part_algorithm'] = ds_part_algorithm
        if ds_part_digest_type:
            _params['ds_part_digest_type'] = ds_part_digest_type
        if ds_part_key_tag:
            _params['ds_part_key_tag'] = ds_part_key_tag
        if kx_part_preference:
            _params['kx_part_preference'] = kx_part_preference
        if loc_part_lat_deg:
            _params['loc_part_lat_deg'] = loc_part_lat_deg
        if loc_part_lat_min:
            _params['loc_part_lat_min'] = loc_part_lat_min
        if loc_part_lon_deg:
            _params['loc_part_lon_deg'] = loc_part_lon_deg
        if loc_part_lon_min:
            _params['loc_part_lon_min'] = loc_part_lon_min
        if mx_part_preference:
            _params['mx_part_preference'] = mx_part_preference
        if naptr_part_order:
            _params['naptr_part_order'] = naptr_part_order
        if naptr_part_preference:
            _params['naptr_part_preference'] = naptr_part_preference
        if srv_part_port:
            _params['srv_part_port'] = srv_part_port
        if srv_part_priority:
            _params['srv_part_priority'] = srv_part_priority
        if srv_part_weight:
            _params['srv_part_weight'] = srv_part_weight
        if sshfp_part_algorithm:
            _params['sshfp_part_algorithm'] = sshfp_part_algorithm
        if sshfp_part_fp_type:
            _params['sshfp_part_fp_type'] = sshfp_part_fp_type
        if tlsa_part_cert_usage:
            _params['tlsa_part_cert_usage'] = tlsa_part_cert_usage
        if tlsa_part_matching_type:
            _params['tlsa_part_matching_type'] = tlsa_part_matching_type
        if tlsa_part_selector:
            _params['tlsa_part_selector'] = tlsa_part_selector
        if uri_part_priority:
            _params['uri_part_priority'] = uri_part_priority
        if uri_part_weight:
            _params['uri_part_weight'] = uri_part_weight
        if a6_part_data:
            _params['a6_part_data'] = a6_part_data
        if a_part_ip_address:
            _params['a_part_ip_address'] = a_part_ip_address
        if aaaa_part_ip_address:
            _params['aaaa_part_ip_address'] = aaaa_part_ip_address
        if addattr:
            _params['addattr'] = addattr
        if cert_part_certificate_or_crl:
            _params['cert_part_certificate_or_crl'] = cert_part_certificate_or_crl
        if dlv_part_digest:
            _params['dlv_part_digest'] = dlv_part_digest
        if ds_part_digest:
            _params['ds_part_digest'] = ds_part_digest
        if naptr_part_flags:
            _params['naptr_part_flags'] = naptr_part_flags
        if naptr_part_regexp:
            _params['naptr_part_regexp'] = naptr_part_regexp
        if naptr_part_replacement:
            _params['naptr_part_replacement'] = naptr_part_replacement
        if naptr_part_service:
            _params['naptr_part_service'] = naptr_part_service
        if opt_setattr:
            _params['setattr'] = opt_setattr
        if sshfp_part_fingerprint:
            _params['sshfp_part_fingerprint'] = sshfp_part_fingerprint
        if tlsa_part_cert_association_data:
            _params['tlsa_part_cert_association_data'] = tlsa_part_cert_association_data
        if txt_part_data:
            _params['txt_part_data'] = txt_part_data
        if uri_part_target:
            _params['uri_part_target'] = uri_part_target
        if loc_part_lon_dir:
            _params['loc_part_lon_dir'] = loc_part_lon_dir
        if loc_part_lat_dir:
            _params['loc_part_lat_dir'] = loc_part_lat_dir
        if a_extra_create_reverse:
            _params['a_extra_create_reverse'] = a_extra_create_reverse
        if aaaa_extra_create_reverse:
            _params['aaaa_extra_create_reverse'] = aaaa_extra_create_reverse
        _params['all'] = opt_all
        _params['force'] = force
        _params['raw'] = raw
        _params['structured'] = structured
        if a6record:
            _params['a6record'] = a6record
        if aaaarecord:
            _params['aaaarecord'] = aaaarecord
        if afsdbrecord:
            _params['afsdbrecord'] = afsdbrecord
        if aplrecord:
            _params['aplrecord'] = aplrecord
        if arecord:
            _params['arecord'] = arecord
        if certrecord:
            _params['certrecord'] = certrecord
        if cnamerecord:
            _params['cnamerecord'] = cnamerecord
        if dhcidrecord:
            _params['dhcidrecord'] = dhcidrecord
        if dlvrecord:
            _params['dlvrecord'] = dlvrecord
        if dnamerecord:
            _params['dnamerecord'] = dnamerecord
        if dsrecord:
            _params['dsrecord'] = dsrecord
        if hiprecord:
            _params['hiprecord'] = hiprecord
        if ipseckeyrecord:
            _params['ipseckeyrecord'] = ipseckeyrecord
        if dnsttl:
            _params['dnsttl'] = dnsttl
        if keyrecord:
            _params['keyrecord'] = keyrecord
        if kxrecord:
            _params['kxrecord'] = kxrecord
        if locrecord:
            _params['locrecord'] = locrecord
        if mxrecord:
            _params['mxrecord'] = mxrecord
        if naptrrecord:
            _params['naptrrecord'] = naptrrecord
        if nsecrecord:
            _params['nsecrecord'] = nsecrecord
        if nsrecord:
            _params['nsrecord'] = nsrecord
        if ptrrecord:
            _params['ptrrecord'] = ptrrecord
        if rprecord:
            _params['rprecord'] = rprecord
        if rrsigrecord:
            _params['rrsigrecord'] = rrsigrecord
        if sigrecord:
            _params['sigrecord'] = sigrecord
        if spfrecord:
            _params['spfrecord'] = spfrecord
        if srvrecord:
            _params['srvrecord'] = srvrecord
        if sshfprecord:
            _params['sshfprecord'] = sshfprecord
        if dnsclass:
            _params['dnsclass'] = dnsclass
        if tlsarecord:
            _params['tlsarecord'] = tlsarecord
        if txtrecord:
            _params['txtrecord'] = txtrecord
        if urirecord:
            _params['urirecord'] = urirecord
        
        return self._request(method, _args, _params)

    def dnsrecord_del(
        self,
        dnszoneidnsname,
        idnsname,
        del_all=False,
        raw=False,
        structured=False,
        a6record=None,
        aaaarecord=None,
        afsdbrecord=None,
        aplrecord=None,
        arecord=None,
        certrecord=None,
        cnamerecord=None,
        dhcidrecord=None,
        dlvrecord=None,
        dnamerecord=None,
        dsrecord=None,
        hiprecord=None,
        ipseckeyrecord=None,
        dnsttl=None,
        keyrecord=None,
        kxrecord=None,
        locrecord=None,
        mxrecord=None,
        naptrrecord=None,
        nsecrecord=None,
        nsrecord=None,
        ptrrecord=None,
        rprecord=None,
        rrsigrecord=None,
        sigrecord=None,
        spfrecord=None,
        srvrecord=None,
        sshfprecord=None,
        dnsclass=None,
        tlsarecord=None,
        txtrecord=None,
        urirecord=None,
    ):
        """Delete DNS resource record.
        :param dnszoneidnsname: Zone name (FQDN)
        :type dnszoneidnsname: DNSNameParam
        :param idnsname: Record name
        :type idnsname: DNSNameParam
        :param del_all: Delete all associated records
        :type del_all: Flag
        :param raw: <raw>
        :type raw: Flag
        :param structured: Parse all raw DNS records and return them in a structured way
        :type structured: Flag
        :param a6record: Raw A6 records
        :type a6record: A6Record
        :param aaaarecord: Raw AAAA records
        :type aaaarecord: AAAARecord
        :param afsdbrecord: Raw AFSDB records
        :type afsdbrecord: AFSDBRecord
        :param aplrecord: Raw APL records
        :type aplrecord: APLRecord
        :param arecord: Raw A records
        :type arecord: ARecord
        :param certrecord: Raw CERT records
        :type certrecord: CERTRecord
        :param cnamerecord: Raw CNAME records
        :type cnamerecord: CNAMERecord
        :param dhcidrecord: Raw DHCID records
        :type dhcidrecord: DHCIDRecord
        :param dlvrecord: Raw DLV records
        :type dlvrecord: DLVRecord
        :param dnamerecord: Raw DNAME records
        :type dnamerecord: DNAMERecord
        :param dsrecord: Raw DS records
        :type dsrecord: DSRecord
        :param hiprecord: Raw HIP records
        :type hiprecord: HIPRecord
        :param ipseckeyrecord: Raw IPSECKEY records
        :type ipseckeyrecord: IPSECKEYRecord
        :param dnsttl: Time to live
        :type dnsttl: Int
        :param keyrecord: Raw KEY records
        :type keyrecord: KEYRecord
        :param kxrecord: Raw KX records
        :type kxrecord: KXRecord
        :param locrecord: Raw LOC records
        :type locrecord: LOCRecord
        :param mxrecord: Raw MX records
        :type mxrecord: MXRecord
        :param naptrrecord: Raw NAPTR records
        :type naptrrecord: NAPTRRecord
        :param nsecrecord: Raw NSEC records
        :type nsecrecord: NSECRecord
        :param nsrecord: Raw NS records
        :type nsrecord: NSRecord
        :param ptrrecord: Raw PTR records
        :type ptrrecord: PTRRecord
        :param rprecord: Raw RP records
        :type rprecord: RPRecord
        :param rrsigrecord: Raw RRSIG records
        :type rrsigrecord: RRSIGRecord
        :param sigrecord: Raw SIG records
        :type sigrecord: SIGRecord
        :param spfrecord: Raw SPF records
        :type spfrecord: SPFRecord
        :param srvrecord: Raw SRV records
        :type srvrecord: SRVRecord
        :param sshfprecord: Raw SSHFP records
        :type sshfprecord: SSHFPRecord
        :param dnsclass: <dnsclass>
        :type dnsclass: StrEnum
        :param tlsarecord: Raw TLSA records
        :type tlsarecord: TLSARecord
        :param txtrecord: Raw TXT records
        :type txtrecord: TXTRecord
        :param urirecord: Raw URI records
        :type urirecord: URIRecord
        """
        method = 'dnsrecord_del'
        
        _args = list()
        _args.append(dnszoneidnsname)
        _args.append(idnsname)
        
        _params = dict()
        _params['del_all'] = del_all
        _params['raw'] = raw
        _params['structured'] = structured
        if a6record:
            _params['a6record'] = a6record
        if aaaarecord:
            _params['aaaarecord'] = aaaarecord
        if afsdbrecord:
            _params['afsdbrecord'] = afsdbrecord
        if aplrecord:
            _params['aplrecord'] = aplrecord
        if arecord:
            _params['arecord'] = arecord
        if certrecord:
            _params['certrecord'] = certrecord
        if cnamerecord:
            _params['cnamerecord'] = cnamerecord
        if dhcidrecord:
            _params['dhcidrecord'] = dhcidrecord
        if dlvrecord:
            _params['dlvrecord'] = dlvrecord
        if dnamerecord:
            _params['dnamerecord'] = dnamerecord
        if dsrecord:
            _params['dsrecord'] = dsrecord
        if hiprecord:
            _params['hiprecord'] = hiprecord
        if ipseckeyrecord:
            _params['ipseckeyrecord'] = ipseckeyrecord
        if dnsttl:
            _params['dnsttl'] = dnsttl
        if keyrecord:
            _params['keyrecord'] = keyrecord
        if kxrecord:
            _params['kxrecord'] = kxrecord
        if locrecord:
            _params['locrecord'] = locrecord
        if mxrecord:
            _params['mxrecord'] = mxrecord
        if naptrrecord:
            _params['naptrrecord'] = naptrrecord
        if nsecrecord:
            _params['nsecrecord'] = nsecrecord
        if nsrecord:
            _params['nsrecord'] = nsrecord
        if ptrrecord:
            _params['ptrrecord'] = ptrrecord
        if rprecord:
            _params['rprecord'] = rprecord
        if rrsigrecord:
            _params['rrsigrecord'] = rrsigrecord
        if sigrecord:
            _params['sigrecord'] = sigrecord
        if spfrecord:
            _params['spfrecord'] = spfrecord
        if srvrecord:
            _params['srvrecord'] = srvrecord
        if sshfprecord:
            _params['sshfprecord'] = sshfprecord
        if dnsclass:
            _params['dnsclass'] = dnsclass
        if tlsarecord:
            _params['tlsarecord'] = tlsarecord
        if txtrecord:
            _params['txtrecord'] = txtrecord
        if urirecord:
            _params['urirecord'] = urirecord
        
        return self._request(method, _args, _params)

    def dnsrecord_delentry(
        self,
        dnszoneidnsname,
        idnsname,
        opt_continue=False,
    ):
        """
    Delete DNS record entry.
    
        :param dnszoneidnsname: Zone name (FQDN)
        :type dnszoneidnsname: DNSNameParam
        :param idnsname: Record name
        :type idnsname: DNSNameParam
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'dnsrecord_delentry'
        
        _args = list()
        _args.append(dnszoneidnsname)
        _args.append(idnsname)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def dnsrecord_find(
        self,
        dnszoneidnsname,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        structured=False,
        a6record=None,
        aaaarecord=None,
        afsdbrecord=None,
        aplrecord=None,
        arecord=None,
        certrecord=None,
        cnamerecord=None,
        dhcidrecord=None,
        dlvrecord=None,
        dnamerecord=None,
        idnsname=None,
        dsrecord=None,
        hiprecord=None,
        ipseckeyrecord=None,
        dnsttl=None,
        keyrecord=None,
        kxrecord=None,
        locrecord=None,
        mxrecord=None,
        naptrrecord=None,
        nsecrecord=None,
        nsrecord=None,
        ptrrecord=None,
        rprecord=None,
        rrsigrecord=None,
        sigrecord=None,
        spfrecord=None,
        srvrecord=None,
        sshfprecord=None,
        dnsclass=None,
        tlsarecord=None,
        txtrecord=None,
        urirecord=None,
    ):
        """Search for DNS resources.
        :param dnszoneidnsname: Zone name (FQDN)
        :type dnszoneidnsname: DNSNameParam
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param structured: Parse all raw DNS records and return them in a structured way
        :type structured: Flag
        :param a6record: Raw A6 records
        :type a6record: A6Record
        :param aaaarecord: Raw AAAA records
        :type aaaarecord: AAAARecord
        :param afsdbrecord: Raw AFSDB records
        :type afsdbrecord: AFSDBRecord
        :param aplrecord: Raw APL records
        :type aplrecord: APLRecord
        :param arecord: Raw A records
        :type arecord: ARecord
        :param certrecord: Raw CERT records
        :type certrecord: CERTRecord
        :param cnamerecord: Raw CNAME records
        :type cnamerecord: CNAMERecord
        :param dhcidrecord: Raw DHCID records
        :type dhcidrecord: DHCIDRecord
        :param dlvrecord: Raw DLV records
        :type dlvrecord: DLVRecord
        :param dnamerecord: Raw DNAME records
        :type dnamerecord: DNAMERecord
        :param idnsname: Record name
        :type idnsname: DNSNameParam
        :param dsrecord: Raw DS records
        :type dsrecord: DSRecord
        :param hiprecord: Raw HIP records
        :type hiprecord: HIPRecord
        :param ipseckeyrecord: Raw IPSECKEY records
        :type ipseckeyrecord: IPSECKEYRecord
        :param dnsttl: Time to live
        :type dnsttl: Int
        :param keyrecord: Raw KEY records
        :type keyrecord: KEYRecord
        :param kxrecord: Raw KX records
        :type kxrecord: KXRecord
        :param locrecord: Raw LOC records
        :type locrecord: LOCRecord
        :param mxrecord: Raw MX records
        :type mxrecord: MXRecord
        :param naptrrecord: Raw NAPTR records
        :type naptrrecord: NAPTRRecord
        :param nsecrecord: Raw NSEC records
        :type nsecrecord: NSECRecord
        :param nsrecord: Raw NS records
        :type nsrecord: NSRecord
        :param ptrrecord: Raw PTR records
        :type ptrrecord: PTRRecord
        :param rprecord: Raw RP records
        :type rprecord: RPRecord
        :param rrsigrecord: Raw RRSIG records
        :type rrsigrecord: RRSIGRecord
        :param sigrecord: Raw SIG records
        :type sigrecord: SIGRecord
        :param spfrecord: Raw SPF records
        :type spfrecord: SPFRecord
        :param srvrecord: Raw SRV records
        :type srvrecord: SRVRecord
        :param sshfprecord: Raw SSHFP records
        :type sshfprecord: SSHFPRecord
        :param dnsclass: <dnsclass>
        :type dnsclass: StrEnum
        :param tlsarecord: Raw TLSA records
        :type tlsarecord: TLSARecord
        :param txtrecord: Raw TXT records
        :type txtrecord: TXTRecord
        :param urirecord: Raw URI records
        :type urirecord: URIRecord
        """
        method = 'dnsrecord_find'
        
        _args = list()
        _args.append(dnszoneidnsname)
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        _params['structured'] = structured
        if a6record:
            _params['a6record'] = a6record
        if aaaarecord:
            _params['aaaarecord'] = aaaarecord
        if afsdbrecord:
            _params['afsdbrecord'] = afsdbrecord
        if aplrecord:
            _params['aplrecord'] = aplrecord
        if arecord:
            _params['arecord'] = arecord
        if certrecord:
            _params['certrecord'] = certrecord
        if cnamerecord:
            _params['cnamerecord'] = cnamerecord
        if dhcidrecord:
            _params['dhcidrecord'] = dhcidrecord
        if dlvrecord:
            _params['dlvrecord'] = dlvrecord
        if dnamerecord:
            _params['dnamerecord'] = dnamerecord
        if idnsname:
            _params['idnsname'] = idnsname
        if dsrecord:
            _params['dsrecord'] = dsrecord
        if hiprecord:
            _params['hiprecord'] = hiprecord
        if ipseckeyrecord:
            _params['ipseckeyrecord'] = ipseckeyrecord
        if dnsttl:
            _params['dnsttl'] = dnsttl
        if keyrecord:
            _params['keyrecord'] = keyrecord
        if kxrecord:
            _params['kxrecord'] = kxrecord
        if locrecord:
            _params['locrecord'] = locrecord
        if mxrecord:
            _params['mxrecord'] = mxrecord
        if naptrrecord:
            _params['naptrrecord'] = naptrrecord
        if nsecrecord:
            _params['nsecrecord'] = nsecrecord
        if nsrecord:
            _params['nsrecord'] = nsrecord
        if ptrrecord:
            _params['ptrrecord'] = ptrrecord
        if rprecord:
            _params['rprecord'] = rprecord
        if rrsigrecord:
            _params['rrsigrecord'] = rrsigrecord
        if sigrecord:
            _params['sigrecord'] = sigrecord
        if spfrecord:
            _params['spfrecord'] = spfrecord
        if srvrecord:
            _params['srvrecord'] = srvrecord
        if sshfprecord:
            _params['sshfprecord'] = sshfprecord
        if dnsclass:
            _params['dnsclass'] = dnsclass
        if tlsarecord:
            _params['tlsarecord'] = tlsarecord
        if txtrecord:
            _params['txtrecord'] = txtrecord
        if urirecord:
            _params['urirecord'] = urirecord
        
        return self._request(method, _args, _params)

    def dnsrecord_mod(
        self,
        dnszoneidnsname,
        idnsname,
        afsdb_part_hostname=None,
        cname_part_hostname=None,
        dname_part_target=None,
        kx_part_exchanger=None,
        mx_part_exchanger=None,
        ns_part_hostname=None,
        ptr_part_hostname=None,
        rename=None,
        srv_part_target=None,
        loc_part_altitude=None,
        loc_part_h_precision=None,
        loc_part_lat_sec=None,
        loc_part_lon_sec=None,
        loc_part_size=None,
        loc_part_v_precision=None,
        afsdb_part_subtype=None,
        cert_part_algorithm=None,
        cert_part_key_tag=None,
        cert_part_type=None,
        dlv_part_algorithm=None,
        dlv_part_digest_type=None,
        dlv_part_key_tag=None,
        ds_part_algorithm=None,
        ds_part_digest_type=None,
        ds_part_key_tag=None,
        kx_part_preference=None,
        loc_part_lat_deg=None,
        loc_part_lat_min=None,
        loc_part_lon_deg=None,
        loc_part_lon_min=None,
        mx_part_preference=None,
        naptr_part_order=None,
        naptr_part_preference=None,
        srv_part_port=None,
        srv_part_priority=None,
        srv_part_weight=None,
        sshfp_part_algorithm=None,
        sshfp_part_fp_type=None,
        tlsa_part_cert_usage=None,
        tlsa_part_matching_type=None,
        tlsa_part_selector=None,
        uri_part_priority=None,
        uri_part_weight=None,
        a6_part_data=None,
        a_part_ip_address=None,
        aaaa_part_ip_address=None,
        addattr=None,
        cert_part_certificate_or_crl=None,
        opt_delattr=None,
        dlv_part_digest=None,
        ds_part_digest=None,
        naptr_part_flags=None,
        naptr_part_regexp=None,
        naptr_part_replacement=None,
        naptr_part_service=None,
        opt_setattr=None,
        sshfp_part_fingerprint=None,
        tlsa_part_cert_association_data=None,
        txt_part_data=None,
        uri_part_target=None,
        loc_part_lon_dir=None,
        loc_part_lat_dir=None,
        opt_all=True,
        raw=False,
        rights=False,
        structured=False,
        a6record=None,
        aaaarecord=None,
        afsdbrecord=None,
        aplrecord=None,
        arecord=None,
        certrecord=None,
        cnamerecord=None,
        dhcidrecord=None,
        dlvrecord=None,
        dnamerecord=None,
        dsrecord=None,
        hiprecord=None,
        ipseckeyrecord=None,
        dnsttl=None,
        keyrecord=None,
        kxrecord=None,
        locrecord=None,
        mxrecord=None,
        naptrrecord=None,
        nsecrecord=None,
        nsrecord=None,
        ptrrecord=None,
        rprecord=None,
        rrsigrecord=None,
        sigrecord=None,
        spfrecord=None,
        srvrecord=None,
        sshfprecord=None,
        dnsclass=None,
        tlsarecord=None,
        txtrecord=None,
        urirecord=None,
    ):
        """Modify a DNS resource record.
        :param dnszoneidnsname: Zone name (FQDN)
        :type dnszoneidnsname: DNSNameParam
        :param idnsname: Record name
        :type idnsname: DNSNameParam
        :param afsdb_part_hostname: AFSDB Hostname
        :type afsdb_part_hostname: DNSNameParam
        :param cname_part_hostname: A hostname which this alias hostname points to
        :type cname_part_hostname: DNSNameParam
        :param dname_part_target: DNAME Target
        :type dname_part_target: DNSNameParam
        :param kx_part_exchanger: A host willing to act as a key exchanger
        :type kx_part_exchanger: DNSNameParam
        :param mx_part_exchanger: A host willing to act as a mail exchanger
        :type mx_part_exchanger: DNSNameParam
        :param ns_part_hostname: NS Hostname
        :type ns_part_hostname: DNSNameParam
        :param ptr_part_hostname: The hostname this reverse record points to
        :type ptr_part_hostname: DNSNameParam
        :param rename: Rename the DNS resource record object
        :type rename: DNSNameParam
        :param srv_part_target: The domain name of the target host or '.' if the service is decidedly not available at this domain
        :type srv_part_target: DNSNameParam
        :param loc_part_altitude: LOC Altitude
        :type loc_part_altitude: Decimal
        :param loc_part_h_precision: LOC Horizontal Precision
        :type loc_part_h_precision: Decimal
        :param loc_part_lat_sec: LOC Seconds Latitude
        :type loc_part_lat_sec: Decimal
        :param loc_part_lon_sec: LOC Seconds Longitude
        :type loc_part_lon_sec: Decimal
        :param loc_part_size: LOC Size
        :type loc_part_size: Decimal
        :param loc_part_v_precision: LOC Vertical Precision
        :type loc_part_v_precision: Decimal
        :param afsdb_part_subtype: AFSDB Subtype
        :type afsdb_part_subtype: Int
        :param cert_part_algorithm: CERT Algorithm
        :type cert_part_algorithm: Int
        :param cert_part_key_tag: CERT Key Tag
        :type cert_part_key_tag: Int
        :param cert_part_type: CERT Certificate Type
        :type cert_part_type: Int
        :param dlv_part_algorithm: DLV Algorithm
        :type dlv_part_algorithm: Int
        :param dlv_part_digest_type: DLV Digest Type
        :type dlv_part_digest_type: Int
        :param dlv_part_key_tag: DLV Key Tag
        :type dlv_part_key_tag: Int
        :param ds_part_algorithm: DS Algorithm
        :type ds_part_algorithm: Int
        :param ds_part_digest_type: DS Digest Type
        :type ds_part_digest_type: Int
        :param ds_part_key_tag: DS Key Tag
        :type ds_part_key_tag: Int
        :param kx_part_preference: Preference given to this exchanger. Lower values are more preferred
        :type kx_part_preference: Int
        :param loc_part_lat_deg: LOC Degrees Latitude
        :type loc_part_lat_deg: Int
        :param loc_part_lat_min: LOC Minutes Latitude
        :type loc_part_lat_min: Int
        :param loc_part_lon_deg: LOC Degrees Longitude
        :type loc_part_lon_deg: Int
        :param loc_part_lon_min: LOC Minutes Longitude
        :type loc_part_lon_min: Int
        :param mx_part_preference: Preference given to this exchanger. Lower values are more preferred
        :type mx_part_preference: Int
        :param naptr_part_order: NAPTR Order
        :type naptr_part_order: Int
        :param naptr_part_preference: NAPTR Preference
        :type naptr_part_preference: Int
        :param srv_part_port: SRV Port
        :type srv_part_port: Int
        :param srv_part_priority: Lower number means higher priority. Clients will attempt to contact the server with the lowest-numbered priority they can reach.
        :type srv_part_priority: Int
        :param srv_part_weight: Relative weight for entries with the same priority.
        :type srv_part_weight: Int
        :param sshfp_part_algorithm: SSHFP Algorithm
        :type sshfp_part_algorithm: Int
        :param sshfp_part_fp_type: SSHFP Fingerprint Type
        :type sshfp_part_fp_type: Int
        :param tlsa_part_cert_usage: TLSA Certificate Usage
        :type tlsa_part_cert_usage: Int
        :param tlsa_part_matching_type: TLSA Matching Type
        :type tlsa_part_matching_type: Int
        :param tlsa_part_selector: TLSA Selector
        :type tlsa_part_selector: Int
        :param uri_part_priority: Lower number means higher priority. Clients will attempt to contact the URI with the lowest-numbered priority they can reach.
        :type uri_part_priority: Int
        :param uri_part_weight: Relative weight for entries with the same priority.
        :type uri_part_weight: Int
        :param a6_part_data: A6 Record data
        :type a6_part_data: Str
        :param a_part_ip_address: A IP Address
        :type a_part_ip_address: Str
        :param aaaa_part_ip_address: AAAA IP Address
        :type aaaa_part_ip_address: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param cert_part_certificate_or_crl: CERT Certificate/CRL
        :type cert_part_certificate_or_crl: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param dlv_part_digest: DLV Digest
        :type dlv_part_digest: Str
        :param ds_part_digest: DS Digest
        :type ds_part_digest: Str
        :param naptr_part_flags: NAPTR Flags
        :type naptr_part_flags: Str
        :param naptr_part_regexp: NAPTR Regular Expression
        :type naptr_part_regexp: Str
        :param naptr_part_replacement: NAPTR Replacement
        :type naptr_part_replacement: Str
        :param naptr_part_service: NAPTR Service
        :type naptr_part_service: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param sshfp_part_fingerprint: SSHFP Fingerprint
        :type sshfp_part_fingerprint: Str
        :param tlsa_part_cert_association_data: TLSA Certificate Association Data
        :type tlsa_part_cert_association_data: Str
        :param txt_part_data: TXT Text Data
        :type txt_part_data: Str
        :param uri_part_target: Target Uniform Resource Identifier according to RFC 3986
        :type uri_part_target: Str
        :param loc_part_lon_dir: LOC Direction Longitude
        :type loc_part_lon_dir: StrEnum
        :param loc_part_lat_dir: LOC Direction Latitude
        :type loc_part_lat_dir: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param structured: Parse all raw DNS records and return them in a structured way
        :type structured: Flag
        :param a6record: Raw A6 records
        :type a6record: A6Record
        :param aaaarecord: Raw AAAA records
        :type aaaarecord: AAAARecord
        :param afsdbrecord: Raw AFSDB records
        :type afsdbrecord: AFSDBRecord
        :param aplrecord: Raw APL records
        :type aplrecord: APLRecord
        :param arecord: Raw A records
        :type arecord: ARecord
        :param certrecord: Raw CERT records
        :type certrecord: CERTRecord
        :param cnamerecord: Raw CNAME records
        :type cnamerecord: CNAMERecord
        :param dhcidrecord: Raw DHCID records
        :type dhcidrecord: DHCIDRecord
        :param dlvrecord: Raw DLV records
        :type dlvrecord: DLVRecord
        :param dnamerecord: Raw DNAME records
        :type dnamerecord: DNAMERecord
        :param dsrecord: Raw DS records
        :type dsrecord: DSRecord
        :param hiprecord: Raw HIP records
        :type hiprecord: HIPRecord
        :param ipseckeyrecord: Raw IPSECKEY records
        :type ipseckeyrecord: IPSECKEYRecord
        :param dnsttl: Time to live
        :type dnsttl: Int
        :param keyrecord: Raw KEY records
        :type keyrecord: KEYRecord
        :param kxrecord: Raw KX records
        :type kxrecord: KXRecord
        :param locrecord: Raw LOC records
        :type locrecord: LOCRecord
        :param mxrecord: Raw MX records
        :type mxrecord: MXRecord
        :param naptrrecord: Raw NAPTR records
        :type naptrrecord: NAPTRRecord
        :param nsecrecord: Raw NSEC records
        :type nsecrecord: NSECRecord
        :param nsrecord: Raw NS records
        :type nsrecord: NSRecord
        :param ptrrecord: Raw PTR records
        :type ptrrecord: PTRRecord
        :param rprecord: Raw RP records
        :type rprecord: RPRecord
        :param rrsigrecord: Raw RRSIG records
        :type rrsigrecord: RRSIGRecord
        :param sigrecord: Raw SIG records
        :type sigrecord: SIGRecord
        :param spfrecord: Raw SPF records
        :type spfrecord: SPFRecord
        :param srvrecord: Raw SRV records
        :type srvrecord: SRVRecord
        :param sshfprecord: Raw SSHFP records
        :type sshfprecord: SSHFPRecord
        :param dnsclass: <dnsclass>
        :type dnsclass: StrEnum
        :param tlsarecord: Raw TLSA records
        :type tlsarecord: TLSARecord
        :param txtrecord: Raw TXT records
        :type txtrecord: TXTRecord
        :param urirecord: Raw URI records
        :type urirecord: URIRecord
        """
        method = 'dnsrecord_mod'
        
        _args = list()
        _args.append(dnszoneidnsname)
        _args.append(idnsname)
        
        _params = dict()
        if afsdb_part_hostname:
            _params['afsdb_part_hostname'] = afsdb_part_hostname
        if cname_part_hostname:
            _params['cname_part_hostname'] = cname_part_hostname
        if dname_part_target:
            _params['dname_part_target'] = dname_part_target
        if kx_part_exchanger:
            _params['kx_part_exchanger'] = kx_part_exchanger
        if mx_part_exchanger:
            _params['mx_part_exchanger'] = mx_part_exchanger
        if ns_part_hostname:
            _params['ns_part_hostname'] = ns_part_hostname
        if ptr_part_hostname:
            _params['ptr_part_hostname'] = ptr_part_hostname
        if rename:
            _params['rename'] = rename
        if srv_part_target:
            _params['srv_part_target'] = srv_part_target
        if loc_part_altitude:
            _params['loc_part_altitude'] = loc_part_altitude
        if loc_part_h_precision:
            _params['loc_part_h_precision'] = loc_part_h_precision
        if loc_part_lat_sec:
            _params['loc_part_lat_sec'] = loc_part_lat_sec
        if loc_part_lon_sec:
            _params['loc_part_lon_sec'] = loc_part_lon_sec
        if loc_part_size:
            _params['loc_part_size'] = loc_part_size
        if loc_part_v_precision:
            _params['loc_part_v_precision'] = loc_part_v_precision
        if afsdb_part_subtype:
            _params['afsdb_part_subtype'] = afsdb_part_subtype
        if cert_part_algorithm:
            _params['cert_part_algorithm'] = cert_part_algorithm
        if cert_part_key_tag:
            _params['cert_part_key_tag'] = cert_part_key_tag
        if cert_part_type:
            _params['cert_part_type'] = cert_part_type
        if dlv_part_algorithm:
            _params['dlv_part_algorithm'] = dlv_part_algorithm
        if dlv_part_digest_type:
            _params['dlv_part_digest_type'] = dlv_part_digest_type
        if dlv_part_key_tag:
            _params['dlv_part_key_tag'] = dlv_part_key_tag
        if ds_part_algorithm:
            _params['ds_part_algorithm'] = ds_part_algorithm
        if ds_part_digest_type:
            _params['ds_part_digest_type'] = ds_part_digest_type
        if ds_part_key_tag:
            _params['ds_part_key_tag'] = ds_part_key_tag
        if kx_part_preference:
            _params['kx_part_preference'] = kx_part_preference
        if loc_part_lat_deg:
            _params['loc_part_lat_deg'] = loc_part_lat_deg
        if loc_part_lat_min:
            _params['loc_part_lat_min'] = loc_part_lat_min
        if loc_part_lon_deg:
            _params['loc_part_lon_deg'] = loc_part_lon_deg
        if loc_part_lon_min:
            _params['loc_part_lon_min'] = loc_part_lon_min
        if mx_part_preference:
            _params['mx_part_preference'] = mx_part_preference
        if naptr_part_order:
            _params['naptr_part_order'] = naptr_part_order
        if naptr_part_preference:
            _params['naptr_part_preference'] = naptr_part_preference
        if srv_part_port:
            _params['srv_part_port'] = srv_part_port
        if srv_part_priority:
            _params['srv_part_priority'] = srv_part_priority
        if srv_part_weight:
            _params['srv_part_weight'] = srv_part_weight
        if sshfp_part_algorithm:
            _params['sshfp_part_algorithm'] = sshfp_part_algorithm
        if sshfp_part_fp_type:
            _params['sshfp_part_fp_type'] = sshfp_part_fp_type
        if tlsa_part_cert_usage:
            _params['tlsa_part_cert_usage'] = tlsa_part_cert_usage
        if tlsa_part_matching_type:
            _params['tlsa_part_matching_type'] = tlsa_part_matching_type
        if tlsa_part_selector:
            _params['tlsa_part_selector'] = tlsa_part_selector
        if uri_part_priority:
            _params['uri_part_priority'] = uri_part_priority
        if uri_part_weight:
            _params['uri_part_weight'] = uri_part_weight
        if a6_part_data:
            _params['a6_part_data'] = a6_part_data
        if a_part_ip_address:
            _params['a_part_ip_address'] = a_part_ip_address
        if aaaa_part_ip_address:
            _params['aaaa_part_ip_address'] = aaaa_part_ip_address
        if addattr:
            _params['addattr'] = addattr
        if cert_part_certificate_or_crl:
            _params['cert_part_certificate_or_crl'] = cert_part_certificate_or_crl
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if dlv_part_digest:
            _params['dlv_part_digest'] = dlv_part_digest
        if ds_part_digest:
            _params['ds_part_digest'] = ds_part_digest
        if naptr_part_flags:
            _params['naptr_part_flags'] = naptr_part_flags
        if naptr_part_regexp:
            _params['naptr_part_regexp'] = naptr_part_regexp
        if naptr_part_replacement:
            _params['naptr_part_replacement'] = naptr_part_replacement
        if naptr_part_service:
            _params['naptr_part_service'] = naptr_part_service
        if opt_setattr:
            _params['setattr'] = opt_setattr
        if sshfp_part_fingerprint:
            _params['sshfp_part_fingerprint'] = sshfp_part_fingerprint
        if tlsa_part_cert_association_data:
            _params['tlsa_part_cert_association_data'] = tlsa_part_cert_association_data
        if txt_part_data:
            _params['txt_part_data'] = txt_part_data
        if uri_part_target:
            _params['uri_part_target'] = uri_part_target
        if loc_part_lon_dir:
            _params['loc_part_lon_dir'] = loc_part_lon_dir
        if loc_part_lat_dir:
            _params['loc_part_lat_dir'] = loc_part_lat_dir
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        _params['structured'] = structured
        if a6record:
            _params['a6record'] = a6record
        if aaaarecord:
            _params['aaaarecord'] = aaaarecord
        if afsdbrecord:
            _params['afsdbrecord'] = afsdbrecord
        if aplrecord:
            _params['aplrecord'] = aplrecord
        if arecord:
            _params['arecord'] = arecord
        if certrecord:
            _params['certrecord'] = certrecord
        if cnamerecord:
            _params['cnamerecord'] = cnamerecord
        if dhcidrecord:
            _params['dhcidrecord'] = dhcidrecord
        if dlvrecord:
            _params['dlvrecord'] = dlvrecord
        if dnamerecord:
            _params['dnamerecord'] = dnamerecord
        if dsrecord:
            _params['dsrecord'] = dsrecord
        if hiprecord:
            _params['hiprecord'] = hiprecord
        if ipseckeyrecord:
            _params['ipseckeyrecord'] = ipseckeyrecord
        if dnsttl:
            _params['dnsttl'] = dnsttl
        if keyrecord:
            _params['keyrecord'] = keyrecord
        if kxrecord:
            _params['kxrecord'] = kxrecord
        if locrecord:
            _params['locrecord'] = locrecord
        if mxrecord:
            _params['mxrecord'] = mxrecord
        if naptrrecord:
            _params['naptrrecord'] = naptrrecord
        if nsecrecord:
            _params['nsecrecord'] = nsecrecord
        if nsrecord:
            _params['nsrecord'] = nsrecord
        if ptrrecord:
            _params['ptrrecord'] = ptrrecord
        if rprecord:
            _params['rprecord'] = rprecord
        if rrsigrecord:
            _params['rrsigrecord'] = rrsigrecord
        if sigrecord:
            _params['sigrecord'] = sigrecord
        if spfrecord:
            _params['spfrecord'] = spfrecord
        if srvrecord:
            _params['srvrecord'] = srvrecord
        if sshfprecord:
            _params['sshfprecord'] = sshfprecord
        if dnsclass:
            _params['dnsclass'] = dnsclass
        if tlsarecord:
            _params['tlsarecord'] = tlsarecord
        if txtrecord:
            _params['txtrecord'] = txtrecord
        if urirecord:
            _params['urirecord'] = urirecord
        
        return self._request(method, _args, _params)

    def dnsrecord_show(
        self,
        dnszoneidnsname,
        idnsname,
        opt_all=True,
        raw=False,
        rights=False,
        structured=False,
    ):
        """Display DNS resource.
        :param dnszoneidnsname: Zone name (FQDN)
        :type dnszoneidnsname: DNSNameParam
        :param idnsname: Record name
        :type idnsname: DNSNameParam
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param structured: Parse all raw DNS records and return them in a structured way
        :type structured: Flag
        """
        method = 'dnsrecord_show'
        
        _args = list()
        _args.append(dnszoneidnsname)
        _args.append(idnsname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        _params['structured'] = structured
        
        return self._request(method, _args, _params)

    def dnsrecord_split_parts(
        self,
        name,
        value,
    ):
        """None
        :param name: <name>
        :type name: Str
        :param value: <value>
        :type value: Str
        """
        method = 'dnsrecord_split_parts'
        
        _args = list()
        _args.append(name)
        _args.append(value)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnsserver_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        idnssoamname=None,
        idnsforwarders=None,
        idnsserverid=None,
        idnsforwardpolicy=None,
    ):
        """Search for DNS servers.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("hostname")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param idnssoamname: SOA mname (authoritative server) override
        :type idnssoamname: DNSNameParam
        :param idnsforwarders: Per-server forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param idnsserverid: DNS Server name
        :type idnsserverid: Str
        :param idnsforwardpolicy: Per-server conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type idnsforwardpolicy: StrEnum
        """
        method = 'dnsserver_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if idnssoamname:
            _params['idnssoamname'] = idnssoamname
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if idnsserverid:
            _params['idnsserverid'] = idnsserverid
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        
        return self._request(method, _args, _params)

    def dnsserver_mod(
        self,
        idnsserverid,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        idnssoamname=None,
        idnsforwarders=None,
        idnsforwardpolicy=None,
    ):
        """Modify DNS server configuration
        :param idnsserverid: DNS Server name
        :type idnsserverid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param idnssoamname: SOA mname (authoritative server) override
        :type idnssoamname: DNSNameParam
        :param idnsforwarders: Per-server forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param idnsforwardpolicy: Per-server conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type idnsforwardpolicy: StrEnum
        """
        method = 'dnsserver_mod'
        
        _args = list()
        _args.append(idnsserverid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if idnssoamname:
            _params['idnssoamname'] = idnssoamname
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        
        return self._request(method, _args, _params)

    def dnsserver_show(
        self,
        idnsserverid,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display configuration of a DNS server.
        :param idnsserverid: DNS Server name
        :type idnsserverid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'dnsserver_show'
        
        _args = list()
        _args.append(idnsserverid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def dnszone_add(
        self,
        idnsname,
        idnssoaserial,
        addattr=None,
        ip_address=None,
        name_from_ip=None,
        opt_setattr=None,
        opt_all=True,
        force=False,
        raw=False,
        skip_nameserver_check=False,
        skip_overlap_check=False,
        idnsallowsyncptr=None,
        idnssecinlinesigning=False,
        idnssoamname=None,
        dnsdefaultttl=None,
        dnsttl=None,
        idnsforwarders=None,
        nsec3paramrecord=None,
        dnsclass=None,
        idnsforwardpolicy=None,
        idnsallowdynupdate=False,
        idnssoarname='',
        idnssoaexpire=1209600,
        idnssoaminimum=3600,
        idnssoarefresh=3600,
        idnssoaretry=900,
        idnsallowquery='any;',
        idnsallowtransfer='none;',
        idnsupdatepolicy=None,
    ):
        """Create new DNS zone (SOA record).
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param ip_address: <ip_address>
        :type ip_address: Str
        :param name_from_ip: IP network to create reverse zone name from
        :type name_from_ip: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param force: Force DNS zone creation even if nameserver is not resolvable. (Deprecated)
        :type force: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param skip_nameserver_check: Force DNS zone creation even if nameserver is not resolvable.
        :type skip_nameserver_check: Flag
        :param skip_overlap_check: Force DNS zone creation even if it will overlap with an existing zone.
        :type skip_overlap_check: Flag
        :param idnsallowsyncptr: Allow synchronization of forward (A, AAAA) and reverse (PTR) records in the zone
        :type idnsallowsyncptr: Bool
        :param idnssecinlinesigning: Allow inline DNSSEC signing of records in the zone
        :type idnssecinlinesigning: Bool
        :param idnssoamname: Authoritative nameserver domain name
        :type idnssoamname: DNSNameParam
        :param dnsdefaultttl: Time to live for records without explicit TTL definition
        :type dnsdefaultttl: Int
        :param dnsttl: Time to live for records at zone apex
        :type dnsttl: Int
        :param idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param nsec3paramrecord: NSEC3PARAM record for zone in format: hash_algorithm flags iterations salt
        :type nsec3paramrecord: Str
        :param dnsclass: <dnsclass>
        :type dnsclass: StrEnum
        :param idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type idnsforwardpolicy: StrEnum
        :param idnsallowdynupdate: Allow dynamic updates.
        :type idnsallowdynupdate: Bool
        :param idnssoarname: Administrator e-mail address
        :type idnssoarname: DNSNameParam
        :param idnssoaexpire: SOA record expire time
        :type idnssoaexpire: Int
        :param idnssoaminimum: How long should negative responses be cached
        :type idnssoaminimum: Int
        :param idnssoarefresh: SOA record refresh time
        :type idnssoarefresh: Int
        :param idnssoaretry: SOA record retry time
        :type idnssoaretry: Int
        :param idnssoaserial: SOA record serial number
        :type idnssoaserial: Int
        :param idnsallowquery: Semicolon separated list of IP addresses or networks which are allowed to issue queries
        :type idnsallowquery: Str
        :param idnsallowtransfer: Semicolon separated list of IP addresses or networks which are allowed to transfer the zone
        :type idnsallowtransfer: Str
        :param idnsupdatepolicy: BIND update policy
        :type idnsupdatepolicy: Str
        """
        method = 'dnszone_add'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if ip_address:
            _params['ip_address'] = ip_address
        if name_from_ip:
            _params['name_from_ip'] = name_from_ip
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['force'] = force
        _params['raw'] = raw
        _params['skip_nameserver_check'] = skip_nameserver_check
        _params['skip_overlap_check'] = skip_overlap_check
        if idnsallowsyncptr:
            _params['idnsallowsyncptr'] = idnsallowsyncptr
        if idnssecinlinesigning:
            _params['idnssecinlinesigning'] = idnssecinlinesigning
        if idnssoamname:
            _params['idnssoamname'] = idnssoamname
        if dnsdefaultttl:
            _params['dnsdefaultttl'] = dnsdefaultttl
        if dnsttl:
            _params['dnsttl'] = dnsttl
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if nsec3paramrecord:
            _params['nsec3paramrecord'] = nsec3paramrecord
        if dnsclass:
            _params['dnsclass'] = dnsclass
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        if idnsallowdynupdate:
            _params['idnsallowdynupdate'] = idnsallowdynupdate
        _params['idnssoarname'] = idnssoarname
        _params['idnssoaexpire'] = idnssoaexpire
        _params['idnssoaminimum'] = idnssoaminimum
        _params['idnssoarefresh'] = idnssoarefresh
        _params['idnssoaretry'] = idnssoaretry
        _params['idnssoaserial'] = idnssoaserial
        if idnsallowquery:
            _params['idnsallowquery'] = idnsallowquery
        if idnsallowtransfer:
            _params['idnsallowtransfer'] = idnsallowtransfer
        if idnsupdatepolicy:
            _params['idnsupdatepolicy'] = idnsupdatepolicy
        
        return self._request(method, _args, _params)

    def dnszone_add_permission(
        self,
        idnsname,
    ):
        """Add a permission for per-zone access delegation.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        """
        method = 'dnszone_add_permission'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnszone_del(
        self,
        idnsname,
        opt_continue=False,
    ):
        """Delete DNS zone (SOA record).
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'dnszone_del'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def dnszone_disable(
        self,
        idnsname,
    ):
        """Disable DNS Zone.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        """
        method = 'dnszone_disable'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnszone_enable(
        self,
        idnsname,
    ):
        """Enable DNS Zone.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        """
        method = 'dnszone_enable'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnszone_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        name_from_ip=None,
        opt_all=True,
        forward_only=False,
        pkey_only=False,
        raw=False,
        idnsallowsyncptr=None,
        idnssecinlinesigning=False,
        idnsallowdynupdate=False,
        idnszoneactive=None,
        idnssoarname='',
        idnsname=None,
        idnssoamname=None,
        dnsdefaultttl=None,
        idnssoaexpire=1209600,
        idnssoaminimum=3600,
        idnssoarefresh=3600,
        idnssoaretry=900,
        idnssoaserial=None,
        dnsttl=None,
        idnsallowquery='any;',
        idnsallowtransfer='none;',
        idnsforwarders=None,
        nsec3paramrecord=None,
        idnsupdatepolicy=None,
        dnsclass=None,
        idnsforwardpolicy=None,
    ):
        """Search for DNS zones (SOA records).
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param name_from_ip: IP network to create reverse zone name from
        :type name_from_ip: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param forward_only: Search for forward zones only
        :type forward_only: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param idnsallowsyncptr: Allow synchronization of forward (A, AAAA) and reverse (PTR) records in the zone
        :type idnsallowsyncptr: Bool
        :param idnssecinlinesigning: Allow inline DNSSEC signing of records in the zone
        :type idnssecinlinesigning: Bool
        :param idnsallowdynupdate: Allow dynamic updates.
        :type idnsallowdynupdate: Bool
        :param idnszoneactive: Is zone active?
        :type idnszoneactive: Bool
        :param idnssoarname: Administrator e-mail address
        :type idnssoarname: DNSNameParam
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param idnssoamname: Authoritative nameserver domain name
        :type idnssoamname: DNSNameParam
        :param dnsdefaultttl: Time to live for records without explicit TTL definition
        :type dnsdefaultttl: Int
        :param idnssoaexpire: SOA record expire time
        :type idnssoaexpire: Int
        :param idnssoaminimum: How long should negative responses be cached
        :type idnssoaminimum: Int
        :param idnssoarefresh: SOA record refresh time
        :type idnssoarefresh: Int
        :param idnssoaretry: SOA record retry time
        :type idnssoaretry: Int
        :param idnssoaserial: SOA record serial number
        :type idnssoaserial: Int
        :param dnsttl: Time to live for records at zone apex
        :type dnsttl: Int
        :param idnsallowquery: Semicolon separated list of IP addresses or networks which are allowed to issue queries
        :type idnsallowquery: Str
        :param idnsallowtransfer: Semicolon separated list of IP addresses or networks which are allowed to transfer the zone
        :type idnsallowtransfer: Str
        :param idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param nsec3paramrecord: NSEC3PARAM record for zone in format: hash_algorithm flags iterations salt
        :type nsec3paramrecord: Str
        :param idnsupdatepolicy: BIND update policy
        :type idnsupdatepolicy: Str
        :param dnsclass: <dnsclass>
        :type dnsclass: StrEnum
        :param idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type idnsforwardpolicy: StrEnum
        """
        method = 'dnszone_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if name_from_ip:
            _params['name_from_ip'] = name_from_ip
        _params['all'] = opt_all
        _params['forward_only'] = forward_only
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if idnsallowsyncptr:
            _params['idnsallowsyncptr'] = idnsallowsyncptr
        if idnssecinlinesigning:
            _params['idnssecinlinesigning'] = idnssecinlinesigning
        if idnsallowdynupdate:
            _params['idnsallowdynupdate'] = idnsallowdynupdate
        if idnszoneactive:
            _params['idnszoneactive'] = idnszoneactive
        if idnssoarname:
            _params['idnssoarname'] = idnssoarname
        if idnsname:
            _params['idnsname'] = idnsname
        if idnssoamname:
            _params['idnssoamname'] = idnssoamname
        if dnsdefaultttl:
            _params['dnsdefaultttl'] = dnsdefaultttl
        if idnssoaexpire:
            _params['idnssoaexpire'] = idnssoaexpire
        if idnssoaminimum:
            _params['idnssoaminimum'] = idnssoaminimum
        if idnssoarefresh:
            _params['idnssoarefresh'] = idnssoarefresh
        if idnssoaretry:
            _params['idnssoaretry'] = idnssoaretry
        if idnssoaserial:
            _params['idnssoaserial'] = idnssoaserial
        if dnsttl:
            _params['dnsttl'] = dnsttl
        if idnsallowquery:
            _params['idnsallowquery'] = idnsallowquery
        if idnsallowtransfer:
            _params['idnsallowtransfer'] = idnsallowtransfer
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if nsec3paramrecord:
            _params['nsec3paramrecord'] = nsec3paramrecord
        if idnsupdatepolicy:
            _params['idnsupdatepolicy'] = idnsupdatepolicy
        if dnsclass:
            _params['dnsclass'] = dnsclass
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        
        return self._request(method, _args, _params)

    def dnszone_mod(
        self,
        idnsname,
        addattr=None,
        opt_delattr=None,
        name_from_ip=None,
        opt_setattr=None,
        opt_all=True,
        force=False,
        raw=False,
        rights=False,
        idnsallowsyncptr=None,
        idnssecinlinesigning=False,
        idnsallowdynupdate=False,
        idnssoarname='',
        idnssoamname=None,
        dnsdefaultttl=None,
        idnssoaexpire=1209600,
        idnssoaminimum=3600,
        idnssoarefresh=3600,
        idnssoaretry=900,
        idnssoaserial=None,
        dnsttl=None,
        idnsallowquery='any;',
        idnsallowtransfer='none;',
        idnsforwarders=None,
        nsec3paramrecord=None,
        idnsupdatepolicy=None,
        dnsclass=None,
        idnsforwardpolicy=None,
    ):
        """Modify DNS zone (SOA record).
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param name_from_ip: IP network to create reverse zone name from
        :type name_from_ip: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param force: Force nameserver change even if nameserver not in DNS
        :type force: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param idnsallowsyncptr: Allow synchronization of forward (A, AAAA) and reverse (PTR) records in the zone
        :type idnsallowsyncptr: Bool
        :param idnssecinlinesigning: Allow inline DNSSEC signing of records in the zone
        :type idnssecinlinesigning: Bool
        :param idnsallowdynupdate: Allow dynamic updates.
        :type idnsallowdynupdate: Bool
        :param idnssoarname: Administrator e-mail address
        :type idnssoarname: DNSNameParam
        :param idnssoamname: Authoritative nameserver domain name
        :type idnssoamname: DNSNameParam
        :param dnsdefaultttl: Time to live for records without explicit TTL definition
        :type dnsdefaultttl: Int
        :param idnssoaexpire: SOA record expire time
        :type idnssoaexpire: Int
        :param idnssoaminimum: How long should negative responses be cached
        :type idnssoaminimum: Int
        :param idnssoarefresh: SOA record refresh time
        :type idnssoarefresh: Int
        :param idnssoaretry: SOA record retry time
        :type idnssoaretry: Int
        :param idnssoaserial: SOA record serial number
        :type idnssoaserial: Int
        :param dnsttl: Time to live for records at zone apex
        :type dnsttl: Int
        :param idnsallowquery: Semicolon separated list of IP addresses or networks which are allowed to issue queries
        :type idnsallowquery: Str
        :param idnsallowtransfer: Semicolon separated list of IP addresses or networks which are allowed to transfer the zone
        :type idnsallowtransfer: Str
        :param idnsforwarders: Per-zone forwarders. A custom port can be specified for each forwarder using a standard format "IP_ADDRESS port PORT"
        :type idnsforwarders: Str
        :param nsec3paramrecord: NSEC3PARAM record for zone in format: hash_algorithm flags iterations salt
        :type nsec3paramrecord: Str
        :param idnsupdatepolicy: BIND update policy
        :type idnsupdatepolicy: Str
        :param dnsclass: <dnsclass>
        :type dnsclass: StrEnum
        :param idnsforwardpolicy: Per-zone conditional forwarding policy. Set to "none" to disable forwarding to global forwarder for this zone. In that case, conditional zone forwarders are disregarded.
        :type idnsforwardpolicy: StrEnum
        """
        method = 'dnszone_mod'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if name_from_ip:
            _params['name_from_ip'] = name_from_ip
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['force'] = force
        _params['raw'] = raw
        _params['rights'] = rights
        if idnsallowsyncptr:
            _params['idnsallowsyncptr'] = idnsallowsyncptr
        if idnssecinlinesigning:
            _params['idnssecinlinesigning'] = idnssecinlinesigning
        if idnsallowdynupdate:
            _params['idnsallowdynupdate'] = idnsallowdynupdate
        if idnssoarname:
            _params['idnssoarname'] = idnssoarname
        if idnssoamname:
            _params['idnssoamname'] = idnssoamname
        if dnsdefaultttl:
            _params['dnsdefaultttl'] = dnsdefaultttl
        if idnssoaexpire:
            _params['idnssoaexpire'] = idnssoaexpire
        if idnssoaminimum:
            _params['idnssoaminimum'] = idnssoaminimum
        if idnssoarefresh:
            _params['idnssoarefresh'] = idnssoarefresh
        if idnssoaretry:
            _params['idnssoaretry'] = idnssoaretry
        if idnssoaserial:
            _params['idnssoaserial'] = idnssoaserial
        if dnsttl:
            _params['dnsttl'] = dnsttl
        if idnsallowquery:
            _params['idnsallowquery'] = idnsallowquery
        if idnsallowtransfer:
            _params['idnsallowtransfer'] = idnsallowtransfer
        if idnsforwarders:
            _params['idnsforwarders'] = idnsforwarders
        if nsec3paramrecord:
            _params['nsec3paramrecord'] = nsec3paramrecord
        if idnsupdatepolicy:
            _params['idnsupdatepolicy'] = idnsupdatepolicy
        if dnsclass:
            _params['dnsclass'] = dnsclass
        if idnsforwardpolicy:
            _params['idnsforwardpolicy'] = idnsforwardpolicy
        
        return self._request(method, _args, _params)

    def dnszone_remove_permission(
        self,
        idnsname,
    ):
        """Remove a permission for per-zone access delegation.
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        """
        method = 'dnszone_remove_permission'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def dnszone_show(
        self,
        idnsname,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about a DNS zone (SOA record).
        :param idnsname: Zone name (FQDN)
        :type idnsname: DNSNameParam
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'dnszone_show'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
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
        ipadomainlevel,
    ):
        """Change current Domain Level.
        :param ipadomainlevel: Domain Level
        :type ipadomainlevel: Int
        """
        method = 'domainlevel_set'
        
        _args = list()
        _args.append(ipadomainlevel)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def env(
        self,
        *args,
        opt_all=True,
        server=False,
    ):
        """Show environment variables.
        :param opt_all: retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param server: Forward to server instead of running locally
        :type server: Flag
        """
        method = 'env'
        
        _args = list()
        _args += args
        
        _params = dict()
        _params['all'] = opt_all
        if server:
            _params['server'] = server
        
        return self._request(method, _args, _params)

    def group_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        external=False,
        no_members=False,
        nonposix=False,
        raw=False,
        gidnumber=None,
        description=None,
    ):
        """Create a new group.
        :param cn: Group name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param external: Allow adding external non-IPA members from trusted domains
        :type external: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param nonposix: Create as a non-POSIX group
        :type nonposix: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param gidnumber: GID (use this option to set it manually)
        :type gidnumber: Int
        :param description: Group description
        :type description: Str
        """
        method = 'group_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['external'] = external
        _params['no_members'] = no_members
        _params['nonposix'] = nonposix
        _params['raw'] = raw
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def group_add_member(
        self,
        cn,
        ipaexternalmember=None,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Add members to a group.
        :param cn: Group name
        :type cn: Str
        :param ipaexternalmember: Members of a trusted domain in DOM\name or name@domain form
        :type ipaexternalmember: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param user: users to add
        :type user: Str
        """
        method = 'group_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if ipaexternalmember:
            _params['ipaexternalmember'] = ipaexternalmember
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def group_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete group.
        :param cn: Group name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'group_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def group_detach(
        self,
        cn,
    ):
        """Detach a managed group from a user.
        :param cn: Group name
        :type cn: Str
        """
        method = 'group_detach'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def group_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        group=None,
        in_group=None,
        in_hbacrule=None,
        in_netgroup=None,
        in_role=None,
        in_sudorule=None,
        no_group=None,
        no_user=None,
        not_in_group=None,
        not_in_hbacrule=None,
        not_in_netgroup=None,
        not_in_role=None,
        not_in_sudorule=None,
        user=None,
        opt_all=True,
        external=False,
        no_members=True,
        nonposix=False,
        pkey_only=False,
        posix=False,
        private=False,
        raw=False,
        gidnumber=None,
        description=None,
        cn=None,
    ):
        """Search for groups.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param group: Search for groups with these member groups.
        :type group: Str
        :param in_group: Search for groups with these member of groups.
        :type in_group: Str
        :param in_hbacrule: Search for groups with these member of HBAC rules.
        :type in_hbacrule: Str
        :param in_netgroup: Search for groups with these member of netgroups.
        :type in_netgroup: Str
        :param in_role: Search for groups with these member of roles.
        :type in_role: Str
        :param in_sudorule: Search for groups with these member of sudo rules.
        :type in_sudorule: Str
        :param no_group: Search for groups without these member groups.
        :type no_group: Str
        :param no_user: Search for groups without these member users.
        :type no_user: Str
        :param not_in_group: Search for groups without these member of groups.
        :type not_in_group: Str
        :param not_in_hbacrule: Search for groups without these member of HBAC rules.
        :type not_in_hbacrule: Str
        :param not_in_netgroup: Search for groups without these member of netgroups.
        :type not_in_netgroup: Str
        :param not_in_role: Search for groups without these member of roles.
        :type not_in_role: Str
        :param not_in_sudorule: Search for groups without these member of sudo rules.
        :type not_in_sudorule: Str
        :param user: Search for groups with these member users.
        :type user: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param external: search for groups with support of external non-IPA members from trusted domains
        :type external: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param nonposix: search for non-POSIX groups
        :type nonposix: Flag
        :param pkey_only: Results should contain primary key attribute only ("group-name")
        :type pkey_only: Flag
        :param posix: search for POSIX groups
        :type posix: Flag
        :param private: search for private groups
        :type private: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param gidnumber: GID (use this option to set it manually)
        :type gidnumber: Int
        :param description: Group description
        :type description: Str
        :param cn: Group name
        :type cn: Str
        """
        method = 'group_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if group:
            _params['group'] = group
        if in_group:
            _params['in_group'] = in_group
        if in_hbacrule:
            _params['in_hbacrule'] = in_hbacrule
        if in_netgroup:
            _params['in_netgroup'] = in_netgroup
        if in_role:
            _params['in_role'] = in_role
        if in_sudorule:
            _params['in_sudorule'] = in_sudorule
        if no_group:
            _params['no_group'] = no_group
        if no_user:
            _params['no_user'] = no_user
        if not_in_group:
            _params['not_in_group'] = not_in_group
        if not_in_hbacrule:
            _params['not_in_hbacrule'] = not_in_hbacrule
        if not_in_netgroup:
            _params['not_in_netgroup'] = not_in_netgroup
        if not_in_role:
            _params['not_in_role'] = not_in_role
        if not_in_sudorule:
            _params['not_in_sudorule'] = not_in_sudorule
        if user:
            _params['user'] = user
        _params['all'] = opt_all
        _params['external'] = external
        _params['no_members'] = no_members
        _params['nonposix'] = nonposix
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['posix'] = posix
        _params['private'] = private
        _params['raw'] = raw
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def group_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        external=False,
        no_members=False,
        posix=False,
        raw=False,
        rights=False,
        gidnumber=None,
        description=None,
    ):
        """Modify a group.
        :param cn: Group name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the group object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param external: change to support external non-IPA members from trusted domains
        :type external: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param posix: change to a POSIX group
        :type posix: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param gidnumber: GID (use this option to set it manually)
        :type gidnumber: Int
        :param description: Group description
        :type description: Str
        """
        method = 'group_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['external'] = external
        _params['no_members'] = no_members
        _params['posix'] = posix
        _params['raw'] = raw
        _params['rights'] = rights
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def group_remove_member(
        self,
        cn,
        ipaexternalmember=None,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Remove members from a group.
        :param cn: Group name
        :type cn: Str
        :param ipaexternalmember: Members of a trusted domain in DOM\name or name@domain form
        :type ipaexternalmember: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'group_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if ipaexternalmember:
            _params['ipaexternalmember'] = ipaexternalmember
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def group_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a named group.
        :param cn: Group name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'group_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def hbacrule_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        ipaenabledflag=None,
        description=None,
        externalhost=None,
        hostcategory=None,
        servicecategory=None,
        sourcehostcategory=None,
        usercategory=None,
        accessruletype='allow',
    ):
        """Create a new HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param servicecategory: Service category the rule applies to
        :type servicecategory: StrEnum
        :param sourcehostcategory: Source host category the rule applies to
        :type sourcehostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        :param accessruletype: Rule type (allow)
        :type accessruletype: StrEnum
        """
        method = 'hbacrule_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if servicecategory:
            _params['servicecategory'] = servicecategory
        if sourcehostcategory:
            _params['sourcehostcategory'] = sourcehostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        _params['accessruletype'] = accessruletype
        
        return self._request(method, _args, _params)

    def hbacrule_add_host(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Add target hosts and hostgroups to an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        """
        method = 'hbacrule_add_host'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def hbacrule_add_service(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hbacsvcgroup=None,
        hbacsvc=None,
    ):
        """Add services to an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hbacsvcgroup: HBAC service groups to add
        :type hbacsvcgroup: Str
        :param hbacsvc: HBAC services to add
        :type hbacsvc: Str
        """
        method = 'hbacrule_add_service'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hbacsvcgroup:
            _params['hbacsvcgroup'] = hbacsvcgroup
        if hbacsvc:
            _params['hbacsvc'] = hbacsvc
        
        return self._request(method, _args, _params)

    def hbacrule_add_sourcehost(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """None
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        """
        method = 'hbacrule_add_sourcehost'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def hbacrule_add_user(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Add users and groups to an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param user: users to add
        :type user: Str
        """
        method = 'hbacrule_add_user'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def hbacrule_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'hbacrule_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def hbacrule_disable(
        self,
        cn,
    ):
        """Disable an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        """
        method = 'hbacrule_disable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def hbacrule_enable(
        self,
        cn,
    ):
        """Enable an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        """
        method = 'hbacrule_enable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def hbacrule_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        ipaenabledflag=None,
        description=None,
        externalhost=None,
        cn=None,
        hostcategory=None,
        servicecategory=None,
        sourcehostcategory=None,
        usercategory=None,
        accessruletype='allow',
    ):
        """Search for HBAC rules.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param cn: Rule name
        :type cn: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param servicecategory: Service category the rule applies to
        :type servicecategory: StrEnum
        :param sourcehostcategory: Source host category the rule applies to
        :type sourcehostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        :param accessruletype: Rule type (allow)
        :type accessruletype: StrEnum
        """
        method = 'hbacrule_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if cn:
            _params['cn'] = cn
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if servicecategory:
            _params['servicecategory'] = servicecategory
        if sourcehostcategory:
            _params['sourcehostcategory'] = sourcehostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        if accessruletype:
            _params['accessruletype'] = accessruletype
        
        return self._request(method, _args, _params)

    def hbacrule_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        ipaenabledflag=None,
        description=None,
        externalhost=None,
        hostcategory=None,
        servicecategory=None,
        sourcehostcategory=None,
        usercategory=None,
        accessruletype='allow',
    ):
        """Modify an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the HBAC rule object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param servicecategory: Service category the rule applies to
        :type servicecategory: StrEnum
        :param sourcehostcategory: Source host category the rule applies to
        :type sourcehostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        :param accessruletype: Rule type (allow)
        :type accessruletype: StrEnum
        """
        method = 'hbacrule_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if servicecategory:
            _params['servicecategory'] = servicecategory
        if sourcehostcategory:
            _params['sourcehostcategory'] = sourcehostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        if accessruletype:
            _params['accessruletype'] = accessruletype
        
        return self._request(method, _args, _params)

    def hbacrule_remove_host(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Remove target hosts and hostgroups from an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        """
        method = 'hbacrule_remove_host'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def hbacrule_remove_service(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hbacsvcgroup=None,
        hbacsvc=None,
    ):
        """Remove service and service groups from an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hbacsvcgroup: HBAC service groups to remove
        :type hbacsvcgroup: Str
        :param hbacsvc: HBAC services to remove
        :type hbacsvc: Str
        """
        method = 'hbacrule_remove_service'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hbacsvcgroup:
            _params['hbacsvcgroup'] = hbacsvcgroup
        if hbacsvc:
            _params['hbacsvc'] = hbacsvc
        
        return self._request(method, _args, _params)

    def hbacrule_remove_sourcehost(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """None
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        """
        method = 'hbacrule_remove_sourcehost'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def hbacrule_remove_user(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Remove users and groups from an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'hbacrule_remove_user'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def hbacrule_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display the properties of an HBAC rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'hbacrule_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def hbacsvc_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        description=None,
    ):
        """Add a new HBAC service.
        :param cn: HBAC service
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: HBAC service description
        :type description: Str
        """
        method = 'hbacsvc_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def hbacsvc_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete an existing HBAC service.
        :param cn: HBAC service
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'hbacsvc_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def hbacsvc_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        description=None,
        cn=None,
    ):
        """Search for HBAC services.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("service")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: HBAC service description
        :type description: Str
        :param cn: HBAC service
        :type cn: Str
        """
        method = 'hbacsvc_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def hbacsvc_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify an HBAC service.
        :param cn: HBAC service
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: HBAC service description
        :type description: Str
        """
        method = 'hbacsvc_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def hbacsvc_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about an HBAC service.
        :param cn: HBAC service
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'hbacsvc_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def hbacsvcgroup_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        description=None,
    ):
        """Add a new HBAC service group.
        :param cn: Service group name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: HBAC service group description
        :type description: Str
        """
        method = 'hbacsvcgroup_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def hbacsvcgroup_add_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hbacsvc=None,
    ):
        """Add members to an HBAC service group.
        :param cn: Service group name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hbacsvc: HBAC services to add
        :type hbacsvc: Str
        """
        method = 'hbacsvcgroup_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hbacsvc:
            _params['hbacsvc'] = hbacsvc
        
        return self._request(method, _args, _params)

    def hbacsvcgroup_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete an HBAC service group.
        :param cn: Service group name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'hbacsvcgroup_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def hbacsvcgroup_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        description=None,
        cn=None,
    ):
        """Search for an HBAC service group.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: HBAC service group description
        :type description: Str
        :param cn: Service group name
        :type cn: Str
        """
        method = 'hbacsvcgroup_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def hbacsvcgroup_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify an HBAC service group.
        :param cn: Service group name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: HBAC service group description
        :type description: Str
        """
        method = 'hbacsvcgroup_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def hbacsvcgroup_remove_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hbacsvc=None,
    ):
        """Remove members from an HBAC service group.
        :param cn: Service group name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hbacsvc: HBAC services to remove
        :type hbacsvc: Str
        """
        method = 'hbacsvcgroup_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hbacsvc:
            _params['hbacsvc'] = hbacsvc
        
        return self._request(method, _args, _params)

    def hbacsvcgroup_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about an HBAC service group.
        :param cn: Service group name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'hbacsvcgroup_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def hbactest(
        self,
        targethost,
        service,
        user,
        sizelimit=None,
        rules=None,
        sourcehost=None,
        disabled=False,
        enabled=False,
        nodetail=False,
    ):
        """Simulate use of Host-based access controls
        :param sizelimit: Maximum number of rules to process when no --rules is specified
        :type sizelimit: Int
        :param targethost: Target host
        :type targethost: Str
        :param rules: Rules to test. If not specified, --enabled is assumed
        :type rules: Str
        :param service: Service
        :type service: Str
        :param sourcehost: Source host
        :type sourcehost: Str
        :param user: User name
        :type user: Str
        :param disabled: Include all disabled IPA rules into test
        :type disabled: Flag
        :param enabled: Include all enabled IPA rules into test [default]
        :type enabled: Flag
        :param nodetail: Hide details which rules are matched, not matched, or invalid
        :type nodetail: Flag
        """
        method = 'hbactest'
        
        _args = list()
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        _params['targethost'] = targethost
        if rules:
            _params['rules'] = rules
        _params['service'] = service
        if sourcehost:
            _params['sourcehost'] = sourcehost
        _params['user'] = user
        if disabled:
            _params['disabled'] = disabled
        if enabled:
            _params['enabled'] = enabled
        if nodetail:
            _params['nodetail'] = nodetail
        
        return self._request(method, _args, _params)

    def host_add(
        self,
        fqdn,
        ipakrbokasdelegate=None,
        ipakrboktoauthasdelegate=None,
        ipakrbrequirespreauth=None,
        addattr=None,
        ip_address=None,
        opt_setattr=None,
        opt_all=True,
        force=False,
        no_members=False,
        no_reverse=False,
        random=False,
        raw=False,
        usercertificate=None,
        krbprincipalauthind=None,
        userclass=None,
        description=None,
        ipaassignedidview=None,
        l=None,
        nshostlocation=None,
        macaddress=None,
        nsosversion=None,
        userpassword=None,
        nshardwareplatform=None,
        ipasshpubkey=None,
    ):
        """Add a new host.
        :param fqdn: Host name
        :type fqdn: Str
        :param ipakrbokasdelegate: Client credentials may be delegated to the service
        :type ipakrbokasdelegate: Bool
        :param ipakrboktoauthasdelegate: The service is allowed to authenticate on behalf of a client
        :type ipakrboktoauthasdelegate: Bool
        :param ipakrbrequirespreauth: Pre-authentication is required for the service
        :type ipakrbrequirespreauth: Bool
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param ip_address: Add the host to DNS with this IP address
        :type ip_address: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param force: force host name even if not in DNS
        :type force: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param no_reverse: skip reverse DNS detection
        :type no_reverse: Flag
        :param random: Generate a random password to be used in bulk enrollment
        :type random: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded host certificate
        :type usercertificate: Certificate
        :param krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type krbprincipalauthind: Str
        :param userclass: Host category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param description: A description of this host
        :type description: Str
        :param ipaassignedidview: Assigned ID View
        :type ipaassignedidview: Str
        :param l: Host locality (e.g. "Baltimore, MD")
        :type l: Str
        :param nshostlocation: Host location (e.g. "Lab 2")
        :type nshostlocation: Str
        :param macaddress: Hardware MAC address(es) on this host
        :type macaddress: Str
        :param nsosversion: Host operating system and version (e.g. "Fedora 9")
        :type nsosversion: Str
        :param userpassword: Password used in bulk enrollment
        :type userpassword: Str
        :param nshardwareplatform: Host hardware platform (e.g. "Lenovo T61")
        :type nshardwareplatform: Str
        :param ipasshpubkey: SSH public key
        :type ipasshpubkey: Str
        """
        method = 'host_add'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        if ipakrbokasdelegate:
            _params['ipakrbokasdelegate'] = ipakrbokasdelegate
        if ipakrboktoauthasdelegate:
            _params['ipakrboktoauthasdelegate'] = ipakrboktoauthasdelegate
        if ipakrbrequirespreauth:
            _params['ipakrbrequirespreauth'] = ipakrbrequirespreauth
        if addattr:
            _params['addattr'] = addattr
        if ip_address:
            _params['ip_address'] = ip_address
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['force'] = force
        _params['no_members'] = no_members
        _params['no_reverse'] = no_reverse
        if random:
            _params['random'] = random
        _params['raw'] = raw
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbprincipalauthind:
            _params['krbprincipalauthind'] = krbprincipalauthind
        if userclass:
            _params['userclass'] = userclass
        if description:
            _params['description'] = description
        if ipaassignedidview:
            _params['ipaassignedidview'] = ipaassignedidview
        if l:
            _params['l'] = l
        if nshostlocation:
            _params['nshostlocation'] = nshostlocation
        if macaddress:
            _params['macaddress'] = macaddress
        if nsosversion:
            _params['nsosversion'] = nsosversion
        if userpassword:
            _params['userpassword'] = userpassword
        if nshardwareplatform:
            _params['nshardwareplatform'] = nshardwareplatform
        if ipasshpubkey:
            _params['ipasshpubkey'] = ipasshpubkey
        
        return self._request(method, _args, _params)

    def host_add_cert(
        self,
        fqdn,
        usercertificate,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add certificates to host entry
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded host certificate
        :type usercertificate: Certificate
        """
        method = 'host_add_cert'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def host_add_managedby(
        self,
        fqdn,
        opt_all=True,
        no_members=False,
        raw=False,
        host=None,
    ):
        """Add hosts that can manage this host.
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param host: hosts to add
        :type host: Str
        """
        method = 'host_add_managedby'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def host_add_principal(
        self,
        fqdn,
        krbprincipalname,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add new principal alias to host entry
        :param fqdn: Host name
        :type fqdn: Str
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'host_add_principal'
        
        _args = list()
        _args.append(fqdn)
        _args.append(krbprincipalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def host_allow_create_keytab(
        self,
        fqdn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        user=None,
    ):
        """Allow users, groups, hosts or host groups to create a keytab of this host.
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        :param user: users to add
        :type user: Str
        """
        method = 'host_allow_create_keytab'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def host_allow_retrieve_keytab(
        self,
        fqdn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        user=None,
    ):
        """Allow users, groups, hosts or host groups to retrieve a keytab of this host.
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        :param user: users to add
        :type user: Str
        """
        method = 'host_allow_retrieve_keytab'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def host_del(
        self,
        fqdn,
        opt_continue=False,
        updatedns=False,
    ):
        """Delete a host.
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        :param updatedns: Remove A, AAAA, SSHFP and PTR records of the host(s) managed by IPA DNS
        :type updatedns: Flag
        """
        method = 'host_del'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['continue'] = opt_continue
        if updatedns:
            _params['updatedns'] = updatedns
        
        return self._request(method, _args, _params)

    def host_disable(
        self,
        fqdn,
    ):
        """Disable the Kerberos key, SSL certificate and all services of a host.
        :param fqdn: Host name
        :type fqdn: Str
        """
        method = 'host_disable'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def host_disallow_create_keytab(
        self,
        fqdn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        user=None,
    ):
        """Disallow users, groups, hosts or host groups to create a keytab of this host.
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'host_disallow_create_keytab'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def host_disallow_retrieve_keytab(
        self,
        fqdn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        user=None,
    ):
        """Disallow users, groups, hosts or host groups to retrieve a keytab of this host.
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'host_disallow_retrieve_keytab'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def host_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        enroll_by_user=None,
        in_hbacrule=None,
        in_hostgroup=None,
        in_netgroup=None,
        in_role=None,
        in_sudorule=None,
        man_by_host=None,
        man_host=None,
        not_enroll_by_user=None,
        not_in_hbacrule=None,
        not_in_hostgroup=None,
        not_in_netgroup=None,
        not_in_role=None,
        not_in_sudorule=None,
        not_man_by_host=None,
        not_man_host=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        usercertificate=None,
        krbprincipalauthind=None,
        userclass=None,
        description=None,
        fqdn=None,
        ipaassignedidview=None,
        l=None,
        nshostlocation=None,
        macaddress=None,
        nsosversion=None,
        userpassword=None,
        nshardwareplatform=None,
    ):
        """Search for hosts.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param enroll_by_user: Search for hosts with these enrolled by users.
        :type enroll_by_user: Str
        :param in_hbacrule: Search for hosts with these member of HBAC rules.
        :type in_hbacrule: Str
        :param in_hostgroup: Search for hosts with these member of host groups.
        :type in_hostgroup: Str
        :param in_netgroup: Search for hosts with these member of netgroups.
        :type in_netgroup: Str
        :param in_role: Search for hosts with these member of roles.
        :type in_role: Str
        :param in_sudorule: Search for hosts with these member of sudo rules.
        :type in_sudorule: Str
        :param man_by_host: Search for hosts with these managed by hosts.
        :type man_by_host: Str
        :param man_host: Search for hosts with these managing hosts.
        :type man_host: Str
        :param not_enroll_by_user: Search for hosts without these enrolled by users.
        :type not_enroll_by_user: Str
        :param not_in_hbacrule: Search for hosts without these member of HBAC rules.
        :type not_in_hbacrule: Str
        :param not_in_hostgroup: Search for hosts without these member of host groups.
        :type not_in_hostgroup: Str
        :param not_in_netgroup: Search for hosts without these member of netgroups.
        :type not_in_netgroup: Str
        :param not_in_role: Search for hosts without these member of roles.
        :type not_in_role: Str
        :param not_in_sudorule: Search for hosts without these member of sudo rules.
        :type not_in_sudorule: Str
        :param not_man_by_host: Search for hosts without these managed by hosts.
        :type not_man_by_host: Str
        :param not_man_host: Search for hosts without these managing hosts.
        :type not_man_host: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("hostname")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded host certificate
        :type usercertificate: Certificate
        :param krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type krbprincipalauthind: Str
        :param userclass: Host category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param description: A description of this host
        :type description: Str
        :param fqdn: Host name
        :type fqdn: Str
        :param ipaassignedidview: Assigned ID View
        :type ipaassignedidview: Str
        :param l: Host locality (e.g. "Baltimore, MD")
        :type l: Str
        :param nshostlocation: Host location (e.g. "Lab 2")
        :type nshostlocation: Str
        :param macaddress: Hardware MAC address(es) on this host
        :type macaddress: Str
        :param nsosversion: Host operating system and version (e.g. "Fedora 9")
        :type nsosversion: Str
        :param userpassword: Password used in bulk enrollment
        :type userpassword: Str
        :param nshardwareplatform: Host hardware platform (e.g. "Lenovo T61")
        :type nshardwareplatform: Str
        """
        method = 'host_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if enroll_by_user:
            _params['enroll_by_user'] = enroll_by_user
        if in_hbacrule:
            _params['in_hbacrule'] = in_hbacrule
        if in_hostgroup:
            _params['in_hostgroup'] = in_hostgroup
        if in_netgroup:
            _params['in_netgroup'] = in_netgroup
        if in_role:
            _params['in_role'] = in_role
        if in_sudorule:
            _params['in_sudorule'] = in_sudorule
        if man_by_host:
            _params['man_by_host'] = man_by_host
        if man_host:
            _params['man_host'] = man_host
        if not_enroll_by_user:
            _params['not_enroll_by_user'] = not_enroll_by_user
        if not_in_hbacrule:
            _params['not_in_hbacrule'] = not_in_hbacrule
        if not_in_hostgroup:
            _params['not_in_hostgroup'] = not_in_hostgroup
        if not_in_netgroup:
            _params['not_in_netgroup'] = not_in_netgroup
        if not_in_role:
            _params['not_in_role'] = not_in_role
        if not_in_sudorule:
            _params['not_in_sudorule'] = not_in_sudorule
        if not_man_by_host:
            _params['not_man_by_host'] = not_man_by_host
        if not_man_host:
            _params['not_man_host'] = not_man_host
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbprincipalauthind:
            _params['krbprincipalauthind'] = krbprincipalauthind
        if userclass:
            _params['userclass'] = userclass
        if description:
            _params['description'] = description
        if fqdn:
            _params['fqdn'] = fqdn
        if ipaassignedidview:
            _params['ipaassignedidview'] = ipaassignedidview
        if l:
            _params['l'] = l
        if nshostlocation:
            _params['nshostlocation'] = nshostlocation
        if macaddress:
            _params['macaddress'] = macaddress
        if nsosversion:
            _params['nsosversion'] = nsosversion
        if userpassword:
            _params['userpassword'] = userpassword
        if nshardwareplatform:
            _params['nshardwareplatform'] = nshardwareplatform
        
        return self._request(method, _args, _params)

    def host_mod(
        self,
        fqdn,
        ipakrbokasdelegate=None,
        ipakrboktoauthasdelegate=None,
        ipakrbrequirespreauth=None,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        random=False,
        raw=False,
        rights=False,
        updatedns=False,
        usercertificate=None,
        krbprincipalname=None,
        krbprincipalauthind=None,
        userclass=None,
        description=None,
        ipaassignedidview=None,
        l=None,
        nshostlocation=None,
        macaddress=None,
        nsosversion=None,
        userpassword=None,
        nshardwareplatform=None,
        ipasshpubkey=None,
    ):
        """Modify information about a host.
        :param fqdn: Host name
        :type fqdn: Str
        :param ipakrbokasdelegate: Client credentials may be delegated to the service
        :type ipakrbokasdelegate: Bool
        :param ipakrboktoauthasdelegate: The service is allowed to authenticate on behalf of a client
        :type ipakrboktoauthasdelegate: Bool
        :param ipakrbrequirespreauth: Pre-authentication is required for the service
        :type ipakrbrequirespreauth: Bool
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param random: Generate a random password to be used in bulk enrollment
        :type random: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param updatedns: Update DNS entries
        :type updatedns: Flag
        :param usercertificate: Base-64 encoded host certificate
        :type usercertificate: Certificate
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type krbprincipalauthind: Str
        :param userclass: Host category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param description: A description of this host
        :type description: Str
        :param ipaassignedidview: Assigned ID View
        :type ipaassignedidview: Str
        :param l: Host locality (e.g. "Baltimore, MD")
        :type l: Str
        :param nshostlocation: Host location (e.g. "Lab 2")
        :type nshostlocation: Str
        :param macaddress: Hardware MAC address(es) on this host
        :type macaddress: Str
        :param nsosversion: Host operating system and version (e.g. "Fedora 9")
        :type nsosversion: Str
        :param userpassword: Password used in bulk enrollment
        :type userpassword: Str
        :param nshardwareplatform: Host hardware platform (e.g. "Lenovo T61")
        :type nshardwareplatform: Str
        :param ipasshpubkey: SSH public key
        :type ipasshpubkey: Str
        """
        method = 'host_mod'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        if ipakrbokasdelegate:
            _params['ipakrbokasdelegate'] = ipakrbokasdelegate
        if ipakrboktoauthasdelegate:
            _params['ipakrboktoauthasdelegate'] = ipakrboktoauthasdelegate
        if ipakrbrequirespreauth:
            _params['ipakrbrequirespreauth'] = ipakrbrequirespreauth
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if random:
            _params['random'] = random
        _params['raw'] = raw
        _params['rights'] = rights
        if updatedns:
            _params['updatedns'] = updatedns
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        if krbprincipalauthind:
            _params['krbprincipalauthind'] = krbprincipalauthind
        if userclass:
            _params['userclass'] = userclass
        if description:
            _params['description'] = description
        if ipaassignedidview:
            _params['ipaassignedidview'] = ipaassignedidview
        if l:
            _params['l'] = l
        if nshostlocation:
            _params['nshostlocation'] = nshostlocation
        if macaddress:
            _params['macaddress'] = macaddress
        if nsosversion:
            _params['nsosversion'] = nsosversion
        if userpassword:
            _params['userpassword'] = userpassword
        if nshardwareplatform:
            _params['nshardwareplatform'] = nshardwareplatform
        if ipasshpubkey:
            _params['ipasshpubkey'] = ipasshpubkey
        
        return self._request(method, _args, _params)

    def host_remove_cert(
        self,
        fqdn,
        usercertificate,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove certificates from host entry
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded host certificate
        :type usercertificate: Certificate
        """
        method = 'host_remove_cert'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def host_remove_managedby(
        self,
        fqdn,
        opt_all=True,
        no_members=False,
        raw=False,
        host=None,
    ):
        """Remove hosts that can manage this host.
        :param fqdn: Host name
        :type fqdn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param host: hosts to remove
        :type host: Str
        """
        method = 'host_remove_managedby'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def host_remove_principal(
        self,
        fqdn,
        krbprincipalname,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove principal alias from a host entry
        :param fqdn: Host name
        :type fqdn: Str
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'host_remove_principal'
        
        _args = list()
        _args.append(fqdn)
        _args.append(krbprincipalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def host_show(
        self,
        fqdn,
        out=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a host.
        :param fqdn: Host name
        :type fqdn: Str
        :param out: file to store certificate in
        :type out: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'host_show'
        
        _args = list()
        _args.append(fqdn)
        
        _params = dict()
        if out:
            _params['out'] = out
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def hostgroup_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        description=None,
    ):
        """Add a new hostgroup.
        :param cn: Name of host-group
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this host-group
        :type description: Str
        """
        method = 'hostgroup_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def hostgroup_add_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Add members to a hostgroup.
        :param cn: Name of host-group
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        """
        method = 'hostgroup_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def hostgroup_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a hostgroup.
        :param cn: Name of host-group
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'hostgroup_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def hostgroup_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        hostgroup=None,
        host=None,
        in_hbacrule=None,
        in_hostgroup=None,
        in_netgroup=None,
        in_sudorule=None,
        no_hostgroup=None,
        no_host=None,
        not_in_hbacrule=None,
        not_in_hostgroup=None,
        not_in_netgroup=None,
        not_in_sudorule=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        description=None,
        cn=None,
    ):
        """Search for hostgroups.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param hostgroup: Search for host groups with these member host groups.
        :type hostgroup: Str
        :param host: Search for host groups with these member hosts.
        :type host: Str
        :param in_hbacrule: Search for host groups with these member of HBAC rules.
        :type in_hbacrule: Str
        :param in_hostgroup: Search for host groups with these member of host groups.
        :type in_hostgroup: Str
        :param in_netgroup: Search for host groups with these member of netgroups.
        :type in_netgroup: Str
        :param in_sudorule: Search for host groups with these member of sudo rules.
        :type in_sudorule: Str
        :param no_hostgroup: Search for host groups without these member host groups.
        :type no_hostgroup: Str
        :param no_host: Search for host groups without these member hosts.
        :type no_host: Str
        :param not_in_hbacrule: Search for host groups without these member of HBAC rules.
        :type not_in_hbacrule: Str
        :param not_in_hostgroup: Search for host groups without these member of host groups.
        :type not_in_hostgroup: Str
        :param not_in_netgroup: Search for host groups without these member of netgroups.
        :type not_in_netgroup: Str
        :param not_in_sudorule: Search for host groups without these member of sudo rules.
        :type not_in_sudorule: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("hostgroup-name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this host-group
        :type description: Str
        :param cn: Name of host-group
        :type cn: Str
        """
        method = 'hostgroup_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if in_hbacrule:
            _params['in_hbacrule'] = in_hbacrule
        if in_hostgroup:
            _params['in_hostgroup'] = in_hostgroup
        if in_netgroup:
            _params['in_netgroup'] = in_netgroup
        if in_sudorule:
            _params['in_sudorule'] = in_sudorule
        if no_hostgroup:
            _params['no_hostgroup'] = no_hostgroup
        if no_host:
            _params['no_host'] = no_host
        if not_in_hbacrule:
            _params['not_in_hbacrule'] = not_in_hbacrule
        if not_in_hostgroup:
            _params['not_in_hostgroup'] = not_in_hostgroup
        if not_in_netgroup:
            _params['not_in_netgroup'] = not_in_netgroup
        if not_in_sudorule:
            _params['not_in_sudorule'] = not_in_sudorule
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def hostgroup_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify a hostgroup.
        :param cn: Name of host-group
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: A description of this host-group
        :type description: Str
        """
        method = 'hostgroup_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def hostgroup_remove_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Remove members from a hostgroup.
        :param cn: Name of host-group
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        """
        method = 'hostgroup_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def hostgroup_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a hostgroup.
        :param cn: Name of host-group
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'hostgroup_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
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
        idviewcn,
        ipaanchoruuid,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        fallback_to_ldap=False,
        raw=False,
        gidnumber=None,
        description=None,
        cn=None,
    ):
        """Add a new Group ID override.
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param description: Description
        :type description: Str
        :param cn: Group name
        :type cn: Str
        """
        method = 'idoverridegroup_add'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        _params['raw'] = raw
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def idoverridegroup_del(
        self,
        idviewcn,
        ipaanchoruuid,
        opt_continue=False,
        fallback_to_ldap=False,
    ):
        """Delete an Group ID override.
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        """
        method = 'idoverridegroup_del'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        _params['continue'] = opt_continue
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        
        return self._request(method, _args, _params)

    def idoverridegroup_find(
        self,
        idviewcn,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        fallback_to_ldap=False,
        pkey_only=False,
        raw=False,
        gidnumber=None,
        ipaanchoruuid=None,
        description=None,
        cn=None,
    ):
        """Search for an Group ID override.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param pkey_only: Results should contain primary key attribute only ("anchor")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param description: Description
        :type description: Str
        :param cn: Group name
        :type cn: Str
        """
        method = 'idoverridegroup_find'
        
        _args = list()
        _args.append(criteria)
        _args.append(idviewcn)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if ipaanchoruuid:
            _params['ipaanchoruuid'] = ipaanchoruuid
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def idoverridegroup_mod(
        self,
        idviewcn,
        ipaanchoruuid,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        fallback_to_ldap=False,
        raw=False,
        rights=False,
        gidnumber=None,
        description=None,
        cn=None,
    ):
        """Modify an Group ID override.
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the Group ID override object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param description: Description
        :type description: Str
        :param cn: Group name
        :type cn: Str
        """
        method = 'idoverridegroup_mod'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        _params['raw'] = raw
        _params['rights'] = rights
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def idoverridegroup_show(
        self,
        idviewcn,
        ipaanchoruuid,
        opt_all=True,
        fallback_to_ldap=False,
        raw=False,
        rights=False,
    ):
        """Display information about an Group ID override.
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'idoverridegroup_show'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def idoverrideuser_add(
        self,
        idviewcn,
        ipaanchoruuid,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        fallback_to_ldap=False,
        raw=False,
        usercertificate=None,
        gidnumber=None,
        uidnumber=None,
        description=None,
        gecos=None,
        homedirectory=None,
        ipaoriginaluid=None,
        uid=None,
        loginshell=None,
        ipasshpubkey=None,
    ):
        """Add a new User ID override.
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number
        :type uidnumber: Int
        :param description: Description
        :type description: Str
        :param gecos: GECOS
        :type gecos: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param ipaoriginaluid: <ipaoriginaluid>
        :type ipaoriginaluid: Str
        :param uid: User login
        :type uid: Str
        :param loginshell: Login shell
        :type loginshell: Str
        :param ipasshpubkey: SSH public key
        :type ipasshpubkey: Str
        """
        method = 'idoverrideuser_add'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        _params['raw'] = raw
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if description:
            _params['description'] = description
        if gecos:
            _params['gecos'] = gecos
        if homedirectory:
            _params['homedirectory'] = homedirectory
        if ipaoriginaluid:
            _params['ipaoriginaluid'] = ipaoriginaluid
        if uid:
            _params['uid'] = uid
        if loginshell:
            _params['loginshell'] = loginshell
        if ipasshpubkey:
            _params['ipasshpubkey'] = ipasshpubkey
        
        return self._request(method, _args, _params)

    def idoverrideuser_add_cert(
        self,
        idviewcn,
        ipaanchoruuid,
        usercertificate,
        opt_all=True,
        fallback_to_ldap=False,
        raw=False,
    ):
        """Add one or more certificates to the idoverrideuser entry
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        """
        method = 'idoverrideuser_add_cert'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def idoverrideuser_del(
        self,
        idviewcn,
        ipaanchoruuid,
        opt_continue=False,
        fallback_to_ldap=False,
    ):
        """Delete an User ID override.
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        """
        method = 'idoverrideuser_del'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        _params['continue'] = opt_continue
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        
        return self._request(method, _args, _params)

    def idoverrideuser_find(
        self,
        idviewcn,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        fallback_to_ldap=False,
        pkey_only=False,
        raw=False,
        gidnumber=None,
        uidnumber=None,
        ipaanchoruuid=None,
        description=None,
        gecos=None,
        homedirectory=None,
        ipaoriginaluid=None,
        uid=None,
        loginshell=None,
    ):
        """Search for an User ID override.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param pkey_only: Results should contain primary key attribute only ("anchor")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number
        :type uidnumber: Int
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param description: Description
        :type description: Str
        :param gecos: GECOS
        :type gecos: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param ipaoriginaluid: <ipaoriginaluid>
        :type ipaoriginaluid: Str
        :param uid: User login
        :type uid: Str
        :param loginshell: Login shell
        :type loginshell: Str
        """
        method = 'idoverrideuser_find'
        
        _args = list()
        _args.append(criteria)
        _args.append(idviewcn)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if ipaanchoruuid:
            _params['ipaanchoruuid'] = ipaanchoruuid
        if description:
            _params['description'] = description
        if gecos:
            _params['gecos'] = gecos
        if homedirectory:
            _params['homedirectory'] = homedirectory
        if ipaoriginaluid:
            _params['ipaoriginaluid'] = ipaoriginaluid
        if uid:
            _params['uid'] = uid
        if loginshell:
            _params['loginshell'] = loginshell
        
        return self._request(method, _args, _params)

    def idoverrideuser_mod(
        self,
        idviewcn,
        ipaanchoruuid,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        fallback_to_ldap=False,
        raw=False,
        rights=False,
        usercertificate=None,
        gidnumber=None,
        uidnumber=None,
        description=None,
        gecos=None,
        homedirectory=None,
        ipaoriginaluid=None,
        uid=None,
        loginshell=None,
        ipasshpubkey=None,
    ):
        """Modify an User ID override.
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the User ID override object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number
        :type uidnumber: Int
        :param description: Description
        :type description: Str
        :param gecos: GECOS
        :type gecos: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param ipaoriginaluid: <ipaoriginaluid>
        :type ipaoriginaluid: Str
        :param uid: User login
        :type uid: Str
        :param loginshell: Login shell
        :type loginshell: Str
        :param ipasshpubkey: SSH public key
        :type ipasshpubkey: Str
        """
        method = 'idoverrideuser_mod'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        _params['raw'] = raw
        _params['rights'] = rights
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if description:
            _params['description'] = description
        if gecos:
            _params['gecos'] = gecos
        if homedirectory:
            _params['homedirectory'] = homedirectory
        if ipaoriginaluid:
            _params['ipaoriginaluid'] = ipaoriginaluid
        if uid:
            _params['uid'] = uid
        if loginshell:
            _params['loginshell'] = loginshell
        if ipasshpubkey:
            _params['ipasshpubkey'] = ipasshpubkey
        
        return self._request(method, _args, _params)

    def idoverrideuser_remove_cert(
        self,
        idviewcn,
        ipaanchoruuid,
        usercertificate,
        opt_all=True,
        fallback_to_ldap=False,
        raw=False,
    ):
        """Remove one or more certificates to the idoverrideuser entry
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        """
        method = 'idoverrideuser_remove_cert'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def idoverrideuser_show(
        self,
        idviewcn,
        ipaanchoruuid,
        opt_all=True,
        fallback_to_ldap=False,
        raw=False,
        rights=False,
    ):
        """Display information about an User ID override.
        :param idviewcn: ID View Name
        :type idviewcn: Str
        :param ipaanchoruuid: Anchor to override
        :type ipaanchoruuid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param fallback_to_ldap: Allow falling back to AD DC LDAP when resolving AD trusted objects. For two-way trusts only.
        :type fallback_to_ldap: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'idoverrideuser_show'
        
        _args = list()
        _args.append(idviewcn)
        _args.append(ipaanchoruuid)
        
        _params = dict()
        _params['all'] = opt_all
        if fallback_to_ldap:
            _params['fallback_to_ldap'] = fallback_to_ldap
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def idrange_add(
        self,
        cn,
        ipabaseid,
        ipaidrangesize,
        addattr=None,
        ipanttrusteddomainname=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        ipabaserid=None,
        ipasecondarybaserid=None,
        ipanttrusteddomainsid=None,
        iparangetype=None,
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


        :param cn: Range name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param ipanttrusteddomainname: Name of the trusted domain
        :type ipanttrusteddomainname: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipabaseid: First Posix ID of the range
        :type ipabaseid: Int
        :param ipaidrangesize: Number of IDs in the range
        :type ipaidrangesize: Int
        :param ipabaserid: First RID of the corresponding RID range
        :type ipabaserid: Int
        :param ipasecondarybaserid: First RID of the secondary RID range
        :type ipasecondarybaserid: Int
        :param ipanttrusteddomainsid: Domain SID of the trusted domain
        :type ipanttrusteddomainsid: Str
        :param iparangetype: ID range type, one of ipa-ad-trust, ipa-ad-trust-posix, ipa-local
        :type iparangetype: StrEnum
        """
        method = 'idrange_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if ipanttrusteddomainname:
            _params['ipanttrusteddomainname'] = ipanttrusteddomainname
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['ipabaseid'] = ipabaseid
        _params['ipaidrangesize'] = ipaidrangesize
        if ipabaserid:
            _params['ipabaserid'] = ipabaserid
        if ipasecondarybaserid:
            _params['ipasecondarybaserid'] = ipasecondarybaserid
        if ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = ipanttrusteddomainsid
        if iparangetype:
            _params['iparangetype'] = iparangetype
        
        return self._request(method, _args, _params)

    def idrange_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete an ID range.
        :param cn: Range name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'idrange_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def idrange_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        ipabaseid=None,
        ipaidrangesize=None,
        ipabaserid=None,
        ipasecondarybaserid=None,
        ipanttrusteddomainsid=None,
        cn=None,
        iparangetype=None,
    ):
        """Search for ranges.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipabaseid: First Posix ID of the range
        :type ipabaseid: Int
        :param ipaidrangesize: Number of IDs in the range
        :type ipaidrangesize: Int
        :param ipabaserid: First RID of the corresponding RID range
        :type ipabaserid: Int
        :param ipasecondarybaserid: First RID of the secondary RID range
        :type ipasecondarybaserid: Int
        :param ipanttrusteddomainsid: Domain SID of the trusted domain
        :type ipanttrusteddomainsid: Str
        :param cn: Range name
        :type cn: Str
        :param iparangetype: ID range type, one of ipa-ad-trust, ipa-ad-trust-posix, ipa-local
        :type iparangetype: StrEnum
        """
        method = 'idrange_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipabaseid:
            _params['ipabaseid'] = ipabaseid
        if ipaidrangesize:
            _params['ipaidrangesize'] = ipaidrangesize
        if ipabaserid:
            _params['ipabaserid'] = ipabaserid
        if ipasecondarybaserid:
            _params['ipasecondarybaserid'] = ipasecondarybaserid
        if ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = ipanttrusteddomainsid
        if cn:
            _params['cn'] = cn
        if iparangetype:
            _params['iparangetype'] = iparangetype
        
        return self._request(method, _args, _params)

    def idrange_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        ipanttrusteddomainname=None,
        ipanttrusteddomainsid=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        ipabaseid=None,
        ipaidrangesize=None,
        ipabaserid=None,
        ipasecondarybaserid=None,
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


        :param cn: Range name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param ipanttrusteddomainname: Name of the trusted domain
        :type ipanttrusteddomainname: Str
        :param ipanttrusteddomainsid: Domain SID of the trusted domain
        :type ipanttrusteddomainsid: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipabaseid: First Posix ID of the range
        :type ipabaseid: Int
        :param ipaidrangesize: Number of IDs in the range
        :type ipaidrangesize: Int
        :param ipabaserid: First RID of the corresponding RID range
        :type ipabaserid: Int
        :param ipasecondarybaserid: First RID of the secondary RID range
        :type ipasecondarybaserid: Int
        """
        method = 'idrange_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if ipanttrusteddomainname:
            _params['ipanttrusteddomainname'] = ipanttrusteddomainname
        if ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = ipanttrusteddomainsid
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if ipabaseid:
            _params['ipabaseid'] = ipabaseid
        if ipaidrangesize:
            _params['ipaidrangesize'] = ipaidrangesize
        if ipabaserid:
            _params['ipabaserid'] = ipabaserid
        if ipasecondarybaserid:
            _params['ipasecondarybaserid'] = ipasecondarybaserid
        
        return self._request(method, _args, _params)

    def idrange_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about a range.
        :param cn: Range name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'idrange_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def idview_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        description=None,
        ipadomainresolutionorder=None,
    ):
        """Add a new ID View.
        :param cn: ID View Name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Description
        :type description: Str
        :param ipadomainresolutionorder: colon-separated list of domains used for short name qualification
        :type ipadomainresolutionorder: Str
        """
        method = 'idview_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if ipadomainresolutionorder:
            _params['ipadomainresolutionorder'] = ipadomainresolutionorder
        
        return self._request(method, _args, _params)

    def idview_apply(
        self,
        cn,
        hostgroup=None,
        host=None,
    ):
        """Applies ID View to specified hosts or current members of specified hostgroups. If any other ID View is applied to the host, it is overridden.
        :param cn: ID View Name
        :type cn: Str
        :param hostgroup: Hostgroups to whose hosts apply the ID View to. Please note that view is not applied automatically to any hosts added to the hostgroup after running the idview-apply command.
        :type hostgroup: Str
        :param host: Hosts to apply the ID View to
        :type host: Str
        """
        method = 'idview_apply'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def idview_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete an ID View.
        :param cn: ID View Name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'idview_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def idview_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        description=None,
        cn=None,
    ):
        """Search for an ID View.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Description
        :type description: Str
        :param cn: ID View Name
        :type cn: Str
        """
        method = 'idview_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def idview_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        description=None,
        ipadomainresolutionorder=None,
    ):
        """Modify an ID View.
        :param cn: ID View Name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the ID View object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: Description
        :type description: Str
        :param ipadomainresolutionorder: colon-separated list of domains used for short name qualification
        :type ipadomainresolutionorder: Str
        """
        method = 'idview_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        if ipadomainresolutionorder:
            _params['ipadomainresolutionorder'] = ipadomainresolutionorder
        
        return self._request(method, _args, _params)

    def idview_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
        show_hosts=False,
    ):
        """Display information about an ID View.
        :param cn: ID View Name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param show_hosts: Enumerate all the hosts the view applies to.
        :type show_hosts: Flag
        """
        method = 'idview_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if show_hosts:
            _params['show_hosts'] = show_hosts
        
        return self._request(method, _args, _params)

    def idview_unapply(
        self,
        hostgroup=None,
        host=None,
    ):
        """Clears ID View from specified hosts or current members of specified hostgroups.
        :param hostgroup: Hostgroups whose hosts should have ID Views cleared. Note that view is not cleared automatically from any host added to the hostgroup after running idview-unapply command.
        :type hostgroup: Str
        :param host: Hosts to clear (any) ID View from.
        :type host: Str
        """
        method = 'idview_unapply'
        
        _args = list()
        
        _params = dict()
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def join(
        self,
        cn,
        realm,
        nsosversion=None,
        nshardwareplatform=None,
    ):
        """Join an IPA domain
        :param cn: The hostname to register as
        :type cn: Str
        :param nsosversion: Operating System and version of the host (e.g. Fedora 9)
        :type nsosversion: Str
        :param nshardwareplatform: Hardware platform of the host (e.g. Lenovo T61)
        :type nshardwareplatform: Str
        :param realm: The IPA realm
        :type realm: Str
        """
        method = 'join'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if nsosversion:
            _params['nsosversion'] = nsosversion
        if nshardwareplatform:
            _params['nshardwareplatform'] = nshardwareplatform
        _params['realm'] = realm
        
        return self._request(method, _args, _params)

    def json_metadata(
        self,
        methodname=None,
        objname=None,
        command=None,
        opt_method=None,
        opt_object=None,
    ):
        """
    Export plugin meta-data for the webUI.
    
        :param methodname: Name of method to export
        :type methodname: Str
        :param objname: Name of object to export
        :type objname: Str
        :param command: Name of command to export
        :type command: Str
        :param opt_method: Name of method to export
        :type opt_method: Str
        :param opt_object: Name of object to export
        :type opt_object: Str
        """
        method = 'json_metadata'
        
        _args = list()
        _args.append(methodname)
        _args.append(objname)
        
        _params = dict()
        if command:
            _params['command'] = command
        if opt_method:
            _params['method'] = opt_method
        if opt_object:
            _params['object'] = opt_object
        
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
        uid=None,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        krbmaxticketlife=None,
        krbmaxrenewableage=None,
    ):
        """Modify Kerberos ticket policy.
        :param uid: Manage ticket policy for specific user
        :type uid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param krbmaxticketlife: Maximum ticket life (seconds)
        :type krbmaxticketlife: Int
        :param krbmaxrenewableage: Maximum renewable age (seconds)
        :type krbmaxrenewableage: Int
        """
        method = 'krbtpolicy_mod'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if krbmaxticketlife:
            _params['krbmaxticketlife'] = krbmaxticketlife
        if krbmaxrenewableage:
            _params['krbmaxrenewableage'] = krbmaxrenewableage
        
        return self._request(method, _args, _params)

    def krbtpolicy_reset(
        self,
        uid=None,
        opt_all=True,
        raw=False,
    ):
        """Reset Kerberos ticket policy to the default values.
        :param uid: Manage ticket policy for specific user
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'krbtpolicy_reset'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def krbtpolicy_show(
        self,
        uid=None,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display the current Kerberos ticket policy.
        :param uid: Manage ticket policy for specific user
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'krbtpolicy_show'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def location_add(
        self,
        idnsname,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        description=None,
    ):
        """Add a new IPA location.
        :param idnsname: IPA location name
        :type idnsname: DNSNameParam
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: IPA Location description
        :type description: Str
        """
        method = 'location_add'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def location_del(
        self,
        idnsname,
        opt_continue=False,
    ):
        """Delete an IPA location.
        :param idnsname: IPA location name
        :type idnsname: DNSNameParam
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'location_del'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def location_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        idnsname=None,
        description=None,
    ):
        """Search for IPA locations.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param idnsname: IPA location name
        :type idnsname: DNSNameParam
        :param description: IPA Location description
        :type description: Str
        """
        method = 'location_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if idnsname:
            _params['idnsname'] = idnsname
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def location_mod(
        self,
        idnsname,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify information about an IPA location.
        :param idnsname: IPA location name
        :type idnsname: DNSNameParam
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: IPA Location description
        :type description: Str
        """
        method = 'location_mod'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def location_show(
        self,
        idnsname,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about an IPA location.
        :param idnsname: IPA location name
        :type idnsname: DNSNameParam
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'location_show'
        
        _args = list()
        _args.append(idnsname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def migrate_ds(
        self,
        bindpw,
        ldapuri,
        basedn=None,
        cacertfile=None,
        use_def_group=True,
        binddn='cn=directory manager',
        groupcontainer='ou=groups',
        usercontainer='ou=people',
        opt_continue=False,
        groupoverwritegid=False,
        compat=False,
        exclude_groups=None,
        exclude_users=None,
        groupignoreattribute=None,
        groupignoreobjectclass=None,
        groupobjectclass=None,
        userignoreattribute=None,
        userignoreobjectclass=None,
        userobjectclass=None,
        schema='RFC2307bis',
        scope='onelevel',
    ):
        """Migrate users and groups from DS to IPA.
        :param bindpw: bind password
        :type bindpw: Password
        :param ldapuri: LDAP URI of DS server to migrate from
        :type ldapuri: Str
        :param basedn: Base DN on remote LDAP server
        :type basedn: DNParam
        :param cacertfile: Load CA certificate of LDAP server from FILE
        :type cacertfile: Str
        :param use_def_group: Add migrated users without a group to a default group (default: true)
        :type use_def_group: Bool
        :param binddn: Bind DN
        :type binddn: DNParam
        :param groupcontainer: DN of container for groups in DS relative to base DN
        :type groupcontainer: DNParam
        :param usercontainer: DN of container for users in DS relative to base DN
        :type usercontainer: DNParam
        :param opt_continue: Continuous operation mode. Errors are reported but the process continues
        :type opt_continue: Flag
        :param groupoverwritegid: When migrating a group already existing in IPA domain overwrite the group GID and report as success
        :type groupoverwritegid: Flag
        :param compat: Allows migration despite the usage of compat plugin
        :type compat: Flag
        :param exclude_groups: groups to exclude from migration
        :type exclude_groups: Str
        :param exclude_users: users to exclude from migration
        :type exclude_users: Str
        :param groupignoreattribute: Attributes to be ignored for group entries in DS
        :type groupignoreattribute: Str
        :param groupignoreobjectclass: Objectclasses to be ignored for group entries in DS
        :type groupignoreobjectclass: Str
        :param groupobjectclass: Objectclasses used to search for group entries in DS
        :type groupobjectclass: Str
        :param userignoreattribute: Attributes to be ignored for user entries in DS
        :type userignoreattribute: Str
        :param userignoreobjectclass: Objectclasses to be ignored for user entries in DS
        :type userignoreobjectclass: Str
        :param userobjectclass: Objectclasses used to search for user entries in DS
        :type userobjectclass: Str
        :param schema: The schema used on the LDAP server. Supported values are RFC2307 and RFC2307bis. The default is RFC2307bis
        :type schema: StrEnum
        :param scope: LDAP search scope for users and groups: base, onelevel, or subtree. Defaults to onelevel
        :type scope: StrEnum
        """
        method = 'migrate_ds'
        
        _args = list()
        _args.append(bindpw)
        _args.append(ldapuri)
        
        _params = dict()
        if basedn:
            _params['basedn'] = basedn
        if cacertfile:
            _params['cacertfile'] = cacertfile
        if use_def_group:
            _params['use_def_group'] = use_def_group
        if binddn:
            _params['binddn'] = binddn
        _params['groupcontainer'] = groupcontainer
        _params['usercontainer'] = usercontainer
        if opt_continue:
            _params['continue'] = opt_continue
        _params['groupoverwritegid'] = groupoverwritegid
        if compat:
            _params['compat'] = compat
        if exclude_groups:
            _params['exclude_groups'] = exclude_groups
        if exclude_users:
            _params['exclude_users'] = exclude_users
        if groupignoreattribute:
            _params['groupignoreattribute'] = groupignoreattribute
        if groupignoreobjectclass:
            _params['groupignoreobjectclass'] = groupignoreobjectclass
        _params['groupobjectclass'] = groupobjectclass
        if userignoreattribute:
            _params['userignoreattribute'] = userignoreattribute
        if userignoreobjectclass:
            _params['userignoreobjectclass'] = userignoreobjectclass
        _params['userobjectclass'] = userobjectclass
        if schema:
            _params['schema'] = schema
        _params['scope'] = scope
        
        return self._request(method, _args, _params)

    def netgroup_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        description=None,
        externalhost=None,
        nisdomainname=None,
        hostcategory=None,
        usercategory=None,
    ):
        """Add a new netgroup.
        :param cn: Netgroup name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Netgroup description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param nisdomainname: NIS domain name
        :type nisdomainname: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'netgroup_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if nisdomainname:
            _params['nisdomainname'] = nisdomainname
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def netgroup_add_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        netgroup=None,
        user=None,
    ):
        """Add members to a netgroup.
        :param cn: Netgroup name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        :param netgroup: netgroups to add
        :type netgroup: Str
        :param user: users to add
        :type user: Str
        """
        method = 'netgroup_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if netgroup:
            _params['netgroup'] = netgroup
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def netgroup_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a netgroup.
        :param cn: Netgroup name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'netgroup_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def netgroup_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        group=None,
        hostgroup=None,
        host=None,
        in_netgroup=None,
        netgroup=None,
        no_group=None,
        no_hostgroup=None,
        no_host=None,
        no_netgroup=None,
        no_user=None,
        not_in_netgroup=None,
        user=None,
        opt_all=True,
        managed=False,
        no_members=True,
        pkey_only=False,
        private=False,
        raw=False,
        description=None,
        externalhost=None,
        cn=None,
        nisdomainname=None,
        ipauniqueid=None,
        hostcategory=None,
        usercategory=None,
    ):
        """Search for a netgroup.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param group: Search for netgroups with these member groups.
        :type group: Str
        :param hostgroup: Search for netgroups with these member host groups.
        :type hostgroup: Str
        :param host: Search for netgroups with these member hosts.
        :type host: Str
        :param in_netgroup: Search for netgroups with these member of netgroups.
        :type in_netgroup: Str
        :param netgroup: Search for netgroups with these member netgroups.
        :type netgroup: Str
        :param no_group: Search for netgroups without these member groups.
        :type no_group: Str
        :param no_hostgroup: Search for netgroups without these member host groups.
        :type no_hostgroup: Str
        :param no_host: Search for netgroups without these member hosts.
        :type no_host: Str
        :param no_netgroup: Search for netgroups without these member netgroups.
        :type no_netgroup: Str
        :param no_user: Search for netgroups without these member users.
        :type no_user: Str
        :param not_in_netgroup: Search for netgroups without these member of netgroups.
        :type not_in_netgroup: Str
        :param user: Search for netgroups with these member users.
        :type user: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param managed: search for managed groups
        :type managed: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param private: <private>
        :type private: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Netgroup description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param cn: Netgroup name
        :type cn: Str
        :param nisdomainname: NIS domain name
        :type nisdomainname: Str
        :param ipauniqueid: IPA unique ID
        :type ipauniqueid: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'netgroup_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if in_netgroup:
            _params['in_netgroup'] = in_netgroup
        if netgroup:
            _params['netgroup'] = netgroup
        if no_group:
            _params['no_group'] = no_group
        if no_hostgroup:
            _params['no_hostgroup'] = no_hostgroup
        if no_host:
            _params['no_host'] = no_host
        if no_netgroup:
            _params['no_netgroup'] = no_netgroup
        if no_user:
            _params['no_user'] = no_user
        if not_in_netgroup:
            _params['not_in_netgroup'] = not_in_netgroup
        if user:
            _params['user'] = user
        _params['all'] = opt_all
        _params['managed'] = managed
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['private'] = private
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if cn:
            _params['cn'] = cn
        if nisdomainname:
            _params['nisdomainname'] = nisdomainname
        if ipauniqueid:
            _params['ipauniqueid'] = ipauniqueid
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def netgroup_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        description=None,
        externalhost=None,
        nisdomainname=None,
        hostcategory=None,
        usercategory=None,
    ):
        """Modify a netgroup.
        :param cn: Netgroup name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: Netgroup description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param nisdomainname: NIS domain name
        :type nisdomainname: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'netgroup_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if nisdomainname:
            _params['nisdomainname'] = nisdomainname
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def netgroup_remove_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        netgroup=None,
        user=None,
    ):
        """Remove members from a netgroup.
        :param cn: Netgroup name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        :param netgroup: netgroups to remove
        :type netgroup: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'netgroup_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if netgroup:
            _params['netgroup'] = netgroup
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def netgroup_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a netgroup.
        :param cn: Netgroup name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'netgroup_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def otpconfig_mod(
        self,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        ipatokenhotpauthwindow=None,
        ipatokenhotpsyncwindow=None,
        ipatokentotpauthwindow=None,
        ipatokentotpsyncwindow=None,
    ):
        """Modify OTP configuration options.
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipatokenhotpauthwindow: HOTP authentication skip-ahead
        :type ipatokenhotpauthwindow: Int
        :param ipatokenhotpsyncwindow: HOTP synchronization skip-ahead
        :type ipatokenhotpsyncwindow: Int
        :param ipatokentotpauthwindow: TOTP authentication time variance (seconds)
        :type ipatokentotpauthwindow: Int
        :param ipatokentotpsyncwindow: TOTP synchronization time variance (seconds)
        :type ipatokentotpsyncwindow: Int
        """
        method = 'otpconfig_mod'
        
        _args = list()
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if ipatokenhotpauthwindow:
            _params['ipatokenhotpauthwindow'] = ipatokenhotpauthwindow
        if ipatokenhotpsyncwindow:
            _params['ipatokenhotpsyncwindow'] = ipatokenhotpsyncwindow
        if ipatokentotpauthwindow:
            _params['ipatokentotpauthwindow'] = ipatokentotpauthwindow
        if ipatokentotpsyncwindow:
            _params['ipatokentotpsyncwindow'] = ipatokentotpsyncwindow
        
        return self._request(method, _args, _params)

    def otpconfig_show(
        self,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Show the current OTP configuration.
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'otpconfig_show'
        
        _args = list()
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def otptoken_add(
        self,
        ipatokenuniqueid=None,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        no_qrcode=False,
        qrcode=False,
        raw=False,
        opt_type='totp',
        ipatokendisabled=None,
        ipatokennotafter=None,
        ipatokennotbefore=None,
        description=None,
        ipatokenmodel=None,
        ipatokenowner=None,
        ipatokenserial=None,
        ipatokenvendor=None,
        ipatokenhotpcounter=0,
        ipatokentotptimestep=30,
        ipatokentotpclockoffset=0,
        ipatokenotpdigits=6,
        ipatokenotpkey=None,
        ipatokenotpalgorithm='sha1',
    ):
        """Add a new OTP token.
        :param ipatokenuniqueid: Unique ID
        :type ipatokenuniqueid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param no_qrcode: Do not display QR code
        :type no_qrcode: Flag
        :param qrcode: (deprecated)
        :type qrcode: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param opt_type: Type of the token
        :type opt_type: StrEnum
        :param ipatokendisabled: Mark the token as disabled (default: false)
        :type ipatokendisabled: Bool
        :param ipatokennotafter: Last date/time the token can be used
        :type ipatokennotafter: DateTime
        :param ipatokennotbefore: First date/time the token can be used
        :type ipatokennotbefore: DateTime
        :param description: Token description (informational only)
        :type description: Str
        :param ipatokenmodel: Token model (informational only)
        :type ipatokenmodel: Str
        :param ipatokenowner: Assigned user of the token (default: self)
        :type ipatokenowner: Str
        :param ipatokenserial: Token serial (informational only)
        :type ipatokenserial: Str
        :param ipatokenvendor: Token vendor name (informational only)
        :type ipatokenvendor: Str
        :param ipatokenhotpcounter: Initial counter for the HOTP token
        :type ipatokenhotpcounter: Int
        :param ipatokentotptimestep: Length of TOTP token code validity
        :type ipatokentotptimestep: Int
        :param ipatokentotpclockoffset: TOTP token / FreeIPA server time difference
        :type ipatokentotpclockoffset: Int
        :param ipatokenotpdigits: Number of digits each token code will have
        :type ipatokenotpdigits: IntEnum
        :param ipatokenotpkey: Token secret (Base32; default: random)
        :type ipatokenotpkey: OTPTokenKey
        :param ipatokenotpalgorithm: Token hash algorithm
        :type ipatokenotpalgorithm: StrEnum
        """
        method = 'otptoken_add'
        
        _args = list()
        _args.append(ipatokenuniqueid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['no_qrcode'] = no_qrcode
        if qrcode:
            _params['qrcode'] = qrcode
        _params['raw'] = raw
        if opt_type:
            _params['type'] = opt_type
        if ipatokendisabled:
            _params['ipatokendisabled'] = ipatokendisabled
        if ipatokennotafter:
            _params['ipatokennotafter'] = ipatokennotafter
        if ipatokennotbefore:
            _params['ipatokennotbefore'] = ipatokennotbefore
        if description:
            _params['description'] = description
        if ipatokenmodel:
            _params['ipatokenmodel'] = ipatokenmodel
        if ipatokenowner:
            _params['ipatokenowner'] = ipatokenowner
        if ipatokenserial:
            _params['ipatokenserial'] = ipatokenserial
        if ipatokenvendor:
            _params['ipatokenvendor'] = ipatokenvendor
        if ipatokenhotpcounter:
            _params['ipatokenhotpcounter'] = ipatokenhotpcounter
        if ipatokentotptimestep:
            _params['ipatokentotptimestep'] = ipatokentotptimestep
        if ipatokentotpclockoffset:
            _params['ipatokentotpclockoffset'] = ipatokentotpclockoffset
        if ipatokenotpdigits:
            _params['ipatokenotpdigits'] = ipatokenotpdigits
        if ipatokenotpkey:
            _params['ipatokenotpkey'] = ipatokenotpkey
        if ipatokenotpalgorithm:
            _params['ipatokenotpalgorithm'] = ipatokenotpalgorithm
        
        return self._request(method, _args, _params)

    def otptoken_add_managedby(
        self,
        ipatokenuniqueid,
        opt_all=True,
        no_members=False,
        raw=False,
        user=None,
    ):
        """Add users that can manage this token.
        :param ipatokenuniqueid: Unique ID
        :type ipatokenuniqueid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param user: users to add
        :type user: Str
        """
        method = 'otptoken_add_managedby'
        
        _args = list()
        _args.append(ipatokenuniqueid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def otptoken_del(
        self,
        ipatokenuniqueid,
        opt_continue=False,
    ):
        """Delete an OTP token.
        :param ipatokenuniqueid: Unique ID
        :type ipatokenuniqueid: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'otptoken_del'
        
        _args = list()
        _args.append(ipatokenuniqueid)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def otptoken_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_type='totp',
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        ipatokendisabled=None,
        ipatokennotafter=None,
        ipatokennotbefore=None,
        ipatokenhotpcounter=0,
        ipatokentotptimestep=30,
        ipatokentotpclockoffset=0,
        ipatokenotpdigits=6,
        description=None,
        ipatokenuniqueid=None,
        ipatokenmodel=None,
        ipatokenowner=None,
        ipatokenserial=None,
        ipatokenvendor=None,
        ipatokenotpalgorithm='sha1',
    ):
        """Search for OTP token.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_type: Type of the token
        :type opt_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("id")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipatokendisabled: Mark the token as disabled (default: false)
        :type ipatokendisabled: Bool
        :param ipatokennotafter: Last date/time the token can be used
        :type ipatokennotafter: DateTime
        :param ipatokennotbefore: First date/time the token can be used
        :type ipatokennotbefore: DateTime
        :param ipatokenhotpcounter: Initial counter for the HOTP token
        :type ipatokenhotpcounter: Int
        :param ipatokentotptimestep: Length of TOTP token code validity
        :type ipatokentotptimestep: Int
        :param ipatokentotpclockoffset: TOTP token / FreeIPA server time difference
        :type ipatokentotpclockoffset: Int
        :param ipatokenotpdigits: Number of digits each token code will have
        :type ipatokenotpdigits: IntEnum
        :param description: Token description (informational only)
        :type description: Str
        :param ipatokenuniqueid: Unique ID
        :type ipatokenuniqueid: Str
        :param ipatokenmodel: Token model (informational only)
        :type ipatokenmodel: Str
        :param ipatokenowner: Assigned user of the token (default: self)
        :type ipatokenowner: Str
        :param ipatokenserial: Token serial (informational only)
        :type ipatokenserial: Str
        :param ipatokenvendor: Token vendor name (informational only)
        :type ipatokenvendor: Str
        :param ipatokenotpalgorithm: Token hash algorithm
        :type ipatokenotpalgorithm: StrEnum
        """
        method = 'otptoken_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if opt_type:
            _params['type'] = opt_type
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipatokendisabled:
            _params['ipatokendisabled'] = ipatokendisabled
        if ipatokennotafter:
            _params['ipatokennotafter'] = ipatokennotafter
        if ipatokennotbefore:
            _params['ipatokennotbefore'] = ipatokennotbefore
        if ipatokenhotpcounter:
            _params['ipatokenhotpcounter'] = ipatokenhotpcounter
        if ipatokentotptimestep:
            _params['ipatokentotptimestep'] = ipatokentotptimestep
        if ipatokentotpclockoffset:
            _params['ipatokentotpclockoffset'] = ipatokentotpclockoffset
        if ipatokenotpdigits:
            _params['ipatokenotpdigits'] = ipatokenotpdigits
        if description:
            _params['description'] = description
        if ipatokenuniqueid:
            _params['ipatokenuniqueid'] = ipatokenuniqueid
        if ipatokenmodel:
            _params['ipatokenmodel'] = ipatokenmodel
        if ipatokenowner:
            _params['ipatokenowner'] = ipatokenowner
        if ipatokenserial:
            _params['ipatokenserial'] = ipatokenserial
        if ipatokenvendor:
            _params['ipatokenvendor'] = ipatokenvendor
        if ipatokenotpalgorithm:
            _params['ipatokenotpalgorithm'] = ipatokenotpalgorithm
        
        return self._request(method, _args, _params)

    def otptoken_mod(
        self,
        ipatokenuniqueid,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        ipatokendisabled=None,
        ipatokennotafter=None,
        ipatokennotbefore=None,
        description=None,
        ipatokenmodel=None,
        ipatokenowner=None,
        ipatokenserial=None,
        ipatokenvendor=None,
    ):
        """Modify a OTP token.
        :param ipatokenuniqueid: Unique ID
        :type ipatokenuniqueid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the OTP token object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipatokendisabled: Mark the token as disabled (default: false)
        :type ipatokendisabled: Bool
        :param ipatokennotafter: Last date/time the token can be used
        :type ipatokennotafter: DateTime
        :param ipatokennotbefore: First date/time the token can be used
        :type ipatokennotbefore: DateTime
        :param description: Token description (informational only)
        :type description: Str
        :param ipatokenmodel: Token model (informational only)
        :type ipatokenmodel: Str
        :param ipatokenowner: Assigned user of the token (default: self)
        :type ipatokenowner: Str
        :param ipatokenserial: Token serial (informational only)
        :type ipatokenserial: Str
        :param ipatokenvendor: Token vendor name (informational only)
        :type ipatokenvendor: Str
        """
        method = 'otptoken_mod'
        
        _args = list()
        _args.append(ipatokenuniqueid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if ipatokendisabled:
            _params['ipatokendisabled'] = ipatokendisabled
        if ipatokennotafter:
            _params['ipatokennotafter'] = ipatokennotafter
        if ipatokennotbefore:
            _params['ipatokennotbefore'] = ipatokennotbefore
        if description:
            _params['description'] = description
        if ipatokenmodel:
            _params['ipatokenmodel'] = ipatokenmodel
        if ipatokenowner:
            _params['ipatokenowner'] = ipatokenowner
        if ipatokenserial:
            _params['ipatokenserial'] = ipatokenserial
        if ipatokenvendor:
            _params['ipatokenvendor'] = ipatokenvendor
        
        return self._request(method, _args, _params)

    def otptoken_remove_managedby(
        self,
        ipatokenuniqueid,
        opt_all=True,
        no_members=False,
        raw=False,
        user=None,
    ):
        """Remove users that can manage this token.
        :param ipatokenuniqueid: Unique ID
        :type ipatokenuniqueid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param user: users to remove
        :type user: Str
        """
        method = 'otptoken_remove_managedby'
        
        _args = list()
        _args.append(ipatokenuniqueid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def otptoken_show(
        self,
        ipatokenuniqueid,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about an OTP token.
        :param ipatokenuniqueid: Unique ID
        :type ipatokenuniqueid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'otptoken_show'
        
        _args = list()
        _args.append(ipatokenuniqueid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def output_find(
        self,
        commandfull_name,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
    ):
        """Search for command outputs.
        :param commandfull_name: Full name
        :type commandfull_name: Str
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'output_find'
        
        _args = list()
        _args.append(commandfull_name)
        _args.append(criteria)
        
        _params = dict()
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def output_show(
        self,
        commandfull_name,
        name,
        opt_all=True,
        raw=False,
    ):
        """Display information about a command output.
        :param commandfull_name: Full name
        :type commandfull_name: Str
        :param name: Name
        :type name: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'output_show'
        
        _args = list()
        _args.append(commandfull_name)
        _args.append(name)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def param_find(
        self,
        metaobjectfull_name,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
    ):
        """Search command parameters.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param metaobjectfull_name: Full name
        :type metaobjectfull_name: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'param_find'
        
        _args = list()
        _args.append(criteria)
        _args.append(metaobjectfull_name)
        
        _params = dict()
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def param_show(
        self,
        metaobjectfull_name,
        name,
        opt_all=True,
        raw=False,
    ):
        """Display information about a command parameter.
        :param metaobjectfull_name: Full name
        :type metaobjectfull_name: Str
        :param name: Name
        :type name: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'param_show'
        
        _args = list()
        _args.append(metaobjectfull_name)
        _args.append(name)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def passwd(
        self,
        password,
        current_password,
        principal,
        otp=None,
    ):
        """Set a user's password.
        :param password: New Password
        :type password: Password
        :param current_password: Current Password
        :type current_password: Password
        :param principal: User name
        :type principal: Principal
        :param otp: One Time Password
        :type otp: Password
        """
        method = 'passwd'
        
        _args = list()
        _args.append(password)
        _args.append(current_password)
        _args.append(principal)
        
        _params = dict()
        if otp:
            _params['otp'] = otp
        
        return self._request(method, _args, _params)

    def permission_add(
        self,
        cn,
        addattr=None,
        attrs=None,
        opt_filter=None,
        extratargetfilter=None,
        permissions=None,
        opt_setattr=None,
        subtree=None,
        opt_all=True,
        no_members=False,
        raw=False,
        ipapermtarget=None,
        ipapermtargetfrom=None,
        ipapermtargetto=None,
        ipapermtargetfilter=None,
        ipapermbindruletype='permission',
        memberof=None,
        targetgroup=None,
        opt_type=None,
        ipapermlocation=None,
        ipapermright=None,
    ):
        """Add a new permission.
        :param cn: Permission name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param attrs: All attributes to which the permission applies
        :type attrs: Str
        :param opt_filter: Deprecated; use extratargetfilter
        :type opt_filter: Str
        :param extratargetfilter: Extra target filter
        :type extratargetfilter: Str
        :param permissions: Deprecated; use ipapermright
        :type permissions: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param subtree: Deprecated; use ipapermlocation
        :type subtree: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipapermtarget: Optional DN to apply the permission to (must be in the subtree, but may not yet exist)
        :type ipapermtarget: DNParam
        :param ipapermtargetfrom: Optional DN subtree from where an entry can be moved (must be in the subtree, but may not yet exist)
        :type ipapermtargetfrom: DNParam
        :param ipapermtargetto: Optional DN subtree where an entry can be moved to (must be in the subtree, but may not yet exist)
        :type ipapermtargetto: DNParam
        :param ipapermtargetfilter: All target filters, including those implied by type and memberof
        :type ipapermtargetfilter: Str
        :param ipapermbindruletype: Bind rule type
        :type ipapermbindruletype: StrEnum
        :param memberof: Target members of a group (sets memberOf targetfilter)
        :type memberof: Str
        :param targetgroup: User group to apply permissions to (sets target)
        :type targetgroup: Str
        :param opt_type: Type of IPA object (sets subtree and objectClass targetfilter)
        :type opt_type: Str
        :param ipapermlocation: Subtree to apply permissions to
        :type ipapermlocation: DNOrURL
        :param ipapermright: Rights to grant (read, search, compare, write, add, delete, all)
        :type ipapermright: StrEnum
        """
        method = 'permission_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if attrs:
            _params['attrs'] = attrs
        if opt_filter:
            _params['filter'] = opt_filter
        if extratargetfilter:
            _params['extratargetfilter'] = extratargetfilter
        if permissions:
            _params['permissions'] = permissions
        if opt_setattr:
            _params['setattr'] = opt_setattr
        if subtree:
            _params['subtree'] = subtree
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if ipapermtarget:
            _params['ipapermtarget'] = ipapermtarget
        if ipapermtargetfrom:
            _params['ipapermtargetfrom'] = ipapermtargetfrom
        if ipapermtargetto:
            _params['ipapermtargetto'] = ipapermtargetto
        if ipapermtargetfilter:
            _params['ipapermtargetfilter'] = ipapermtargetfilter
        _params['ipapermbindruletype'] = ipapermbindruletype
        if memberof:
            _params['memberof'] = memberof
        if targetgroup:
            _params['targetgroup'] = targetgroup
        if opt_type:
            _params['type'] = opt_type
        if ipapermlocation:
            _params['ipapermlocation'] = ipapermlocation
        if ipapermright:
            _params['ipapermright'] = ipapermright
        
        return self._request(method, _args, _params)

    def permission_add_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        privilege=None,
    ):
        """Add members to a permission.
        :param cn: Permission name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param privilege: privileges to add
        :type privilege: Str
        """
        method = 'permission_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if privilege:
            _params['privilege'] = privilege
        
        return self._request(method, _args, _params)

    def permission_add_noaci(
        self,
        cn,
        ipapermissiontype,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add a system permission without an ACI (internal command)
        :param cn: Permission name
        :type cn: Str
        :param ipapermissiontype: Permission flags
        :type ipapermissiontype: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'permission_add_noaci'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['ipapermissiontype'] = ipapermissiontype
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def permission_del(
        self,
        cn,
        opt_continue=False,
        force=False,
    ):
        """Delete a permission.
        :param cn: Permission name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        :param force: force delete of SYSTEM permissions
        :type force: Flag
        """
        method = 'permission_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        _params['force'] = force
        
        return self._request(method, _args, _params)

    def permission_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        attrs=None,
        opt_filter=None,
        extratargetfilter=None,
        memberof=None,
        permissions=None,
        subtree=None,
        targetgroup=None,
        opt_type=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        ipapermlocation=None,
        ipapermtarget=None,
        ipapermtargetfrom=None,
        ipapermtargetto=None,
        ipapermdefaultattr=None,
        ipapermexcludedattr=None,
        ipapermincludedattr=None,
        cn=None,
        ipapermtargetfilter=None,
        ipapermbindruletype='permission',
        ipapermright=None,
    ):
        """Search for permissions.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param attrs: All attributes to which the permission applies
        :type attrs: Str
        :param opt_filter: Deprecated; use extratargetfilter
        :type opt_filter: Str
        :param extratargetfilter: Extra target filter
        :type extratargetfilter: Str
        :param memberof: Target members of a group (sets memberOf targetfilter)
        :type memberof: Str
        :param permissions: Deprecated; use ipapermright
        :type permissions: Str
        :param subtree: Deprecated; use ipapermlocation
        :type subtree: Str
        :param targetgroup: User group to apply permissions to (sets target)
        :type targetgroup: Str
        :param opt_type: Type of IPA object (sets subtree and objectClass targetfilter)
        :type opt_type: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipapermlocation: Subtree to apply permissions to
        :type ipapermlocation: DNOrURL
        :param ipapermtarget: Optional DN to apply the permission to (must be in the subtree, but may not yet exist)
        :type ipapermtarget: DNParam
        :param ipapermtargetfrom: Optional DN subtree from where an entry can be moved (must be in the subtree, but may not yet exist)
        :type ipapermtargetfrom: DNParam
        :param ipapermtargetto: Optional DN subtree where an entry can be moved to (must be in the subtree, but may not yet exist)
        :type ipapermtargetto: DNParam
        :param ipapermdefaultattr: Attributes to which the permission applies by default
        :type ipapermdefaultattr: Str
        :param ipapermexcludedattr: User-specified attributes to which the permission explicitly does not apply
        :type ipapermexcludedattr: Str
        :param ipapermincludedattr: User-specified attributes to which the permission applies
        :type ipapermincludedattr: Str
        :param cn: Permission name
        :type cn: Str
        :param ipapermtargetfilter: All target filters, including those implied by type and memberof
        :type ipapermtargetfilter: Str
        :param ipapermbindruletype: Bind rule type
        :type ipapermbindruletype: StrEnum
        :param ipapermright: Rights to grant (read, search, compare, write, add, delete, all)
        :type ipapermright: StrEnum
        """
        method = 'permission_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if attrs:
            _params['attrs'] = attrs
        if opt_filter:
            _params['filter'] = opt_filter
        if extratargetfilter:
            _params['extratargetfilter'] = extratargetfilter
        if memberof:
            _params['memberof'] = memberof
        if permissions:
            _params['permissions'] = permissions
        if subtree:
            _params['subtree'] = subtree
        if targetgroup:
            _params['targetgroup'] = targetgroup
        if opt_type:
            _params['type'] = opt_type
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipapermlocation:
            _params['ipapermlocation'] = ipapermlocation
        if ipapermtarget:
            _params['ipapermtarget'] = ipapermtarget
        if ipapermtargetfrom:
            _params['ipapermtargetfrom'] = ipapermtargetfrom
        if ipapermtargetto:
            _params['ipapermtargetto'] = ipapermtargetto
        if ipapermdefaultattr:
            _params['ipapermdefaultattr'] = ipapermdefaultattr
        if ipapermexcludedattr:
            _params['ipapermexcludedattr'] = ipapermexcludedattr
        if ipapermincludedattr:
            _params['ipapermincludedattr'] = ipapermincludedattr
        if cn:
            _params['cn'] = cn
        if ipapermtargetfilter:
            _params['ipapermtargetfilter'] = ipapermtargetfilter
        if ipapermbindruletype:
            _params['ipapermbindruletype'] = ipapermbindruletype
        if ipapermright:
            _params['ipapermright'] = ipapermright
        
        return self._request(method, _args, _params)

    def permission_mod(
        self,
        cn,
        addattr=None,
        attrs=None,
        opt_delattr=None,
        opt_filter=None,
        extratargetfilter=None,
        memberof=None,
        permissions=None,
        rename=None,
        opt_setattr=None,
        subtree=None,
        targetgroup=None,
        opt_type=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        ipapermlocation=None,
        ipapermtarget=None,
        ipapermtargetfrom=None,
        ipapermtargetto=None,
        ipapermexcludedattr=None,
        ipapermincludedattr=None,
        ipapermtargetfilter=None,
        ipapermbindruletype='permission',
        ipapermright=None,
    ):
        """Modify a permission.
        :param cn: Permission name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param attrs: All attributes to which the permission applies
        :type attrs: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_filter: Deprecated; use extratargetfilter
        :type opt_filter: Str
        :param extratargetfilter: Extra target filter
        :type extratargetfilter: Str
        :param memberof: Target members of a group (sets memberOf targetfilter)
        :type memberof: Str
        :param permissions: Deprecated; use ipapermright
        :type permissions: Str
        :param rename: Rename the permission object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param subtree: Deprecated; use ipapermlocation
        :type subtree: Str
        :param targetgroup: User group to apply permissions to (sets target)
        :type targetgroup: Str
        :param opt_type: Type of IPA object (sets subtree and objectClass targetfilter)
        :type opt_type: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipapermlocation: Subtree to apply permissions to
        :type ipapermlocation: DNOrURL
        :param ipapermtarget: Optional DN to apply the permission to (must be in the subtree, but may not yet exist)
        :type ipapermtarget: DNParam
        :param ipapermtargetfrom: Optional DN subtree from where an entry can be moved (must be in the subtree, but may not yet exist)
        :type ipapermtargetfrom: DNParam
        :param ipapermtargetto: Optional DN subtree where an entry can be moved to (must be in the subtree, but may not yet exist)
        :type ipapermtargetto: DNParam
        :param ipapermexcludedattr: User-specified attributes to which the permission explicitly does not apply
        :type ipapermexcludedattr: Str
        :param ipapermincludedattr: User-specified attributes to which the permission applies
        :type ipapermincludedattr: Str
        :param ipapermtargetfilter: All target filters, including those implied by type and memberof
        :type ipapermtargetfilter: Str
        :param ipapermbindruletype: Bind rule type
        :type ipapermbindruletype: StrEnum
        :param ipapermright: Rights to grant (read, search, compare, write, add, delete, all)
        :type ipapermright: StrEnum
        """
        method = 'permission_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if attrs:
            _params['attrs'] = attrs
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_filter:
            _params['filter'] = opt_filter
        if extratargetfilter:
            _params['extratargetfilter'] = extratargetfilter
        if memberof:
            _params['memberof'] = memberof
        if permissions:
            _params['permissions'] = permissions
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        if subtree:
            _params['subtree'] = subtree
        if targetgroup:
            _params['targetgroup'] = targetgroup
        if opt_type:
            _params['type'] = opt_type
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if ipapermlocation:
            _params['ipapermlocation'] = ipapermlocation
        if ipapermtarget:
            _params['ipapermtarget'] = ipapermtarget
        if ipapermtargetfrom:
            _params['ipapermtargetfrom'] = ipapermtargetfrom
        if ipapermtargetto:
            _params['ipapermtargetto'] = ipapermtargetto
        if ipapermexcludedattr:
            _params['ipapermexcludedattr'] = ipapermexcludedattr
        if ipapermincludedattr:
            _params['ipapermincludedattr'] = ipapermincludedattr
        if ipapermtargetfilter:
            _params['ipapermtargetfilter'] = ipapermtargetfilter
        if ipapermbindruletype:
            _params['ipapermbindruletype'] = ipapermbindruletype
        if ipapermright:
            _params['ipapermright'] = ipapermright
        
        return self._request(method, _args, _params)

    def permission_remove_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        privilege=None,
    ):
        """Remove members from a permission.
        :param cn: Permission name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param privilege: privileges to remove
        :type privilege: Str
        """
        method = 'permission_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if privilege:
            _params['privilege'] = privilege
        
        return self._request(method, _args, _params)

    def permission_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a permission.
        :param cn: Permission name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'permission_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
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
        criteria=None,
        sizelimit=None,
        timelimit=None,
        status=None,
        opt_all=True,
        raw=False,
        server_server=None,
    ):
        """Report PKINIT status on the IPA masters
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param status: Whether PKINIT is enabled or disabled
        :type status: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param server_server: IPA server hostname
        :type server_server: Str
        """
        method = 'pkinit_status'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if status:
            _params['status'] = status
        _params['all'] = opt_all
        _params['raw'] = raw
        if server_server:
            _params['server_server'] = server_server
        
        return self._request(method, _args, _params)

    def plugins(
        self,
        opt_all=True,
        server=False,
    ):
        """Show all loaded plugins.
        :param opt_all: retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param server: Forward to server instead of running locally
        :type server: Flag
        """
        method = 'plugins'
        
        _args = list()
        
        _params = dict()
        _params['all'] = opt_all
        if server:
            _params['server'] = server
        
        return self._request(method, _args, _params)

    def privilege_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        description=None,
    ):
        """Add a new privilege.
        :param cn: Privilege name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Privilege description
        :type description: Str
        """
        method = 'privilege_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def privilege_add_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        role=None,
    ):
        """Add members to a privilege.
        :param cn: Privilege name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param role: roles to add
        :type role: Str
        """
        method = 'privilege_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if role:
            _params['role'] = role
        
        return self._request(method, _args, _params)

    def privilege_add_permission(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        permission=None,
    ):
        """Add permissions to a privilege.
        :param cn: Privilege name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param permission: permissions
        :type permission: Str
        """
        method = 'privilege_add_permission'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if permission:
            _params['permission'] = permission
        
        return self._request(method, _args, _params)

    def privilege_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a privilege.
        :param cn: Privilege name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'privilege_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def privilege_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        description=None,
        cn=None,
    ):
        """Search for privileges.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Privilege description
        :type description: Str
        :param cn: Privilege name
        :type cn: Str
        """
        method = 'privilege_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def privilege_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify a privilege.
        :param cn: Privilege name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the privilege object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: Privilege description
        :type description: Str
        """
        method = 'privilege_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def privilege_remove_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        role=None,
    ):
        """
    Remove members from a privilege
    
        :param cn: Privilege name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param role: roles to remove
        :type role: Str
        """
        method = 'privilege_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if role:
            _params['role'] = role
        
        return self._request(method, _args, _params)

    def privilege_remove_permission(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        permission=None,
    ):
        """Remove permissions from a privilege.
        :param cn: Privilege name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param permission: permissions
        :type permission: Str
        """
        method = 'privilege_remove_permission'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if permission:
            _params['permission'] = permission
        
        return self._request(method, _args, _params)

    def privilege_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a privilege.
        :param cn: Privilege name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'privilege_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def pwpolicy_add(
        self,
        cn,
        cospriority,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        krbpwdfailurecountinterval=None,
        krbpwdhistorylength=None,
        krbpwdlockoutduration=None,
        krbpwdmaxfailure=None,
        krbmaxpwdlife=None,
        krbpwdmindiffchars=None,
        krbpwdminlength=None,
        krbminpwdlife=None,
    ):
        """Add a new group password policy.
        :param cn: Manage password policy for specific group
        :type cn: Str
        :param cospriority: Priority of the policy (higher number means lower priority
        :type cospriority: Int
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param krbpwdfailurecountinterval: Period after which failure count will be reset (seconds)
        :type krbpwdfailurecountinterval: Int
        :param krbpwdhistorylength: Password history size
        :type krbpwdhistorylength: Int
        :param krbpwdlockoutduration: Period for which lockout is enforced (seconds)
        :type krbpwdlockoutduration: Int
        :param krbpwdmaxfailure: Consecutive failures before lockout
        :type krbpwdmaxfailure: Int
        :param krbmaxpwdlife: Maximum password lifetime (in days)
        :type krbmaxpwdlife: Int
        :param krbpwdmindiffchars: Minimum number of character classes
        :type krbpwdmindiffchars: Int
        :param krbpwdminlength: Minimum length of password
        :type krbpwdminlength: Int
        :param krbminpwdlife: Minimum password lifetime (in hours)
        :type krbminpwdlife: Int
        """
        method = 'pwpolicy_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['cospriority'] = cospriority
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        if krbpwdfailurecountinterval:
            _params['krbpwdfailurecountinterval'] = krbpwdfailurecountinterval
        if krbpwdhistorylength:
            _params['krbpwdhistorylength'] = krbpwdhistorylength
        if krbpwdlockoutduration:
            _params['krbpwdlockoutduration'] = krbpwdlockoutduration
        if krbpwdmaxfailure:
            _params['krbpwdmaxfailure'] = krbpwdmaxfailure
        if krbmaxpwdlife:
            _params['krbmaxpwdlife'] = krbmaxpwdlife
        if krbpwdmindiffchars:
            _params['krbpwdmindiffchars'] = krbpwdmindiffchars
        if krbpwdminlength:
            _params['krbpwdminlength'] = krbpwdminlength
        if krbminpwdlife:
            _params['krbminpwdlife'] = krbminpwdlife
        
        return self._request(method, _args, _params)

    def pwpolicy_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a group password policy.
        :param cn: Manage password policy for specific group
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'pwpolicy_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def pwpolicy_find(
        self,
        criteria=None,
        cospriority=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        krbpwdfailurecountinterval=None,
        krbpwdhistorylength=None,
        krbpwdlockoutduration=None,
        krbpwdmaxfailure=None,
        krbmaxpwdlife=None,
        krbpwdmindiffchars=None,
        krbpwdminlength=None,
        krbminpwdlife=None,
        cn=None,
    ):
        """Search for group password policies.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param cospriority: Priority of the policy (higher number means lower priority
        :type cospriority: Int
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("group")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param krbpwdfailurecountinterval: Period after which failure count will be reset (seconds)
        :type krbpwdfailurecountinterval: Int
        :param krbpwdhistorylength: Password history size
        :type krbpwdhistorylength: Int
        :param krbpwdlockoutduration: Period for which lockout is enforced (seconds)
        :type krbpwdlockoutduration: Int
        :param krbpwdmaxfailure: Consecutive failures before lockout
        :type krbpwdmaxfailure: Int
        :param krbmaxpwdlife: Maximum password lifetime (in days)
        :type krbmaxpwdlife: Int
        :param krbpwdmindiffchars: Minimum number of character classes
        :type krbpwdmindiffchars: Int
        :param krbpwdminlength: Minimum length of password
        :type krbpwdminlength: Int
        :param krbminpwdlife: Minimum password lifetime (in hours)
        :type krbminpwdlife: Int
        :param cn: Manage password policy for specific group
        :type cn: Str
        """
        method = 'pwpolicy_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if cospriority:
            _params['cospriority'] = cospriority
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if krbpwdfailurecountinterval:
            _params['krbpwdfailurecountinterval'] = krbpwdfailurecountinterval
        if krbpwdhistorylength:
            _params['krbpwdhistorylength'] = krbpwdhistorylength
        if krbpwdlockoutduration:
            _params['krbpwdlockoutduration'] = krbpwdlockoutduration
        if krbpwdmaxfailure:
            _params['krbpwdmaxfailure'] = krbpwdmaxfailure
        if krbmaxpwdlife:
            _params['krbmaxpwdlife'] = krbmaxpwdlife
        if krbpwdmindiffchars:
            _params['krbpwdmindiffchars'] = krbpwdmindiffchars
        if krbpwdminlength:
            _params['krbpwdminlength'] = krbpwdminlength
        if krbminpwdlife:
            _params['krbminpwdlife'] = krbminpwdlife
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def pwpolicy_mod(
        self,
        cn=None,
        cospriority=None,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        krbpwdfailurecountinterval=None,
        krbpwdhistorylength=None,
        krbpwdlockoutduration=None,
        krbpwdmaxfailure=None,
        krbmaxpwdlife=None,
        krbpwdmindiffchars=None,
        krbpwdminlength=None,
        krbminpwdlife=None,
    ):
        """Modify a group password policy.
        :param cn: Manage password policy for specific group
        :type cn: Str
        :param cospriority: Priority of the policy (higher number means lower priority
        :type cospriority: Int
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param krbpwdfailurecountinterval: Period after which failure count will be reset (seconds)
        :type krbpwdfailurecountinterval: Int
        :param krbpwdhistorylength: Password history size
        :type krbpwdhistorylength: Int
        :param krbpwdlockoutduration: Period for which lockout is enforced (seconds)
        :type krbpwdlockoutduration: Int
        :param krbpwdmaxfailure: Consecutive failures before lockout
        :type krbpwdmaxfailure: Int
        :param krbmaxpwdlife: Maximum password lifetime (in days)
        :type krbmaxpwdlife: Int
        :param krbpwdmindiffchars: Minimum number of character classes
        :type krbpwdmindiffchars: Int
        :param krbpwdminlength: Minimum length of password
        :type krbpwdminlength: Int
        :param krbminpwdlife: Minimum password lifetime (in hours)
        :type krbminpwdlife: Int
        """
        method = 'pwpolicy_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if cospriority:
            _params['cospriority'] = cospriority
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if krbpwdfailurecountinterval:
            _params['krbpwdfailurecountinterval'] = krbpwdfailurecountinterval
        if krbpwdhistorylength:
            _params['krbpwdhistorylength'] = krbpwdhistorylength
        if krbpwdlockoutduration:
            _params['krbpwdlockoutduration'] = krbpwdlockoutduration
        if krbpwdmaxfailure:
            _params['krbpwdmaxfailure'] = krbpwdmaxfailure
        if krbmaxpwdlife:
            _params['krbmaxpwdlife'] = krbmaxpwdlife
        if krbpwdmindiffchars:
            _params['krbpwdmindiffchars'] = krbpwdmindiffchars
        if krbpwdminlength:
            _params['krbpwdminlength'] = krbpwdminlength
        if krbminpwdlife:
            _params['krbminpwdlife'] = krbminpwdlife
        
        return self._request(method, _args, _params)

    def pwpolicy_show(
        self,
        cn=None,
        user=None,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about password policy.
        :param cn: Manage password policy for specific group
        :type cn: Str
        :param user: Display effective policy for a specific user
        :type user: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'pwpolicy_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if user:
            _params['user'] = user
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def radiusproxy_add(
        self,
        cn,
        ipatokenradiussecret,
        ipatokenradiusserver,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        ipatokenradiusretries=None,
        ipatokenradiustimeout=None,
        description=None,
        ipatokenusermapattribute=None,
    ):
        """Add a new RADIUS proxy server.
        :param cn: RADIUS proxy server name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipatokenradiusretries: The number of times to retry authentication
        :type ipatokenradiusretries: Int
        :param ipatokenradiustimeout: The total timeout across all retries (in seconds)
        :type ipatokenradiustimeout: Int
        :param ipatokenradiussecret: The secret used to encrypt data
        :type ipatokenradiussecret: Password
        :param description: A description of this RADIUS proxy server
        :type description: Str
        :param ipatokenradiusserver: The hostname or IP (with or without port)
        :type ipatokenradiusserver: Str
        :param ipatokenusermapattribute: The username attribute on the user object
        :type ipatokenusermapattribute: Str
        """
        method = 'radiusproxy_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        if ipatokenradiusretries:
            _params['ipatokenradiusretries'] = ipatokenradiusretries
        if ipatokenradiustimeout:
            _params['ipatokenradiustimeout'] = ipatokenradiustimeout
        _params['ipatokenradiussecret'] = ipatokenradiussecret
        if description:
            _params['description'] = description
        _params['ipatokenradiusserver'] = ipatokenradiusserver
        if ipatokenusermapattribute:
            _params['ipatokenusermapattribute'] = ipatokenusermapattribute
        
        return self._request(method, _args, _params)

    def radiusproxy_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a RADIUS proxy server.
        :param cn: RADIUS proxy server name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'radiusproxy_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def radiusproxy_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        ipatokenradiusretries=None,
        ipatokenradiustimeout=None,
        ipatokenradiussecret=None,
        description=None,
        cn=None,
        ipatokenradiusserver=None,
        ipatokenusermapattribute=None,
    ):
        """Search for RADIUS proxy servers.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipatokenradiusretries: The number of times to retry authentication
        :type ipatokenradiusretries: Int
        :param ipatokenradiustimeout: The total timeout across all retries (in seconds)
        :type ipatokenradiustimeout: Int
        :param ipatokenradiussecret: The secret used to encrypt data
        :type ipatokenradiussecret: Password
        :param description: A description of this RADIUS proxy server
        :type description: Str
        :param cn: RADIUS proxy server name
        :type cn: Str
        :param ipatokenradiusserver: The hostname or IP (with or without port)
        :type ipatokenradiusserver: Str
        :param ipatokenusermapattribute: The username attribute on the user object
        :type ipatokenusermapattribute: Str
        """
        method = 'radiusproxy_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipatokenradiusretries:
            _params['ipatokenradiusretries'] = ipatokenradiusretries
        if ipatokenradiustimeout:
            _params['ipatokenradiustimeout'] = ipatokenradiustimeout
        if ipatokenradiussecret:
            _params['ipatokenradiussecret'] = ipatokenradiussecret
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        if ipatokenradiusserver:
            _params['ipatokenradiusserver'] = ipatokenradiusserver
        if ipatokenusermapattribute:
            _params['ipatokenusermapattribute'] = ipatokenusermapattribute
        
        return self._request(method, _args, _params)

    def radiusproxy_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        ipatokenradiusretries=None,
        ipatokenradiustimeout=None,
        ipatokenradiussecret=None,
        description=None,
        ipatokenradiusserver=None,
        ipatokenusermapattribute=None,
    ):
        """Modify a RADIUS proxy server.
        :param cn: RADIUS proxy server name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the RADIUS proxy server object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipatokenradiusretries: The number of times to retry authentication
        :type ipatokenradiusretries: Int
        :param ipatokenradiustimeout: The total timeout across all retries (in seconds)
        :type ipatokenradiustimeout: Int
        :param ipatokenradiussecret: The secret used to encrypt data
        :type ipatokenradiussecret: Password
        :param description: A description of this RADIUS proxy server
        :type description: Str
        :param ipatokenradiusserver: The hostname or IP (with or without port)
        :type ipatokenradiusserver: Str
        :param ipatokenusermapattribute: The username attribute on the user object
        :type ipatokenusermapattribute: Str
        """
        method = 'radiusproxy_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if ipatokenradiusretries:
            _params['ipatokenradiusretries'] = ipatokenradiusretries
        if ipatokenradiustimeout:
            _params['ipatokenradiustimeout'] = ipatokenradiustimeout
        if ipatokenradiussecret:
            _params['ipatokenradiussecret'] = ipatokenradiussecret
        if description:
            _params['description'] = description
        if ipatokenradiusserver:
            _params['ipatokenradiusserver'] = ipatokenradiusserver
        if ipatokenusermapattribute:
            _params['ipatokenusermapattribute'] = ipatokenusermapattribute
        
        return self._request(method, _args, _params)

    def radiusproxy_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about a RADIUS proxy server.
        :param cn: RADIUS proxy server name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'radiusproxy_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def realmdomains_mod(
        self,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        force=False,
        raw=False,
        rights=False,
        add_domain=None,
        del_domain=None,
        associateddomain=None,
    ):
        """Modify realm domains.
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param force: Force adding domain even if not in DNS
        :type force: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param add_domain: Add domain
        :type add_domain: Str
        :param del_domain: Delete domain
        :type del_domain: Str
        :param associateddomain: Domain
        :type associateddomain: Str
        """
        method = 'realmdomains_mod'
        
        _args = list()
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['force'] = force
        _params['raw'] = raw
        _params['rights'] = rights
        if add_domain:
            _params['add_domain'] = add_domain
        if del_domain:
            _params['del_domain'] = del_domain
        if associateddomain:
            _params['associateddomain'] = associateddomain
        
        return self._request(method, _args, _params)

    def realmdomains_show(
        self,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display the list of realm domains.
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'realmdomains_show'
        
        _args = list()
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def role_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        description=None,
    ):
        """Add a new role.
        :param cn: Role name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this role-group
        :type description: Str
        """
        method = 'role_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def role_add_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        service=None,
        user=None,
    ):
        """Add members to a role.
        :param cn: Role name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        :param service: services to add
        :type service: Str
        :param user: users to add
        :type user: Str
        """
        method = 'role_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if service:
            _params['service'] = service
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def role_add_privilege(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        privilege=None,
    ):
        """Add privileges to a role.
        :param cn: Role name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param privilege: privileges
        :type privilege: Str
        """
        method = 'role_add_privilege'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if privilege:
            _params['privilege'] = privilege
        
        return self._request(method, _args, _params)

    def role_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a role.
        :param cn: Role name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'role_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def role_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        description=None,
        cn=None,
    ):
        """Search for roles.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this role-group
        :type description: Str
        :param cn: Role name
        :type cn: Str
        """
        method = 'role_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def role_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify a role.
        :param cn: Role name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the role object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: A description of this role-group
        :type description: Str
        """
        method = 'role_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def role_remove_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        service=None,
        user=None,
    ):
        """Remove members from a role.
        :param cn: Role name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        :param service: services to remove
        :type service: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'role_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if service:
            _params['service'] = service
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def role_remove_privilege(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        privilege=None,
    ):
        """Remove privileges from a role.
        :param cn: Role name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param privilege: privileges
        :type privilege: Str
        """
        method = 'role_remove_privilege'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if privilege:
            _params['privilege'] = privilege
        
        return self._request(method, _args, _params)

    def role_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a role.
        :param cn: Role name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'role_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def schema(
        self,
        known_fingerprints=None,
    ):
        """None
        :param known_fingerprints: Fingerprint of schema cached by client
        :type known_fingerprints: Str
        """
        method = 'schema'
        
        _args = list()
        
        _params = dict()
        if known_fingerprints:
            _params['known_fingerprints'] = known_fingerprints
        
        return self._request(method, _args, _params)

    def selfservice_add(
        self,
        aciname,
        attrs,
        opt_all=True,
        raw=False,
        permissions=None,
    ):
        """Add a new self-service permission.
        :param aciname: Self-service name
        :type aciname: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param attrs: Attributes to which the permission applies.
        :type attrs: Str
        :param permissions: Permissions to grant (read, write). Default is write.
        :type permissions: Str
        """
        method = 'selfservice_add'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['attrs'] = attrs
        if permissions:
            _params['permissions'] = permissions
        
        return self._request(method, _args, _params)

    def selfservice_del(
        self,
        aciname,
    ):
        """Delete a self-service permission.
        :param aciname: Self-service name
        :type aciname: Str
        """
        method = 'selfservice_del'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def selfservice_find(
        self,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        attrs=None,
        aciname=None,
        permissions=None,
    ):
        """Search for a self-service permission.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param attrs: Attributes to which the permission applies.
        :type attrs: Str
        :param aciname: Self-service name
        :type aciname: Str
        :param permissions: Permissions to grant (read, write). Default is write.
        :type permissions: Str
        """
        method = 'selfservice_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if attrs:
            _params['attrs'] = attrs
        if aciname:
            _params['aciname'] = aciname
        if permissions:
            _params['permissions'] = permissions
        
        return self._request(method, _args, _params)

    def selfservice_mod(
        self,
        aciname,
        opt_all=True,
        raw=False,
        attrs=None,
        permissions=None,
    ):
        """Modify a self-service permission.
        :param aciname: Self-service name
        :type aciname: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param attrs: Attributes to which the permission applies.
        :type attrs: Str
        :param permissions: Permissions to grant (read, write). Default is write.
        :type permissions: Str
        """
        method = 'selfservice_mod'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        if attrs:
            _params['attrs'] = attrs
        if permissions:
            _params['permissions'] = permissions
        
        return self._request(method, _args, _params)

    def selfservice_show(
        self,
        aciname,
        opt_all=True,
        raw=False,
    ):
        """Display information about a self-service permission.
        :param aciname: Self-service name
        :type aciname: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'selfservice_show'
        
        _args = list()
        _args.append(aciname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def selinuxusermap_add(
        self,
        cn,
        ipaselinuxuser,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        ipaenabledflag=None,
        description=None,
        seealso=None,
        hostcategory=None,
        usercategory=None,
    ):
        """Create a new SELinux User Map.
        :param cn: Rule name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param seealso: HBAC Rule that defines the users, groups and hostgroups
        :type seealso: Str
        :param ipaselinuxuser: SELinux User
        :type ipaselinuxuser: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'selinuxusermap_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if seealso:
            _params['seealso'] = seealso
        _params['ipaselinuxuser'] = ipaselinuxuser
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def selinuxusermap_add_host(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Add target hosts and hostgroups to an SELinux User Map rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        """
        method = 'selinuxusermap_add_host'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def selinuxusermap_add_user(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Add users and groups to an SELinux User Map rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param user: users to add
        :type user: Str
        """
        method = 'selinuxusermap_add_user'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def selinuxusermap_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a SELinux User Map.
        :param cn: Rule name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'selinuxusermap_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def selinuxusermap_disable(
        self,
        cn,
    ):
        """Disable an SELinux User Map rule.
        :param cn: Rule name
        :type cn: Str
        """
        method = 'selinuxusermap_disable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def selinuxusermap_enable(
        self,
        cn,
    ):
        """Enable an SELinux User Map rule.
        :param cn: Rule name
        :type cn: Str
        """
        method = 'selinuxusermap_enable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def selinuxusermap_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        ipaenabledflag=None,
        description=None,
        seealso=None,
        cn=None,
        ipaselinuxuser=None,
        hostcategory=None,
        usercategory=None,
    ):
        """Search for SELinux User Maps.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param seealso: HBAC Rule that defines the users, groups and hostgroups
        :type seealso: Str
        :param cn: Rule name
        :type cn: Str
        :param ipaselinuxuser: SELinux User
        :type ipaselinuxuser: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'selinuxusermap_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if seealso:
            _params['seealso'] = seealso
        if cn:
            _params['cn'] = cn
        if ipaselinuxuser:
            _params['ipaselinuxuser'] = ipaselinuxuser
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def selinuxusermap_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        ipaenabledflag=None,
        description=None,
        seealso=None,
        ipaselinuxuser=None,
        hostcategory=None,
        usercategory=None,
    ):
        """Modify a SELinux User Map.
        :param cn: Rule name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param description: Description
        :type description: Str
        :param seealso: HBAC Rule that defines the users, groups and hostgroups
        :type seealso: Str
        :param ipaselinuxuser: SELinux User
        :type ipaselinuxuser: Str
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'selinuxusermap_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if description:
            _params['description'] = description
        if seealso:
            _params['seealso'] = seealso
        if ipaselinuxuser:
            _params['ipaselinuxuser'] = ipaselinuxuser
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def selinuxusermap_remove_host(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Remove target hosts and hostgroups from an SELinux User Map rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        """
        method = 'selinuxusermap_remove_host'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def selinuxusermap_remove_user(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Remove users and groups from an SELinux User Map rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'selinuxusermap_remove_user'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def selinuxusermap_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display the properties of a SELinux User Map rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'selinuxusermap_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def server_conncheck(
        self,
        remote_cn,
        cn,
    ):
        """Check connection to remote IPA server.
        :param remote_cn: Remote IPA server hostname
        :type remote_cn: Str
        :param cn: IPA server hostname
        :type cn: Str
        """
        method = 'server_conncheck'
        
        _args = list()
        _args.append(remote_cn)
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def server_del(
        self,
        cn,
        opt_continue=False,
        force=False,
        ignore_last_of_role=False,
        ignore_topology_disconnect=False,
    ):
        """Delete IPA server.
        :param cn: IPA server hostname
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        :param force: Force server removal even if it does not exist
        :type force: Flag
        :param ignore_last_of_role: Skip a check whether the last CA master or DNS server is removed
        :type ignore_last_of_role: Flag
        :param ignore_topology_disconnect: Ignore topology connectivity problems after removal
        :type ignore_topology_disconnect: Flag
        """
        method = 'server_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        if force:
            _params['force'] = force
        if ignore_last_of_role:
            _params['ignore_last_of_role'] = ignore_last_of_role
        if ignore_topology_disconnect:
            _params['ignore_topology_disconnect'] = ignore_topology_disconnect
        
        return self._request(method, _args, _params)

    def server_find(
        self,
        criteria=None,
        in_location=None,
        not_in_location=None,
        sizelimit=None,
        timelimit=None,
        no_topologysuffix=None,
        servrole=None,
        topologysuffix=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        ipamaxdomainlevel=None,
        ipamindomainlevel=None,
        cn=None,
    ):
        """Search for IPA servers.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param in_location: Search for servers with these ipa locations.
        :type in_location: DNSNameParam
        :param not_in_location: Search for servers without these ipa locations.
        :type not_in_location: DNSNameParam
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param no_topologysuffix: Search for servers without these managed suffixes.
        :type no_topologysuffix: Str
        :param servrole: Search for servers with these enabled roles.
        :type servrole: Str
        :param topologysuffix: Search for servers with these managed suffixes.
        :type topologysuffix: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipamaxdomainlevel: Maximum domain level
        :type ipamaxdomainlevel: Int
        :param ipamindomainlevel: Minimum domain level
        :type ipamindomainlevel: Int
        :param cn: IPA server hostname
        :type cn: Str
        """
        method = 'server_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if in_location:
            _params['in_location'] = in_location
        if not_in_location:
            _params['not_in_location'] = not_in_location
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if no_topologysuffix:
            _params['no_topologysuffix'] = no_topologysuffix
        if servrole:
            _params['servrole'] = servrole
        if topologysuffix:
            _params['topologysuffix'] = topologysuffix
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipamaxdomainlevel:
            _params['ipamaxdomainlevel'] = ipamaxdomainlevel
        if ipamindomainlevel:
            _params['ipamindomainlevel'] = ipamindomainlevel
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def server_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        ipalocation_location=None,
        ipaserviceweight=None,
    ):
        """Modify information about an IPA server.
        :param cn: IPA server hostname
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipalocation_location: Server location
        :type ipalocation_location: DNSNameParam
        :param ipaserviceweight: Weight for server services
        :type ipaserviceweight: Int
        """
        method = 'server_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if ipalocation_location:
            _params['ipalocation_location'] = ipalocation_location
        if ipaserviceweight:
            _params['ipaserviceweight'] = ipaserviceweight
        
        return self._request(method, _args, _params)

    def server_role_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        role_servrole=None,
        status='enabled',
        opt_all=True,
        include_master=False,
        raw=False,
        server_server=None,
    ):
        """Find a server role on a server(s)
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param role_servrole: IPA server role name
        :type role_servrole: Str
        :param status: Status of the role
        :type status: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param include_master: Include IPA master entries
        :type include_master: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param server_server: IPA server hostname
        :type server_server: Str
        """
        method = 'server_role_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if role_servrole:
            _params['role_servrole'] = role_servrole
        if status:
            _params['status'] = status
        _params['all'] = opt_all
        _params['include_master'] = include_master
        _params['raw'] = raw
        if server_server:
            _params['server_server'] = server_server
        
        return self._request(method, _args, _params)

    def server_role_show(
        self,
        role_servrole,
        server_server,
        opt_all=True,
        raw=False,
    ):
        """Show role status on a server
        :param role_servrole: IPA server role name
        :type role_servrole: Str
        :param server_server: IPA server hostname
        :type server_server: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'server_role_show'
        
        _args = list()
        _args.append(role_servrole)
        _args.append(server_server)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def server_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Show IPA server.
        :param cn: IPA server hostname
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'server_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def server_state(
        self,
        cn,
        state,
    ):
        """Set enabled/hidden state of a server.
        :param cn: IPA server hostname
        :type cn: Str
        :param state: Server state
        :type state: StrEnum
        """
        method = 'server_state'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['state'] = state
        
        return self._request(method, _args, _params)

    def service_add(
        self,
        krbcanonicalname,
        ipakrbokasdelegate=None,
        ipakrboktoauthasdelegate=None,
        ipakrbrequirespreauth=None,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        force=False,
        no_members=False,
        raw=False,
        usercertificate=None,
        krbprincipalauthind=None,
        ipakrbauthzdata=None,
    ):
        """Add a new IPA service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param ipakrbokasdelegate: Client credentials may be delegated to the service
        :type ipakrbokasdelegate: Bool
        :param ipakrboktoauthasdelegate: The service is allowed to authenticate on behalf of a client
        :type ipakrboktoauthasdelegate: Bool
        :param ipakrbrequirespreauth: Pre-authentication is required for the service
        :type ipakrbrequirespreauth: Bool
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param force: force principal name even if not in DNS
        :type force: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded service certificate
        :type usercertificate: Certificate
        :param krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type krbprincipalauthind: Str
        :param ipakrbauthzdata: Override default list of supported PAC types. Use 'NONE' to disable PAC support for this service, e.g. this might be necessary for NFS services.
        :type ipakrbauthzdata: StrEnum
        """
        method = 'service_add'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        if ipakrbokasdelegate:
            _params['ipakrbokasdelegate'] = ipakrbokasdelegate
        if ipakrboktoauthasdelegate:
            _params['ipakrboktoauthasdelegate'] = ipakrboktoauthasdelegate
        if ipakrbrequirespreauth:
            _params['ipakrbrequirespreauth'] = ipakrbrequirespreauth
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['force'] = force
        _params['no_members'] = no_members
        _params['raw'] = raw
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbprincipalauthind:
            _params['krbprincipalauthind'] = krbprincipalauthind
        if ipakrbauthzdata:
            _params['ipakrbauthzdata'] = ipakrbauthzdata
        
        return self._request(method, _args, _params)

    def service_add_cert(
        self,
        krbcanonicalname,
        usercertificate,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add new certificates to a service
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded service certificate
        :type usercertificate: Certificate
        """
        method = 'service_add_cert'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def service_add_host(
        self,
        krbcanonicalname,
        opt_all=True,
        no_members=False,
        raw=False,
        host=None,
    ):
        """Add hosts that can manage this service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param host: hosts to add
        :type host: Str
        """
        method = 'service_add_host'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def service_add_principal(
        self,
        krbcanonicalname,
        krbprincipalname,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add new principal alias to a service
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param krbprincipalname: Service principal alias
        :type krbprincipalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'service_add_principal'
        
        _args = list()
        _args.append(krbcanonicalname)
        _args.append(krbprincipalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def service_allow_create_keytab(
        self,
        krbcanonicalname,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        user=None,
    ):
        """Allow users, groups, hosts or host groups to create a keytab of this service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        :param user: users to add
        :type user: Str
        """
        method = 'service_allow_create_keytab'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def service_allow_retrieve_keytab(
        self,
        krbcanonicalname,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        user=None,
    ):
        """Allow users, groups, hosts or host groups to retrieve a keytab of this service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        :param user: users to add
        :type user: Str
        """
        method = 'service_allow_retrieve_keytab'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def service_del(
        self,
        krbcanonicalname,
        opt_continue=False,
    ):
        """Delete an IPA service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'service_del'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def service_disable(
        self,
        krbcanonicalname,
    ):
        """Disable the Kerberos key and SSL certificate of a service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        """
        method = 'service_disable'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def service_disallow_create_keytab(
        self,
        krbcanonicalname,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        user=None,
    ):
        """Disallow users, groups, hosts or host groups to create a keytab of this service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'service_disallow_create_keytab'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def service_disallow_retrieve_keytab(
        self,
        krbcanonicalname,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        hostgroup=None,
        host=None,
        user=None,
    ):
        """Disallow users, groups, hosts or host groups to retrieve a keytab of this service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'service_disallow_retrieve_keytab'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def service_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        man_by_host=None,
        not_man_by_host=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        krbcanonicalname=None,
        krbprincipalname=None,
        krbprincipalauthind=None,
        ipakrbauthzdata=None,
    ):
        """Search for IPA services.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param man_by_host: Search for services with these managed by hosts.
        :type man_by_host: Str
        :param not_man_by_host: Search for services without these managed by hosts.
        :type not_man_by_host: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("canonical-principal")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param krbprincipalname: Service principal alias
        :type krbprincipalname: Principal
        :param krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type krbprincipalauthind: Str
        :param ipakrbauthzdata: Override default list of supported PAC types. Use 'NONE' to disable PAC support for this service, e.g. this might be necessary for NFS services.
        :type ipakrbauthzdata: StrEnum
        """
        method = 'service_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if man_by_host:
            _params['man_by_host'] = man_by_host
        if not_man_by_host:
            _params['not_man_by_host'] = not_man_by_host
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if krbcanonicalname:
            _params['krbcanonicalname'] = krbcanonicalname
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        if krbprincipalauthind:
            _params['krbprincipalauthind'] = krbprincipalauthind
        if ipakrbauthzdata:
            _params['ipakrbauthzdata'] = ipakrbauthzdata
        
        return self._request(method, _args, _params)

    def service_mod(
        self,
        krbcanonicalname,
        ipakrbokasdelegate=None,
        ipakrboktoauthasdelegate=None,
        ipakrbrequirespreauth=None,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        usercertificate=None,
        krbprincipalname=None,
        krbprincipalauthind=None,
        ipakrbauthzdata=None,
    ):
        """Modify an existing IPA service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param ipakrbokasdelegate: Client credentials may be delegated to the service
        :type ipakrbokasdelegate: Bool
        :param ipakrboktoauthasdelegate: The service is allowed to authenticate on behalf of a client
        :type ipakrboktoauthasdelegate: Bool
        :param ipakrbrequirespreauth: Pre-authentication is required for the service
        :type ipakrbrequirespreauth: Bool
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param usercertificate: Base-64 encoded service certificate
        :type usercertificate: Certificate
        :param krbprincipalname: Service principal alias
        :type krbprincipalname: Principal
        :param krbprincipalauthind: Defines a whitelist for Authentication Indicators. Use 'otp' to allow OTP-based 2FA authentications. Use 'radius' to allow RADIUS-based 2FA authentications. Other values may be used for custom configurations.
        :type krbprincipalauthind: Str
        :param ipakrbauthzdata: Override default list of supported PAC types. Use 'NONE' to disable PAC support for this service, e.g. this might be necessary for NFS services.
        :type ipakrbauthzdata: StrEnum
        """
        method = 'service_mod'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        if ipakrbokasdelegate:
            _params['ipakrbokasdelegate'] = ipakrbokasdelegate
        if ipakrboktoauthasdelegate:
            _params['ipakrboktoauthasdelegate'] = ipakrboktoauthasdelegate
        if ipakrbrequirespreauth:
            _params['ipakrbrequirespreauth'] = ipakrbrequirespreauth
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        if krbprincipalauthind:
            _params['krbprincipalauthind'] = krbprincipalauthind
        if ipakrbauthzdata:
            _params['ipakrbauthzdata'] = ipakrbauthzdata
        
        return self._request(method, _args, _params)

    def service_remove_cert(
        self,
        krbcanonicalname,
        usercertificate,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove certificates from a service
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded service certificate
        :type usercertificate: Certificate
        """
        method = 'service_remove_cert'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def service_remove_host(
        self,
        krbcanonicalname,
        opt_all=True,
        no_members=False,
        raw=False,
        host=None,
    ):
        """Remove hosts that can manage this service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param host: hosts to remove
        :type host: Str
        """
        method = 'service_remove_host'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def service_remove_principal(
        self,
        krbcanonicalname,
        krbprincipalname,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove principal alias from a service
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param krbprincipalname: Service principal alias
        :type krbprincipalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'service_remove_principal'
        
        _args = list()
        _args.append(krbcanonicalname)
        _args.append(krbprincipalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def service_show(
        self,
        krbcanonicalname,
        out=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about an IPA service.
        :param krbcanonicalname: Service principal
        :type krbcanonicalname: Principal
        :param out: file to store certificate in
        :type out: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'service_show'
        
        _args = list()
        _args.append(krbcanonicalname)
        
        _params = dict()
        if out:
            _params['out'] = out
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def servicedelegationrule_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Create a new service delegation rule.
        :param cn: Delegation name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'servicedelegationrule_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def servicedelegationrule_add_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        principal=None,
    ):
        """Add member to a named service delegation rule.
        :param cn: Delegation name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param principal: principal to add
        :type principal: Str
        """
        method = 'servicedelegationrule_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if principal:
            _params['principal'] = principal
        
        return self._request(method, _args, _params)

    def servicedelegationrule_add_target(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        servicedelegationtarget=None,
    ):
        """Add target to a named service delegation rule.
        :param cn: Delegation name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param servicedelegationtarget: service delegation targets to add
        :type servicedelegationtarget: Str
        """
        method = 'servicedelegationrule_add_target'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if servicedelegationtarget:
            _params['servicedelegationtarget'] = servicedelegationtarget
        
        return self._request(method, _args, _params)

    def servicedelegationrule_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete service delegation.
        :param cn: Delegation name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'servicedelegationrule_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def servicedelegationrule_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        cn=None,
    ):
        """Search for service delegations rule.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("delegation-name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param cn: Delegation name
        :type cn: Str
        """
        method = 'servicedelegationrule_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def servicedelegationrule_remove_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        principal=None,
    ):
        """Remove member from a named service delegation rule.
        :param cn: Delegation name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param principal: principal to remove
        :type principal: Str
        """
        method = 'servicedelegationrule_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if principal:
            _params['principal'] = principal
        
        return self._request(method, _args, _params)

    def servicedelegationrule_remove_target(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        servicedelegationtarget=None,
    ):
        """Remove target from a named service delegation rule.
        :param cn: Delegation name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param servicedelegationtarget: service delegation targets to remove
        :type servicedelegationtarget: Str
        """
        method = 'servicedelegationrule_remove_target'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if servicedelegationtarget:
            _params['servicedelegationtarget'] = servicedelegationtarget
        
        return self._request(method, _args, _params)

    def servicedelegationrule_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a named service delegation rule.
        :param cn: Delegation name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'servicedelegationrule_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def servicedelegationtarget_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
    ):
        """Create a new service delegation target.
        :param cn: Delegation name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'servicedelegationtarget_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def servicedelegationtarget_add_member(
        self,
        cn,
        opt_all=True,
        raw=False,
        principal=None,
    ):
        """Add member to a named service delegation target.
        :param cn: Delegation name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param principal: principal to add
        :type principal: Str
        """
        method = 'servicedelegationtarget_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        if principal:
            _params['principal'] = principal
        
        return self._request(method, _args, _params)

    def servicedelegationtarget_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete service delegation target.
        :param cn: Delegation name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'servicedelegationtarget_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def servicedelegationtarget_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        cn=None,
    ):
        """Search for service delegation target.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("delegation-name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param cn: Delegation name
        :type cn: Str
        """
        method = 'servicedelegationtarget_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def servicedelegationtarget_remove_member(
        self,
        cn,
        opt_all=True,
        raw=False,
        principal=None,
    ):
        """Remove member from a named service delegation target.
        :param cn: Delegation name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param principal: principal to remove
        :type principal: Str
        """
        method = 'servicedelegationtarget_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        if principal:
            _params['principal'] = principal
        
        return self._request(method, _args, _params)

    def servicedelegationtarget_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about a named service delegation target.
        :param cn: Delegation name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'servicedelegationtarget_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
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
        uid,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Activate a stage user.
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'stageuser_activate'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def stageuser_add(
        self,
        uid,
        givenname,
        sn,
        cn,
        from_delete=None,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        random=False,
        raw=False,
        usercertificate=None,
        krbpasswordexpiration=None,
        krbprincipalexpiration=None,
        gidnumber=None,
        uidnumber=None,
        userpassword=None,
        carlicense=None,
        l=None,
        userclass=None,
        departmentnumber=None,
        mail=None,
        employeenumber=None,
        employeetype=None,
        facsimiletelephonenumber=None,
        homedirectory=None,
        manager=None,
        mobile=None,
        ou=None,
        pager=None,
        telephonenumber=None,
        postalcode=None,
        preferredlanguage=None,
        ipatokenradiusconfiglink=None,
        ipatokenradiususername=None,
        loginshell=None,
        ipasshpubkey=None,
        st=None,
        street=None,
        title=None,
        ipauserauthtype=None,
        krbprincipalname=None,
        displayname=None,
        gecos=None,
        initials=None,
    ):
        """Add a new stage user.
        :param uid: User login
        :type uid: Str
        :param from_delete: Create Stage user in from a delete user
        :type from_delete: Bool
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param random: Generate a random user password
        :type random: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        :param krbpasswordexpiration: User password expiration
        :type krbpasswordexpiration: DateTime
        :param krbprincipalexpiration: Kerberos principal expiration
        :type krbprincipalexpiration: DateTime
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number (system will assign one if not provided)
        :type uidnumber: Int
        :param userpassword: Prompt to set the user password
        :type userpassword: Password
        :param carlicense: Car License
        :type carlicense: Str
        :param l: City
        :type l: Str
        :param userclass: User category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param departmentnumber: Department Number
        :type departmentnumber: Str
        :param mail: Email address
        :type mail: Str
        :param employeenumber: Employee Number
        :type employeenumber: Str
        :param employeetype: Employee Type
        :type employeetype: Str
        :param facsimiletelephonenumber: Fax Number
        :type facsimiletelephonenumber: Str
        :param givenname: First name
        :type givenname: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param sn: Last name
        :type sn: Str
        :param manager: Manager
        :type manager: Str
        :param mobile: Mobile Telephone Number
        :type mobile: Str
        :param ou: Org. Unit
        :type ou: Str
        :param pager: Pager Number
        :type pager: Str
        :param telephonenumber: Telephone Number
        :type telephonenumber: Str
        :param postalcode: ZIP
        :type postalcode: Str
        :param preferredlanguage: Preferred Language
        :type preferredlanguage: Str
        :param ipatokenradiusconfiglink: RADIUS proxy configuration
        :type ipatokenradiusconfiglink: Str
        :param ipatokenradiususername: RADIUS proxy username
        :type ipatokenradiususername: Str
        :param loginshell: Login shell
        :type loginshell: Str
        :param ipasshpubkey: SSH public key
        :type ipasshpubkey: Str
        :param st: State/Province
        :type st: Str
        :param street: Street address
        :type street: Str
        :param title: Job Title
        :type title: Str
        :param ipauserauthtype: Types of supported user authentication
        :type ipauserauthtype: StrEnum
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param cn: Full name
        :type cn: Str
        :param displayname: Display name
        :type displayname: Str
        :param gecos: GECOS
        :type gecos: Str
        :param initials: Initials
        :type initials: Str
        """
        method = 'stageuser_add'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        if from_delete:
            _params['from_delete'] = from_delete
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if random:
            _params['random'] = random
        _params['raw'] = raw
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbpasswordexpiration:
            _params['krbpasswordexpiration'] = krbpasswordexpiration
        if krbprincipalexpiration:
            _params['krbprincipalexpiration'] = krbprincipalexpiration
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if userpassword:
            _params['userpassword'] = userpassword
        if carlicense:
            _params['carlicense'] = carlicense
        if l:
            _params['l'] = l
        if userclass:
            _params['userclass'] = userclass
        if departmentnumber:
            _params['departmentnumber'] = departmentnumber
        if mail:
            _params['mail'] = mail
        if employeenumber:
            _params['employeenumber'] = employeenumber
        if employeetype:
            _params['employeetype'] = employeetype
        if facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = facsimiletelephonenumber
        _params['givenname'] = givenname
        if homedirectory:
            _params['homedirectory'] = homedirectory
        _params['sn'] = sn
        if manager:
            _params['manager'] = manager
        if mobile:
            _params['mobile'] = mobile
        if ou:
            _params['ou'] = ou
        if pager:
            _params['pager'] = pager
        if telephonenumber:
            _params['telephonenumber'] = telephonenumber
        if postalcode:
            _params['postalcode'] = postalcode
        if preferredlanguage:
            _params['preferredlanguage'] = preferredlanguage
        if ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = ipatokenradiusconfiglink
        if ipatokenradiususername:
            _params['ipatokenradiususername'] = ipatokenradiususername
        if loginshell:
            _params['loginshell'] = loginshell
        if ipasshpubkey:
            _params['ipasshpubkey'] = ipasshpubkey
        if st:
            _params['st'] = st
        if street:
            _params['street'] = street
        if title:
            _params['title'] = title
        if ipauserauthtype:
            _params['ipauserauthtype'] = ipauserauthtype
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        _params['cn'] = cn
        if displayname:
            _params['displayname'] = displayname
        if gecos:
            _params['gecos'] = gecos
        if initials:
            _params['initials'] = initials
        
        return self._request(method, _args, _params)

    def stageuser_add_cert(
        self,
        uid,
        usercertificate,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add one or more certificates to the stageuser entry
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        """
        method = 'stageuser_add_cert'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def stageuser_add_certmapdata(
        self,
        uid,
        ipacertmapdata=None,
        certificate=None,
        issuer=None,
        subject=None,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add one or more certificate mappings to the stage user entry.
        :param ipacertmapdata: Certificate mapping data
        :type ipacertmapdata: Str
        :param uid: User login
        :type uid: Str
        :param certificate: Base-64 encoded user certificate
        :type certificate: Certificate
        :param issuer: Issuer of the certificate
        :type issuer: DNParam
        :param subject: Subject of the certificate
        :type subject: DNParam
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'stageuser_add_certmapdata'
        
        _args = list()
        _args.append(ipacertmapdata)
        _args.append(uid)
        
        _params = dict()
        if certificate:
            _params['certificate'] = certificate
        if issuer:
            _params['issuer'] = issuer
        if subject:
            _params['subject'] = subject
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def stageuser_add_manager(
        self,
        uid,
        opt_all=True,
        no_members=False,
        raw=False,
        user=None,
    ):
        """Add a manager to the stage user entry
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param user: users to add
        :type user: Str
        """
        method = 'stageuser_add_manager'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def stageuser_add_principal(
        self,
        uid,
        krbprincipalname,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add new principal alias to the stageuser entry
        :param uid: User login
        :type uid: Str
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'stageuser_add_principal'
        
        _args = list()
        _args.append(uid)
        _args.append(krbprincipalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def stageuser_del(
        self,
        uid,
        opt_continue=False,
    ):
        """Delete a stage user.
        :param uid: User login
        :type uid: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'stageuser_del'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def stageuser_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        in_group=None,
        in_hbacrule=None,
        in_netgroup=None,
        in_role=None,
        in_sudorule=None,
        not_in_group=None,
        not_in_hbacrule=None,
        not_in_netgroup=None,
        not_in_role=None,
        not_in_sudorule=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        usercertificate=None,
        krbpasswordexpiration=None,
        krbprincipalexpiration=None,
        gidnumber=None,
        uidnumber=None,
        userpassword=None,
        krbprincipalname=None,
        carlicense=None,
        l=None,
        userclass=None,
        cn=None,
        departmentnumber=None,
        displayname=None,
        mail=None,
        employeenumber=None,
        employeetype=None,
        facsimiletelephonenumber=None,
        givenname=None,
        gecos=None,
        homedirectory=None,
        initials=None,
        sn=None,
        uid=None,
        manager=None,
        mobile=None,
        ou=None,
        pager=None,
        telephonenumber=None,
        postalcode=None,
        preferredlanguage=None,
        ipatokenradiusconfiglink=None,
        ipatokenradiususername=None,
        loginshell=None,
        st=None,
        street=None,
        title=None,
        ipauserauthtype=None,
    ):
        """Search for stage users.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param in_group: Search for stage users with these member of groups.
        :type in_group: Str
        :param in_hbacrule: Search for stage users with these member of HBAC rules.
        :type in_hbacrule: Str
        :param in_netgroup: Search for stage users with these member of netgroups.
        :type in_netgroup: Str
        :param in_role: Search for stage users with these member of roles.
        :type in_role: Str
        :param in_sudorule: Search for stage users with these member of sudo rules.
        :type in_sudorule: Str
        :param not_in_group: Search for stage users without these member of groups.
        :type not_in_group: Str
        :param not_in_hbacrule: Search for stage users without these member of HBAC rules.
        :type not_in_hbacrule: Str
        :param not_in_netgroup: Search for stage users without these member of netgroups.
        :type not_in_netgroup: Str
        :param not_in_role: Search for stage users without these member of roles.
        :type not_in_role: Str
        :param not_in_sudorule: Search for stage users without these member of sudo rules.
        :type not_in_sudorule: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("login")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        :param krbpasswordexpiration: User password expiration
        :type krbpasswordexpiration: DateTime
        :param krbprincipalexpiration: Kerberos principal expiration
        :type krbprincipalexpiration: DateTime
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number (system will assign one if not provided)
        :type uidnumber: Int
        :param userpassword: Prompt to set the user password
        :type userpassword: Password
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param carlicense: Car License
        :type carlicense: Str
        :param l: City
        :type l: Str
        :param userclass: User category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param cn: Full name
        :type cn: Str
        :param departmentnumber: Department Number
        :type departmentnumber: Str
        :param displayname: Display name
        :type displayname: Str
        :param mail: Email address
        :type mail: Str
        :param employeenumber: Employee Number
        :type employeenumber: Str
        :param employeetype: Employee Type
        :type employeetype: Str
        :param facsimiletelephonenumber: Fax Number
        :type facsimiletelephonenumber: Str
        :param givenname: First name
        :type givenname: Str
        :param gecos: GECOS
        :type gecos: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param initials: Initials
        :type initials: Str
        :param sn: Last name
        :type sn: Str
        :param uid: User login
        :type uid: Str
        :param manager: Manager
        :type manager: Str
        :param mobile: Mobile Telephone Number
        :type mobile: Str
        :param ou: Org. Unit
        :type ou: Str
        :param pager: Pager Number
        :type pager: Str
        :param telephonenumber: Telephone Number
        :type telephonenumber: Str
        :param postalcode: ZIP
        :type postalcode: Str
        :param preferredlanguage: Preferred Language
        :type preferredlanguage: Str
        :param ipatokenradiusconfiglink: RADIUS proxy configuration
        :type ipatokenradiusconfiglink: Str
        :param ipatokenradiususername: RADIUS proxy username
        :type ipatokenradiususername: Str
        :param loginshell: Login shell
        :type loginshell: Str
        :param st: State/Province
        :type st: Str
        :param street: Street address
        :type street: Str
        :param title: Job Title
        :type title: Str
        :param ipauserauthtype: Types of supported user authentication
        :type ipauserauthtype: StrEnum
        """
        method = 'stageuser_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if in_group:
            _params['in_group'] = in_group
        if in_hbacrule:
            _params['in_hbacrule'] = in_hbacrule
        if in_netgroup:
            _params['in_netgroup'] = in_netgroup
        if in_role:
            _params['in_role'] = in_role
        if in_sudorule:
            _params['in_sudorule'] = in_sudorule
        if not_in_group:
            _params['not_in_group'] = not_in_group
        if not_in_hbacrule:
            _params['not_in_hbacrule'] = not_in_hbacrule
        if not_in_netgroup:
            _params['not_in_netgroup'] = not_in_netgroup
        if not_in_role:
            _params['not_in_role'] = not_in_role
        if not_in_sudorule:
            _params['not_in_sudorule'] = not_in_sudorule
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbpasswordexpiration:
            _params['krbpasswordexpiration'] = krbpasswordexpiration
        if krbprincipalexpiration:
            _params['krbprincipalexpiration'] = krbprincipalexpiration
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if userpassword:
            _params['userpassword'] = userpassword
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        if carlicense:
            _params['carlicense'] = carlicense
        if l:
            _params['l'] = l
        if userclass:
            _params['userclass'] = userclass
        if cn:
            _params['cn'] = cn
        if departmentnumber:
            _params['departmentnumber'] = departmentnumber
        if displayname:
            _params['displayname'] = displayname
        if mail:
            _params['mail'] = mail
        if employeenumber:
            _params['employeenumber'] = employeenumber
        if employeetype:
            _params['employeetype'] = employeetype
        if facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = facsimiletelephonenumber
        if givenname:
            _params['givenname'] = givenname
        if gecos:
            _params['gecos'] = gecos
        if homedirectory:
            _params['homedirectory'] = homedirectory
        if initials:
            _params['initials'] = initials
        if sn:
            _params['sn'] = sn
        if uid:
            _params['uid'] = uid
        if manager:
            _params['manager'] = manager
        if mobile:
            _params['mobile'] = mobile
        if ou:
            _params['ou'] = ou
        if pager:
            _params['pager'] = pager
        if telephonenumber:
            _params['telephonenumber'] = telephonenumber
        if postalcode:
            _params['postalcode'] = postalcode
        if preferredlanguage:
            _params['preferredlanguage'] = preferredlanguage
        if ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = ipatokenradiusconfiglink
        if ipatokenradiususername:
            _params['ipatokenradiususername'] = ipatokenradiususername
        if loginshell:
            _params['loginshell'] = loginshell
        if st:
            _params['st'] = st
        if street:
            _params['street'] = street
        if title:
            _params['title'] = title
        if ipauserauthtype:
            _params['ipauserauthtype'] = ipauserauthtype
        
        return self._request(method, _args, _params)

    def stageuser_mod(
        self,
        uid,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        random=False,
        raw=False,
        rights=False,
        usercertificate=None,
        krbpasswordexpiration=None,
        krbprincipalexpiration=None,
        gidnumber=None,
        uidnumber=None,
        userpassword=None,
        krbprincipalname=None,
        carlicense=None,
        l=None,
        userclass=None,
        cn=None,
        departmentnumber=None,
        displayname=None,
        mail=None,
        employeenumber=None,
        employeetype=None,
        facsimiletelephonenumber=None,
        givenname=None,
        gecos=None,
        homedirectory=None,
        initials=None,
        sn=None,
        manager=None,
        mobile=None,
        ou=None,
        pager=None,
        telephonenumber=None,
        postalcode=None,
        preferredlanguage=None,
        ipatokenradiusconfiglink=None,
        ipatokenradiususername=None,
        loginshell=None,
        ipasshpubkey=None,
        st=None,
        street=None,
        title=None,
        ipauserauthtype=None,
    ):
        """Modify a stage user.
        :param uid: User login
        :type uid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the stage user object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param random: Generate a random user password
        :type random: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        :param krbpasswordexpiration: User password expiration
        :type krbpasswordexpiration: DateTime
        :param krbprincipalexpiration: Kerberos principal expiration
        :type krbprincipalexpiration: DateTime
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number (system will assign one if not provided)
        :type uidnumber: Int
        :param userpassword: Prompt to set the user password
        :type userpassword: Password
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param carlicense: Car License
        :type carlicense: Str
        :param l: City
        :type l: Str
        :param userclass: User category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param cn: Full name
        :type cn: Str
        :param departmentnumber: Department Number
        :type departmentnumber: Str
        :param displayname: Display name
        :type displayname: Str
        :param mail: Email address
        :type mail: Str
        :param employeenumber: Employee Number
        :type employeenumber: Str
        :param employeetype: Employee Type
        :type employeetype: Str
        :param facsimiletelephonenumber: Fax Number
        :type facsimiletelephonenumber: Str
        :param givenname: First name
        :type givenname: Str
        :param gecos: GECOS
        :type gecos: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param initials: Initials
        :type initials: Str
        :param sn: Last name
        :type sn: Str
        :param manager: Manager
        :type manager: Str
        :param mobile: Mobile Telephone Number
        :type mobile: Str
        :param ou: Org. Unit
        :type ou: Str
        :param pager: Pager Number
        :type pager: Str
        :param telephonenumber: Telephone Number
        :type telephonenumber: Str
        :param postalcode: ZIP
        :type postalcode: Str
        :param preferredlanguage: Preferred Language
        :type preferredlanguage: Str
        :param ipatokenradiusconfiglink: RADIUS proxy configuration
        :type ipatokenradiusconfiglink: Str
        :param ipatokenradiususername: RADIUS proxy username
        :type ipatokenradiususername: Str
        :param loginshell: Login shell
        :type loginshell: Str
        :param ipasshpubkey: SSH public key
        :type ipasshpubkey: Str
        :param st: State/Province
        :type st: Str
        :param street: Street address
        :type street: Str
        :param title: Job Title
        :type title: Str
        :param ipauserauthtype: Types of supported user authentication
        :type ipauserauthtype: StrEnum
        """
        method = 'stageuser_mod'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if random:
            _params['random'] = random
        _params['raw'] = raw
        _params['rights'] = rights
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbpasswordexpiration:
            _params['krbpasswordexpiration'] = krbpasswordexpiration
        if krbprincipalexpiration:
            _params['krbprincipalexpiration'] = krbprincipalexpiration
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if userpassword:
            _params['userpassword'] = userpassword
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        if carlicense:
            _params['carlicense'] = carlicense
        if l:
            _params['l'] = l
        if userclass:
            _params['userclass'] = userclass
        if cn:
            _params['cn'] = cn
        if departmentnumber:
            _params['departmentnumber'] = departmentnumber
        if displayname:
            _params['displayname'] = displayname
        if mail:
            _params['mail'] = mail
        if employeenumber:
            _params['employeenumber'] = employeenumber
        if employeetype:
            _params['employeetype'] = employeetype
        if facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = facsimiletelephonenumber
        if givenname:
            _params['givenname'] = givenname
        if gecos:
            _params['gecos'] = gecos
        if homedirectory:
            _params['homedirectory'] = homedirectory
        if initials:
            _params['initials'] = initials
        if sn:
            _params['sn'] = sn
        if manager:
            _params['manager'] = manager
        if mobile:
            _params['mobile'] = mobile
        if ou:
            _params['ou'] = ou
        if pager:
            _params['pager'] = pager
        if telephonenumber:
            _params['telephonenumber'] = telephonenumber
        if postalcode:
            _params['postalcode'] = postalcode
        if preferredlanguage:
            _params['preferredlanguage'] = preferredlanguage
        if ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = ipatokenradiusconfiglink
        if ipatokenradiususername:
            _params['ipatokenradiususername'] = ipatokenradiususername
        if loginshell:
            _params['loginshell'] = loginshell
        if ipasshpubkey:
            _params['ipasshpubkey'] = ipasshpubkey
        if st:
            _params['st'] = st
        if street:
            _params['street'] = street
        if title:
            _params['title'] = title
        if ipauserauthtype:
            _params['ipauserauthtype'] = ipauserauthtype
        
        return self._request(method, _args, _params)

    def stageuser_remove_cert(
        self,
        uid,
        usercertificate,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove one or more certificates to the stageuser entry
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        """
        method = 'stageuser_remove_cert'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def stageuser_remove_certmapdata(
        self,
        uid,
        ipacertmapdata=None,
        certificate=None,
        issuer=None,
        subject=None,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove one or more certificate mappings from the stage user entry.
        :param ipacertmapdata: Certificate mapping data
        :type ipacertmapdata: Str
        :param uid: User login
        :type uid: Str
        :param certificate: Base-64 encoded user certificate
        :type certificate: Certificate
        :param issuer: Issuer of the certificate
        :type issuer: DNParam
        :param subject: Subject of the certificate
        :type subject: DNParam
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'stageuser_remove_certmapdata'
        
        _args = list()
        _args.append(ipacertmapdata)
        _args.append(uid)
        
        _params = dict()
        if certificate:
            _params['certificate'] = certificate
        if issuer:
            _params['issuer'] = issuer
        if subject:
            _params['subject'] = subject
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def stageuser_remove_manager(
        self,
        uid,
        opt_all=True,
        no_members=False,
        raw=False,
        user=None,
    ):
        """Remove a manager to the stage user entry
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param user: users to remove
        :type user: Str
        """
        method = 'stageuser_remove_manager'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def stageuser_remove_principal(
        self,
        uid,
        krbprincipalname,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove principal alias from the stageuser entry
        :param uid: User login
        :type uid: Str
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'stageuser_remove_principal'
        
        _args = list()
        _args.append(uid)
        _args.append(krbprincipalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def stageuser_show(
        self,
        uid,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a stage user.
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'stageuser_show'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def sudocmd_add(
        self,
        sudocmd,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        description=None,
    ):
        """Create new Sudo Command.
        :param sudocmd: Sudo Command
        :type sudocmd: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: A description of this command
        :type description: Str
        """
        method = 'sudocmd_add'
        
        _args = list()
        _args.append(sudocmd)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def sudocmd_del(
        self,
        sudocmd,
        opt_continue=False,
    ):
        """Delete Sudo Command.
        :param sudocmd: Sudo Command
        :type sudocmd: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'sudocmd_del'
        
        _args = list()
        _args.append(sudocmd)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def sudocmd_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        sudocmd=None,
        description=None,
    ):
        """Search for Sudo Commands.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("command")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param sudocmd: Sudo Command
        :type sudocmd: Str
        :param description: A description of this command
        :type description: Str
        """
        method = 'sudocmd_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if sudocmd:
            _params['sudocmd'] = sudocmd
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def sudocmd_mod(
        self,
        sudocmd,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify Sudo Command.
        :param sudocmd: Sudo Command
        :type sudocmd: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: A description of this command
        :type description: Str
        """
        method = 'sudocmd_mod'
        
        _args = list()
        _args.append(sudocmd)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def sudocmd_show(
        self,
        sudocmd,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display Sudo Command.
        :param sudocmd: Sudo Command
        :type sudocmd: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'sudocmd_show'
        
        _args = list()
        _args.append(sudocmd)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def sudocmdgroup_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        description=None,
    ):
        """Create new Sudo Command Group.
        :param cn: Sudo Command Group
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Group description
        :type description: Str
        """
        method = 'sudocmdgroup_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def sudocmdgroup_add_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        sudocmd=None,
    ):
        """Add members to Sudo Command Group.
        :param cn: Sudo Command Group
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param sudocmd: sudo commands to add
        :type sudocmd: Str
        """
        method = 'sudocmdgroup_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if sudocmd:
            _params['sudocmd'] = sudocmd
        
        return self._request(method, _args, _params)

    def sudocmdgroup_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete Sudo Command Group.
        :param cn: Sudo Command Group
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'sudocmdgroup_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def sudocmdgroup_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        description=None,
        cn=None,
    ):
        """Search for Sudo Command Groups.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("sudocmdgroup-name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param description: Group description
        :type description: Str
        :param cn: Sudo Command Group
        :type cn: Str
        """
        method = 'sudocmdgroup_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def sudocmdgroup_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        description=None,
    ):
        """Modify Sudo Command Group.
        :param cn: Sudo Command Group
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param description: Group description
        :type description: Str
        """
        method = 'sudocmdgroup_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if description:
            _params['description'] = description
        
        return self._request(method, _args, _params)

    def sudocmdgroup_remove_member(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        sudocmd=None,
    ):
        """Remove members from Sudo Command Group.
        :param cn: Sudo Command Group
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param sudocmd: sudo commands to remove
        :type sudocmd: Str
        """
        method = 'sudocmdgroup_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if sudocmd:
            _params['sudocmd'] = sudocmd
        
        return self._request(method, _args, _params)

    def sudocmdgroup_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display Sudo Command Group.
        :param cn: Sudo Command Group
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'sudocmdgroup_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def sudorule_add(
        self,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        ipaenabledflag=None,
        sudoorder=0,
        description=None,
        externalhost=None,
        externaluser=None,
        ipasudorunasextgroup=None,
        ipasudorunasextuser=None,
        cmdcategory=None,
        hostcategory=None,
        ipasudorunasgroupcategory=None,
        ipasudorunasusercategory=None,
        usercategory=None,
    ):
        """Create new Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param sudoorder: integer to order the Sudo rules
        :type sudoorder: Int
        :param description: Description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param externaluser: External User the rule applies to (sudorule-find only)
        :type externaluser: Str
        :param ipasudorunasextgroup: External Group the commands can run as (sudorule-find only)
        :type ipasudorunasextgroup: Str
        :param ipasudorunasextuser: External User the commands can run as (sudorule-find only)
        :type ipasudorunasextuser: Str
        :param cmdcategory: Command category the rule applies to
        :type cmdcategory: StrEnum
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param ipasudorunasgroupcategory: RunAs Group category the rule applies to
        :type ipasudorunasgroupcategory: StrEnum
        :param ipasudorunasusercategory: RunAs User category the rule applies to
        :type ipasudorunasusercategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'sudorule_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if sudoorder:
            _params['sudoorder'] = sudoorder
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if externaluser:
            _params['externaluser'] = externaluser
        if ipasudorunasextgroup:
            _params['ipasudorunasextgroup'] = ipasudorunasextgroup
        if ipasudorunasextuser:
            _params['ipasudorunasextuser'] = ipasudorunasextuser
        if cmdcategory:
            _params['cmdcategory'] = cmdcategory
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if ipasudorunasgroupcategory:
            _params['ipasudorunasgroupcategory'] = ipasudorunasgroupcategory
        if ipasudorunasusercategory:
            _params['ipasudorunasusercategory'] = ipasudorunasusercategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def sudorule_add_allow_command(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        sudocmdgroup=None,
        sudocmd=None,
    ):
        """Add commands and sudo command groups affected by Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param sudocmdgroup: sudo command groups to add
        :type sudocmdgroup: Str
        :param sudocmd: sudo commands to add
        :type sudocmd: Str
        """
        method = 'sudorule_add_allow_command'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if sudocmdgroup:
            _params['sudocmdgroup'] = sudocmdgroup
        if sudocmd:
            _params['sudocmd'] = sudocmd
        
        return self._request(method, _args, _params)

    def sudorule_add_deny_command(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        sudocmdgroup=None,
        sudocmd=None,
    ):
        """Add commands and sudo command groups affected by Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param sudocmdgroup: sudo command groups to add
        :type sudocmdgroup: Str
        :param sudocmd: sudo commands to add
        :type sudocmd: Str
        """
        method = 'sudorule_add_deny_command'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if sudocmdgroup:
            _params['sudocmdgroup'] = sudocmdgroup
        if sudocmd:
            _params['sudocmd'] = sudocmd
        
        return self._request(method, _args, _params)

    def sudorule_add_host(
        self,
        cn,
        hostmask=None,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Add hosts and hostgroups affected by Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param hostmask: host masks of allowed hosts
        :type hostmask: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to add
        :type hostgroup: Str
        :param host: hosts to add
        :type host: Str
        """
        method = 'sudorule_add_host'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if hostmask:
            _params['hostmask'] = hostmask
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def sudorule_add_option(
        self,
        cn,
        ipasudoopt,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add an option to the Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param ipasudoopt: Sudo Option
        :type ipasudoopt: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'sudorule_add_option'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['ipasudoopt'] = ipasudoopt
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def sudorule_add_runasgroup(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
    ):
        """Add group for Sudo to execute as.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        """
        method = 'sudorule_add_runasgroup'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        
        return self._request(method, _args, _params)

    def sudorule_add_runasuser(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Add users and groups for Sudo to execute as.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param user: users to add
        :type user: Str
        """
        method = 'sudorule_add_runasuser'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def sudorule_add_user(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Add users and groups affected by Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to add
        :type group: Str
        :param user: users to add
        :type user: Str
        """
        method = 'sudorule_add_user'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def sudorule_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'sudorule_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def sudorule_disable(
        self,
        cn,
    ):
        """Disable a Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        """
        method = 'sudorule_disable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def sudorule_enable(
        self,
        cn,
    ):
        """Enable a Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        """
        method = 'sudorule_enable'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def sudorule_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        ipaenabledflag=None,
        sudoorder=0,
        description=None,
        externalhost=None,
        externaluser=None,
        ipasudorunasextgroup=None,
        ipasudorunasextuser=None,
        cn=None,
        cmdcategory=None,
        hostcategory=None,
        ipasudorunasgroupcategory=None,
        ipasudorunasusercategory=None,
        usercategory=None,
    ):
        """Search for Sudo Rule.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("sudorule-name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param sudoorder: integer to order the Sudo rules
        :type sudoorder: Int
        :param description: Description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param externaluser: External User the rule applies to (sudorule-find only)
        :type externaluser: Str
        :param ipasudorunasextgroup: External Group the commands can run as (sudorule-find only)
        :type ipasudorunasextgroup: Str
        :param ipasudorunasextuser: External User the commands can run as (sudorule-find only)
        :type ipasudorunasextuser: Str
        :param cn: Rule name
        :type cn: Str
        :param cmdcategory: Command category the rule applies to
        :type cmdcategory: StrEnum
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param ipasudorunasgroupcategory: RunAs Group category the rule applies to
        :type ipasudorunasgroupcategory: StrEnum
        :param ipasudorunasusercategory: RunAs User category the rule applies to
        :type ipasudorunasusercategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'sudorule_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if sudoorder:
            _params['sudoorder'] = sudoorder
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if externaluser:
            _params['externaluser'] = externaluser
        if ipasudorunasextgroup:
            _params['ipasudorunasextgroup'] = ipasudorunasextgroup
        if ipasudorunasextuser:
            _params['ipasudorunasextuser'] = ipasudorunasextuser
        if cn:
            _params['cn'] = cn
        if cmdcategory:
            _params['cmdcategory'] = cmdcategory
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if ipasudorunasgroupcategory:
            _params['ipasudorunasgroupcategory'] = ipasudorunasgroupcategory
        if ipasudorunasusercategory:
            _params['ipasudorunasusercategory'] = ipasudorunasusercategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def sudorule_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        ipaenabledflag=None,
        sudoorder=0,
        description=None,
        externalhost=None,
        externaluser=None,
        ipasudorunasextgroup=None,
        ipasudorunasextuser=None,
        cmdcategory=None,
        hostcategory=None,
        ipasudorunasgroupcategory=None,
        ipasudorunasusercategory=None,
        usercategory=None,
    ):
        """Modify Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the sudo rule object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipaenabledflag: Enabled
        :type ipaenabledflag: Bool
        :param sudoorder: integer to order the Sudo rules
        :type sudoorder: Int
        :param description: Description
        :type description: Str
        :param externalhost: External host
        :type externalhost: Str
        :param externaluser: External User the rule applies to (sudorule-find only)
        :type externaluser: Str
        :param ipasudorunasextgroup: External Group the commands can run as (sudorule-find only)
        :type ipasudorunasextgroup: Str
        :param ipasudorunasextuser: External User the commands can run as (sudorule-find only)
        :type ipasudorunasextuser: Str
        :param cmdcategory: Command category the rule applies to
        :type cmdcategory: StrEnum
        :param hostcategory: Host category the rule applies to
        :type hostcategory: StrEnum
        :param ipasudorunasgroupcategory: RunAs Group category the rule applies to
        :type ipasudorunasgroupcategory: StrEnum
        :param ipasudorunasusercategory: RunAs User category the rule applies to
        :type ipasudorunasusercategory: StrEnum
        :param usercategory: User category the rule applies to
        :type usercategory: StrEnum
        """
        method = 'sudorule_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if ipaenabledflag:
            _params['ipaenabledflag'] = ipaenabledflag
        if sudoorder:
            _params['sudoorder'] = sudoorder
        if description:
            _params['description'] = description
        if externalhost:
            _params['externalhost'] = externalhost
        if externaluser:
            _params['externaluser'] = externaluser
        if ipasudorunasextgroup:
            _params['ipasudorunasextgroup'] = ipasudorunasextgroup
        if ipasudorunasextuser:
            _params['ipasudorunasextuser'] = ipasudorunasextuser
        if cmdcategory:
            _params['cmdcategory'] = cmdcategory
        if hostcategory:
            _params['hostcategory'] = hostcategory
        if ipasudorunasgroupcategory:
            _params['ipasudorunasgroupcategory'] = ipasudorunasgroupcategory
        if ipasudorunasusercategory:
            _params['ipasudorunasusercategory'] = ipasudorunasusercategory
        if usercategory:
            _params['usercategory'] = usercategory
        
        return self._request(method, _args, _params)

    def sudorule_remove_allow_command(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        sudocmdgroup=None,
        sudocmd=None,
    ):
        """Remove commands and sudo command groups affected by Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param sudocmdgroup: sudo command groups to remove
        :type sudocmdgroup: Str
        :param sudocmd: sudo commands to remove
        :type sudocmd: Str
        """
        method = 'sudorule_remove_allow_command'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if sudocmdgroup:
            _params['sudocmdgroup'] = sudocmdgroup
        if sudocmd:
            _params['sudocmd'] = sudocmd
        
        return self._request(method, _args, _params)

    def sudorule_remove_deny_command(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        sudocmdgroup=None,
        sudocmd=None,
    ):
        """Remove commands and sudo command groups affected by Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param sudocmdgroup: sudo command groups to remove
        :type sudocmdgroup: Str
        :param sudocmd: sudo commands to remove
        :type sudocmd: Str
        """
        method = 'sudorule_remove_deny_command'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if sudocmdgroup:
            _params['sudocmdgroup'] = sudocmdgroup
        if sudocmd:
            _params['sudocmd'] = sudocmd
        
        return self._request(method, _args, _params)

    def sudorule_remove_host(
        self,
        cn,
        hostmask=None,
        opt_all=True,
        no_members=False,
        raw=False,
        hostgroup=None,
        host=None,
    ):
        """Remove hosts and hostgroups affected by Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param hostmask: host masks of allowed hosts
        :type hostmask: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param hostgroup: host groups to remove
        :type hostgroup: Str
        :param host: hosts to remove
        :type host: Str
        """
        method = 'sudorule_remove_host'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if hostmask:
            _params['hostmask'] = hostmask
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if hostgroup:
            _params['hostgroup'] = hostgroup
        if host:
            _params['host'] = host
        
        return self._request(method, _args, _params)

    def sudorule_remove_option(
        self,
        cn,
        ipasudoopt,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove an option from Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param ipasudoopt: Sudo Option
        :type ipasudoopt: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'sudorule_remove_option'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['ipasudoopt'] = ipasudoopt
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def sudorule_remove_runasgroup(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
    ):
        """Remove group for Sudo to execute as.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        """
        method = 'sudorule_remove_runasgroup'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        
        return self._request(method, _args, _params)

    def sudorule_remove_runasuser(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Remove users and groups for Sudo to execute as.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'sudorule_remove_runasuser'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def sudorule_remove_user(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        group=None,
        user=None,
    ):
        """Remove users and groups affected by Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param group: groups to remove
        :type group: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'sudorule_remove_user'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if group:
            _params['group'] = group
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def sudorule_show(
        self,
        cn,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display Sudo Rule.
        :param cn: Rule name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'sudorule_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def topic_find(
        self,
        criteria=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
    ):
        """Search for help topics.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'topic_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def topic_show(
        self,
        full_name,
        opt_all=True,
        raw=False,
    ):
        """Display information about a help topic.
        :param full_name: Full name
        :type full_name: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'topic_show'
        
        _args = list()
        _args.append(full_name)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def topologysegment_add(
        self,
        topologysuffixcn,
        cn,
        iparepltoposegmentleftnode,
        iparepltoposegmentrightnode,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        nsds5replicatimeout=None,
        nsds5replicatedattributelist=None,
        nsds5replicatedattributelisttotal=None,
        nsds5replicastripattrs=None,
        nsds5replicaenabled=None,
        iparepltoposegmentdirection='both',
    ):
        """Add a new segment.
        :param topologysuffixcn: Suffix name
        :type topologysuffixcn: Str
        :param cn: Arbitrary string identifying the segment
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param nsds5replicatimeout: Number of seconds outbound LDAP operations waits for a response from the remote replica before timing out and failing
        :type nsds5replicatimeout: Int
        :param iparepltoposegmentleftnode: Left replication node - an IPA server
        :type iparepltoposegmentleftnode: Str
        :param nsds5replicatedattributelist: Attributes that are not replicated to a consumer server during a fractional update. E.g., `(objectclass=*) $ EXCLUDE accountlockout memberof
        :type nsds5replicatedattributelist: Str
        :param nsds5replicatedattributelisttotal: Attributes that are not replicated to a consumer server during a total update. E.g. (objectclass=*) $ EXCLUDE accountlockout
        :type nsds5replicatedattributelisttotal: Str
        :param iparepltoposegmentrightnode: Right replication node - an IPA server
        :type iparepltoposegmentrightnode: Str
        :param nsds5replicastripattrs: A space separated list of attributes which are removed from replication updates.
        :type nsds5replicastripattrs: Str
        :param nsds5replicaenabled: Whether a replication agreement is active, meaning whether replication is occurring per that agreement
        :type nsds5replicaenabled: StrEnum
        :param iparepltoposegmentdirection: Direction of replication between left and right replication node
        :type iparepltoposegmentdirection: StrEnum
        """
        method = 'topologysegment_add'
        
        _args = list()
        _args.append(topologysuffixcn)
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        if nsds5replicatimeout:
            _params['nsds5replicatimeout'] = nsds5replicatimeout
        _params['iparepltoposegmentleftnode'] = iparepltoposegmentleftnode
        if nsds5replicatedattributelist:
            _params['nsds5replicatedattributelist'] = nsds5replicatedattributelist
        if nsds5replicatedattributelisttotal:
            _params['nsds5replicatedattributelisttotal'] = nsds5replicatedattributelisttotal
        _params['iparepltoposegmentrightnode'] = iparepltoposegmentrightnode
        if nsds5replicastripattrs:
            _params['nsds5replicastripattrs'] = nsds5replicastripattrs
        if nsds5replicaenabled:
            _params['nsds5replicaenabled'] = nsds5replicaenabled
        _params['iparepltoposegmentdirection'] = iparepltoposegmentdirection
        
        return self._request(method, _args, _params)

    def topologysegment_del(
        self,
        topologysuffixcn,
        cn,
        opt_continue=False,
    ):
        """Delete a segment.
        :param topologysuffixcn: Suffix name
        :type topologysuffixcn: Str
        :param cn: Arbitrary string identifying the segment
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'topologysegment_del'
        
        _args = list()
        _args.append(topologysuffixcn)
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def topologysegment_find(
        self,
        topologysuffixcn,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        nsds5replicatimeout=None,
        iparepltoposegmentleftnode=None,
        cn=None,
        nsds5replicatedattributelist=None,
        nsds5replicatedattributelisttotal=None,
        iparepltoposegmentrightnode=None,
        nsds5replicastripattrs=None,
        iparepltoposegmentdirection='both',
        nsds5replicaenabled=None,
    ):
        """Search for topology segments.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param topologysuffixcn: Suffix name
        :type topologysuffixcn: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param nsds5replicatimeout: Number of seconds outbound LDAP operations waits for a response from the remote replica before timing out and failing
        :type nsds5replicatimeout: Int
        :param iparepltoposegmentleftnode: Left replication node - an IPA server
        :type iparepltoposegmentleftnode: Str
        :param cn: Arbitrary string identifying the segment
        :type cn: Str
        :param nsds5replicatedattributelist: Attributes that are not replicated to a consumer server during a fractional update. E.g., `(objectclass=*) $ EXCLUDE accountlockout memberof
        :type nsds5replicatedattributelist: Str
        :param nsds5replicatedattributelisttotal: Attributes that are not replicated to a consumer server during a total update. E.g. (objectclass=*) $ EXCLUDE accountlockout
        :type nsds5replicatedattributelisttotal: Str
        :param iparepltoposegmentrightnode: Right replication node - an IPA server
        :type iparepltoposegmentrightnode: Str
        :param nsds5replicastripattrs: A space separated list of attributes which are removed from replication updates.
        :type nsds5replicastripattrs: Str
        :param iparepltoposegmentdirection: Direction of replication between left and right replication node
        :type iparepltoposegmentdirection: StrEnum
        :param nsds5replicaenabled: Whether a replication agreement is active, meaning whether replication is occurring per that agreement
        :type nsds5replicaenabled: StrEnum
        """
        method = 'topologysegment_find'
        
        _args = list()
        _args.append(criteria)
        _args.append(topologysuffixcn)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if nsds5replicatimeout:
            _params['nsds5replicatimeout'] = nsds5replicatimeout
        if iparepltoposegmentleftnode:
            _params['iparepltoposegmentleftnode'] = iparepltoposegmentleftnode
        if cn:
            _params['cn'] = cn
        if nsds5replicatedattributelist:
            _params['nsds5replicatedattributelist'] = nsds5replicatedattributelist
        if nsds5replicatedattributelisttotal:
            _params['nsds5replicatedattributelisttotal'] = nsds5replicatedattributelisttotal
        if iparepltoposegmentrightnode:
            _params['iparepltoposegmentrightnode'] = iparepltoposegmentrightnode
        if nsds5replicastripattrs:
            _params['nsds5replicastripattrs'] = nsds5replicastripattrs
        if iparepltoposegmentdirection:
            _params['iparepltoposegmentdirection'] = iparepltoposegmentdirection
        if nsds5replicaenabled:
            _params['nsds5replicaenabled'] = nsds5replicaenabled
        
        return self._request(method, _args, _params)

    def topologysegment_mod(
        self,
        topologysuffixcn,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        nsds5replicatimeout=None,
        nsds5replicatedattributelist=None,
        nsds5replicatedattributelisttotal=None,
        nsds5replicastripattrs=None,
        nsds5replicaenabled=None,
    ):
        """Modify a segment.
        :param topologysuffixcn: Suffix name
        :type topologysuffixcn: Str
        :param cn: Arbitrary string identifying the segment
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param nsds5replicatimeout: Number of seconds outbound LDAP operations waits for a response from the remote replica before timing out and failing
        :type nsds5replicatimeout: Int
        :param nsds5replicatedattributelist: Attributes that are not replicated to a consumer server during a fractional update. E.g., `(objectclass=*) $ EXCLUDE accountlockout memberof
        :type nsds5replicatedattributelist: Str
        :param nsds5replicatedattributelisttotal: Attributes that are not replicated to a consumer server during a total update. E.g. (objectclass=*) $ EXCLUDE accountlockout
        :type nsds5replicatedattributelisttotal: Str
        :param nsds5replicastripattrs: A space separated list of attributes which are removed from replication updates.
        :type nsds5replicastripattrs: Str
        :param nsds5replicaenabled: Whether a replication agreement is active, meaning whether replication is occurring per that agreement
        :type nsds5replicaenabled: StrEnum
        """
        method = 'topologysegment_mod'
        
        _args = list()
        _args.append(topologysuffixcn)
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if nsds5replicatimeout:
            _params['nsds5replicatimeout'] = nsds5replicatimeout
        if nsds5replicatedattributelist:
            _params['nsds5replicatedattributelist'] = nsds5replicatedattributelist
        if nsds5replicatedattributelisttotal:
            _params['nsds5replicatedattributelisttotal'] = nsds5replicatedattributelisttotal
        if nsds5replicastripattrs:
            _params['nsds5replicastripattrs'] = nsds5replicastripattrs
        if nsds5replicaenabled:
            _params['nsds5replicaenabled'] = nsds5replicaenabled
        
        return self._request(method, _args, _params)

    def topologysegment_reinitialize(
        self,
        topologysuffixcn,
        cn,
        left=False,
        right=False,
        stop=False,
    ):
        """Request a full re-initialization of the node retrieving data from the other node.
        :param topologysuffixcn: Suffix name
        :type topologysuffixcn: Str
        :param cn: Arbitrary string identifying the segment
        :type cn: Str
        :param left: Initialize left node
        :type left: Flag
        :param right: Initialize right node
        :type right: Flag
        :param stop: Stop already started refresh of chosen node(s)
        :type stop: Flag
        """
        method = 'topologysegment_reinitialize'
        
        _args = list()
        _args.append(topologysuffixcn)
        _args.append(cn)
        
        _params = dict()
        if left:
            _params['left'] = left
        if right:
            _params['right'] = right
        if stop:
            _params['stop'] = stop
        
        return self._request(method, _args, _params)

    def topologysegment_show(
        self,
        topologysuffixcn,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display a segment.
        :param topologysuffixcn: Suffix name
        :type topologysuffixcn: Str
        :param cn: Arbitrary string identifying the segment
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'topologysegment_show'
        
        _args = list()
        _args.append(topologysuffixcn)
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def topologysuffix_add(
        self,
        cn,
        iparepltopoconfroot,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
    ):
        """Add a new topology suffix to be managed.
        :param cn: Suffix name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param iparepltopoconfroot: Managed LDAP suffix DN
        :type iparepltopoconfroot: DNParam
        """
        method = 'topologysuffix_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['iparepltopoconfroot'] = iparepltopoconfroot
        
        return self._request(method, _args, _params)

    def topologysuffix_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a topology suffix.
        :param cn: Suffix name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'topologysuffix_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def topologysuffix_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        iparepltopoconfroot=None,
        cn=None,
    ):
        """Search for topology suffixes.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param iparepltopoconfroot: Managed LDAP suffix DN
        :type iparepltopoconfroot: DNParam
        :param cn: Suffix name
        :type cn: Str
        """
        method = 'topologysuffix_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if iparepltopoconfroot:
            _params['iparepltopoconfroot'] = iparepltopoconfroot
        if cn:
            _params['cn'] = cn
        
        return self._request(method, _args, _params)

    def topologysuffix_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        iparepltopoconfroot=None,
    ):
        """Modify a topology suffix.
        :param cn: Suffix name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param iparepltopoconfroot: Managed LDAP suffix DN
        :type iparepltopoconfroot: DNParam
        """
        method = 'topologysuffix_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if iparepltopoconfroot:
            _params['iparepltopoconfroot'] = iparepltopoconfroot
        
        return self._request(method, _args, _params)

    def topologysuffix_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Show managed suffix.
        :param cn: Suffix name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'topologysuffix_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def topologysuffix_verify(
        self,
        cn,
    ):
        """
Verify replication topology for suffix.

Checks done:
  1. check if a topology is not disconnected. In other words if there are
     replication paths between all servers.
  2. check if servers don't have more than the recommended number of
     replication agreements

        :param cn: Suffix name
        :type cn: Str
        """
        method = 'topologysuffix_verify'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def trust_add(
        self,
        cn,
        external=False,
        bidirectional=False,
        base_id=None,
        range_size=None,
        realm_passwd=None,
        trust_secret=None,
        addattr=None,
        realm_admin=None,
        realm_server=None,
        opt_setattr=None,
        range_type=None,
        opt_all=True,
        raw=False,
        trust_type='ad',
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
    
        :param cn: Realm name
        :type cn: Str
        :param external: Establish external trust to a domain in another forest. The trust is not transitive beyond the domain.
        :type external: Bool
        :param bidirectional: Establish bi-directional trust. By default trust is inbound one-way only.
        :type bidirectional: Bool
        :param base_id: First Posix ID of the range reserved for the trusted domain
        :type base_id: Int
        :param range_size: Size of the ID range reserved for the trusted domain
        :type range_size: Int
        :param realm_passwd: Active Directory domain administrator's password
        :type realm_passwd: Password
        :param trust_secret: Shared secret for the trust
        :type trust_secret: Password
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param realm_admin: Active Directory domain administrator
        :type realm_admin: Str
        :param realm_server: Domain controller for the Active Directory domain (optional)
        :type realm_server: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param range_type: Type of trusted domain ID range, one of ipa-ad-trust, ipa-ad-trust-posix
        :type range_type: StrEnum
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param trust_type: Trust type (ad for Active Directory, default)
        :type trust_type: StrEnum
        """
        method = 'trust_add'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if external:
            _params['external'] = external
        if bidirectional:
            _params['bidirectional'] = bidirectional
        if base_id:
            _params['base_id'] = base_id
        if range_size:
            _params['range_size'] = range_size
        if realm_passwd:
            _params['realm_passwd'] = realm_passwd
        if trust_secret:
            _params['trust_secret'] = trust_secret
        if addattr:
            _params['addattr'] = addattr
        if realm_admin:
            _params['realm_admin'] = realm_admin
        if realm_server:
            _params['realm_server'] = realm_server
        if opt_setattr:
            _params['setattr'] = opt_setattr
        if range_type:
            _params['range_type'] = range_type
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['trust_type'] = trust_type
        
        return self._request(method, _args, _params)

    def trust_del(
        self,
        cn,
        opt_continue=False,
    ):
        """Delete a trust.
        :param cn: Realm name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'trust_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def trust_fetch_domains(
        self,
        cn,
        realm_passwd=None,
        realm_admin=None,
        realm_server=None,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Refresh list of the domains associated with the trust
        :param cn: Realm name
        :type cn: Str
        :param realm_passwd: Active Directory domain administrator's password
        :type realm_passwd: Password
        :param realm_admin: Active Directory domain administrator
        :type realm_admin: Str
        :param realm_server: Domain controller for the Active Directory domain (optional)
        :type realm_server: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'trust_fetch_domains'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if realm_passwd:
            _params['realm_passwd'] = realm_passwd
        if realm_admin:
            _params['realm_admin'] = realm_admin
        if realm_server:
            _params['realm_server'] = realm_server
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def trust_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        ipantflatname=None,
        cn=None,
        ipanttrusteddomainsid=None,
        ipantsidblacklistincoming=None,
        ipantsidblacklistoutgoing=None,
    ):
        """Search for trusts.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("realm")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param ipantflatname: Domain NetBIOS name
        :type ipantflatname: Str
        :param cn: Realm name
        :type cn: Str
        :param ipanttrusteddomainsid: Domain Security Identifier
        :type ipanttrusteddomainsid: Str
        :param ipantsidblacklistincoming: SID blacklist incoming
        :type ipantsidblacklistincoming: Str
        :param ipantsidblacklistoutgoing: SID blacklist outgoing
        :type ipantsidblacklistoutgoing: Str
        """
        method = 'trust_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if ipantflatname:
            _params['ipantflatname'] = ipantflatname
        if cn:
            _params['cn'] = cn
        if ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = ipanttrusteddomainsid
        if ipantsidblacklistincoming:
            _params['ipantsidblacklistincoming'] = ipantsidblacklistincoming
        if ipantsidblacklistoutgoing:
            _params['ipantsidblacklistoutgoing'] = ipantsidblacklistoutgoing
        
        return self._request(method, _args, _params)

    def trust_mod(
        self,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        ipantsidblacklistincoming=None,
        ipantsidblacklistoutgoing=None,
        ipantadditionalsuffixes=None,
    ):
        """
    Modify a trust (for future use).

    Currently only the default option to modify the LDAP attributes is
    available. More specific options will be added in coming releases.
    
        :param cn: Realm name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param ipantsidblacklistincoming: SID blacklist incoming
        :type ipantsidblacklistincoming: Str
        :param ipantsidblacklistoutgoing: SID blacklist outgoing
        :type ipantsidblacklistoutgoing: Str
        :param ipantadditionalsuffixes: UPN suffixes
        :type ipantadditionalsuffixes: Str
        """
        method = 'trust_mod'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        if ipantsidblacklistincoming:
            _params['ipantsidblacklistincoming'] = ipantsidblacklistincoming
        if ipantsidblacklistoutgoing:
            _params['ipantsidblacklistoutgoing'] = ipantsidblacklistoutgoing
        if ipantadditionalsuffixes:
            _params['ipantadditionalsuffixes'] = ipantadditionalsuffixes
        
        return self._request(method, _args, _params)

    def trust_resolve(
        self,
        sids,
        opt_all=True,
        raw=False,
    ):
        """Resolve security identifiers of users and groups in trusted domains
        :param sids: Security Identifiers (SIDs)
        :type sids: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'trust_resolve'
        
        _args = list()
        
        _params = dict()
        _params['sids'] = sids
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def trust_show(
        self,
        cn,
        opt_all=True,
        raw=False,
        rights=False,
    ):
        """Display information about a trust.
        :param cn: Realm name
        :type cn: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'trust_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def trustconfig_mod(
        self,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        trust_type='ad',
        ipantfallbackprimarygroup=None,
    ):
        """Modify global trust configuration.
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param trust_type: Trust type (ad for Active Directory, default)
        :type trust_type: StrEnum
        :param ipantfallbackprimarygroup: Fallback primary group
        :type ipantfallbackprimarygroup: Str
        """
        method = 'trustconfig_mod'
        
        _args = list()
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        _params['trust_type'] = trust_type
        if ipantfallbackprimarygroup:
            _params['ipantfallbackprimarygroup'] = ipantfallbackprimarygroup
        
        return self._request(method, _args, _params)

    def trustconfig_show(
        self,
        opt_all=True,
        raw=False,
        rights=False,
        trust_type='ad',
    ):
        """Show global trust configuration.
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param trust_type: Trust type (ad for Active Directory, default)
        :type trust_type: StrEnum
        """
        method = 'trustconfig_show'
        
        _args = list()
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        _params['trust_type'] = trust_type
        
        return self._request(method, _args, _params)

    def trustdomain_add(
        self,
        trustcn,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        trust_type='ad',
        ipantflatname=None,
        ipanttrusteddomainsid=None,
    ):
        """Allow access from the trusted domain
        :param trustcn: Realm name
        :type trustcn: Str
        :param cn: Domain name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param trust_type: Trust type (ad for Active Directory, default)
        :type trust_type: StrEnum
        :param ipantflatname: Domain NetBIOS name
        :type ipantflatname: Str
        :param ipanttrusteddomainsid: Domain Security Identifier
        :type ipanttrusteddomainsid: Str
        """
        method = 'trustdomain_add'
        
        _args = list()
        _args.append(trustcn)
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['trust_type'] = trust_type
        if ipantflatname:
            _params['ipantflatname'] = ipantflatname
        if ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = ipanttrusteddomainsid
        
        return self._request(method, _args, _params)

    def trustdomain_del(
        self,
        trustcn,
        cn,
        opt_continue=False,
    ):
        """Remove information about the domain associated with the trust.
        :param trustcn: Realm name
        :type trustcn: Str
        :param cn: Domain name
        :type cn: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'trustdomain_del'
        
        _args = list()
        _args.append(trustcn)
        _args.append(cn)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def trustdomain_disable(
        self,
        trustcn,
        cn,
    ):
        """Disable use of IPA resources by the domain of the trust
        :param trustcn: Realm name
        :type trustcn: Str
        :param cn: Domain name
        :type cn: Str
        """
        method = 'trustdomain_disable'
        
        _args = list()
        _args.append(trustcn)
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def trustdomain_enable(
        self,
        trustcn,
        cn,
    ):
        """Allow use of IPA resources by the domain of the trust
        :param trustcn: Realm name
        :type trustcn: Str
        :param cn: Domain name
        :type cn: Str
        """
        method = 'trustdomain_enable'
        
        _args = list()
        _args.append(trustcn)
        _args.append(cn)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def trustdomain_find(
        self,
        trustcn,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        opt_all=True,
        pkey_only=False,
        raw=False,
        cn=None,
        ipantflatname=None,
        ipanttrusteddomainsid=None,
    ):
        """Search domains of the trust
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param trustcn: Realm name
        :type trustcn: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param pkey_only: Results should contain primary key attribute only ("domain")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param cn: Domain name
        :type cn: Str
        :param ipantflatname: Domain NetBIOS name
        :type ipantflatname: Str
        :param ipanttrusteddomainsid: Domain Security Identifier
        :type ipanttrusteddomainsid: Str
        """
        method = 'trustdomain_find'
        
        _args = list()
        _args.append(criteria)
        _args.append(trustcn)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        _params['all'] = opt_all
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if cn:
            _params['cn'] = cn
        if ipantflatname:
            _params['ipantflatname'] = ipantflatname
        if ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = ipanttrusteddomainsid
        
        return self._request(method, _args, _params)

    def trustdomain_mod(
        self,
        trustcn,
        cn,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        opt_all=True,
        raw=False,
        rights=False,
        trust_type='ad',
        ipantflatname=None,
        ipanttrusteddomainsid=None,
    ):
        """Modify trustdomain of the trust
        :param trustcn: Realm name
        :type trustcn: Str
        :param cn: Domain name
        :type cn: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param trust_type: Trust type (ad for Active Directory, default)
        :type trust_type: StrEnum
        :param ipantflatname: Domain NetBIOS name
        :type ipantflatname: Str
        :param ipanttrusteddomainsid: Domain Security Identifier
        :type ipanttrusteddomainsid: Str
        """
        method = 'trustdomain_mod'
        
        _args = list()
        _args.append(trustcn)
        _args.append(cn)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['raw'] = raw
        _params['rights'] = rights
        _params['trust_type'] = trust_type
        if ipantflatname:
            _params['ipantflatname'] = ipantflatname
        if ipanttrusteddomainsid:
            _params['ipanttrusteddomainsid'] = ipanttrusteddomainsid
        
        return self._request(method, _args, _params)

    def user_add(
        self,
        uid,
        givenname,
        sn,
        cn,
        addattr=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        noprivate=False,
        random=False,
        raw=False,
        nsaccountlock=False,
        usercertificate=None,
        krbpasswordexpiration=None,
        krbprincipalexpiration=None,
        gidnumber=None,
        uidnumber=None,
        userpassword=None,
        carlicense=None,
        l=None,
        userclass=None,
        departmentnumber=None,
        mail=None,
        employeenumber=None,
        employeetype=None,
        facsimiletelephonenumber=None,
        homedirectory=None,
        manager=None,
        mobile=None,
        ou=None,
        pager=None,
        telephonenumber=None,
        postalcode=None,
        preferredlanguage=None,
        ipatokenradiusconfiglink=None,
        ipatokenradiususername=None,
        loginshell=None,
        ipasshpubkey=None,
        st=None,
        street=None,
        title=None,
        ipauserauthtype=None,
        krbprincipalname=None,
        displayname=None,
        gecos=None,
        initials=None,
    ):
        """Add a new user.
        :param uid: User login
        :type uid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param noprivate: Don't create user private group
        :type noprivate: Flag
        :param random: Generate a random user password
        :type random: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param nsaccountlock: Account disabled
        :type nsaccountlock: Bool
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        :param krbpasswordexpiration: User password expiration
        :type krbpasswordexpiration: DateTime
        :param krbprincipalexpiration: Kerberos principal expiration
        :type krbprincipalexpiration: DateTime
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number (system will assign one if not provided)
        :type uidnumber: Int
        :param userpassword: Prompt to set the user password
        :type userpassword: Password
        :param carlicense: Car License
        :type carlicense: Str
        :param l: City
        :type l: Str
        :param userclass: User category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param departmentnumber: Department Number
        :type departmentnumber: Str
        :param mail: Email address
        :type mail: Str
        :param employeenumber: Employee Number
        :type employeenumber: Str
        :param employeetype: Employee Type
        :type employeetype: Str
        :param facsimiletelephonenumber: Fax Number
        :type facsimiletelephonenumber: Str
        :param givenname: First name
        :type givenname: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param sn: Last name
        :type sn: Str
        :param manager: Manager
        :type manager: Str
        :param mobile: Mobile Telephone Number
        :type mobile: Str
        :param ou: Org. Unit
        :type ou: Str
        :param pager: Pager Number
        :type pager: Str
        :param telephonenumber: Telephone Number
        :type telephonenumber: Str
        :param postalcode: ZIP
        :type postalcode: Str
        :param preferredlanguage: Preferred Language
        :type preferredlanguage: Str
        :param ipatokenradiusconfiglink: RADIUS proxy configuration
        :type ipatokenradiusconfiglink: Str
        :param ipatokenradiususername: RADIUS proxy username
        :type ipatokenradiususername: Str
        :param loginshell: Login shell
        :type loginshell: Str
        :param ipasshpubkey: SSH public key
        :type ipasshpubkey: Str
        :param st: State/Province
        :type st: Str
        :param street: Street address
        :type street: Str
        :param title: Job Title
        :type title: Str
        :param ipauserauthtype: Types of supported user authentication
        :type ipauserauthtype: StrEnum
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param cn: Full name
        :type cn: Str
        :param displayname: Display name
        :type displayname: Str
        :param gecos: GECOS
        :type gecos: Str
        :param initials: Initials
        :type initials: Str
        """
        method = 'user_add'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['noprivate'] = noprivate
        if random:
            _params['random'] = random
        _params['raw'] = raw
        if nsaccountlock:
            _params['nsaccountlock'] = nsaccountlock
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbpasswordexpiration:
            _params['krbpasswordexpiration'] = krbpasswordexpiration
        if krbprincipalexpiration:
            _params['krbprincipalexpiration'] = krbprincipalexpiration
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if userpassword:
            _params['userpassword'] = userpassword
        if carlicense:
            _params['carlicense'] = carlicense
        if l:
            _params['l'] = l
        if userclass:
            _params['userclass'] = userclass
        if departmentnumber:
            _params['departmentnumber'] = departmentnumber
        if mail:
            _params['mail'] = mail
        if employeenumber:
            _params['employeenumber'] = employeenumber
        if employeetype:
            _params['employeetype'] = employeetype
        if facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = facsimiletelephonenumber
        _params['givenname'] = givenname
        if homedirectory:
            _params['homedirectory'] = homedirectory
        _params['sn'] = sn
        if manager:
            _params['manager'] = manager
        if mobile:
            _params['mobile'] = mobile
        if ou:
            _params['ou'] = ou
        if pager:
            _params['pager'] = pager
        if telephonenumber:
            _params['telephonenumber'] = telephonenumber
        if postalcode:
            _params['postalcode'] = postalcode
        if preferredlanguage:
            _params['preferredlanguage'] = preferredlanguage
        if ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = ipatokenradiusconfiglink
        if ipatokenradiususername:
            _params['ipatokenradiususername'] = ipatokenradiususername
        if loginshell:
            _params['loginshell'] = loginshell
        if ipasshpubkey:
            _params['ipasshpubkey'] = ipasshpubkey
        if st:
            _params['st'] = st
        if street:
            _params['street'] = street
        if title:
            _params['title'] = title
        if ipauserauthtype:
            _params['ipauserauthtype'] = ipauserauthtype
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        _params['cn'] = cn
        if displayname:
            _params['displayname'] = displayname
        if gecos:
            _params['gecos'] = gecos
        if initials:
            _params['initials'] = initials
        
        return self._request(method, _args, _params)

    def user_add_cert(
        self,
        uid,
        usercertificate,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add one or more certificates to the user entry
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        """
        method = 'user_add_cert'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def user_add_certmapdata(
        self,
        uid,
        ipacertmapdata=None,
        certificate=None,
        issuer=None,
        subject=None,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add one or more certificate mappings to the user entry.
        :param ipacertmapdata: Certificate mapping data
        :type ipacertmapdata: Str
        :param uid: User login
        :type uid: Str
        :param certificate: Base-64 encoded user certificate
        :type certificate: Certificate
        :param issuer: Issuer of the certificate
        :type issuer: DNParam
        :param subject: Subject of the certificate
        :type subject: DNParam
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'user_add_certmapdata'
        
        _args = list()
        _args.append(ipacertmapdata)
        _args.append(uid)
        
        _params = dict()
        if certificate:
            _params['certificate'] = certificate
        if issuer:
            _params['issuer'] = issuer
        if subject:
            _params['subject'] = subject
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def user_add_manager(
        self,
        uid,
        opt_all=True,
        no_members=False,
        raw=False,
        user=None,
    ):
        """Add a manager to the user entry
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param user: users to add
        :type user: Str
        """
        method = 'user_add_manager'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def user_add_principal(
        self,
        uid,
        krbprincipalname,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Add new principal alias to the user entry
        :param uid: User login
        :type uid: Str
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'user_add_principal'
        
        _args = list()
        _args.append(uid)
        _args.append(krbprincipalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def user_del(
        self,
        uid,
        preserve=None,
        opt_continue=False,
    ):
        """Delete a user.
        :param uid: User login
        :type uid: Str
        :param preserve: <preserve>
        :type preserve: Bool
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'user_del'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        if preserve:
            _params['preserve'] = preserve
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def user_disable(
        self,
        uid,
    ):
        """Disable a user account.
        :param uid: User login
        :type uid: Str
        """
        method = 'user_disable'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def user_enable(
        self,
        uid,
    ):
        """Enable a user account.
        :param uid: User login
        :type uid: Str
        """
        method = 'user_enable'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def user_find(
        self,
        criteria=None,
        preserved=False,
        sizelimit=None,
        timelimit=None,
        in_group=None,
        in_hbacrule=None,
        in_netgroup=None,
        in_role=None,
        in_sudorule=None,
        not_in_group=None,
        not_in_hbacrule=None,
        not_in_netgroup=None,
        not_in_role=None,
        not_in_sudorule=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        whoami=False,
        nsaccountlock=False,
        usercertificate=None,
        krbpasswordexpiration=None,
        krbprincipalexpiration=None,
        gidnumber=None,
        uidnumber=None,
        userpassword=None,
        krbprincipalname=None,
        carlicense=None,
        l=None,
        userclass=None,
        cn=None,
        departmentnumber=None,
        displayname=None,
        mail=None,
        employeenumber=None,
        employeetype=None,
        facsimiletelephonenumber=None,
        givenname=None,
        gecos=None,
        homedirectory=None,
        initials=None,
        sn=None,
        uid=None,
        manager=None,
        mobile=None,
        ou=None,
        pager=None,
        telephonenumber=None,
        postalcode=None,
        preferredlanguage=None,
        ipatokenradiusconfiglink=None,
        ipatokenradiususername=None,
        loginshell=None,
        st=None,
        street=None,
        title=None,
        ipauserauthtype=None,
    ):
        """Search for users.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param preserved: Preserved user
        :type preserved: Bool
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param in_group: Search for users with these member of groups.
        :type in_group: Str
        :param in_hbacrule: Search for users with these member of HBAC rules.
        :type in_hbacrule: Str
        :param in_netgroup: Search for users with these member of netgroups.
        :type in_netgroup: Str
        :param in_role: Search for users with these member of roles.
        :type in_role: Str
        :param in_sudorule: Search for users with these member of sudo rules.
        :type in_sudorule: Str
        :param not_in_group: Search for users without these member of groups.
        :type not_in_group: Str
        :param not_in_hbacrule: Search for users without these member of HBAC rules.
        :type not_in_hbacrule: Str
        :param not_in_netgroup: Search for users without these member of netgroups.
        :type not_in_netgroup: Str
        :param not_in_role: Search for users without these member of roles.
        :type not_in_role: Str
        :param not_in_sudorule: Search for users without these member of sudo rules.
        :type not_in_sudorule: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("login")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param whoami: Display user record for current Kerberos principal
        :type whoami: Flag
        :param nsaccountlock: Account disabled
        :type nsaccountlock: Bool
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        :param krbpasswordexpiration: User password expiration
        :type krbpasswordexpiration: DateTime
        :param krbprincipalexpiration: Kerberos principal expiration
        :type krbprincipalexpiration: DateTime
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number (system will assign one if not provided)
        :type uidnumber: Int
        :param userpassword: Prompt to set the user password
        :type userpassword: Password
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param carlicense: Car License
        :type carlicense: Str
        :param l: City
        :type l: Str
        :param userclass: User category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param cn: Full name
        :type cn: Str
        :param departmentnumber: Department Number
        :type departmentnumber: Str
        :param displayname: Display name
        :type displayname: Str
        :param mail: Email address
        :type mail: Str
        :param employeenumber: Employee Number
        :type employeenumber: Str
        :param employeetype: Employee Type
        :type employeetype: Str
        :param facsimiletelephonenumber: Fax Number
        :type facsimiletelephonenumber: Str
        :param givenname: First name
        :type givenname: Str
        :param gecos: GECOS
        :type gecos: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param initials: Initials
        :type initials: Str
        :param sn: Last name
        :type sn: Str
        :param uid: User login
        :type uid: Str
        :param manager: Manager
        :type manager: Str
        :param mobile: Mobile Telephone Number
        :type mobile: Str
        :param ou: Org. Unit
        :type ou: Str
        :param pager: Pager Number
        :type pager: Str
        :param telephonenumber: Telephone Number
        :type telephonenumber: Str
        :param postalcode: ZIP
        :type postalcode: Str
        :param preferredlanguage: Preferred Language
        :type preferredlanguage: Str
        :param ipatokenradiusconfiglink: RADIUS proxy configuration
        :type ipatokenradiusconfiglink: Str
        :param ipatokenradiususername: RADIUS proxy username
        :type ipatokenradiususername: Str
        :param loginshell: Login shell
        :type loginshell: Str
        :param st: State/Province
        :type st: Str
        :param street: Street address
        :type street: Str
        :param title: Job Title
        :type title: Str
        :param ipauserauthtype: Types of supported user authentication
        :type ipauserauthtype: StrEnum
        """
        method = 'user_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if preserved:
            _params['preserved'] = preserved
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if in_group:
            _params['in_group'] = in_group
        if in_hbacrule:
            _params['in_hbacrule'] = in_hbacrule
        if in_netgroup:
            _params['in_netgroup'] = in_netgroup
        if in_role:
            _params['in_role'] = in_role
        if in_sudorule:
            _params['in_sudorule'] = in_sudorule
        if not_in_group:
            _params['not_in_group'] = not_in_group
        if not_in_hbacrule:
            _params['not_in_hbacrule'] = not_in_hbacrule
        if not_in_netgroup:
            _params['not_in_netgroup'] = not_in_netgroup
        if not_in_role:
            _params['not_in_role'] = not_in_role
        if not_in_sudorule:
            _params['not_in_sudorule'] = not_in_sudorule
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        _params['whoami'] = whoami
        if nsaccountlock:
            _params['nsaccountlock'] = nsaccountlock
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbpasswordexpiration:
            _params['krbpasswordexpiration'] = krbpasswordexpiration
        if krbprincipalexpiration:
            _params['krbprincipalexpiration'] = krbprincipalexpiration
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if userpassword:
            _params['userpassword'] = userpassword
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        if carlicense:
            _params['carlicense'] = carlicense
        if l:
            _params['l'] = l
        if userclass:
            _params['userclass'] = userclass
        if cn:
            _params['cn'] = cn
        if departmentnumber:
            _params['departmentnumber'] = departmentnumber
        if displayname:
            _params['displayname'] = displayname
        if mail:
            _params['mail'] = mail
        if employeenumber:
            _params['employeenumber'] = employeenumber
        if employeetype:
            _params['employeetype'] = employeetype
        if facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = facsimiletelephonenumber
        if givenname:
            _params['givenname'] = givenname
        if gecos:
            _params['gecos'] = gecos
        if homedirectory:
            _params['homedirectory'] = homedirectory
        if initials:
            _params['initials'] = initials
        if sn:
            _params['sn'] = sn
        if uid:
            _params['uid'] = uid
        if manager:
            _params['manager'] = manager
        if mobile:
            _params['mobile'] = mobile
        if ou:
            _params['ou'] = ou
        if pager:
            _params['pager'] = pager
        if telephonenumber:
            _params['telephonenumber'] = telephonenumber
        if postalcode:
            _params['postalcode'] = postalcode
        if preferredlanguage:
            _params['preferredlanguage'] = preferredlanguage
        if ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = ipatokenradiusconfiglink
        if ipatokenradiususername:
            _params['ipatokenradiususername'] = ipatokenradiususername
        if loginshell:
            _params['loginshell'] = loginshell
        if st:
            _params['st'] = st
        if street:
            _params['street'] = street
        if title:
            _params['title'] = title
        if ipauserauthtype:
            _params['ipauserauthtype'] = ipauserauthtype
        
        return self._request(method, _args, _params)

    def user_mod(
        self,
        uid,
        addattr=None,
        opt_delattr=None,
        rename=None,
        opt_setattr=None,
        opt_all=True,
        no_members=False,
        random=False,
        raw=False,
        rights=False,
        nsaccountlock=False,
        usercertificate=None,
        krbpasswordexpiration=None,
        krbprincipalexpiration=None,
        gidnumber=None,
        uidnumber=None,
        userpassword=None,
        krbprincipalname=None,
        carlicense=None,
        l=None,
        userclass=None,
        cn=None,
        departmentnumber=None,
        displayname=None,
        mail=None,
        employeenumber=None,
        employeetype=None,
        facsimiletelephonenumber=None,
        givenname=None,
        gecos=None,
        homedirectory=None,
        initials=None,
        sn=None,
        manager=None,
        mobile=None,
        ou=None,
        pager=None,
        telephonenumber=None,
        postalcode=None,
        preferredlanguage=None,
        ipatokenradiusconfiglink=None,
        ipatokenradiususername=None,
        loginshell=None,
        ipasshpubkey=None,
        st=None,
        street=None,
        title=None,
        ipauserauthtype=None,
    ):
        """Modify a user.
        :param uid: User login
        :type uid: Str
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param rename: Rename the user object
        :type rename: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param random: Generate a random user password
        :type random: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param nsaccountlock: Account disabled
        :type nsaccountlock: Bool
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        :param krbpasswordexpiration: User password expiration
        :type krbpasswordexpiration: DateTime
        :param krbprincipalexpiration: Kerberos principal expiration
        :type krbprincipalexpiration: DateTime
        :param gidnumber: Group ID Number
        :type gidnumber: Int
        :param uidnumber: User ID Number (system will assign one if not provided)
        :type uidnumber: Int
        :param userpassword: Prompt to set the user password
        :type userpassword: Password
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param carlicense: Car License
        :type carlicense: Str
        :param l: City
        :type l: Str
        :param userclass: User category (semantics placed on this attribute are for local interpretation)
        :type userclass: Str
        :param cn: Full name
        :type cn: Str
        :param departmentnumber: Department Number
        :type departmentnumber: Str
        :param displayname: Display name
        :type displayname: Str
        :param mail: Email address
        :type mail: Str
        :param employeenumber: Employee Number
        :type employeenumber: Str
        :param employeetype: Employee Type
        :type employeetype: Str
        :param facsimiletelephonenumber: Fax Number
        :type facsimiletelephonenumber: Str
        :param givenname: First name
        :type givenname: Str
        :param gecos: GECOS
        :type gecos: Str
        :param homedirectory: Home directory
        :type homedirectory: Str
        :param initials: Initials
        :type initials: Str
        :param sn: Last name
        :type sn: Str
        :param manager: Manager
        :type manager: Str
        :param mobile: Mobile Telephone Number
        :type mobile: Str
        :param ou: Org. Unit
        :type ou: Str
        :param pager: Pager Number
        :type pager: Str
        :param telephonenumber: Telephone Number
        :type telephonenumber: Str
        :param postalcode: ZIP
        :type postalcode: Str
        :param preferredlanguage: Preferred Language
        :type preferredlanguage: Str
        :param ipatokenradiusconfiglink: RADIUS proxy configuration
        :type ipatokenradiusconfiglink: Str
        :param ipatokenradiususername: RADIUS proxy username
        :type ipatokenradiususername: Str
        :param loginshell: Login shell
        :type loginshell: Str
        :param ipasshpubkey: SSH public key
        :type ipasshpubkey: Str
        :param st: State/Province
        :type st: Str
        :param street: Street address
        :type street: Str
        :param title: Job Title
        :type title: Str
        :param ipauserauthtype: Types of supported user authentication
        :type ipauserauthtype: StrEnum
        """
        method = 'user_mod'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if rename:
            _params['rename'] = rename
        if opt_setattr:
            _params['setattr'] = opt_setattr
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if random:
            _params['random'] = random
        _params['raw'] = raw
        _params['rights'] = rights
        if nsaccountlock:
            _params['nsaccountlock'] = nsaccountlock
        if usercertificate:
            _params['usercertificate'] = usercertificate
        if krbpasswordexpiration:
            _params['krbpasswordexpiration'] = krbpasswordexpiration
        if krbprincipalexpiration:
            _params['krbprincipalexpiration'] = krbprincipalexpiration
        if gidnumber:
            _params['gidnumber'] = gidnumber
        if uidnumber:
            _params['uidnumber'] = uidnumber
        if userpassword:
            _params['userpassword'] = userpassword
        if krbprincipalname:
            _params['krbprincipalname'] = krbprincipalname
        if carlicense:
            _params['carlicense'] = carlicense
        if l:
            _params['l'] = l
        if userclass:
            _params['userclass'] = userclass
        if cn:
            _params['cn'] = cn
        if departmentnumber:
            _params['departmentnumber'] = departmentnumber
        if displayname:
            _params['displayname'] = displayname
        if mail:
            _params['mail'] = mail
        if employeenumber:
            _params['employeenumber'] = employeenumber
        if employeetype:
            _params['employeetype'] = employeetype
        if facsimiletelephonenumber:
            _params['facsimiletelephonenumber'] = facsimiletelephonenumber
        if givenname:
            _params['givenname'] = givenname
        if gecos:
            _params['gecos'] = gecos
        if homedirectory:
            _params['homedirectory'] = homedirectory
        if initials:
            _params['initials'] = initials
        if sn:
            _params['sn'] = sn
        if manager:
            _params['manager'] = manager
        if mobile:
            _params['mobile'] = mobile
        if ou:
            _params['ou'] = ou
        if pager:
            _params['pager'] = pager
        if telephonenumber:
            _params['telephonenumber'] = telephonenumber
        if postalcode:
            _params['postalcode'] = postalcode
        if preferredlanguage:
            _params['preferredlanguage'] = preferredlanguage
        if ipatokenradiusconfiglink:
            _params['ipatokenradiusconfiglink'] = ipatokenradiusconfiglink
        if ipatokenradiususername:
            _params['ipatokenradiususername'] = ipatokenradiususername
        if loginshell:
            _params['loginshell'] = loginshell
        if ipasshpubkey:
            _params['ipasshpubkey'] = ipasshpubkey
        if st:
            _params['st'] = st
        if street:
            _params['street'] = street
        if title:
            _params['title'] = title
        if ipauserauthtype:
            _params['ipauserauthtype'] = ipauserauthtype
        
        return self._request(method, _args, _params)

    def user_remove_cert(
        self,
        uid,
        usercertificate,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove one or more certificates to the user entry
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param usercertificate: Base-64 encoded user certificate
        :type usercertificate: Certificate
        """
        method = 'user_remove_cert'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['usercertificate'] = usercertificate
        
        return self._request(method, _args, _params)

    def user_remove_certmapdata(
        self,
        uid,
        ipacertmapdata=None,
        certificate=None,
        issuer=None,
        subject=None,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove one or more certificate mappings from the user entry.
        :param ipacertmapdata: Certificate mapping data
        :type ipacertmapdata: Str
        :param uid: User login
        :type uid: Str
        :param certificate: Base-64 encoded user certificate
        :type certificate: Certificate
        :param issuer: Issuer of the certificate
        :type issuer: DNParam
        :param subject: Subject of the certificate
        :type subject: DNParam
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'user_remove_certmapdata'
        
        _args = list()
        _args.append(ipacertmapdata)
        _args.append(uid)
        
        _params = dict()
        if certificate:
            _params['certificate'] = certificate
        if issuer:
            _params['issuer'] = issuer
        if subject:
            _params['subject'] = subject
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def user_remove_manager(
        self,
        uid,
        opt_all=True,
        no_members=False,
        raw=False,
        user=None,
    ):
        """Remove a manager to the user entry
        :param uid: User login
        :type uid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param user: users to remove
        :type user: Str
        """
        method = 'user_remove_manager'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def user_remove_principal(
        self,
        uid,
        krbprincipalname,
        opt_all=True,
        no_members=False,
        raw=False,
    ):
        """Remove principal alias from the user entry
        :param uid: User login
        :type uid: Str
        :param krbprincipalname: Principal alias
        :type krbprincipalname: Principal
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'user_remove_principal'
        
        _args = list()
        _args.append(uid)
        _args.append(krbprincipalname)
        
        _params = dict()
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def user_show(
        self,
        uid,
        out=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
    ):
        """Display information about a user.
        :param uid: User login
        :type uid: Str
        :param out: file to store certificate in
        :type out: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        """
        method = 'user_show'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        if out:
            _params['out'] = out
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        
        return self._request(method, _args, _params)

    def user_stage(
        self,
        uid,
        opt_continue=False,
    ):
        """Move deleted user into staged area
        :param uid: User login
        :type uid: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        """
        method = 'user_stage'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        _params['continue'] = opt_continue
        
        return self._request(method, _args, _params)

    def user_status(
        self,
        useruid,
        opt_all=True,
        raw=False,
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
        :param useruid: User login
        :type useruid: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'user_status'
        
        _args = list()
        _args.append(useruid)
        
        _params = dict()
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def user_undel(
        self,
        uid,
    ):
        """Undelete a delete user account.
        :param uid: User login
        :type uid: Str
        """
        method = 'user_undel'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def user_unlock(
        self,
        uid,
    ):
        """
    Unlock a user account

    An account may become locked if the password is entered incorrectly too
    many times within a specific time period as controlled by password
    policy. A locked account is a temporary condition and may be unlocked by
    an administrator.
        :param uid: User login
        :type uid: Str
        """
        method = 'user_unlock'
        
        _args = list()
        _args.append(uid)
        
        _params = dict()
        
        return self._request(method, _args, _params)

    def vault_add_internal(
        self,
        cn,
        service=None,
        addattr=None,
        opt_setattr=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        shared=False,
        ipavaultpublickey=None,
        ipavaultsalt=None,
        description=None,
        ipavaulttype='symmetric',
    ):
        """None
        :param cn: Vault name
        :type cn: Str
        :param service: Service name of the service vault
        :type service: Principal
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param ipavaultpublickey: Vault public key
        :type ipavaultpublickey: Bytes
        :param ipavaultsalt: Vault salt
        :type ipavaultsalt: Bytes
        :param description: Vault description
        :type description: Str
        :param ipavaulttype: Vault type
        :type ipavaulttype: StrEnum
        """
        method = 'vault_add_internal'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if service:
            _params['service'] = service
        if addattr:
            _params['addattr'] = addattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        if ipavaultpublickey:
            _params['ipavaultpublickey'] = ipavaultpublickey
        if ipavaultsalt:
            _params['ipavaultsalt'] = ipavaultsalt
        if description:
            _params['description'] = description
        if ipavaulttype:
            _params['ipavaulttype'] = ipavaulttype
        
        return self._request(method, _args, _params)

    def vault_add_member(
        self,
        cn,
        service=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        shared=False,
        group=None,
        services=None,
        user=None,
    ):
        """Add members to a vault.
        :param cn: Vault name
        :type cn: Str
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param group: groups to add
        :type group: Str
        :param services: services to add
        :type services: Str
        :param user: users to add
        :type user: Str
        """
        method = 'vault_add_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        if group:
            _params['group'] = group
        if services:
            _params['services'] = services
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def vault_add_owner(
        self,
        cn,
        service=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        shared=False,
        group=None,
        services=None,
        user=None,
    ):
        """Add owners to a vault.
        :param cn: Vault name
        :type cn: Str
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param group: groups to add
        :type group: Str
        :param services: services to add
        :type services: Str
        :param user: users to add
        :type user: Str
        """
        method = 'vault_add_owner'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        if group:
            _params['group'] = group
        if services:
            _params['services'] = services
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def vault_archive_internal(
        self,
        cn,
        nonce,
        session_key,
        vault_data,
        service=None,
        username=None,
        opt_all=True,
        raw=False,
        shared=False,
    ):
        """None
        :param cn: Vault name
        :type cn: Str
        :param nonce: Nonce
        :type nonce: Bytes
        :param session_key: Session key wrapped with transport certificate
        :type session_key: Bytes
        :param vault_data: Vault data encrypted with session key
        :type vault_data: Bytes
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        """
        method = 'vault_archive_internal'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['nonce'] = nonce
        _params['session_key'] = session_key
        _params['vault_data'] = vault_data
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        
        return self._request(method, _args, _params)

    def vault_del(
        self,
        cn,
        service=None,
        username=None,
        opt_continue=False,
        shared=False,
    ):
        """Delete a vault.
        :param cn: Vault name
        :type cn: Str
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        :param shared: Shared vault
        :type shared: Flag
        """
        method = 'vault_del'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['continue'] = opt_continue
        if shared:
            _params['shared'] = shared
        
        return self._request(method, _args, _params)

    def vault_find(
        self,
        criteria=None,
        sizelimit=None,
        timelimit=None,
        service=None,
        username=None,
        opt_all=True,
        no_members=True,
        pkey_only=False,
        raw=False,
        services=False,
        shared=False,
        users=False,
        description=None,
        cn=None,
        ipavaulttype='symmetric',
    ):
        """Search for vaults.
        :param criteria: A string searched in all relevant object attributes
        :type criteria: Str
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: Int
        :param timelimit: Time limit of search in seconds (0 is unlimited)
        :type timelimit: Int
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param pkey_only: Results should contain primary key attribute only ("name")
        :type pkey_only: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param services: List all service vaults
        :type services: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param users: List all user vaults
        :type users: Flag
        :param description: Vault description
        :type description: Str
        :param cn: Vault name
        :type cn: Str
        :param ipavaulttype: Vault type
        :type ipavaulttype: StrEnum
        """
        method = 'vault_find'
        
        _args = list()
        _args.append(criteria)
        
        _params = dict()
        if sizelimit:
            _params['sizelimit'] = sizelimit
        if timelimit:
            _params['timelimit'] = timelimit
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        if pkey_only:
            _params['pkey_only'] = pkey_only
        _params['raw'] = raw
        if services:
            _params['services'] = services
        if shared:
            _params['shared'] = shared
        if users:
            _params['users'] = users
        if description:
            _params['description'] = description
        if cn:
            _params['cn'] = cn
        if ipavaulttype:
            _params['ipavaulttype'] = ipavaulttype
        
        return self._request(method, _args, _params)

    def vault_mod_internal(
        self,
        cn,
        service=None,
        addattr=None,
        opt_delattr=None,
        opt_setattr=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        shared=False,
        ipavaultpublickey=None,
        ipavaultsalt=None,
        description=None,
        ipavaulttype='symmetric',
    ):
        """None
        :param cn: Vault name
        :type cn: Str
        :param service: Service name of the service vault
        :type service: Principal
        :param addattr: Add an attribute/value pair. Format is attr=value. The attribute
must be part of the schema.
        :type addattr: Str
        :param opt_delattr: Delete an attribute/value pair. The option will be evaluated
last, after all sets and adds.
        :type opt_delattr: Str
        :param opt_setattr: Set an attribute to a name/value pair. Format is attr=value.
For multi-valued attributes, the command replaces the values already present.
        :type opt_setattr: Str
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param ipavaultpublickey: Vault public key
        :type ipavaultpublickey: Bytes
        :param ipavaultsalt: Vault salt
        :type ipavaultsalt: Bytes
        :param description: Vault description
        :type description: Str
        :param ipavaulttype: Vault type
        :type ipavaulttype: StrEnum
        """
        method = 'vault_mod_internal'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if service:
            _params['service'] = service
        if addattr:
            _params['addattr'] = addattr
        if opt_delattr:
            _params['delattr'] = opt_delattr
        if opt_setattr:
            _params['setattr'] = opt_setattr
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if shared:
            _params['shared'] = shared
        if ipavaultpublickey:
            _params['ipavaultpublickey'] = ipavaultpublickey
        if ipavaultsalt:
            _params['ipavaultsalt'] = ipavaultsalt
        if description:
            _params['description'] = description
        if ipavaulttype:
            _params['ipavaulttype'] = ipavaulttype
        
        return self._request(method, _args, _params)

    def vault_remove_member(
        self,
        cn,
        service=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        shared=False,
        group=None,
        services=None,
        user=None,
    ):
        """Remove members from a vault.
        :param cn: Vault name
        :type cn: Str
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param group: groups to remove
        :type group: Str
        :param services: services to remove
        :type services: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'vault_remove_member'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        if group:
            _params['group'] = group
        if services:
            _params['services'] = services
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def vault_remove_owner(
        self,
        cn,
        service=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        shared=False,
        group=None,
        services=None,
        user=None,
    ):
        """Remove owners from a vault.
        :param cn: Vault name
        :type cn: Str
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param group: groups to remove
        :type group: Str
        :param services: services to remove
        :type services: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'vault_remove_owner'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        if group:
            _params['group'] = group
        if services:
            _params['services'] = services
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def vault_retrieve_internal(
        self,
        cn,
        session_key,
        service=None,
        username=None,
        opt_all=True,
        raw=False,
        shared=False,
    ):
        """None
        :param cn: Vault name
        :type cn: Str
        :param session_key: Session key wrapped with transport certificate
        :type session_key: Bytes
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        """
        method = 'vault_retrieve_internal'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        _params['session_key'] = session_key
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        
        return self._request(method, _args, _params)

    def vault_show(
        self,
        cn,
        service=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        shared=False,
    ):
        """Display information about a vault.
        :param cn: Vault name
        :type cn: Str
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param shared: Shared vault
        :type shared: Flag
        """
        method = 'vault_show'
        
        _args = list()
        _args.append(cn)
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if shared:
            _params['shared'] = shared
        
        return self._request(method, _args, _params)

    def vaultconfig_show(
        self,
        transport_out=None,
        opt_all=True,
        raw=False,
    ):
        """Show vault configuration.
        :param transport_out: Output file to store the transport certificate
        :type transport_out: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        """
        method = 'vaultconfig_show'
        
        _args = list()
        
        _params = dict()
        if transport_out:
            _params['transport_out'] = transport_out
        _params['all'] = opt_all
        _params['raw'] = raw
        
        return self._request(method, _args, _params)

    def vaultcontainer_add_owner(
        self,
        service=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        shared=False,
        group=None,
        services=None,
        user=None,
    ):
        """Add owners to a vault container.
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param group: groups to add
        :type group: Str
        :param services: services to add
        :type services: Str
        :param user: users to add
        :type user: Str
        """
        method = 'vaultcontainer_add_owner'
        
        _args = list()
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        if group:
            _params['group'] = group
        if services:
            _params['services'] = services
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def vaultcontainer_del(
        self,
        service=None,
        username=None,
        opt_continue=False,
        shared=False,
    ):
        """Delete a vault container.
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_continue: Continuous mode: Don't stop on errors.
        :type opt_continue: Flag
        :param shared: Shared vault
        :type shared: Flag
        """
        method = 'vaultcontainer_del'
        
        _args = list()
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['continue'] = opt_continue
        if shared:
            _params['shared'] = shared
        
        return self._request(method, _args, _params)

    def vaultcontainer_remove_owner(
        self,
        service=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        shared=False,
        group=None,
        services=None,
        user=None,
    ):
        """Remove owners from a vault container.
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param shared: Shared vault
        :type shared: Flag
        :param group: groups to remove
        :type group: Str
        :param services: services to remove
        :type services: Str
        :param user: users to remove
        :type user: Str
        """
        method = 'vaultcontainer_remove_owner'
        
        _args = list()
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        if shared:
            _params['shared'] = shared
        if group:
            _params['group'] = group
        if services:
            _params['services'] = services
        if user:
            _params['user'] = user
        
        return self._request(method, _args, _params)

    def vaultcontainer_show(
        self,
        service=None,
        username=None,
        opt_all=True,
        no_members=False,
        raw=False,
        rights=False,
        shared=False,
    ):
        """Display information about a vault container.
        :param service: Service name of the service vault
        :type service: Principal
        :param username: Username of the user vault
        :type username: Str
        :param opt_all: Retrieve and print all attributes from the server. Affects command output.
        :type opt_all: Flag
        :param no_members: Suppress processing of membership attributes.
        :type no_members: Flag
        :param raw: Print entries as stored on the server. Only affects output format.
        :type raw: Flag
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details.
        :type rights: Flag
        :param shared: Shared vault
        :type shared: Flag
        """
        method = 'vaultcontainer_show'
        
        _args = list()
        
        _params = dict()
        if service:
            _params['service'] = service
        if username:
            _params['username'] = username
        _params['all'] = opt_all
        _params['no_members'] = no_members
        _params['raw'] = raw
        _params['rights'] = rights
        if shared:
            _params['shared'] = shared
        
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
