# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name: python-bytesize
Version: 1.0
Release: 1%{?dist}
Summary: A module for computing, displaying, and parsing sizes in bytes

License: LGPLv2+
URL: http://python-bytesize.readthedocs.org
%define realname bytesize
Source0: http://mulhern.fedorapeople.org/%{realname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: pylint
BuildRequires: python-setuptools

%description
The python-bytesize package is a python module for computing, displaying,
and parsing sizes in bytes.


%prep
%setup -q -n %{realname}-%{version}

%build

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%check
make test
make check

%files
%doc README.md ChangeLog LICENSE
%{python2_sitelib}/*


%changelog
