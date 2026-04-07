%define module parsing

Name:		python-parsing
Summary:	An object-oriented approach to text processing
Version:	3.3.2
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://github.com/pyparsing/pyparsing
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
The pyparsing module provides an alternative approach to creating and
executing simple grammars in Python versus the traditional lex/yacc
approach or the use of regular expressions. It provides a library of
classes that client code can use to construct a grammar directly.

%files
%{py_puresitedir}/py%{module}
%{py_puresitedir}/py%{module}-%{version}.dist-info
