#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : libgudev
Version  : 238
Release  : 24
URL      : https://download.gnome.org/sources/libgudev/238/libgudev-238.tar.xz
Source0  : https://download.gnome.org/sources/libgudev/238/libgudev-238.tar.xz
Summary  : GObject bindings for libudev
Group    : Development/Tools
License  : LGPL-2.1
Requires: libgudev-data = %{version}-%{release}
Requires: libgudev-lib = %{version}-%{release}
Requires: libgudev-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libudev)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libgudev
========
This is libgudev, a library providing GObject bindings for libudev. It
used to be part of udev, then merged into systemd. It's now a project
on its own.

%package data
Summary: data components for the libgudev package.
Group: Data

%description data
data components for the libgudev package.


%package dev
Summary: dev components for the libgudev package.
Group: Development
Requires: libgudev-lib = %{version}-%{release}
Requires: libgudev-data = %{version}-%{release}
Provides: libgudev-devel = %{version}-%{release}
Requires: libgudev = %{version}-%{release}

%description dev
dev components for the libgudev package.


%package lib
Summary: lib components for the libgudev package.
Group: Libraries
Requires: libgudev-data = %{version}-%{release}
Requires: libgudev-license = %{version}-%{release}

%description lib
lib components for the libgudev package.


%package license
Summary: license components for the libgudev package.
Group: Default

%description license
license components for the libgudev package.


%prep
%setup -q -n libgudev-238
cd %{_builddir}/libgudev-238
pushd ..
cp -a libgudev-238 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688664634
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dtests=disabled \
-Dgtk_doc=false  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dtests=disabled \
-Dgtk_doc=false  builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libgudev
cp %{_builddir}/libgudev-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libgudev/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GUdev-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gudev-1.0.deps
/usr/share/vala/vapi/gudev-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gudev-1.0/gudev/gudev.h
/usr/include/gudev-1.0/gudev/gudevclient.h
/usr/include/gudev-1.0/gudev/gudevdevice.h
/usr/include/gudev-1.0/gudev/gudevenumerator.h
/usr/include/gudev-1.0/gudev/gudevenums.h
/usr/include/gudev-1.0/gudev/gudevenumtypes.h
/usr/include/gudev-1.0/gudev/gudevtypes.h
/usr/lib64/libgudev-1.0.so
/usr/lib64/pkgconfig/gudev-1.0.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgudev-1.0.so.0.3.0
/usr/lib64/libgudev-1.0.so.0
/usr/lib64/libgudev-1.0.so.0.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgudev/01a6b4bf79aca9b556822601186afab86e8c4fbf
