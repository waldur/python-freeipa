Name: python-freeipa
Summary: Lightweight FreeIPA client
Group: Development/Libraries
Version: 0.2.1
Release: 1.el7
License: MIT
Url: https://waldur.com
Source0: python-freeipa-%{version}.tar.gz

Requires: python-requests

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
Lightweight FreeIPA client.

%prep
%setup -q -n python-freeipa-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Tue Aug 14 2018 Henry Z. Graham <hgraham@redhat.com> - 0.2.1-1.hzg.el7
- https://github.com/sirwalrus/python-freeipa/pull/1/commits/5dde963b200178addc21f03f4d37ef886594994e

* Thu Jun 28 2018 Jenkins <jenkins@opennodecloud.com> - 0.2.1-1.el7
- New upstream release

* Fri May 25 2018 Brian J. Atkisson <brian@atkisson.net> - 0.2.0-1.bja.el7
- https://github.com/sirwalrus/python-freeipa/commit/1f7d697ee2cd0bbebea49028c82132e61789b24a

* Sun May 6 2018 Jenkins <jenkins@opennodecloud.com> - 0.2.0-1.el7
- New upstream release

* Fri Apr 20 2018 Jenkins <jenkins@opennodecloud.com> - 0.1.3-1.el7
- New upstream release

* Fri May 26 2017 Jenkins <jenkins@opennodecloud.com> - 0.1.2-1.el7
- New upstream release

* Wed May 24 2017 Jenkins <jenkins@opennodecloud.com> - 0.1.1-1.el7
- New upstream release

* Wed May 24 2017 Victor Mireyev <victor@opennodecloud.com> - 0.1.0-1
- Initial version of the package.
