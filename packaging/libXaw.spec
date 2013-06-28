Name:           libXaw
Version:        1.0.11
Release:        1
License:        MIT
Summary:        X Athena Widget Set
Url:            http://www.x.org
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXaw.manifest
BuildRequires:  ed
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)

%description
Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(xmu)
Requires:       pkgconfig(xpm)
Requires:       pkgconfig(xproto)
Requires:       pkgconfig(xt)

%description devel
X.Org X11 libXaw development package

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS="${CFLAGS} %{optflags} -Os"
%reconfigure \
	       --disable-xaw8 --disable-static \
	       --disable-xaw6
make %{?_smp_mflags}

%install

make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_libdir}/*.la

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXaw.so.7
%{_libdir}/libXaw7.so.7
%{_libdir}/libXaw7.so.7.0.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*.h
# FIXME:  Is this C file really supposed to be here?
%{_includedir}/X11/Xaw/Template.c
%{_libdir}/libXaw.so
%{_libdir}/libXaw7.so
%{_libdir}/pkgconfig/xaw7.pc
