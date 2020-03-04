# TODO
# - finish with_apidocs
#
# Conditional build:
%bcond_with	apidocs		# API documentation
%bcond_without	dotnet		# .NET (mono) bindings
%bcond_without	gtk2		# GTK+ 2 UI (+ bshell and avahi-discover-standalone utilities if no gtk3)
%bcond_without	gtk3		# GTK+ 3 UI (+ bshell and avahi-discover-standalone utilities)
%bcond_without	pygobject	# PyGObject based avahi-discover utility
%bcond_without	libevent	# libevent main loop integration
%bcond_without	qt		# (any) Qt main loop integration
%bcond_without	qt3		# Qt 3 main loop integration
%bcond_without	qt4		# Qt 4 main loop integration
%bcond_without	qt5		# Qt 5 main loop integration

%ifnarch %{ix86} %{x8664} alpha %{arm} hppa ia64 mips ppc s390 s390x sparc sparcv9
%undefine with_dotnet
%endif
%ifarch i386
%undefine with_dotnet
%endif

%if %{without qt}
%undefine	with_qt3
%undefine	with_qt4
%undefine	with_qt5
%endif

# see http://lists.pld-linux.org/mailman/pipermail/pld-devel-pl/2012-October/155984.html
%undefine _ssp_cflags

Summary:	Free mDNS/DNS-SD/Zeroconf implementation
Summary(pl.UTF-8):	Wolna implementacja mDNS/DNS-SD/Zeroconf
Name:		avahi
Version:	0.8
Release:	2
License:	LGPL v2.1+
Group:		Applications/Networking
#Source0Download: https://github.com/lathiat/avahi/releases
Source0:	https://github.com/lathiat/avahi/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	229c6aa30674fc43c202b22c5f8c2be7
Source1:	%{name}-daemon
Source2:	%{name}-dnsconfd
Source3:	%{name}.png
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-missing.patch
Patch2:		%{name}-destdir.patch
Patch3:		%{name}-mono-dir.patch
Patch4:		nss-mdns-package.patch
Patch5:		%{name}-dhclient_hooks.patch
Patch6:		%{name}-autoipd-sbin_ip.patch
Patch7:		%{name}-man-conditions.patch
Patch8:		%{name}-qt3.patch
Patch9:		%{name}-libevent.patch
Patch10:	%{name}-localedir.patch
URL:		http://avahi.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 0.92
%if %{with apidocs}
BuildRequires:	doxygen
# for the 'dot' tool used by doxygen
BuildRequires:	graphviz
%endif
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.12.2
BuildRequires:	gobject-introspection-devel >= 0.9.5
%if %{with gtk2}
BuildRequires:	gtk+2-devel >= 2:2.14.0
%endif
%if %{with gtk3}
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gtk+3-devel >= 3.0.0
%endif
BuildRequires:	libcap-devel
BuildRequires:	libdaemon-devel >= 0.14
%{?with_libevent:BuildRequires:	libevent-devel >= 2.0.21}
BuildRequires:	libtool
%if %{with dotnet}
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10
BuildRequires:	mono-csharp
BuildRequires:	monodoc >= 2.6
%endif
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.6
BuildRequires:	python-dbus >= 0.71
%{?with_pygobject:BuildRequires:	python-pygobject3-devel >= 3.0}
%if %{with qt3}
BuildRequires:	qt-devel >= 1:3.0
%endif
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4.0.0
BuildRequires:	qt4-build >= 4.0.0
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5.0.0
BuildRequires:	qt5-build >= 5.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.626
BuildRequires:	xmltoman
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 0.92
Requires:	libdaemon >= 0.14
Requires:	rc-scripts >= 0.4.3
Requires:	systemd-units >= 38
Suggests:	nss_mdns >= 0.10-2
Provides:	group(avahi)
Provides:	user(avahi)
Obsoletes:	avahi-systemd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Avahi is an implementation the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing. It uses D-BUS for communication
between user applications and a system daemon.

%description -l pl.UTF-8
Avahi jest implementacją specyfikacji DNS Service Discovery i
Multicast DNS dla Zeroconf Computing. Używa D-BUSa dla komunikacji
pomiędzy programami użytkownika a demonem systemowym.

%package autoipd
Summary:	IPv4LL network address configuration daemon
Summary(pl.UTF-8):	Demon configurujący adresy IPv4LL
Group:		Networking/Daemons
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Provides:	group(avahi)
Provides:	user(avahi)

%description autoipd
avahi-autoipd implements IPv4LL, "Dynamic Configuration of IPv4 Link-
Local Addresses" (IETF RFC3927), a protocol for automatic IP address
configuration from the link-local 169.254.0.0/16 range without the
need for a central server. It is primarily intended to be used in
ad-hoc networks which lack a DHCP server.

IPv4LL is part of the Zeroconf stack.

%description autoipd -l pl.UTF-8
avahi-autoipd jest implementacją IPv4LL, protokołu umożliwiającego
automatyczną konfigurację adresu z zakresu 169.254.0.0/16 bez potrzeby
użycia centralnego serwera. Jego głównym zastosowaniem są sieci
ad-hoc, w których brakuje serwera DHCP.

IPv4LL jest częścią stosu Zeroconf.

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
Requires:	gtk+2 >= 2:2.14.0

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
Requires:	%{name}-ui-devel-common = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.14.0

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

%package ui-devel-common
Summary:	Header files for Avahi UI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Avahi UI
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description ui-devel-common
Header files for Avahi UI library.

%description ui-devel-common -l pl.UTF-8
Pliki nagłówkowe biblioteki Avahi GTK+ UI.

%package ui-gtk3
Summary:	Avahi UI library - GTK+ 3.x version
Summary(pl.UTF-8):	Biblioteka Avahi UI - wersja dla GTK+ 3.x
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.28.0
Requires:	gtk+3 >= 3.0.0

%description ui-gtk3
Common GTK+ 3.x UI support library for Avahi.

%description ui-gtk3 -l pl.UTF-8
Biblioteka wspólnego interfejsu użytkownika GTK+ 3.x dla Avahi.

%package ui-gtk3-devel
Summary:	Header files for Avahi UI library - GTK+ 3.x version
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Avahi UI - wersja dla GTK+ 3.x
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ui-devel-common = %{version}-%{release}
Requires:	%{name}-ui-gtk3 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+3-devel >= 3.0.0

%description ui-gtk3-devel
Header files for Avahi GTK+ 3.x UI library.

%description ui-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Avahi GTK+ 3.x UI.

%package ui-gtk3-static
Summary:	Static Avahi UI library - GTK+ 3.x version
Summary(pl.UTF-8):	Statyczna biblioteka Avahi UI - wersja GTK+ 3.x
Group:		X11/Development/Libraries
Requires:	%{name}-ui-gtk3-devel = %{version}-%{release}

%description ui-gtk3-static
Static Avahi GTK+ 3.x UI library.

%description ui-gtk3-static -l pl.UTF-8
Statyczna biblioteka Avahi GTK+ 3.x UI.

%package compat-libdns_sd
Summary:	Avahi Bonjour compat library
Summary(pl.UTF-8):	Biblioteka Avahi zgodna z Bonjour
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
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
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.12.2

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

%package gobject
Summary:	Avahi GObject interface
Summary(pl.UTF-8):	Interfejs GObject do Avahi
Group:		Libraries
Requires:	%{name}-glib = %{version}-%{release}

%description gobject
Avahi GObject interface.

%description gobject -l pl.UTF-8
Interfejs GObject do Avahi.

%package gobject-devel
Summary:	Header files for Avahi GObject interface
Summary(pl.UTF-8):	Pliki nagłówkowe interfejsu GObject do Avahi
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}
Requires:	%{name}-gobject = %{version}-%{release}

%description gobject-devel
This is the package containing the header files for Avahi GObject
interface.

%description gobject-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe interfejsu GObject do Avahi.

%package gobject-static
Summary:	Static Avahi GObject library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi GObject
Group:		Development/Libraries
Requires:	%{name}-gobject-devel = %{version}-%{release}

%description gobject-static
Static Avahi GObject library.

%description gobject-static -l pl.UTF-8
Statyczna biblioteka Avahi GObject.

%package libevent
Summary:	Avahi libevent support library
Summary(pl.UTF-8):	Wiązania Avahi obsługująca libevent
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libevent >= 2.0.21

%description libevent
Avahi libevent support library.

%description libevent -l pl.UTF-8
Biblioteka Avahi obsługująca libevent.

%package libevent-devel
Summary:	Header files for Avahi libevent support library
Summary(pl.UTF-8):	Pliki nagłówkowe Avahi dla biblioteki obsługującej libevent
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-libevent = %{version}-%{release}
Requires:	libevent-devel >= 2.0.21

%description libevent-devel
This is the package containing the header files for Avahi libevent
library.

%description libevent-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki Avahi libevent.

%package libevent-static
Summary:	Static Avahi libevent library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi libevent
Group:		Development/Libraries
Requires:	%{name}-libevent-devel = %{version}-%{release}

%description libevent-static
Static Avahi libevent library.

%description libevent-static -l pl.UTF-8
Statyczna biblioteka Avahi libevent.

%package qt3
Summary:	Avahi Qt 3 library bindings
Summary(pl.UTF-8):	Wiązania Avahi dla biblioteki Qt 3
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Provides:	avahi-qt = %{version}-%{release}
Obsoletes:	avahi-qt < 0.8

%description qt3
Avahi Qt 3 library bindings.

%description qt3 -l pl.UTF-8
Wiązania Avahi dla biblioteki Qt 3.

%package qt3-devel
Summary:	Header files for Avahi Qt 3 library bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt3 = %{version}-%{release}
Requires:	qt-devel >= 1:3.0
Provides:	avahi-qt-devel = %{version}-%{release}
Obsoletes:	avahi-qt-devel < 0.8

%description qt3-devel
Header files for Avahi Qt 3 library bindings.

%description qt3-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 3.

%package qt3-static
Summary:	Static Avahi Qt 3 library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi Qt 3
Group:		Development/Libraries
Requires:	%{name}-qt3-devel = %{version}-%{release}
Provides:	avahi-qt-static = %{version}-%{release}
Obsoletes:	avahi-qt-static < 0.8

%description qt3-static
Static Avahi Qt 3 library.

%description qt3-static -l pl.UTF-8
Statyczna biblioteka Avahi Qt 3.

%package qt4
Summary:	Avahi Qt 4 library bindings
Summary(pl.UTF-8):	Wiązania Avahi dla biblioteki Qt 4
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Provides:	avahi-Qt = %{version}-%{release}
Obsoletes:	avahi-Qt < 0.8

%description qt4
Avahi Qt 4 library bindings.

%description qt4 -l pl.UTF-8
Wiązania Avahi dla biblioteki Qt 4.

%package qt4-devel
Summary:	Header files for Avahi Qt 4 library bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 4
Group:		Development/Libraries
Requires:	%{name}-qt4 = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	QtCore-devel >= 4.0.0
Provides:	avahi-Qt-devel = %{version}-%{release}
Obsoletes:	avahi-Qt-devel < 0.8

%description qt4-devel
Header files for Avahi Qt 4 library bindings.

%description qt4-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 4.

%package qt4-static
Summary:	Static Avahi Qt 4 library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi Qt 4
Group:		Development/Libraries
Requires:	%{name}-qt4-devel = %{version}-%{release}
Provides:	avahi-Qt-static = %{version}-%{release}
Obsoletes:	avahi-Qt-static < 0.8

%description qt4-static
Static Avahi Qt 4 library.

%description qt4-static -l pl.UTF-8
Statyczna biblioteka Avahi Qt 4.

%package qt5
Summary:	Avahi Qt 5 library bindings
Summary(pl.UTF-8):	Wiązania Avahi dla biblioteki Qt 5
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description qt5
Avahi Qt 5 library bindings.

%description qt5 -l pl.UTF-8
Wiązania Avahi dla biblioteki Qt 5.

%package qt5-devel
Summary:	Header files for Avahi Qt 5 library bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 5
Group:		Development/Libraries
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.0.0

%description qt5-devel
Header files for Avahi Qt 5 library bindings.

%description qt5-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Avahi dla biblioteki Qt 5.

%package qt5-static
Summary:	Static Avahi Qt 5 library
Summary(pl.UTF-8):	Statyczna biblioteka Avahi Qt 5
Group:		Development/Libraries
Requires:	%{name}-qt5-devel = %{version}-%{release}

%description qt5-static
Static Avahi Qt 5 library.

%description qt5-static -l pl.UTF-8
Statyczna biblioteka Avahi Qt 5.

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
Requires:	monodoc >= 2.6

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
Requires:	monodoc >= 2.6

%description -n dotnet-avahi-ui-devel
Development files for MONO Avahi UI bindings.

%description -n dotnet-avahi-ui-devel -l pl.UTF-8
Pliki rozwojowe wiązań Avahi UI dla MONO.

%package bookmarks
Summary:	Miniature web server
Summary(pl.UTF-8):	Miniaturowy serwer WWW
Group:		Applications/Networking

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
Group:		X11/Applications/Networking
Requires:	gtk+3 >= 3.0
Requires:	python-avahi = %{version}-%{release}
Requires:	python-pygobject3 >= 3.0

%description discover
A tool for enumerating all available services on the local LAN
(Python/PyGObject implementation).

%description discover -l pl.UTF-8
Narzędzie wymieniające wszystkie dostępne usługi w sieci lokalnej LAN
(implementacja oparta na szkielecie Python/PyGObject).

%package discover-standalone
Summary:	Avahi Zeroconf browser
Summary(pl.UTF-8):	Przeglądarka Zeroconf Avahi
Group:		X11/Applications/Networking
Requires:	%{name}-glib = %{version}-%{release}
%if %{with gtk3}
Requires:	gtk+3 >= 3.0.0
%else
Requires:	gtk+2 >= 2:2.14.0
%endif

%description discover-standalone
GTK+ tool for enumerating all available services on the local LAN.

%description discover-standalone -l pl.UTF-8
Narzędzie GTK+ wymieniające wszystkie dostępne usługi w sieci lokalnej
LAN.

%package bshell
Summary:	Avahi SSH/VNC servers browser
Summary(pl.UTF-8):	Przeglądarka serwerów SSH/VNC oparta na Avahi
Group:		X11/Applications/Networking
%if %{with gtk3}
Requires:	%{name}-ui-gtk3 = %{version}-%{release}
%else
Requires:	%{name}-ui = %{version}-%{release}
%endif

%description bshell
bshell/bssh/bvnc browses for SSH/VNC servers on the local network,
shows them in a GUI for the user to select one and finally calls
ssh/vncviewer after a selection was made.

%description bshell -l pl.UTF-8
bshell/bssh/bvnc pozwala przeglądać serwery SSH/VNC w sieci lokalnej,
pokazywać je w graficznym interfejsie, aby któryś wybrać i wywołać
dla niego ssh/vncviewer.

%package utils
Summary:	Avahi CLI utilities
Summary(pl.UTF-8):	Narzędzia CLI Avahi
Group:		Applications/Networking

%description utils
Command line utilities using avahi-client.

%description utils -l pl.UTF-8
Narzędzia linii poleceń korzystające z avahi-client.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%{__libtoolize}
%{__aclocal} -I common
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python} \
	--enable-compat-libdns_sd \
	--enable-compat-howl \
	%{!?with_apidocs:--disable-doxygen-doc} \
	%{?with_gtk2:--enable-gtk} \
	%{!?with_gtk3:--disable-gtk3} \
	%{!?with_pygobject:--disable-pygobject} \
	%{!?with_libevent:--disable-libevent} \
	%{!?with_dotnet:--disable-mono} \
	%{!?with_dotnet:--disable-monodoc} \
	%{?with_qt3:--enable-qt3} \
	%{?with_qt4:--enable-qt4} \
	%{!?with_qt5:--disable-qt5} \
	--disable-silent-rules \
	--disable-stack-protector \
	--with-autoipd-user=avahi \
	--with-autoipd-group=avahi \
	--with-avahi-priv-access-group=adm \
	--with-distro=none \
	--with-systemdsystemunitdir=%{systemdunitdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},/etc/rc.d/init.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitedir}

install -p %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf %{_includedir}/avahi-compat-libdns_sd/dns_sd.h \
	$RPM_BUILD_ROOT%{_includedir}/dns_sd.h

ln -sf %{_pkgconfigdir}/avahi-compat-howl.pc \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/howl.pc

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/avahi-{browse-domains,publish-address,publish-service,resolve-address,resolve-host-name}.1
echo '.so avahi-browse.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-browse-domains.1
echo '.so avahi-publish.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-publish-address.1
echo '.so avahi-publish.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-publish-service.1
echo '.so avahi-resolve.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-resolve-address.1
echo '.so avahi-resolve.1' > $RPM_BUILD_ROOT%{_mandir}/man1/avahi-resolve-host-name.1
%if %{with gtk2} || %{with gtk3}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/bvnc.1
echo '.so bssh.1' > $RPM_BUILD_ROOT%{_mandir}/man1/bvnc.1
echo '.so bssh.1' > $RPM_BUILD_ROOT%{_mandir}/man1/bshell.1
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 165 -r -f avahi
%useradd -u 165 -r -d /usr/share/empty -s /bin/false -c "Avahi daemon" -g avahi avahi

%pre autoipd
%groupadd -g 165 -r -f avahi
%useradd -u 165 -r -d /usr/share/empty -s /bin/false -c "Avahi daemon" -g avahi avahi

%post
/sbin/chkconfig --add %{name}-daemon
%service %{name}-daemon restart
/sbin/chkconfig --add %{name}-dnsconfd
%service %{name}-dnsconfd restart
%systemd_post avahi-daemon.service avahi-dnsconfd.service avahi-daemon.socket

%preun
if [ "$1" = "0" ]; then
	%service -q %{name}-dnsconfd stop
	/sbin/chkconfig --del %{name}-dnsconfd
	%service -q %{name}-daemon stop
	/sbin/chkconfig --del %{name}-daemon
fi
%systemd_preun avahi-daemon.service avahi-dnsconfd.service avahi-daemon.socket

%postun
if [ "$1" = "0" ]; then
	%userremove avahi
	%groupremove avahi
fi
%systemd_reload

%triggerpostun -- avahi < 0.6.30-7
%systemd_trigger avahi-daemon.service avahi-dnsconfd.service avahi-daemon.socket

%postun autoipd
if [ "$1" = "0" ]; then
	%userremove avahi
	%groupremove avahi
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	ui -p /sbin/ldconfig
%postun	ui -p /sbin/ldconfig

%post	ui-gtk3 -p /sbin/ldconfig
%postun	ui-gtk3 -p /sbin/ldconfig

%post	compat-libdns_sd -p /sbin/ldconfig
%postun	compat-libdns_sd -p /sbin/ldconfig

%post	compat-howl -p /sbin/ldconfig
%postun	compat-howl -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	gobject -p /sbin/ldconfig
%postun	gobject -p /sbin/ldconfig

%post	libevent -p /sbin/ldconfig
%postun	libevent -p /sbin/ldconfig

%post	qt3 -p /sbin/ldconfig
%postun	qt3 -p /sbin/ldconfig

%post	qt4 -p /sbin/ldconfig
%postun	qt4 -p /sbin/ldconfig

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/COMPAT-LAYERS docs/NEWS docs/README docs/TODO

%dir %{_sysconfdir}/avahi
%dir %{_sysconfdir}/avahi/services
%attr(755,root,root) %{_sysconfdir}/avahi/avahi-dnsconfd.action
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/avahi-daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/hosts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/services/ssh.service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/avahi/services/sftp-ssh.service
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/avahi-dbus.conf

%{systemdunitdir}/avahi-daemon.service
%{systemdunitdir}/avahi-daemon.socket
%{systemdunitdir}/avahi-dnsconfd.service
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service

%attr(755,root,root) %{_bindir}/avahi-set-host-name

%attr(755,root,root) %{_sbindir}/avahi-daemon
%attr(755,root,root) %{_sbindir}/avahi-dnsconfd
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/service-types.db
%{_datadir}/%{name}/avahi-service.dtd
%{_datadir}/dbus-1/interfaces/org.freedesktop.Avahi.*.xml

%{_mandir}/man1/avahi-set-host-name.1*
%{_mandir}/man5/avahi-daemon.conf.5*
%{_mandir}/man5/avahi.hosts.5*
%{_mandir}/man5/avahi.service.5*
%{_mandir}/man8/avahi-daemon.8*
%{_mandir}/man8/avahi-dnsconfd.8*
%{_mandir}/man8/avahi-dnsconfd.action.8*

%attr(754,root,root) /etc/rc.d/init.d/%{name}-daemon
%attr(754,root,root) /etc/rc.d/init.d/%{name}-dnsconfd

%files autoipd
%defattr(644,root,root,755)
%dir %{_sysconfdir}/avahi
%attr(755,root,root) %{_sysconfdir}/%{name}/avahi-autoipd.action
%config(noreplace) %verify(not md5 mtime size) /etc/dhclient-enter-hooks.d/avahi-autoipd
%config(noreplace) %verify(not md5 mtime size) /etc/dhclient-exit-hooks.d/avahi-autoipd
%attr(755,root,root) %{_sbindir}/avahi-autoipd
%{_mandir}/man8/avahi-autoipd.8*
%{_mandir}/man8/avahi-autoipd.action.8*

%files libs -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-client.so.3
%attr(755,root,root) %{_libdir}/libavahi-common.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-common.so.3
%attr(755,root,root) %{_libdir}/libavahi-core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-core.so.7
# common for -discover*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/interfaces

%files devel
%defattr(644,root,root,755)
%doc docs/API-CHANGES-0.6 docs/DBUS-API docs/HACKING docs/MALLOC
%attr(755,root,root) %{_libdir}/libavahi-client.so
%attr(755,root,root) %{_libdir}/libavahi-common.so
%attr(755,root,root) %{_libdir}/libavahi-core.so
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

%if %{with gtk2}
%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-ui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-ui.so.0

%files ui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-ui.so
%{_pkgconfigdir}/avahi-ui.pc

%files ui-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-ui.a
%endif

%if %{with gtk2} || %{with gtk3}
%files ui-devel-common
%defattr(644,root,root,755)
%{_includedir}/avahi-ui
%endif

%if %{with gtk3}
%files ui-gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-ui-gtk3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-ui-gtk3.so.0

%files ui-gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-ui-gtk3.so
%{_pkgconfigdir}/avahi-ui-gtk3.pc

%files ui-gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-ui-gtk3.a
%endif

%files compat-libdns_sd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdns_sd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdns_sd.so.1

%files compat-libdns_sd-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdns_sd.so
%{_includedir}/avahi-compat-libdns_sd
%{_includedir}/dns_sd.h
%{_pkgconfigdir}/avahi-compat-libdns_sd.pc

%files compat-libdns_sd-static
%defattr(644,root,root,755)
%{_libdir}/libdns_sd.a

%files compat-howl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhowl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhowl.so.0

%files compat-howl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhowl.so
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
%{_prefix}/lib/mono/avahi-sharp
%{_prefix}/lib/monodoc/sources/avahi-sharp-docs.*
%{_pkgconfigdir}/avahi-sharp.pc

%files -n dotnet-avahi-ui
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/avahi-ui-sharp

%files -n dotnet-avahi-ui-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/avahi-ui-sharp
%{_prefix}/lib/monodoc/sources/avahi-ui-sharp-docs.*
%{_pkgconfigdir}/avahi-ui-sharp.pc
%endif

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-glib.so.1

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-glib.so
%{_includedir}/avahi-glib
%{_pkgconfigdir}/avahi-glib.pc

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-glib.a

%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-gobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-gobject.so.0
%{_libdir}/girepository-1.0/Avahi-0.6.typelib
%{_libdir}/girepository-1.0/AvahiCore-0.6.typelib

%files gobject-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-gobject.so
%{_includedir}/avahi-gobject
%{_pkgconfigdir}/avahi-gobject.pc
%{_datadir}/gir-1.0/Avahi-0.6.gir
%{_datadir}/gir-1.0/AvahiCore-0.6.gir

%files gobject-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-gobject.a

%if %{with libevent}
%files libevent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-libevent.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-libevent.so.1

%files libevent-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-libevent.so
%{_includedir}/avahi-libevent
%{_pkgconfigdir}/avahi-libevent.pc

%files libevent-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-libevent.a
%endif

%if %{with qt3}
%files qt3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-qt3.so.1

%files qt3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so
%{_includedir}/avahi-qt3
%{_pkgconfigdir}/avahi-qt3.pc

%files qt3-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-qt3.a
%endif

%if %{with qt4}
%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-qt4.so.1

%files qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt4.so
%{_includedir}/avahi-qt4
%{_pkgconfigdir}/avahi-qt4.pc

%files qt4-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-qt4.a
%endif

%if %{with qt5}
%files qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavahi-qt5.so.1

%files qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavahi-qt5.so
%{_includedir}/avahi-qt5
%{_pkgconfigdir}/avahi-qt5.pc

%files qt5-static
%defattr(644,root,root,755)
%{_libdir}/libavahi-qt5.a
%endif

%files bookmarks
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-bookmarks
%{_mandir}/man1/avahi-bookmarks.1*

%if %{with pygobject}
%files discover
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-discover
%{_datadir}/%{name}/interfaces/avahi-discover.ui
%{_desktopdir}/avahi-discover.desktop
%{_pixmapsdir}/avahi.png
%{_mandir}/man1/avahi-discover.1*
%endif

%if %{with gtk2} || %{with gtk3}
%files discover-standalone
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-discover-standalone

%files bshell
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bshell
%attr(755,root,root) %{_bindir}/bssh
%attr(755,root,root) %{_bindir}/bvnc
%{_mandir}/man1/bshell.1*
%{_mandir}/man1/bssh.1*
%{_mandir}/man1/bvnc.1*
%{_desktopdir}/bssh.desktop
%{_desktopdir}/bvnc.desktop
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avahi-browse
%attr(755,root,root) %{_bindir}/avahi-browse-domains
%attr(755,root,root) %{_bindir}/avahi-publish
%attr(755,root,root) %{_bindir}/avahi-publish-address
%attr(755,root,root) %{_bindir}/avahi-publish-service
%attr(755,root,root) %{_bindir}/avahi-resolve
%attr(755,root,root) %{_bindir}/avahi-resolve-address
%attr(755,root,root) %{_bindir}/avahi-resolve-host-name
%{_mandir}/man1/avahi-browse.1*
%{_mandir}/man1/avahi-browse-domains.1*
%{_mandir}/man1/avahi-publish.1*
%{_mandir}/man1/avahi-publish-address.1*
%{_mandir}/man1/avahi-publish-service.1*
%{_mandir}/man1/avahi-resolve.1*
%{_mandir}/man1/avahi-resolve-address.1*
%{_mandir}/man1/avahi-resolve-host-name.1*
