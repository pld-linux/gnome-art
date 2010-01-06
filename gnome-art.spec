Summary:	A frontend for art.gnome.org
Summary(pl.UTF-8):	Frontend do art.gnome.org
Name:		gnome-art
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.miketech.net/gnome-art/download/%{name}-%{version}.tar.gz
# Source0-md5:	4dd59ba8a84efe8dcb5637ba051394e7
Source1:	%{name}.desktop
Source2:	gnome-splashscreen-manager.desktop
URL:		http://www.miketech.net/gnome-art/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1.8.2
BuildRequires:	ruby-modules
Requires:	ruby-gnome2 >= 0.12.0
Requires:	ruby-rbogl
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Art is the graphical frontend for art.gnome.org. Backgrounds and
all themes can be downloaded and previewed. Backgrounds, icon themes
and splash screens can be installed directly. GNOME Splash Screen
Manager is for managing the splash screens of the GNOME desktop.

%description -l pl.UTF-8
GNOME Art to graficzny interfejs do art.gnome.org. Pozwala podglądać i
ściągać tła oraz wszystkie motywy. Można bezpośrednio instalować tła,
motywy ikon i ekrany startowe. GNOME Splash Screen Manager służy do
zarządzania ekranami startowymi środowiska GNOME.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}/gnome-art/ui
install -d $RPM_BUILD_ROOT%{_datadir}/gnome-art/glade
install -d $RPM_BUILD_ROOT%{_datadir}/gnome-art/images
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}/gnome-splashscreen-manager/ui
install -d $RPM_BUILD_ROOT%{_datadir}/gnome-splashscreen-manager/glade
install -d $RPM_BUILD_ROOT%{_desktopdir}

install gnome-art/bin/gnome-art $RPM_BUILD_ROOT%{_bindir}
install gnome-art/lib/gnome_art.rb $RPM_BUILD_ROOT%{ruby_rubylibdir}
install gnome-art/lib/gnome-art/*.rb \
    $RPM_BUILD_ROOT%{ruby_rubylibdir}/gnome-art
install gnome-art/lib/gnome-art/ui/*.rb \
    $RPM_BUILD_ROOT%{ruby_rubylibdir}/gnome-art/ui
install gnome-art/data/gnome-art/glade/*.glade \
    $RPM_BUILD_ROOT%{_datadir}/gnome-art/glade
install gnome-art/data/gnome-art/glade/*.png \
    $RPM_BUILD_ROOT%{_datadir}/gnome-art/glade
install gnome-art/data/gnome-art/images/*.png \
    $RPM_BUILD_ROOT%{_datadir}/gnome-art/images

install gnome-splashscreen-manager/bin/gnome-splashscreen-manager \
    $RPM_BUILD_ROOT%{_bindir}
install gnome-splashscreen-manager/lib/gnome_splashscreen_manager.rb \
    $RPM_BUILD_ROOT%{ruby_rubylibdir}
install gnome-splashscreen-manager/lib/gnome-splashscreen-manager/*.rb \
    $RPM_BUILD_ROOT%{ruby_rubylibdir}/gnome-splashscreen-manager
install gnome-splashscreen-manager/lib/gnome-splashscreen-manager/ui/*.rb \
    $RPM_BUILD_ROOT%{ruby_rubylibdir}/gnome-splashscreen-manager/ui
install gnome-splashscreen-manager/data/gnome-splashscreen-manager/glade/*.glade \
    $RPM_BUILD_ROOT%{_datadir}/gnome-splashscreen-manager/glade
install gnome-splashscreen-manager/data/gnome-splashscreen-manager/glade/*.png \
    $RPM_BUILD_ROOT%{_datadir}/gnome-splashscreen-manager/glade

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%dir %{ruby_rubylibdir}/gnome-art
%{ruby_rubylibdir}/gnome-art/*.rb
%dir %{ruby_rubylibdir}/gnome-art/ui
%{ruby_rubylibdir}/gnome-art/ui/*.rb
%dir %{ruby_rubylibdir}/gnome-splashscreen-manager
%{ruby_rubylibdir}/gnome-splashscreen-manager/*.rb
%dir %{ruby_rubylibdir}/gnome-splashscreen-manager/ui
%{ruby_rubylibdir}/gnome-splashscreen-manager/ui/*.rb
%dir %{_datadir}/gnome-art
%dir %{_datadir}/gnome-art/glade
%{_datadir}/gnome-art/glade/*.glade
%{_datadir}/gnome-art/glade/*.png
%dir %{_datadir}/gnome-art/images
%{_datadir}/gnome-art/images/*.png
%dir %{_datadir}/gnome-splashscreen-manager
%dir %{_datadir}/gnome-splashscreen-manager/glade
%{_datadir}/gnome-splashscreen-manager/glade/*.glade
%{_datadir}/gnome-splashscreen-manager/glade/*.png
%{_desktopdir}/*.desktop
