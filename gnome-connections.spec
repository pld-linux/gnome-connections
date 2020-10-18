Summary:	Remote desktop client for the GNOME desktop environment
Summary(pl.UTF-8):	Klient zdalnego pulpitu dla środowiska graficznego GNOME
Name:		gnome-connections
Version:	3.38.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/connections/3.38/connections-%{version}.tar.xz
# Source0-md5:	3d6d331c06953fc08d0dbe045fd60d2d
URL:		https://wiki.gnome.org/Apps/Connections
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gtk-frdp-devel >= 0.1
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk3-vnc-devel >= 0.4.5
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	vala-gtk-frdp >= 0.1
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.50
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.50
Requires:	gtk+3 >= 3.22
Requires:	gtk3-vnc >= 0.4.5
Requires:	hicolor-icon-theme
Requires:	libxml2 >= 1:2.7.8
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remote desktop client for the GNOME desktop environment. It aims at
replacing Vinagre.

%description -l pl.UTF-8
Klient zdalnego pulpitu dla środowiska graficznego GNOME. Celem jest
zastąpienie Vinagre.

%prep
%setup -q -n connections-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang connections

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database

%postun
%glib_compile_schemas
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database

%files -f connections.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/connections
%{_datadir}/appdata/org.gnome.Connections.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Connections.service
%{_datadir}/glib-2.0/schemas/org.gnome.Connections.gschema.xml
%{_datadir}/mime/packages/org.gnome.Connections.xml
%{_desktopdir}/org.gnome.Connections.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Connections.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Connections.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Connections-symbolic.svg
