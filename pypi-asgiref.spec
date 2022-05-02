#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-asgiref
Version  : 3.5.1
Release  : 33
URL      : https://files.pythonhosted.org/packages/6d/b6/44c179fdee3857af5e76ee04426cac8119ef736900a0068d12c1c018301c/asgiref-3.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/b6/44c179fdee3857af5e76ee04426cac8119ef736900a0068d12c1c018301c/asgiref-3.5.1.tar.gz
Summary  : ASGI specs, helper code, and adapters
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-asgiref-license = %{version}-%{release}
Requires: pypi-asgiref-python = %{version}-%{release}
Requires: pypi-asgiref-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
asgiref
=======
.. image:: https://api.travis-ci.org/django/asgiref.svg
:target: https://travis-ci.org/django/asgiref

%package license
Summary: license components for the pypi-asgiref package.
Group: Default

%description license
license components for the pypi-asgiref package.


%package python
Summary: python components for the pypi-asgiref package.
Group: Default
Requires: pypi-asgiref-python3 = %{version}-%{release}

%description python
python components for the pypi-asgiref package.


%package python3
Summary: python3 components for the pypi-asgiref package.
Group: Default
Requires: python3-core
Provides: pypi(asgiref)

%description python3
python3 components for the pypi-asgiref package.


%prep
%setup -q -n asgiref-3.5.1
cd %{_builddir}/asgiref-3.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651521464
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-asgiref
cp %{_builddir}/asgiref-3.5.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-asgiref/baf11129ce63c4eef654f39a360b31cfc7d1ac67
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-asgiref/baf11129ce63c4eef654f39a360b31cfc7d1ac67

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*