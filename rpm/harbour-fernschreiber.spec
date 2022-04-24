# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-fernschreiber

# >> macros
%define __provides_exclude_from ^%{_datadir}/.*$
%define __requires_exclude ^libtdjson.*$
# << macros

Summary:    Fernschreiber is a Telegram client for Sailfish OS
Version:    0.14
Release:    2
Group:      Qt/Qt
License:    LICENSE
URL:        http://werkwolf.eu/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-fernschreiber.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(nemonotifications-qt5)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  gperf
BuildRequires:  desktop-file-utils

%description
Fernschreiber is a Telegram client for Sailfish OS


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
