Name: python-freeipa
Summary: Lightweight FreeIPA client
Group: Development/Libraries
Version: 0.2.5
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
* Sun Nov 24 2019 Jenkins <jenkins@opennodecloud.com> - 0.2.5-1.el7
- New upstream release

* Wed Oct 23 2019 Jenkins <jenkins@opennodecloud.com> - 0.2.4-1.el7
- New upstream release

* Tue Apr 30 2019 Jenkins <jenkins@opennodecloud.com> - 0.2.3-1.el7
- New upstream release

* Tue Apr 23 2019 Jenkins <jenkins@opennodecloud.com> - 0.2.2-1.el7
- New upstream release


* Thu Jun 28 2018 Jenkins <jenkins@opennodecloud.com> - 0.2.1-1.el7
- New upstream release

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
