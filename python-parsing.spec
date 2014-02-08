%define module	parsing
%define name	python-%{module}
%define version	1.5.6
%define release	2

Summary:	An object-oriented approach to text processing
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Development/Python
License:	MIT
URL:		http://pyparsing.wikispaces.com/
Source0:	http://prdownloads.sourceforge.net/py%{module}/py%{module}-%{version}.zip
BuildArch:	noarch
BuildRequires:	python-devel

%description
The pyparsing module provides an alternative approach to creating and
executing simple grammars in Python versus the traditional lex/yacc
approach or the use of regular expressions. It provides a library of
classes that client code can use to construct a grammar directly.

%prep
%setup -q -n py%{module}-%{version}

%build
%{__python} setup.py build

install -m 644 pyparsingClassDiagram.PNG pyparsingClassDiagram.png

%install
%__rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot} --record=FILE_LIST

# fix permissions
chmod 0644 examples/* htmldoc/* CHANGES HowToUsePyparsing.html pyparsingClassDiagram.png README LICENSE

%files
%doc CHANGES examples HowToUsePyparsing.html htmldoc pyparsingClassDiagram.png README LICENSE
%py_puresitedir/*
