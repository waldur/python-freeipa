# Use Python 2 for RHEL/CentOS 7 and Python 3 for everything else
%if 0%{?el7}
%global __python %{__python2}
%global python_pkgversion %{nil}
%else
%global __python %{__python3}
%global python_pkgversion %{python3_pkgversion}
%endif

Name: python-freeipa
Summary: Lightweight FreeIPA client
Group: Development/Libraries
Version: 1.0.4
Release: 1.el7
License: MIT
Url: https://python-freeipa.readthedocs.io/
Source0: python-freeipa-%{version}.tar.gz

Requires: python%{python_pkgversion}-requests

BuildArch: noarch

BuildRequires: python%{python_pkgversion}-devel
BuildRequires: python%{python_pkgversion}-setuptools

%description
Lightweight FreeIPA client.

%prep
%autosetup

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/*

%changelog
* Wed Apr 22 2020 Jenkins <jenkins@opennodecloud.com> - 1.0.4-1.el7
- New upstream release

* Fri Apr 17 2020 Jenkins <jenkins@opennodecloud.com> - 1.0.3-1.el7
- New upstream release

* Sun Mar 29 2020 Jenkins <jenkins@opennodecloud.com> - 1.0.2-1.el7
- New upstream release

* Tue Feb 25 2020 Jenkins <jenkins@opennodecloud.com> - 1.0.1-1.el7
- New upstream release

* Tue Jan 21 2020 Jenkins <jenkins@opennodecloud.com> - 1.0.0-1.el7
- New upstream release

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
