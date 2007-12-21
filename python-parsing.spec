%define modname parsing
%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Name:           python-%{modname}
Version:        1.4.2
Release:        %mkrel 3
Summary:        An object-oriented approach to text processing

Group:          Development/Python
License:        MIT
URL:            http://pyparsing.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/pyparsing/py%{modname}-%{version}.tar.bz2
Source1:        pyparsing-LICENSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

BuildRequires:  python-devel
Provides:	py%{modname}

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.

%prep
%setup -q -n py%{modname}-%{version}

%build
%{__python} setup.py build
mv pyparsingClassDiagram.PNG pyparsingClassDiagram.png
install -p -m 0644 %{SOURCE1} $RPM_BUILD_DIR/py%{modname}-%{version}/LICENSE

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES examples HowToUsePyparsing.html htmldoc pyparsingClassDiagram.png README LICENSE
%{python_sitelib}/pyparsing.py
%{python_sitelib}/pyparsing.py[co]
%{python_sitelib}/*.egg-info


