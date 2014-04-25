%define module	parsing

Summary:	An object-oriented approach to text processing

Name:		python-%{module}
Version:	2.0.2
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pyparsing.wikispaces.com/
Source0:	http://sourceforge.net/projects/pyparsing/files/pyparsing/pyparsing-2.0.2/pyparsing-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)

%description
The pyparsing module provides an alternative approach to creating and
executing simple grammars in Python versus the traditional lex/yacc
approach or the use of regular expressions. It provides a library of
classes that client code can use to construct a grammar directly.

%prep
%setup -qn py%{module}-%{version}

%build
python setup.py build

install -m 644 pyparsingClassDiagram.PNG pyparsingClassDiagram.png

%install
python setup.py install -O1 --skip-build --root=%{buildroot} --record=FILE_LIST

# fix permissions
chmod 0644 examples/* htmldoc/* CHANGES HowToUsePyparsing.html pyparsingClassDiagram.png README LICENSE

%files
%doc CHANGES examples HowToUsePyparsing.html htmldoc pyparsingClassDiagram.png README LICENSE
%{py_puresitedir}/*



