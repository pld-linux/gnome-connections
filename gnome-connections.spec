#
# Conditional build:
%bcond_with	system_gtk_frdp	# system gtk-frdp library [3.37.1 tag is too old]

Summary:	Remote desktop client for the GNOME desktop environment
Summary(pl.UTF-8):	Klient zdalnego pulpitu dla środowiska graficznego GNOME
Name:		gnome-connections
Version:	47.2.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	https://download.gnome.org/sources/gnome-connections/47/%{name}-%{version}.tar.xz
# Source0-md5:	f86afd80e97cc7d99e14217f13c51081
URL:		https://apps.gnome.org/Connections/
# freerdp3 preferred, with fallback to freerdp2
%{!?with_system_gtk_frdp:BuildRequires:	freerdp3-devel >= 3.0.0}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50
%{?with_system_gtk_frdp:BuildRequires:	gtk-frdp-devel >= 0.2}
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk3-vnc-devel >= 0.4.5
%{!?with_system_gtk_frdp:BuildRequires:	libfuse3-devel >= 3.9.1}
BuildRequires:	libgvnc-devel >= 0.4.5
BuildRequires:	libhandy1-devel >= 1.6.0
BuildRequires:	libsecret-devel
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
%{?with_system_gtk_frdp:BuildRequires:	vala-gtk-frdp >= 0.2}
BuildRequires:	vala-gtk3-vnc >= 0.4.5
BuildRequires:	vala-libhandy1 >= 1.6.0
BuildRequires:	vala-libsecret
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.50
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.50
Requires:	gtk+3 >= 3.22
Requires:	gtk3-vnc >= 0.4.5
Requires:	hicolor-icon-theme
Requires:	libgvnc >= 0.4.5
Requires:	libhandy1 >= 1.6.0
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
%setup -q

%if %{without system_gtk_frdp}
%{__sed} -i -e '/dependency.*gtk-frdp-0.2/ s/gtk-frdp-0.2/gtk-frdp-nonexistent/' src/meson.build
%endif

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{without system_gtk_frdp}
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/gnome-connections/gtk-frdp
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-connections/pkgconfig/gtk-frdp-0.2.pc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/gnome-connections/vapi/gtk-frdp-0.2.*
%endif

%find_lang %{name} --with-gnome

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-connections
%{_datadir}/dbus-1/services/org.gnome.Connections.service
%{_datadir}/glib-2.0/schemas/org.gnome.Connections.gschema.xml
%{_datadir}/metainfo/org.gnome.Connections.appdata.xml
%{_datadir}/mime/packages/org.gnome.Connections.xml
%{_desktopdir}/org.gnome.Connections.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Connections.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Connections-symbolic.svg
%if %{without system_gtk_frdp}
%dir %{_libdir}/gnome-connections
%attr(755,root,root) %{_libdir}/gnome-connections/libgtk-frdp-0.2.so
%{_libdir}/gnome-connections/girepository-1.0
%dir %{_datadir}/gnome-connections
%{_datadir}/gnome-connections/gir-1.0
%endif
