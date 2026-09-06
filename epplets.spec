%define libname %mklibname epplet
%define devname %mklibname -d epplet

Name: epplets
Summary: Applets for enlightenment
Version: 0.18
Release: 1
Source0:	http://downloads.sourceforge.net/enlightenment/e16-epplets-%{version}.tar.xz
Group: Graphical desktop/Enlightenment
URL: https://www.enlightenment.org

BuildRequires:	make
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(glu)

Provides: Epplets = %{EVRD}
Provides: e16-epplets = %{EVRD}
License: GPL

%description
An epplet is an applet designed specificly for use with enlightenment
This packages contains several, two cpu load meters, two clocks, a network
load monitor, aswell as a E-Biff

%package -n %libname
Group: System/Libraries
Summary: Shared library needed by Enlightenment applets

%description -n %libname
An epplet is an applet designed specificly for use with enlightenment
This packages contains several, two cpu load meters, two clocks, a network
load monitor, aswell as a E-Biff

This is needed for running Epplets.

%package -n %{devname}
Group: Development/C
Summary: Development libraries for Enlightenment applets
Provides: libepplet-devel = %version-%release
Provides: epplets-devel = %version-%release
Requires: %libname = %version

%description -n %{devname}
An epplet is an applet designed specificly for use with enlightenment
This packages contains several, two cpu load meters, two clocks, a network
load monitor, aswell as a E-Biff

This is needed for building Epplets.

%prep
%autosetup e16-%{name}-%{version} -p1

%build
%{__sed} -i -e 's/-rpath $(libdir)//' epplets/Makefile.in
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libepplet{,_glx}.{a,la}

%files
%doc ChangeLog 
%{_libdir}/libepplet.so.*
%{_libdir}/libepplet_glx.so.*
%{_bindir}/E*.epplet
%{_datadir}/e16/epplet_icons
%{_datadir}/e16/epplet_data

%files -n %{devname}
%{_includedir}/epplet.h
%{_libdir}/libepplet.so
%{_libdir}/libepplet_glx.so


