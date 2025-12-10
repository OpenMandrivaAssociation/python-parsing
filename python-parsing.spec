%define module parsing

Summary:	An object-oriented approach to text processing

Name:		python-%{module}
Version:	3.2.5
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://github.com/pyparsing/pyparsing
Source0:	https://github.com/pyparsing/pyparsing/releases/download/%{version}/pyparsing-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
The pyparsing module provides an alternative approach to creating and
executing simple grammars in Python versus the traditional lex/yacc
approach or the use of regular expressions. It provides a library of
classes that client code can use to construct a grammar directly.

%files
%{py_puresitedir}/*
