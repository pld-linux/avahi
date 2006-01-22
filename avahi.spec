#
# Conditional build:
%bcond_with	dotnet		# build with dotnet bindings
#
Summary:	Free mDNS/DNS-SD implementation
Summary(pl):	Wolna implementacja mDNS/DNS-SD
Name:		avahi
Version:	0.6.4
Release:	0.1
License:	GPL v.2/LGPL
Group:		Applications
Source0:	http://avahi.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	12eb941043f26f82c51e99821ac52c44
Source1:	%{name}-daemon
Source2:	%{name}-dnsconfd
Source3:	%{name}.png
Patch1:		%{name}-desktop.patch
URL:		http://avahi.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.34
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	graphviz
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libdaemon-devel >= 0.5
BuildRequires:	libglade2-devel >= 2.4.0
BuildRequires:	libtool
%if %{with dotnet}
BuildRequires:	mono
BuildRequires:	monodoc
%endif
BuildRequires:	python-dbus
BuildRequires:	python-pygtk-devel
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Provides:	group(avahi)
Provides:	user(avahi)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Avahi is an implementation the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing. It uses D-BUS for communication
between user applications and a system daemon.

%description -l pl
Avahi jest implementacj± specyfikacji DNS Service Discovery i
Multicast DNS dla Zeroconf Computing. U¿ywa D-BUSa dla komunikacji
pomiêdzy programami u¿ytkownika a demonem systemowym.

%package libs
Summary:	Avahi client, common and core libraries
Summary(pl):	Biblioteki Avahi: klienta, wspólna i g³ówna
Group:		Libraries

%description libs
Avahi client, common and core libraries.

%description libs -l pl
Biblioteki Avahi: klienta, wspólna i g³ówna.

%package devel
Summary:	Header files for Avahi library
Summary(pl):	Pliki nag³ówkowe biblioteki Avahi
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	expat-devel
Requires:	libdaemon-devel >= 0.5

%description devel
This is the package containing the header files for Avahi library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki Avahi.

%package static
Summary:	Static Avahi library
Summary(pl):	Statyczna biblioteka Avahi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Avahi library.

%description static -l pl
Statyczna biblioteka Avahi.

%package glib
Summary:	Avahi GLib library bindings
Summary(pl):	Wi±zania Avahi dla bibioteki GLib
Group:		Libraries

%description glib
Avahi GLib library bindings.

%description glib -l pl
Wi±zania Avahi dla bibioteki GLib.

%package glib-devel
Summary:	Header files for Avahi GLib library bindings
Summary(pl):	Pliki nag³ówkowe wi±zañ Avahi dla biblioteki GLib
Group:		Development/Libraries
Requires:	%{name}-glib = %{version}-%{release}
Requires:	glib2-devel >= 1:2.4.0

%description glib-devel
This is the package containing the header files for Avahi-glib
library.

%description glib-devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki Avahi-glib.

%package glib-static
Summary:	Static Avahi GLib library
Summary(pl):	Statyczna biblioteka Avahi GLib
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static Avahi GLib library.

%description glib-static -l pl
Statyczna biblioteka Avahi GLib.

%package qt3
Summary:	Avahi Qt 3 library bindings
Summary(pl):	Wi±zania Avahi dla biblioteki Qt 3
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description qt3
Avahi Qt 3 library bindings.

%description qt3 -l pl
Wi±zania Avahi dla biblioteki Qt 3.

%package qt3-devel
Summary:	Header files for Avahi Qt 3 library bindings
Summary(pl):	Pliki nag³ówkowe wi±zañ Avahi dla biblioteki Qt 3
Group:		Development/Libraries
Requires:	%{name}-qt3 = %{version}-%{release}
Requires:	qt-devel

%description qt3-devel
Header files for Avahi Qt 3 library bindings.

%description qt3-devel -l pl
Pliki nag³ówkowe wi±zañ Avahi dla biblioteki Qt 3.

%package qt3-static
Summary:	Static Avahi Qt 3 library
Summary(pl):	Statyczna biblioteka Avahi Qt 3
Group:		Development/Libraries
Requires:	%{name}-qt3-devel = %{version}-%{release}

%description qt3-static
Static Avahi Qt 3 library.

%description qt3-static -l pl
Statyczna biblioteka Avahi Qt 3.

%package -n dotnet-avahi
Summary:	Avahi MONO bindings
Summary(pl):	Wi±zania Avahi dla MONO
Group:		Libraries

%description -n dotnet-avahi
Avahi MONO bindings.

%description -n dotnet-avahi -l pl
Wi±zania Avahi dla MONO.

%package -n dotnet-avahi-devel
Summary:	Development files for MONO Avahi bindings
Summary(pl):	Pliki rozwojowe wi±zañ Avahi dla MONO
Group:		Development/Libraries
Requires:	dotnet-avahi = %{version}-%{release}

%description -n dotnet-avahi-devel
Development files for MONO Avahi bindings.

%description -n dotnet-avahi-devel -l pl
Pliki rozwojowe wi±zañ Avahi dla MONO.

%package bookmarks
Summary:	Miniature web server
Summary(pl):	Miniaturowy serwer web
Group:		Applications

%description bookmarks
A Python based miniature web server that browses for mDNS/DNS-SD
services of type '_http._tcp' (i.e. web sites) and makes them
available as HTML links on http://localhost:8080.

%description bookmarks -l pl
Napisany w Pythonie miniaturowy serwer web, pozwalaj±cy na
przegl±danie us³ug typu '_http._tcp' (np. stron web) i udostêpniaj±cy
je jako linki HTML na http://localhost:8080.

%package discover
Summary:	Avahi Zeroconf browser
Summary(pl):	Przegl±darka Zeroconf Avahi
Group:		Applications

%description discover
A tool for enumerating all available services on the local LAN
(python-pygtk implementation).

%description discover -l pl
Narzêdzie wymieniaj±ce wszystkie dostêpne us³ugi w sieci lokalnej LAN
(implementacja w python-pygtk).

%package discover-standalone
Summary:	Avahi Zeroconf browser
Summary(pl):	Przegl±darka Zeroconf Avahi
Group:		Applications

%description discover-standalone
GTK+ tool for enumerating all available services on the local LAN.

%description discover-standalone -l pl
Narzêdzie GTK+ wymieniaj±ce wszystkie dostêpne us³ugi w sieci lokalnej
LAN.

%package utils
Summary:	Avahi CLI utilities
Summary(pl):	Narzêdzia CLI Avahi
Group:		Applications

%description utils
Command line utilities using avahi-client.

%description utils -l pl
Narzêdzia linii poleceñ korzystaj±ce z avahi-client.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I common
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-distro=none \
	--disable-qt4 \
	%{!?with_dotnet:--disable-mono} \
	%{!?with_dotnet:--disable-monodoc}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},/etc/rc.d/init.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitedir}

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

#rm -f $RPM_BUILD_ROOT%{py_sitedir}/avahi/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 165 -r -f avahi
%useradd -u 165 -r -d /usr/share/empty -s /bin/false -c "Avahi daemon" -g avahi avahi

%post
/sbin/chkconfig --add %{name}-daemon
%service %{name}-daemon restart
/sbin/chkconfig --add %{name}-dnsconfd
%service %{name}-dnsconfd restart

%preun
if [ "$1" = "0" ]; then
	%service -q %{name}-dnsconfd stop
	/sbin/chkconfig --del %{name}-dnsconfd
	%service -q %{name}-daemon stop
	/sbin/chkconfig --del %{name}-daemon
fi

%postun
if [ "$1" = "0" ]; then
        %userremove avahi
	%groupremove avahi
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	qt3 -p /sbin/ldconfig
%postun	qt3 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/COMPAT-LAYERS docs/NEWS docs/README docs/TODO

%dir %{_sysconfdir}/avahi
%dir %{_sysconfdir}/avahi/services
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/avahi-daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/avahi-dnsconfd.action
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/services/ssh.service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/*

%attr(755,root,root) %{_bindir}/avahi-browse
%attr(755,root,root) %{_bindir}/avahi-publish
%attr(755,root,root) %{_bindir}/avahi-resolve

%attr(755,root,root) %{_sbindir}/avahi-daemon
%attr(755,root,root) %{_sbindir}/avahi-dnsconfd

%dir %{_datadir}/%{name}
%dir
%dir %{_datadir}/%{name}/introspection
%{_datadir}/%{name}/introspection/*.introspect
%{_datadir}/%{name}/avahi-service.dtd
%{_datadir}/%{name}/service-types
%{_datadir}/%{name}/service-types.db

%{_mandir}/man*/*

%attr(754,root,root) /etc/rc.d/init.d/%{name}-daemon
%attr(754,root,root) /etc/rc.d/init.d/%{name}-dnsconfd

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-client.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-common.so.*.*.*
%attr(755,root,root) %{_libdir}/libavahi-core.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/API-CHANGES-0.6 docs/DBUS-API docs/HACKING docs/MALLOC
%attr(755,root,root) %{_libdir}/libavahi-client.so
%attr(755,root,root) %{_libdir}/libavahi-common.so
%attr(755,root,root) %{_libdir}/libavahi-core.so
%{_libdir}/libavahi-client.la
%{_libdir}/libavahi-common.la
%{_libdir}/libavahi-core.la
%{_includedir}/avahi-client
%{_includedir}/avahi-common
%{_includedir}/avahi-core
%{_pkgconfigdir}/avahi-client.pc
%{_pkgconfigdir}/avahi-core.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libavahi-client.a
%{_libdir}/libavahi-common.a
%{_libdir}/libavahi-core.a

#%files -n dotnet-avahi
#%defattr(644,root,root,755)

#%files -n dotnet-avahi-devel
#%defattr(644,root,root,755)

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-glib.so.*.*.*

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-glib.so
%{_libdir}/libavahi-glib.la
%{_includedir}/avahi-glib
%{_pkgconfigdir}/avahi-glib.pc

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-glib.a

%files qt3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so.*.*.*

%files qt3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so
%{_libdir}/libavahi-qt3.la
%{_includedir}/avahi-qt3
%{_pkgconfigdir}/avahi-qt3.pc

%files qt3-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-qt3.a

%files bookmarks
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-bookmarks

%files discover
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-discover
%{_datadir}/%{name}/interfaces/avahi-discover.glade
%{py_sitedir}/avahi
%{_desktopdir}/*.desktop
%{_pixmapsdir}/avahi.png

%files discover-standalone
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-discover-standalone

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-browse
%attr(755,root,root) %{_bindir}/avahi-publish
%attr(755,root,root) %{_bindir}/avahi-resolve
