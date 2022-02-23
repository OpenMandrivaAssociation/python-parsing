%define module parsing

Summary:	An object-oriented approach to text processing

Name:		python-%{module}
Version:	3.0.7
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://github.com/pyparsing/pyparsing
Source0:	https://github.com/pyparsing/pyparsing/archive/pyparsing_%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools

%description
The pyparsing module provides an alternative approach to creating and
executing simple grammars in Python versus the traditional lex/yacc
approach or the use of regular expressions. It provides a library of
classes that client code can use to construct a grammar directly.

%prep
%autosetup -p1 -n py%{module}-py%{module}_%{version}

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root=%{buildroot} --record=FILE_LIST

%files
%{py_puresitedir}/*
