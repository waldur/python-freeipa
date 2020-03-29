from python_freeipa.client import Client
from python_freeipa.exceptions import (
    DuplicateEntry,
    parse_group_management_error,
    parse_hostgroup_management_error,
)


class ClientLegacy(Client):
    """Lightweight FreeIPA JSON RPC client."""

    def __init__(self, host, verify_ssl=True, version=None):
        super(ClientLegacy, self).__init__(
            host=host, verify_ssl=verify_ssl, version=version
        )

    def user_add(
        self,
        username,
        first_name,
        last_name,
        full_name,
        display_name=None,
        noprivate=False,
        mail=None,
        ssh_key=None,
        job_title=None,
        gid_number=None,
        uid_number=None,
        preferred_language=None,
        disabled=False,
        random_pass=False,
        initials=None,
        home_directory=None,
        gecos=None,
        login_shell=None,
        user_password=None,
        street_address=None,
        city=None,
        state=None,
        postal_code=None,
        telephone_number=None,
        mobile_number=None,
        pager_number=None,
        fax_number=None,
        organization_unit=None,
        manager=None,
        car_license=None,
        user_auth_type=None,
        user_class=None,
        radius_proxy_config=None,
        radius_proxy_username=None,
        department_number=None,
        employee_number=None,
        employee_type=None,
        **kwargs
    ):
        """
        Add a new user. Username corresponds to UID field of user.

        :param username: User login, it should be alphanumeric and maximum length is 32.
        :type username: str
        :param first_name: First name
        :type first_name: str
        :param last_name: Last name
        :type last_name: str
        :param full_name: Full name
        :type full_name: str
        :param display_name: Display name
        :type display_name: str
        :param noprivate: Don't create user private group
        :type noprivate: bool
        :param mail: Email address
        :type mail: str or list
        :param ssh_key: SSH public key
        :type ssh_key: str or list
        :param job_title: Job title
        :type job_title: str
        :param gid_number: gidNumber
        :type gid_number: str
        :param uid_number: uidNumber
        :type uid_number: str
        :param preferred_language: Preferred language ISO code
        :type preferred_language: str
        :param disabled: Account disabled
        :type disabled: bool
        :param random_pass: Generate a random user password
        :type random_pass: bool
        :param initials: Represent initials of user
        :type initials: str
        :param home_directory: Home directory field of user
        :type home_directory: str
        :param gecos: GECOS field is a comma-delimited list used to record general information about the user.
        :type gecos: str
        :param login_shell: Login shell field of user
        :type login_shell: str
        :param user_password: Prompt to set the user password
        :type user_password: str
        :param street_address: Street address field of user
        :type street_address: str
        :param city: City field of user
        :type city: str
        :param state: State/Province field of user
        :type state: str
        :param postal_code: ZIP code field of user
        :type postal_code: str
        :param telephone_number: Telephone number field of user
        :type telephone_number: str or list
        :param mobile_number: Mobile number field of user
        :type mobile_number: str or list
        :param pager_number: Pager number field of user
        :type pager_number: str or list
        :param fax_number: Fax number field of user
        :type fax_number: str or list
        :param organization_unit: Organization unit of user
        :type organization_unit: str
        :param manager: Manager field of user
        :type manager: str
        :param car_license: Car license of user
        :type car_license: str or list
        :param user_auth_type: Types of supported user authentication. Possible values(password, radius, otp)
        :type user_auth_type: str or list
        :param user_class: Category of user
        :type user_class: str
        :param radius_proxy_config: RADIUS proxy configuration
        :type radius_proxy_config: str
        :param radius_proxy_username: RADIUS proxy username
        :type radius_proxy_username: str
        :param department_number: Department number of user
        :type department_number: str
        :param employee_number: Employee number of user
        :type employee_number: str
        :param employee_type: Employee type of user
        :type employee_type: str
        """
        params = {
            'all': True,
            'givenname': first_name,
            'sn': last_name,
            'cn': full_name,
        }

        if gid_number:
            params['gidnumber'] = gid_number

        if uid_number:
            params['uidnumber'] = uid_number

        if display_name:
            params['displayname'] = display_name

        if noprivate:
            params['noprivate'] = noprivate

        if mail:
            params['mail'] = mail

        if ssh_key:
            params['ipasshpubkey'] = ssh_key

        if job_title:
            params['title'] = job_title

        if preferred_language:
            params['preferredlanguage'] = preferred_language

        if disabled:
            params['nsaccountlock'] = disabled

        if random_pass:
            params['random'] = True

        if initials:
            params['initials'] = initials

        if home_directory:
            params['homedirectory'] = home_directory

        if gecos:
            params['gecos'] = gecos

        if login_shell:
            params['loginshell'] = login_shell

        if user_password:
            params['userpassword'] = user_password

        if street_address:
            params['street'] = street_address

        if city:
            params['l'] = city

        if state:
            params['st'] = state

        if postal_code:
            params['postalcode'] = postal_code

        if telephone_number:
            params['telephonenumber'] = telephone_number

        if mobile_number:
            params['mobile'] = mobile_number

        if pager_number:
            params['pager'] = pager_number

        if fax_number:
            params['facsimiletelephonenumber'] = fax_number

        if organization_unit:
            params['ou'] = organization_unit

        if manager:
            params['manager'] = manager

        if car_license:
            params['carlicense'] = car_license

        if user_auth_type:
            params['ipauserauthtype'] = user_auth_type

        if user_class:
            params['userclass'] = user_class

        if radius_proxy_config:
            params['ipatokenradiusconfiglink'] = radius_proxy_config

        if radius_proxy_username:
            params['ipatokenradiususername'] = radius_proxy_username

        if department_number:
            params['departmentnumber'] = department_number

        if employee_number:
            params['employeenumber'] = employee_number

        if employee_type:
            params['employeetype'] = employee_type

        params.update(kwargs)
        data = self._request('user_add', username, params)
        return data['result']

    def user_find(self, criteria=None, **kwargs):
        """
        Search for users.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str

        """
        params = {
            'all': True,
            'no_members': False,  # Suppress processing of membership attributes.
            'sizelimit': 0,  # Maximum number of entries returned (0 is unlimited)
            'whoami': False,  # Display user record for current Kerberos principal.
        }
        params.update(kwargs)
        return self._request('user_find', criteria, params)

    def user_show(self, username):
        """
        Display information about a user.

        :param username: User login.
        :type username: str
        """
        data = self._request('user_show', username, {'all': True, 'raw': False})
        return data['result']

    def user_status(self, username):
        """
        Get lockout status of a user account.

        :param username: User login.
        :type username: str
        """
        return self._request('user_status', username, {'all': True, 'raw': False})

    def user_disable(self, username):
        """
        Disable a user account.

        :param username: User login.
        :type username: str
        """
        self._request('user_disable', username)

    def user_enable(self, username):
        """
        Enable a user account.

        :param username: User login.
        :type username: str
        """
        self._request('user_enable', username)

    def user_mod(
        self,
        username,
        first_name=None,
        last_name=None,
        full_name=None,
        display_name=None,
        noprivate=False,
        mail=None,
        ssh_key=None,
        job_title=None,
        preferred_language=None,
        disabled=False,
        random_pass=False,
        initials=None,
        home_directory=None,
        gecos=None,
        login_shell=None,
        user_password=None,
        street_address=None,
        city=None,
        state=None,
        postal_code=None,
        telephone_number=None,
        mobile_number=None,
        pager_number=None,
        fax_number=None,
        organization_unit=None,
        manager=None,
        car_license=None,
        user_auth_type=None,
        user_class=None,
        radius_proxy_config=None,
        radius_proxy_username=None,
        department_number=None,
        employee_number=None,
        employee_type=None,
        **kwargs
    ):
        """
        Modify a user.

        :param username: User login.
        :type username: str
        :param first_name: First name
        :type first_name: str
        :param last_name: Last name
        :type last_name: str
        :param full_name: Full name
        :type full_name: str
        :param display_name: Display name
        :type display_name: str
        :param noprivate: Don't create user private group
        :type noprivate: bool
        :param mail: Email address
        :type mail: str or list
        :param ssh_key: SSH public key
        :type ssh_key: str or list
        :param job_title: Job title
        :type job_title: str
        :param preferred_language: Preferred language ISO code
        :type preferred_language: str
        :param disabled: Account disabled
        :type disabled: bool
        :param random_pass: Generate a random user password
        :type random_pass: bool
        :param initials: Represent initials of user
        :type initials: str
        :param home_directory: Home directory field of user
        :type home_directory: str
        :param gecos: Gecos field of user
        :type gecos: str
        :param login_shell: Login shell field of user
        :type login_shell: str
        :param user_password: Prompt to set the user password
        :type user_password: str
        :param street_address: Street address field of user
        :type street_address: str
        :param city: City field of user
        :type city: str
        :param state: State/Province field of user
        :type state: str
        :param postal_code: ZIP code field of user
        :type postal_code: str
        :param telephone_number: Telephone number field of user
        :type telephone_number: str or list
        :param mobile_number: Mobile number field of user
        :type mobile_number: str or list
        :param pager_number: Pager number field of user
        :type pager_number: str or list
        :param fax_number: Fax number field of user
        :type fax_number: str or list
        :param organization_unit: Organization unit of user
        :type organization_unit: str
        :param manager: Manager field of user
        :type manager: str
        :param car_license: Car license of user
        :type car_license: str or list
        :param user_auth_type: Types of supported user authentication. Possible values(password, radius, otp)
        :type user_auth_type: str or list
        :param user_class: Category of user
        :type user_class: str
        :param radius_proxy_config: RADIUS proxy configuration
        :type radius_proxy_config: str
        :param radius_proxy_username: RADIUS proxy username
        :type radius_proxy_username: str
        :param department_number: Department number of user
        :type department_number: str
        :param employee_number: Employee number of user
        :type employee_number: str
        :param employee_type: Employee type of user
        :type employee_type: str
        """
        params = {
            'all': False,  # Retrieve and print all attributes from the server.
            'no_members': False,  # Suppress processing of membership attributes.
            'raw': False,  # Print entries as stored on the server.
            'rights': False,  # Display the access rights of this entry.
        }

        if first_name:
            params['givenname'] = first_name

        if last_name:
            params['sn'] = last_name

        if full_name:
            params['cn'] = full_name

        if display_name:
            params['displayname'] = display_name

        if noprivate:
            params['noprivate'] = noprivate

        if mail:
            params['mail'] = mail

        if ssh_key:
            params['ipasshpubkey'] = ssh_key

        if job_title:
            params['title'] = job_title

        if preferred_language:
            params['preferredlanguage'] = preferred_language

        if disabled:
            params['nsaccountlock'] = disabled

        if random_pass:
            params['random'] = True

        if initials:
            params['initials'] = initials

        if home_directory:
            params['homedirectory'] = home_directory

        if gecos:
            params['gecos'] = gecos

        if login_shell:
            params['loginshell'] = login_shell

        if user_password:
            params['userpassword'] = user_password

        if street_address:
            params['street'] = street_address

        if city:
            params['l'] = city

        if state:
            params['st'] = state

        if postal_code:
            params['postalcode'] = postal_code

        if telephone_number:
            params['telephonenumber'] = telephone_number

        if mobile_number:
            params['mobile'] = mobile_number

        if pager_number:
            params['pager'] = pager_number

        if fax_number:
            params['facsimiletelephonenumber'] = fax_number

        if organization_unit:
            params['ou'] = organization_unit

        if manager:
            params['manager'] = manager

        if car_license:
            params['carlicense'] = car_license

        if user_auth_type:
            params['ipauserauthtype'] = user_auth_type

        if user_class:
            params['userclass'] = user_class

        if radius_proxy_config:
            params['ipatokenradiusconfiglink'] = radius_proxy_config

        if radius_proxy_username:
            params['ipatokenradiususername'] = radius_proxy_username

        if department_number:
            params['departmentnumber'] = department_number

        if employee_number:
            params['employeenumber'] = employee_number

        if employee_type:
            params['employeetype'] = employee_type
        params.update(kwargs)
        data = self._request('user_mod', username, params)
        return data['result']

    def user_del(self, username, skip_errors=False, soft_delete=False):
        """
        Delete a user.

        :param username: User login.
        :type username: str
        :param skip_errors: Continuous mode: Don't stop on errors.
        :type skip_errors: bool
        :param soft_delete: Mark user as deleted instead of removing record.
        :type soft_delete: bool
        """
        params = {
            'continue': skip_errors,
            'preserve': soft_delete,
        }
        return self._request('user_del', username, params)

    def user_undel(self, username):
        """
        Undelete a user.

        :param username: User login.
        :type username: str
        """
        return self._request('user_undel', username)

    def passwd(self, login, password, current_password=None):
        """
        Set the password of a user.

        :param login: User login (username)
        :type login: str
        :param password: New password for the user
        :type password: str
        :param current_password: current password of the logged in user.
                                 Leave blank if resetting for another user,
                                 this will set the new password to expired
        :type current_password: str
        """
        if not current_password:  # resetting for another user
            params = {}
        else:  # resetting for current user
            params = {'current_password': current_password}

        data = self._request('passwd', args=[login, password], params=params)
        return data['result']

    def group_add(
        self,
        group,
        description=None,
        non_posix=False,
        external=False,
        no_members=False,
        **kwargs
    ):
        """
        Create a new group.

        :param group: Group name, it should be alphanumeric and maximum length is 255.
        :type group: str
        :param description: Group description
        :type description: str
        :param non_posix: Create as non-POSIX group
        :type non_posix: bool
        :param external: Allow adding external non-IPA members from trusted domains
        :type external: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        """
        params = {'all': True}

        if description is not None:
            params['description'] = description

        if non_posix is not None:
            params['nonposix'] = non_posix

        if external is not None:
            params['external'] = external

        if no_members is not None:
            params['no_members'] = no_members

        params.update(kwargs)
        data = self._request('group_add', group, params)
        return data['result']

    def group_del(self, group, skip_errors=False):
        """
        Delete a group.

        :param group: Group name
        :param skip_errors: Continuous mode: Don't stop on errors.
        :type skip_errors: bool
        """
        params = {'continue': skip_errors}
        self._request('group_del', group, params)

    def group_add_member(
        self, group, users=None, groups=None, skip_errors=False, **kwargs
    ):
        """
        Add members to a group.

        :param group: Group name.
        :param users: Users to add.
        :type users: str or list
        :param groups: Groups to add.
        :type groups: str or list
        :param skip_errors: Skip processing errors.
        :type skip_errors: bool
        """
        params = {
            'all': True,
            'raw': True,
            'user': users,
            'group': groups,
        }
        params.update(kwargs)
        data = self._request('group_add_member', group, params)
        if not skip_errors:
            parse_group_management_error(data)
        return data['result']

    def group_remove_member(
        self, group, users=None, groups=None, skip_errors=False, **kwargs
    ):
        """
        Remove members from a group.

        :param group: Group name.
        :param users: Users to remove.
        :type users: str or list
        :param groups: Groups to remove.
        :type groups: str or list
        :param skip_errors: Skip processing errors.
        :type skip_errors: bool
        """
        params = {
            'all': False,
            'no_members': False,
            'raw': False,
            'user': users,
            'group': groups,
        }
        params.update(kwargs)
        data = self._request('group_remove_member', group, params)
        if not skip_errors:
            parse_group_management_error(data)
        return data['result']

    def group_find(self, criteria=None, **kwargs):
        """
        Search for groups.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str
        """
        params = {'all': True, 'sizelimit': 0}
        params.update(kwargs)
        return self._request('group_find', criteria, params)

    def group_show(self, group, **kwargs):
        """
        Display information about a named group.

        :param group: Group name.
        """
        params = {'all': True, 'raw': False}
        params.update(kwargs)
        data = self._request('group_show', group, params)
        return data['result']

    def group_mod(
        self,
        group,
        description=None,
        posix=False,
        external=False,
        no_members=False,
        rename=None,
        **kwargs
    ):
        """
        Modify a group.

        :param group: Group name.
        :type group: str
        :param description: Group description
        :type description: str
        :param posix: change to a POSIX group
        :type posix: bool
        :param external: Allow adding external non-IPA members from trusted domains
        :type external: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param rename: Rename the group object
        :type rename: str
        """
        params = {
            'all': False,
            'raw': False,
            'rights': False,
        }
        if description:
            params['description'] = description

        if posix:
            params['posix'] = posix

        if external:
            params['external'] = external

        if no_members:
            params['no_members'] = no_members

        if rename:
            params['rename'] = rename

        params.update(kwargs)
        data = self._request('group_mod', group, params)
        return data['result']

    def automountkey_find(
        self, location, automount_map, key=None, criteria=None, **kwargs
    ):
        """
        Search for the automount key.

        :param key: Automount key name.
        :type key: str
        :param location: Automount location name
        :type location: str
        :param automount_map: Automount map name
        :type automount_map: str
        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str
        :return:
        :rtype: dict
        """
        args = [location, automount_map]

        if criteria:
            args.append(criteria)

        params = {
            'all': True,
            'raw': False,
        }

        if key:
            params['automountkey'] = key

        params.update(kwargs)

        data = self._request('automountkey_find', args, params)
        return data['result']

    def automountkey_add(self, key, mount_info, location, automount_map, **kwargs):
        """
        Create a new automount key.

        :param key: Automount key name
        :type key: str
        :param mount_info: Mount information
        :type mount_info: str
        :param location: Automount location name
        :type location: str
        :param automount_map: Automount map name
        :type automount_map: str
        :return: automount key data
        :rtype: dict
        """
        if self.automountkey_find(location, automount_map, key):
            raise DuplicateEntry()

        args = [location, automount_map]

        params = {
            'all': True,
            'raw': False,
            'automountkey': key,
            'automountinformation': mount_info,
        }
        params.update(kwargs)

        data = self._request('automountkey_add', args, params)
        return data

    def automountkey_mod(self, key, mount_info, automount_location, automount_map):
        """
        Modify an automount key.

        :param key: Automount key name
        :type key: str
        :param mount_info: Mount information
        :type mount_info: str
        :param automount_location: Automount location name
        :param: type string
        :param automount_map: Automount map name
        :type automount_map: str
        :return: automount key data
        :rtype: dict
        """
        args = [automount_location, automount_map]

        params = {
            'all': True,
            'raw': False,
            'rights': False,
            'automountkey': key,
            'automountinformation': mount_info,
        }

        data = self._request('automountkey_mod', args, params)
        return data

    def automountlocation_add(self, location, **kwargs):
        """
        Create a new automount location.

        :param location: Automount location name.
        :type location: str
        """
        params = {'all': True, 'raw': False}
        params.update(kwargs)

        data = self._request('automountlocation_add', location, params)
        return data

    def automountlocation_del(self, location, skip_errors=False):
        """
        Delete an automount location.

        :param location: Automount location name.
        :type location: str
        """
        params = {'continue': skip_errors}
        data = self._request('automountlocation_del', location, params)
        return data

    def automountlocation_find(self, criteria=None, **kwargs):
        """
        Search for an automount location.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str
        """
        params = {'all': True, 'raw': False, 'sizelimit': 0}
        params.update(kwargs)

        data = self._request('automountlocation_find', criteria, params)
        return data['result']

    def automountlocation_show(self, location, **kwargs):
        """
        Display an automount location.

        :param location: Automount location name.
        :type location: str
        """
        params = {'all': True, 'raw': False, 'rights': False}

        data = self._request('automountlocation_show', location, params)
        return data['result']

    def automountlocation_tofiles(self, location):
        """
        Generate automount files for a specific location.

        :param location: Automount location name
        :type location: str
        """
        data = self._request('automountlocation_tofiles', location)
        return data['result']

    def automountmap_add(self, location, automount_map, **kwargs):
        """
        Display an automount map.

        :param location: Automount location name
        :type location: str
        :param automount_map: Automount map name
        :type automount_map: str
        """
        args = [location, automount_map]

        params = {'all': True, 'raw': False}
        params.update(kwargs)

        data = self._request('automountmap_add', args, params)
        return data

    def automountmap_del(self, location, automount_map, skip_errors=False):
        """
        Delete an automount map.

        :param location: Automount location name
        :type location: str
        :param automount_map: Automount map name
        :type automount_map: str
        """
        args = [location, automount_map]
        params = {'continue': skip_errors}

        data = self._request('automountmap_del', args, params)
        return data

    def automountmap_find(self, location, criteria=None, **kwargs):
        """
        Find an automount map.

        :param location: Automount location name
        :type location: str
        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str
        """
        args = [location]
        if criteria:
            args.append(criteria)

        params = {'all': True, 'raw': False, 'sizelimit': 0}
        params.update(kwargs)

        data = self._request('automountmap_find', args, params)
        return data['result']

    def automountmap_mod(self, location, automount_map, description=None, **kwargs):
        """
        Modify an automount map.

        :param location: Automount location name
        :type location: str
        :param automount_map: Automount map name
        :type automount_map: str
        """
        args = [location, automount_map]

        params = {
            'all': True,
            'raw': False,
            'rights': False,
        }

        if description:
            params['description'] = description

        params.update(kwargs)

        data = self._request('automountmap_mod', args, params)
        return data

    def automountmap_show(self, location, automount_map, **kwargs):
        """
        Display an automount map.

        :param location: Automount location name
        :type location: str
        :param automount_map: Automount map name
        :type automount_map: str
        """
        args = [location, automount_map]

        params = {'all': True, 'raw': False, 'rights': False}
        params.update(kwargs)

        data = self._request('automountmap_show', args, params)
        return data['result']

    def host_add(self, host, **kwargs):
        """
        Create a new host.

        :param host: Host name which should be alphanumeric and maximum length is 255
        :type host: str
        """
        params = {'all': True}
        params.update(kwargs)

        data = self._request('host_add', host, params)
        return data['result']

    def host_del(self, fqdn, skip_errors=False, updatedns=None):
        """
        Delete host from FreeIPA

        :param fqdn: Host name
        :type fqdn: str
        :param skip_errors: Continuous mode: Don't stop on errors
        :type skip_errors: bool
        :param updatedns: Remove A, AAAA, SSHFP and PTR records of the host(s) managed by IPA DNS
        :type updatedns: bool
        """
        params = {"continue": skip_errors}

        if updatedns:
            params['updatedns'] = updatedns

        data = self._request('host_del', fqdn, params)
        return data['result']

    def host_find(
        self,
        criteria=None,
        allattr=True,
        no_members=False,
        sizelimit=0,
        raw=False,
        **kwargs
    ):
        """
        Search for hosts.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: int
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        params = {
            'all': allattr,  # Retrieve and print all attributes from the server. Affects command output
            'no_members': no_members,  # Suppress processing of membership attributes
            'sizelimit': sizelimit,  # Maximum number of entries returned (0 is unlimited)
            'raw': raw,  # Print entries as stored on the server. Only affects output format
        }
        params.update(kwargs)
        return self._request('host_find', criteria, params)

    def host_show(self, fqdn, rights=False, no_members=False, allattr=True, raw=False):
        """
        Display information about a host.

        :param fqdn: Host name
        :type fqdn: str
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details
        :type rights: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        data = self._request(
            'host_show',
            fqdn,
            {'all': allattr, 'rights': rights, 'no_members': no_members, 'raw': raw},
        )
        return data['result']

    def hostgroup_add(self, hostgroup, description=None, no_members=False, **kwargs):
        """
        Create a new host group.

        :param hostgroup: Host Group name, it should be alphanumeric and maximum length is 255.
        :type hostgroup: str
        :param description: Host Group description
        :type description: str
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        """
        params = {'all': True}

        if description:
            params['description'] = description

        if no_members:
            params['no_members'] = no_members

        params.update(kwargs)
        data = self._request('hostgroup_add', hostgroup, params)
        return data['result']

    def hostgroup_del(self, hostgroup_name, skip_errors=False):
        """
        Delete a hostgroup

        :param hostgroup_name: Name of hostgroup
        :type hostgroup_name: str
        :param skip_errors: Continuous mode: Don't stop on errors
        :type skip_errors: bool
        """

        data = self._request('hostgroup_del', hostgroup_name, {'continue': skip_errors})
        return data['result']

    def hostgroup_find(
        self,
        criteria=None,
        allattr=True,
        no_members=False,
        sizelimit=0,
        raw=False,
        **kwargs
    ):
        """
        Search for hostgroups

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: int
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        params = {
            'all': allattr,  # Retrieve and print all attributes from the server. Affects command output
            'no_members': no_members,  # Suppress processing of membership attributes
            'sizelimit': sizelimit,  # Maximum number of entries returned (0 is unlimited)
            'raw': raw,  # Print entries as stored on the server. Only affects output format
        }
        params.update(kwargs)
        return self._request('hostgroup_find', criteria, params)

    def hostgroup_show(
        self, hostgroup, rights=False, no_members=False, allattr=True, raw=False
    ):
        """
        Display information about a host.

        :param hostgroup: Hostgroup name
        :type hostgroup: str
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details
        :type rights: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        data = self._request(
            'hostgroup_show',
            hostgroup,
            {'all': allattr, 'rights': rights, 'no_members': no_members, 'raw': raw},
        )
        return data['result']

    def hostgroup_mod(
        self,
        hostgroup,
        description=None,
        no_members=False,
        rights=False,
        allattr=False,
        raw=False,
        **kwargs
    ):
        """
        Modify a hostgroup.

        :param hostgroup: Group name.
        :type hostgroup: str
        :param description: Group description
        :type description: str
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details
        :type rights: bool
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        params = {
            'all': allattr,
            'raw': raw,
            'rights': rights,
            'no_members': no_members,
        }
        if description:
            params['description'] = description

        params.update(kwargs)
        data = self._request('hostgroup_mod', hostgroup, params)
        return data['result']

    def hostgroup_add_members(
        self,
        hostgroup,
        no_members=False,
        host=None,
        hostgroups=None,
        skip_errors=False,
        **kwargs
    ):
        """
        Add members to a hostgroup.

        :param hostgroup: Host Group name, it should be alphanumeric and maximum length is 255.
        :type hostgroup: str
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param host: Hosts to add
        :type host: list or string
        :param hostgroups: Host group to add
        :type hostgroups: list or string
        :param skip_errors: Skip processing errors.
        :type skip_errors: bool
        """
        params = {'all': True}

        if no_members:
            params['no_members'] = no_members

        if host:
            params['host'] = host

        if hostgroups:
            params['hostgroup'] = hostgroups

        params.update(kwargs)
        data = self._request('hostgroup_add_member', hostgroup, params)
        if not skip_errors:
            parse_hostgroup_management_error(data)
        return data['result']

    def hostgroup_remove_members(
        self,
        hostgroup,
        no_members=False,
        host=None,
        hostgroups=None,
        skip_errors=False,
        **kwargs
    ):
        """
        Remove members from a hostgroup.

        :param hostgroup: Host Group name, it should be alphanumeric and maximum length is 255.
        :type hostgroup: str
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param host: Hosts to remove
        :type host: list or string
        :param hostgroups: Host group to remove
        :type hostgroups: list or string
        :param skip_errors: Skip processing errors.
        :type skip_errors: bool
        """
        params = {'all': True}

        if no_members:
            params['no_members'] = no_members

        if host:
            params['host'] = host

        if hostgroups:
            params['hostgroup'] = hostgroups

        params.update(kwargs)
        data = self._request('hostgroup_remove_member', hostgroup, params)
        if not skip_errors:
            parse_hostgroup_management_error(data)
        return data['result']

    def dnsrecord_add(self, zone_name, record_name, **kwargs):
        """
        Create a new DNS record.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        :param record_name: DNS record name (e.g., host1)
        :type record_name: str
        """
        params = {'all': True}

        params.update(kwargs)
        data = self._request('dnsrecord_add', [zone_name, record_name], params)
        return data['result']

    def dnsrecord_del(self, zone_name, record_name, **kwargs):
        """
        Delete a DNS record.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        :param record_name: DNS record name (e.g., host1)
        :type record_name: str
        """
        params = {}

        params.update(kwargs)
        self._request('dnsrecord_del', [zone_name, record_name], params)

    def dnsrecord_find(self, zone_name, criteria=None, **kwargs):
        """
        Search for DNS records.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str
        """
        params = {'all': True, 'sizelimit': 0}
        params.update(kwargs)
        return self._request('dnsrecord_find', [zone_name, criteria], params)

    def dnsrecord_show(self, zone_name, record_name, **kwargs):
        """
        Display information about a DNS record.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        :param record_name: DNS record name (e.g., host1)
        :type record_name: str
        """
        params = {
            'all': True,
            'raw': False,
            'rights': False,
        }
        params.update(kwargs)
        data = self._request('dnsrecord_show', [zone_name, record_name], params)
        return data['result']

    def dnsrecord_mod(self, zone_name, record_name, **kwargs):
        """
        Modify a DNS record.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        :param record_name: DNS record name (e.g., host1)
        :type record_name: str
        """
        params = {
            'all': False,
            'raw': False,
            'rights': False,
        }

        params.update(kwargs)
        data = self._request('dnsrecord_mod', [zone_name, record_name], params)
        return data['result']

    def dnszone_add(self, zone_name, **kwargs):
        """
        Create a new DNS zone.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        """
        params = {'all': True}

        params.update(kwargs)
        data = self._request('dnszone_add', zone_name, params)
        return data['result']

    def dnszone_del(self, zone_name, **kwargs):
        """
        Delete a DNS zone.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        """
        params = {}

        params.update(kwargs)
        self._request('dnszone_del', zone_name, params)

    def dnszone_find(self, criteria=None, **kwargs):
        """
        Search for DNS zones.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: str
        """
        params = {'all': True, 'sizelimit': 0}
        params.update(kwargs)
        return self._request('dnszone_find', criteria, params)

    def dnszone_show(self, zone_name, **kwargs):
        """
        Display information about a DNS zone.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        """
        params = {
            'all': True,
            'raw': False,
            'rights': False,
        }
        params.update(kwargs)
        data = self._request('dnszone_show', zone_name, params)
        return data['result']

    def dnszone_mod(self, zone_name, **kwargs):
        """
        Modify a DNS zone.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: str
        """
        params = {
            'all': False,
            'raw': False,
            'rights': False,
        }

        params.update(kwargs)
        data = self._request('dnszone_mod', zone_name, params)
        return data['result']
