#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jpype1
Version  : 1.3.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/57/4f/3cddc9b9cd892bbe098e5d48ed3a8aaa02dd3fa732612065fa6b0fab0062/JPype1-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/4f/3cddc9b9cd892bbe098e5d48ed3a8aaa02dd3fa732612065fa6b0fab0062/JPype1-1.3.0.tar.gz
Summary  : A Python to Java bridge.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-jpype1-filemap = %{version}-%{release}
Requires: pypi-jpype1-lib = %{version}-%{release}
Requires: pypi-jpype1-license = %{version}-%{release}
Requires: pypi-jpype1-python = %{version}-%{release}
Requires: pypi-jpype1-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: doc/logo.png
:scale: 50 %
:alt: JPype logo
:align: center
JPype
=====

|implementation|  |pyversions|  |javaversions|  |jvm|  |platform|  |license|

%package filemap
Summary: filemap components for the pypi-jpype1 package.
Group: Default

%description filemap
filemap components for the pypi-jpype1 package.


%package lib
Summary: lib components for the pypi-jpype1 package.
Group: Libraries
Requires: pypi-jpype1-license = %{version}-%{release}
Requires: pypi-jpype1-filemap = %{version}-%{release}

%description lib
lib components for the pypi-jpype1 package.


%package license
Summary: license components for the pypi-jpype1 package.
Group: Default

%description license
license components for the pypi-jpype1 package.


%package python
Summary: python components for the pypi-jpype1 package.
Group: Default
Requires: pypi-jpype1-python3 = %{version}-%{release}

%description python
python components for the pypi-jpype1 package.


%package python3
Summary: python3 components for the pypi-jpype1 package.
Group: Default
Requires: pypi-jpype1-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(jpype1)

%description python3
python3 components for the pypi-jpype1 package.


%prep
%setup -q -n JPype1-1.3.0
cd %{_builddir}/JPype1-1.3.0
pushd ..
cp -a JPype1-1.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653339336
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jpype1
cp %{_builddir}/JPype1-1.3.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jpype1/adeb06dcb98997b978442c639092e33885dc4afc
cp %{_builddir}/JPype1-1.3.0/NOTICE %{buildroot}/usr/share/package-licenses/pypi-jpype1/523827acd23caa6282e6aa25436ba1f1cf49fa92
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-jpype1

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jpype1/523827acd23caa6282e6aa25436ba1f1cf49fa92
/usr/share/package-licenses/pypi-jpype1/adeb06dcb98997b978442c639092e33885dc4afc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
