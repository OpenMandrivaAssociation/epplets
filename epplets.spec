%define libname %mklibname epplet 0
%define eprefix %_prefix
Name: epplets
Summary: Applets for enlightenment
Version: 0.12
Release: %mkrel 3
Source: %{name}-%{version}.tar.gz
Group: Graphical desktop/Enlightenment
URL: https://www.enlightenment.org
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	imagemagick
BuildRequires:	libesound-devel
BuildRequires:	libjpeg-static-devel	
BuildRequires:	texinfo
BuildRequires:	mesaglut-devel
BuildRequires:  libcdaudio-devel
BuildRequires:  chrpath
BuildRequires:  imlib2-devel
Obsoletes: Epplets
Provides: Epplets = %{version}
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

%package -n %libname-devel
Group: Development/C
Summary: Development libraries for Enlightenment applets
Provides: libepplet-devel = %version-%release
Provides: epplets-devel = %version-%release
Requires: %libname = %version

%description -n %libname-devel
An epplet is an applet designed specificly for use with enlightenment
This packages contains several, two cpu load meters, two clocks, a network
load monitor, aswell as a E-Biff

This is needed for building Epplets.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q 

%build
export EROOT=%{eprefix}/share/enlightenment
export EBIN=%{eprefix}/bin
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{eprefix} --enable-fsstd --libdir=%eprefix/%_lib --disable-auto-respawn

perl -p -i -e 's/ppp0/lo/g' epplets/E-NetGraph.c

%make

%install
mkdir -p $RPM_BUILD_ROOT/%{eprefix}
export EROOT=$RPM_BUILD_ROOT%{eprefix}/share/enlightenment
export EBIN=$RPM_BUILD_ROOT%{eprefix}/bin
#perl -p -i -e 's/\$\(EROOT\)\//\$\(DESTDIR\)\/\$\(EROOT\)\//g' epplets/Makefile
make install DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT/usr/share/e16/epplet_icons
for f in `find . -name '*.icon'`; do
  convert -geometry 16x16 $f $f.png
  mv -f $f.png $f
done
chrpath -d %buildroot%eprefix/bin/*

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig   
%endif
     
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig  
%endif

%files
%defattr(-,root,root)
%doc ChangeLog
%eprefix/bin/*
%eprefix/share/e16/epplet*

%files -n %libname
%defattr(-,root,root)
%eprefix/%_lib/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%eprefix/include/*
%eprefix/%_lib/*.so
%attr(644,root,root) %eprefix/%_lib/*a



