Name: python-gbinder
Version: 1.1.1
Release: 1
Summary: Python bindings for libgbinder
License: GPLv3
Group: Development/Python
URL: https://github.com/erfanoabdi/gbinder-python
Source0: https://github.com/erfanoabdi/gbinder-python/archive/%{version}/gbinder-python-%{version}.tar.gz

BuildRequires: pkgconfig(libgbinder)
BuildRequires: pkgconfig(libglibutil)
BuildRequires: pkgconfig(python)
BuildRequires: python3dist(cython)

%description
There are two Cython files: cgbinder.pxd describing the C++ API of the libgbinder library, and gbinder.pyx describing classes that will be visible from Python user code. The .pyx imports .pxd to learn about C functions available to be called.

There is also setup.py file. This file describes how to build the extension module, using distutils. In there, we specify the library to link with as libraries=['gbinder']. The gbinder stands for libgbinder.so that we previously installed.

There are two options to build the package:

One, use Cython's cythonize() function to generate a .c file from the .pyx one, and then compile it against the libgbinder.so library.
Two, if the .c is already provided, just compile it - no Cython required!

%prep
%autosetup -n gbinder-python-%{version} -p1

%build
%py_build -- --cython

%install
%py_install

%files
%{python_sitearch}/gbinder_python-%{version}-py*.*.egg-info
%{python_sitearch}/gbinder.cpython-*-*-linux-gnu.so
