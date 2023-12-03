%define major 6
%define libname %mklibname KPim6Tnef
%define devname %mklibname KPim6Tnef -d

Summary:	KTNEF - an API for handling TNEF data
Name:		plasma6-ktnef
Version:	24.01.80
Release:	1
License:	GPLv2+
Group:		System/Base
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/ktnef-%{version}.tar.xz
URL:		https://www.kde.org/
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	doxygen
BuildRequires:	qt6-qttools-assistant
Requires:	%{libname} >= %{version}

%description
KTNEF - an API for handling TNEF data.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	KTNEF - an API for handling TNEF data
Group:		System/Libraries
Requires:	%{name} >= %{version}

%description -n %{libname}
KTNEF - an API for handling TNEF data.

%files -n %{libname}
%{_libdir}/libKPim6Tnef.so*

#--------------------------------------------------------------------

%package -n %{devname}

Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname kf6tnef -d} < 3:17.04.0
Provides:	%{mklibname kf6tnef -d} = 3:17.04.0

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KPim6/KTNEF
%{_libdir}/cmake/KPim6Tnef

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n ktnef-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libktnef5

%files -f libktnef5.lang
%{_datadir}/qlogging-categories6/ktnef.categories
%{_datadir}/qlogging-categories6/ktnef.renamecategories
