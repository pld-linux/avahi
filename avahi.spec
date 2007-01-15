#
# TODO:
# - autoip subpackage ?
# - autoip start script ?
#
# Conditional build:
%bcond_without	dotnet		# build without dotnet bindings
%bcond_without	qt		# build without (any) qt bindings
%bcond_without	qt3		# build without qt3 bindings
%bcond_without	qt4		# build without qt4 bindings
#
%if !%{with qt}
%undefine	with_qt3
%undefine	with_qt4
%endif
%include /usr/lib/rpm/macros.mono
#
Summary:	Free mDNS/DNS-SD implementation
Summary(pl):	Wolna implementacja mDNS/DNS-SD
Name:		avahi
Version:	0.6.16
Release:	1
License:	GPL v.2/LGPL
Group:		Applications
Source0:	http://avahi.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	3cbc460bbd55bae35f7b57443c063640
Source1:	%{name}-daemon
Source2:	%{name}-dnsconfd
Source3:	%{name}.png
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-glade.patch
Patch2:		%{name}-destdir.patch
URL:		http://avahi.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.92
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel >= 1:2.12.2
BuildRequires:	graphviz
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	libcap-devel
BuildRequires:	libdaemon-devel >= 0.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
%if %{with dotnet}
BuildRequires:	mono-csharp
BuildRequires:	monodoc
%endif
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-dbus >= 0.71
BuildRequires:	python-pygtk-devel >= 2:2.9.6
%if %{with qt3}
BuildRequires:	qt-devel >= 3.0
%endif
%if %{with qt4}
BuildRequires:	QtCore-devel
BuildRequires:	qt4-build
%endif
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:	dbus >= 0.92
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
Requires:	dbus-devel >= 0.92
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

%package compat-libdns_sd
Summary:	Avahi Bonjour compat library
Summary(pl):	Biblioteka Avahi zgodna z Bonjour
Group:		Libraries
Provides:	mdns-bonjour
Obsoletes:	mDNSResponder-libs

%description compat-libdns_sd
Avahi Bonjour compat library.

%description compat-libdns_sd -l pl
Biblioteka Avahi zgodna z Bonjour.

%package compat-libdns_sd-devel
Summary:	Header files for Avahi Bonjour compat library
Summary(pl):	Pliki nag³ówkowe wi±zañ Avahi dla biblioteki zgodnej z Bonjour
Group:		Development/Libraries
Requires:	%{name}-compat-libdns_sd = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Provides:	mdns-bonjour-devel
Obsoletes:	mDNSResponder-devel

%description compat-libdns_sd-devel
Header files for Avahi Bonjour compat library.

%description compat-libdns_sd-devel -l pl
Pliki nag³ówkowe wi±zañ Avahi dla biblioteki zgodnej z Bonjour.

%package compat-libdns_sd-static
Summary:	Static Avahi Bonjour compat library
Summary(pl):	Statyczna biblioteka Avahi zgodna z Bonjour
Group:		Development/Libraries
Requires:	%{name}-compat-libdns_sd-devel = %{version}-%{release}
Provides:	mdns-bonjour-static

%description compat-libdns_sd-static
Static Avahi Bonjour compat library.

%description compat-libdns_sd-static -l pl
Statyczna biblioteka Avahi zgodna z Bonjour.

%package compat-howl
Summary:	Avahi Howl compat library
Summary(pl):	Biblioteka Avahi zgodna z Howl
Group:		Libraries
Provides:	mdns-howl-libs
Obsoletes:	howl-libs

%description compat-howl
Avahi Howl compat library.

%description compat-howl -l pl
Biblioteka Avahi zgodna z Howl.

%package compat-howl-devel
Summary:	Header files for Avahi Howl compat library
Summary(pl):	Pliki nag³ówkowe wi±zañ Avahi dla biblioteki zgodnej z Howl
Group:		Development/Libraries
Requires:	%{name}-compat-howl = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Provides:	mdns-howl-devel
Obsoletes:	howl-devel

%description compat-howl-devel
Header files for Avahi Howl compat library.

%description compat-howl-devel -l pl
Pliki nag³ówkowe wi±zañ Avahi dla biblioteki zgodnej z Howl.

%package compat-howl-static
Summary:	Static Avahi Howl compat library
Summary(pl):	Statyczna biblioteka Avahi zgodna z Howl
Group:		Development/Libraries
Requires:	%{name}-compat-howl-devel = %{version}-%{release}
Provides:	mdns-howl-static
Obsoletes:	howl-static

%description compat-howl-static
Static Avahi Howl compat library.

%description compat-howl-static -l pl
Statyczna biblioteka Avahi zgodna z Howl.

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
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.2

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

%package qt
Summary:	Avahi Qt 3 library bindings
Summary(pl):	Wi±zania Avahi dla biblioteki Qt 3
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	avahi-qt3

%description qt
Avahi Qt 3 library bindings.

%description qt -l pl
Wi±zania Avahi dla biblioteki Qt 3.

%package qt-devel
Summary:	Header files for Avahi Qt 3 library bindings
Summary(pl):	Pliki nag³ówkowe wi±zañ Avahi dla biblioteki Qt 3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	qt-devel >= 3.0
Obsoletes:	avahi-qt3-devel

%description qt-devel
Header files for Avahi Qt 3 library bindings.

%description qt-devel -l pl
Pliki nag³ówkowe wi±zañ Avahi dla biblioteki Qt 3.

%package qt-static
Summary:	Static Avahi Qt 3 library
Summary(pl):	Statyczna biblioteka Avahi Qt 3
Group:		Development/Libraries
Requires:	%{name}-qt-devel = %{version}-%{release}
Obsoletes:	avahi-qt3-static

%description qt-static
Static Avahi Qt 3 library.

%description qt-static -l pl
Statyczna biblioteka Avahi Qt 3.

%package Qt
Summary:	Avahi Qt 4 library bindings
Summary(pl):	Wi±zania Avahi dla biblioteki Qt 4
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description Qt
Avahi Qt 4 library bindings.

%description Qt -l pl
Wi±zania Avahi dla biblioteki Qt 4.

%package Qt-devel
Summary:	Header files for Avahi Qt 4 library bindings
Summary(pl):	Pliki nag³ówkowe wi±zañ Avahi dla biblioteki Qt 4
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-Qt = %{version}-%{release}

%description Qt-devel
Header files for Avahi Qt 4 library bindings.

%description Qt-devel -l pl
Pliki nag³ówkowe wi±zañ Avahi dla biblioteki Qt 4.

%package Qt-static
Summary:	Static Avahi Qt 4 library
Summary(pl):	Statyczna biblioteka Avahi Qt 4
Group:		Development/Libraries
Requires:	%{name}-Qt-devel = %{version}-%{release}

%description Qt-static
Static Avahi Qt 4 library.

%description Qt-static -l pl
Statyczna biblioteka Avahi Qt 4.

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
Requires:	monodoc

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
available as HTML links on http://localhost:8080/.

%description bookmarks -l pl
Napisany w Pythonie miniaturowy serwer WWW, pozwalaj±cy na
przegl±danie us³ug typu '_http._tcp' (np. stron WWW) i udostêpniaj±cy
je jako odno¶niki HTML na http://localhost:8080/.

%package discover
Summary:	Avahi Zeroconf browser
Summary(pl):	Przegl±darka Zeroconf Avahi
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus >= 0.71
Requires:	python-pygtk-glade >= 2:2.9.6

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
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus >= 0.71
Requires:	python-pygtk-glade >= 2:2.9.6

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I common
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-compat-libdns_sd \
	--enable-compat-howl \
	--with-distro=none \
	%{!?with_qt3:--disable-qt3} \
	%{!?with_qt4:--disable-qt4} \
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

ln -sf %{_includedir}/avahi-compat-libdns_sd/dns_sd.h \
	$RPM_BUILD_ROOT%{_includedir}/dns_sd.h

ln -sf %{_pkgconfigdir}/avahi-compat-howl.pc \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/howl.pc

rm -f $RPM_BUILD_ROOT%{py_sitedir}/avahi/{__init__,SimpleGladeApp}.py

# Stop rpm insanity
rm  -f $RPM_BUILD_ROOT%{_mandir}/man1/{avahi-browse-domains.1,avahi-publish-address.1,avahi-publish-service.1,avahi-resolve-address.1,avahi-resolve-host-name.1}

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

%post	compat-libdns_sd -p /sbin/ldconfig
%postun	compat-libdns_sd -p /sbin/ldconfig

%post	compat-howl -p /sbin/ldconfig
%postun	compat-howl -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%post	Qt -p /sbin/ldconfig
%postun	Qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/COMPAT-LAYERS docs/NEWS docs/README docs/TODO

%dir %{_sysconfdir}/avahi
%dir %{_sysconfdir}/avahi/services
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/avahi-daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/avahi-dnsconfd.action
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/hosts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/services/ssh.service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/services/sftp-ssh.service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/*

%attr(755,root,root) %{_bindir}/avahi-set-host-name

%attr(755,root,root) %{_sbindir}/avahi-daemon
%attr(755,root,root) %{_sbindir}/avahi-dnsconfd

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/introspection
%{_datadir}/%{name}/introspection/*.introspect
%{_datadir}/%{name}/avahi-service.dtd
%{_datadir}/%{name}/service-types
%{_datadir}/%{name}/service-types.db

%{_mandir}/man*/*

%attr(754,root,root) /etc/rc.d/init.d/%{name}-daemon
%attr(754,root,root) /etc/rc.d/init.d/%{name}-dnsconfd

%attr(755,root,root) %{_sysconfdir}/%{name}/avahi-autoipd.action
%attr(755,root,root) %{_sbindir}/avahi-autoipd

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

%files compat-libdns_sd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdns_sd.so.*.*.*

%files compat-libdns_sd-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdns_sd.so
%{_libdir}/libdns_sd.la
%{_includedir}/avahi-compat-libdns_sd
%{_includedir}/dns_sd.h
%{_pkgconfigdir}/avahi-compat-libdns_sd.pc

%files compat-libdns_sd-static
%defattr(644,root,root,755)
%{_libdir}/libdns_sd.a

%files compat-howl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhowl.so.*.*.*

%files compat-howl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhowl.so
%{_libdir}/libhowl.la
%{_includedir}/avahi-compat-howl
%{_pkgconfigdir}/avahi-compat-howl.pc
%{_pkgconfigdir}/howl.pc

%files compat-howl-static
%defattr(644,root,root,755)
%{_libdir}/libhowl.a

%if %{with dotnet}
%files -n dotnet-avahi
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/avahi-sharp

%files -n dotnet-avahi-devel
%defattr(644,root,root,755)
%{_libdir}/monodoc/sources/avahi-*
%{_prefix}/lib/mono/avahi-sharp
%{_pkgconfigdir}/avahi-sharp.pc
%endif

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

%if %{with qt3}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so.*.*.*

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so
%{_libdir}/libavahi-qt3.la
%{_includedir}/avahi-qt3
%{_pkgconfigdir}/avahi-qt3.pc

%files qt-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-qt3.a
%endif

%if %{with qt4}
%files Qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt4.so.*.*.*

%files Qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt4.so
%{_libdir}/libavahi-qt4.la
%{_includedir}/avahi-qt4
%{_pkgconfigdir}/avahi-qt4.pc

%files Qt-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-qt4.a
%endif

%files bookmarks
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-bookmarks

%files discover
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-discover
# XXX: possibly missing %{_datadir}/%{name} dir, shared subdir
%dir %{_datadir}/%{name}/interfaces
%{_datadir}/%{name}/interfaces/avahi-discover.glade
%{py_sitedir}/avahi
%{_desktopdir}/*.desktop
%{_pixmapsdir}/avahi.png

%files discover-standalone
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-discover-standalone
# XXX: possibly missing %{_datadir}/%{name} dir, shared subdir
%dir %{_datadir}/%{name}/interfaces
%{_datadir}/%{name}/interfaces/avahi-discover-standalone.glade

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-browse
%attr(755,root,root) %{_bindir}/avahi-publish
%attr(755,root,root) %{_bindir}/avahi-resolve
