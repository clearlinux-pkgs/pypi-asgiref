#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-asgiref
Version  : 3.7.2
Release  : 53
URL      : https://files.pythonhosted.org/packages/12/19/64e38c1c2cbf0da9635b7082bbdf0e89052e93329279f59759c24a10cc96/asgiref-3.7.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/12/19/64e38c1c2cbf0da9635b7082bbdf0e89052e93329279f59759c24a10cc96/asgiref-3.7.2.tar.gz
Summary  : ASGI specs, helper code, and adapters
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-asgiref-license = %{version}-%{release}
Requires: pypi-asgiref-python = %{version}-%{release}
Requires: pypi-asgiref-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n asgiref-3.7.2
cd %{_builddir}/asgiref-3.7.2
pushd ..
cp -a asgiref-3.7.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685241454
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-asgiref
cp %{_builddir}/asgiref-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-asgiref/baf11129ce63c4eef654f39a360b31cfc7d1ac67 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
