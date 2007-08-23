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
Summary(pl.UTF-8):	Wolna implementacja mDNS/DNS-SD
Name:		avahi
Version:	0.6.20
Release:	7
License:	LGPL v2.1+
Group:		Applications
Source0:	http://avahi.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	6acdff79afa2631f765f3bbbc3e25a74
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
BuildRequires:	libdaemon-devel >= 0.11
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
%if %{with dotnet}
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10
BuildRequires:	mono-csharp
BuildRequires:	monodoc
%endif
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-dbus >= 0.71
BuildRequires:	python-pygtk-devel >= 2:2.9.6
%if %{with qt3}
BuildRequires:	qt-devel >= 1:3.0
%endif
%if %{with qt4}
BuildRequires:	QtCore-devel
BuildRequires:	qt4-build
%endif
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 0.92
Requires:	libdaemon >= 0.11
Provides:	group(avahi)
Provides:	user(avahi)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Avahi is an implementation the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing. It uses D-BUS for communication
between user applications and a system daemon.

%description -l pl.UTF-8
Avahi jest implementacją specyfikacji DNS Service Discovery i
Multicast DNS dla Zeroconf Computing. Używa D-BUSa dla komunikacji
pomiędzy programami użytkownika a demonem systemowym.

%package libs
Summary:	Avahi client, common and core libraries
Summary(pl.UTF-8):	Biblioteki Avahi: klienta, wspólna i główna
Group:		Libraries

%description libs
Avahi client, common and core libraries.

%description libs -l pl.UTF-8
Biblioteki Avahi: klienta, wspólna i główna.

%package devel
Summary:	Header files for Avahi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Avahi
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-devel >= 0.92
Requires:	expat-devel

%description devel
This is the package containing the header files for Avahi library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki Avahi.

%package static
Summary:	Static Avahi library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Avahi library.

%description static -l pl.UTF-8
Statyczna biblioteka Avahi.

%package ui
Summary:	Avahi UI library
Summary(pl.UTF-8):	Biblioteka Avahi UI
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2 >= 2:2.10.2

%description ui
Common GTK+ UI support library for Avahi.

%description ui -l pl.UTF-8
Biblioteka wspólnego interfejsu użytkownika GTK+ dla Avahi.

%package ui-devel
Summary:	Header files for Avahi UI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Avahi UI
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ui = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.2

%description ui-devel
Header files for Avahi UI library.

%description ui-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Avahi UI.

%package ui-static
Summary:	Static Avahi UI library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi UI
Group:		X11/Development/Libraries
Requires:	%{name}-ui-devel = %{version}-%{release}

%description ui-static
Static Avahi UI library.

%description ui-static -l pl.UTF-8
Statyczna biblioteka Avahi UI.

%package compat-libdns_sd
Summary:	Avahi Bonjour compat library
Summary(pl.UTF-8):	Biblioteka Avahi zgodna z Bonjour
Group:		Libraries
Provides:	mdns-bonjour
Obsoletes:	mDNSResponder-libs

%description compat-libdns_sd
Avahi Bonjour compat library.

%description compat-libdns_sd -l pl.UTF-8
Biblioteka Avahi zgodna z Bonjour.

%package compat-libdns_sd-devel
Summary:	Header files for Avahi Bonjour compat library
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Avahi dla biblioteki zgodnej z Bonjour
Group:		Development/Libraries
Requires:	%{name}-compat-libdns_sd = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Provides:	mdns-bonjour-devel
Obsoletes:	mDNSResponder-devel

%description compat-libdns_sd-devel
Header files for Avahi Bonjour compat library.

%description compat-libdns_sd-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Avahi dla biblioteki zgodnej z Bonjour.

%package compat-libdns_sd-static
Summary:	Static Avahi Bonjour compat library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi zgodna z Bonjour
Group:		Development/Libraries
Requires:	%{name}-compat-libdns_sd-devel = %{version}-%{release}
Provides:	mdns-bonjour-static

%description compat-libdns_sd-static
Static Avahi Bonjour compat library.

%description compat-libdns_sd-static -l pl.UTF-8
Statyczna biblioteka Avahi zgodna z Bonjour.

%package compat-howl
Summary:	Avahi Howl compat library
Summary(pl.UTF-8):	Biblioteka Avahi zgodna z Howl
Group:		Libraries
Provides:	mdns-howl-libs
Obsoletes:	howl-libs

%description compat-howl
Avahi Howl compat library.

%description compat-howl -l pl.UTF-8
Biblioteka Avahi zgodna z Howl.

%package compat-howl-devel
Summary:	Header files for Avahi Howl compat library
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Avahi dla biblioteki zgodnej z Howl
Group:		Development/Libraries
Requires:	%{name}-compat-howl = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Provides:	mdns-howl-devel
Obsoletes:	howl-devel

%description compat-howl-devel
Header files for Avahi Howl compat library.

%description compat-howl-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Avahi dla biblioteki zgodnej z Howl.

%package compat-howl-static
Summary:	Static Avahi Howl compat library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi zgodna z Howl
Group:		Development/Libraries
Requires:	%{name}-compat-howl-devel = %{version}-%{release}
Provides:	mdns-howl-static
Obsoletes:	howl-static

%description compat-howl-static
Static Avahi Howl compat library.

%description compat-howl-static -l pl.UTF-8
Statyczna biblioteka Avahi zgodna z Howl.

%package glib
Summary:	Avahi GLib library bindings
Summary(pl.UTF-8):	Wiązania Avahi dla bibioteki GLib
Group:		Libraries

%description glib
Avahi GLib library bindings.

%description glib -l pl.UTF-8
Wiązania Avahi dla bibioteki GLib.

%package glib-devel
Summary:	Header files for Avahi GLib library bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Avahi dla biblioteki GLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.2

%description glib-devel
This is the package containing the header files for Avahi-glib
library.

%description glib-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki Avahi-glib.

%package glib-static
Summary:	Static Avahi GLib library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi GLib
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static Avahi GLib library.

%description glib-static -l pl.UTF-8
Statyczna biblioteka Avahi GLib.

%package qt
Summary:	Avahi Qt 3 library bindings
Summary(pl.UTF-8):	Wiązania Avahi dla biblioteki Qt 3
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	avahi-qt3

%description qt
Avahi Qt 3 library bindings.

%description qt -l pl.UTF-8
Wiązania Avahi dla biblioteki Qt 3.

%package qt-devel
Summary:	Header files for Avahi Qt 3 library bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	qt-devel >= 1:3.0
Obsoletes:	avahi-qt3-devel

%description qt-devel
Header files for Avahi Qt 3 library bindings.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 3.

%package qt-static
Summary:	Static Avahi Qt 3 library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi Qt 3
Group:		Development/Libraries
Requires:	%{name}-qt-devel = %{version}-%{release}
Obsoletes:	avahi-qt3-static

%description qt-static
Static Avahi Qt 3 library.

%description qt-static -l pl.UTF-8
Statyczna biblioteka Avahi Qt 3.

%package Qt
Summary:	Avahi Qt 4 library bindings
Summary(pl.UTF-8):	Wiązania Avahi dla biblioteki Qt 4
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description Qt
Avahi Qt 4 library bindings.

%description Qt -l pl.UTF-8
Wiązania Avahi dla biblioteki Qt 4.

%package Qt-devel
Summary:	Header files for Avahi Qt 4 library bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 4
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-Qt = %{version}-%{release}

%description Qt-devel
Header files for Avahi Qt 4 library bindings.

%description Qt-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 4.

%package Qt-static
Summary:	Static Avahi Qt 4 library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi Qt 4
Group:		Development/Libraries
Requires:	%{name}-Qt-devel = %{version}-%{release}

%description Qt-static
Static Avahi Qt 4 library.

%description Qt-static -l pl.UTF-8
Statyczna biblioteka Avahi Qt 4.

%package -n python-avahi
Summary:	Avahi Python bindings
Summary(pl.UTF-8):	Wiązania Avahi dla Pythona
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-dbus >= 0.71

%description -n python-avahi
Avahi Python bindings.

%description -n python-avahi -l pl.UTF-8
Wiązania Avahi dla Pythona.

%package -n dotnet-avahi
Summary:	Avahi MONO bindings
Summary(pl.UTF-8):	Wiązania Avahi dla MONO
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description -n dotnet-avahi
Avahi MONO bindings.

%description -n dotnet-avahi -l pl.UTF-8
Wiązania Avahi dla MONO.

%package -n dotnet-avahi-devel
Summary:	Development files for MONO Avahi bindings
Summary(pl.UTF-8):	Pliki rozwojowe wiązań Avahi dla MONO
Group:		Development/Libraries
Requires:	dotnet-avahi = %{version}-%{release}
Requires:	monodoc

%description -n dotnet-avahi-devel
Development files for MONO Avahi bindings.

%description -n dotnet-avahi-devel -l pl.UTF-8
Pliki rozwojowe wiązań Avahi dla MONO.

%package -n dotnet-avahi-ui
Summary:	Avahi UI MONO bindings
Summary(pl.UTF-8):	Wiązania Avahi UI dla MONO
Group:		X11/Libraries
Requires:	%{name}-ui = %{version}-%{release}
Requires:	dotnet-avahi = %{version}-%{release}

%description -n dotnet-avahi-ui
Avahi UI MONO bindings.

%description -n dotnet-avahi-ui -l pl.UTF-8
Wiązania Avahi UI dla MONO.

%package -n dotnet-avahi-ui-devel
Summary:	Development files for MONO Avahi UI bindings
Summary(pl.UTF-8):	Pliki rozwojowe wiązań Avahi UI dla MONO
Group:		X11/Development/Libraries
Requires:	dotnet-avahi-ui = %{version}-%{release}
Requires:	monodoc

%description -n dotnet-avahi-ui-devel
Development files for MONO Avahi UI bindings.

%description -n dotnet-avahi-ui-devel -l pl.UTF-8
Pliki rozwojowe wiązań Avahi UI dla MONO.

%package bookmarks
Summary:	Miniature web server
Summary(pl.UTF-8):	Miniaturowy serwer web
Group:		Applications

%description bookmarks
A Python based miniature web server that browses for mDNS/DNS-SD
services of type '_http._tcp' (i.e. web sites) and makes them
available as HTML links on http://localhost:8080/.

%description bookmarks -l pl.UTF-8
Napisany w Pythonie miniaturowy serwer WWW, pozwalający na
przeglądanie usług typu '_http._tcp' (np. stron WWW) i udostępniający
je jako odnośniki HTML na http://localhost:8080/.

%package discover
Summary:	Avahi Zeroconf browser
Summary(pl.UTF-8):	Przeglądarka Zeroconf Avahi
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-avahi = %{version}-%{release}
Requires:	python-pygtk-glade >= 2:2.9.6

%description discover
A tool for enumerating all available services on the local LAN
(python-pygtk implementation).

%description discover -l pl.UTF-8
Narzędzie wymieniające wszystkie dostępne usługi w sieci lokalnej LAN
(implementacja w python-pygtk).

%package discover-standalone
Summary:	Avahi Zeroconf browser
Summary(pl.UTF-8):	Przeglądarka Zeroconf Avahi
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus >= 0.71
Requires:	python-pygtk-glade >= 2:2.9.6

%description discover-standalone
GTK+ tool for enumerating all available services on the local LAN.

%description discover-standalone -l pl.UTF-8
Narzędzie GTK+ wymieniające wszystkie dostępne usługi w sieci lokalnej
LAN.

%package utils
Summary:	Avahi CLI utilities
Summary(pl.UTF-8):	Narzędzia CLI Avahi
Group:		Applications

%description utils
Command line utilities using avahi-client.

%description utils -l pl.UTF-8
Narzędzia linii poleceń korzystające z avahi-client.

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

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{avahi-{browse-domains,publish-address,publish-service,resolve-address,resolve-host-name},bvnc}.1
echo '.so avahi-browse.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-browse-domains.1
echo '.so avahi-publish.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-publish-address.1
echo '.so avahi-publish.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-publish-service.1
echo '.so avahi-resolve.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-resolve-address.1
echo '.so avahi-resolve.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-resolve-host-name.1
echo '.so bssh.1' > $RPM_BUILD_ROOT%{_mandir}/man1/bvnc.1

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

%post	ui -p /sbin/ldconfig
%postun	ui -p /sbin/ldconfig

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

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bssh
%attr(755,root,root) %{_bindir}/bvnc
%attr(755,root,root) %{_libdir}/libavahi-ui.so.*.*.*
%{_desktopdir}/bssh.desktop
%{_desktopdir}/bvnc.desktop

%files ui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-ui.so
%{_libdir}/libavahi-ui.la
%{_includedir}/avahi-ui
%{_pkgconfigdir}/avahi-ui.pc

%files ui-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-ui.a

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

%files -n python-avahi
%defattr(644,root,root,755)
%{py_sitedir}/avahi

%if %{with dotnet}
%files -n dotnet-avahi
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/avahi-sharp

%files -n dotnet-avahi-devel
%defattr(644,root,root,755)
%{_libdir}/monodoc/sources/avahi-sharp-docs.*
%{_prefix}/lib/mono/avahi-sharp
%{_pkgconfigdir}/avahi-sharp.pc

%files -n dotnet-avahi-ui
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/avahi-ui-sharp

%files -n dotnet-avahi-ui-devel
%defattr(644,root,root,755)
%{_libdir}/monodoc/sources/avahi-ui-sharp-docs.*
%{_prefix}/lib/mono/avahi-ui-sharp
%{_pkgconfigdir}/avahi-ui-sharp.pc
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
%{_desktopdir}/avahi-discover.desktop
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
