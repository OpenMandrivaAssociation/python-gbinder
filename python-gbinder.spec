%define module gbinder
%define oname gbinder_python

Name:		python-gbinder
Version:	1.3.1
Release:	1
Summary:	Python bindings for libgbinder
License:	GPLv3
Group:		Development/Python
URL:		https://github.com/waydroid/gbinder-python
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:   python
BuildRequires:	pkgconfig(libgbinder)
BuildRequires:	pkgconfig(libglibutil)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(setuptools)


%description
There are two Cython files: cgbinder.pxd describing the C++ API of the
libgbinder library, and gbinder.pyx describing classes that will be visible
from Python user code.

The .pyx imports .pxd to learn about C functions available to be called.

There is also setup.py file. This file describes how to build the extension
module, using distutils. In there, we specify the library to link with as
libraries=['gbinder']. The gbinder stands for libgbinder.so that we previously
installed.

There are two options to build the package:

One, use Cython's cythonize() function to generate a .c file from the .pyx one,
and then compile it against the libgbinder.so library.

Two, if the .c is already provided, just compile it - no Cython required!

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%{python_sitearch}/%{oname}-%{version}-py%{pyver}.egg-info
%{python_sitearch}/%{module}.cpython-*-linux-gnu.so
