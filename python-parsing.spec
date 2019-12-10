%define module parsing

Summary:	An object-oriented approach to text processing

Name:		python-%{module}
Version:	2.4.5
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://github.com/pyparsing/pyparsing
Source0:	https://github.com/pyparsing/pyparsing/archive/pyparsing_%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildRequires:	python-setuptools

%description
The pyparsing module provides an alternative approach to creating and
executing simple grammars in Python versus the traditional lex/yacc
approach or the use of regular expressions. It provides a library of
classes that client code can use to construct a grammar directly.

%package -n python2-%{module}
Summary:	Python 2.x version of the Python parsing module
Group:		Development/Python
BuildRequires:	pkgconfig(python)

%description -n python2-%{module}
The pyparsing module provides an alternative approach to creating and
executing simple grammars in Python versus the traditional lex/yacc
approach or the use of regular expressions. It provides a library of
classes that client code can use to construct a grammar directly.

%prep
%setup -qn py%{module}-py%{module}_%{version}

mkdir PY2
cp -a `ls |grep -v PY2` PY2/

%build
cd PY2
python2 setup.py build

cd ..
python setup.py build

%install
cd PY2
python2 setup.py install -O1 --skip-build --root=%{buildroot} --record=FILE_LIST2

cd ..
python setup.py install -O1 --skip-build --root=%{buildroot} --record=FILE_LIST

%files
%{py_puresitedir}/*

%files -n python2-parsing
%{py2_puresitedir}/*
