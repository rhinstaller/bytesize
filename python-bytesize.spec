Summary: A module for computing, displaying, and parsing sizes in bytes.
Name: python-bytesize		
Url: ?
Version: 1.0
Release: 1%{?dist}
Epoch: 1
License: LGPLv2+
Group: ?
Source0: https://github.com/rhinstaller/bytesize.git
 
BuildArch: noarch
BuildRequires: gettext	
BuildRequires: python-setuptools	

Requires: python
Requires: python-six

%description
The python-bytesize package is a python module for computing, displaying,
and parsing sizes in bytes.

%prep
%setup -q -n %{realname}-%{version}


%build
make


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{realname}

%files -f %{realname}.lang
%defattr(-,root,root,-)
%license LICENSE
%doc README Changelog doc
%{python_sitelib}/*

%changelog
