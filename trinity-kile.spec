%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg kile
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		2.0.3
Release:		%{?tde_version:%{tde_version}_}3
Summary:		TDE Integrated LaTeX Environment [Trinity]
Group:			Applications/Publishing
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/office/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:  	cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:  trinity-tde-cmake >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes: %{name}-i18n-ar < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-bg < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-br < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ca < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-cs < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-cy < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-da < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-de < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-el < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-engb < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-es < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-et < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-eu < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-fi < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-fr < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ga < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-gl < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-hi < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-hu < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-is < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-it < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ja < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-lt < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ms < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-mt < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-nb < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-nds < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-nl < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-nn < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-pa < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-pl < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-pt < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ptbr < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ro < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ru < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-rw < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-sk < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-sr < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-srlatin < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-sv < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ta < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-th < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-tr < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-uk < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-zhcn < %{?epoch:%{epoch}:}%{version}-%{release}


%description
Kile is a user-friendly LaTeX source editor and TeX shell for TDE.

The source editor is a multi-document editor designed for .tex and .bib
files.  Menus, wizards and auto-completion are provided to assist with
tag insertion and code generation.  A structural view of the document
assists with navigation within source files.

The TeX shell integrates the various tools required for TeX processing.
It assists with LaTeX compilation, DVI and postscript document viewing,
generation of bibliographies and indices and other common tasks.

Kile can support large projects consisting of several smaller files.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_prefix}/bin/kile
%{tde_prefix}/share/applications/tde/kile.desktop
%{tde_prefix}/share/apps/tdeconf_update
%{tde_prefix}/share/apps/kile
%{tde_prefix}/share/config.kcfg/kile.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kile.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kile.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kile
%{tde_prefix}/share/mimelnk/text/x-kilepr.desktop

%lang(da) %{tde_prefix}/share/doc/tde/HTML/da/kile/
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/kile/
%lang(et) %{tde_prefix}/share/doc/tde/HTML/et/kile/
%lang(it) %{tde_prefix}/share/doc/tde/HTML/it/kile/
%lang(nl) %{tde_prefix}/share/doc/tde/HTML/nl/kile/
%lang(pt) %{tde_prefix}/share/doc/tde/HTML/pt/kile/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/kile/

%{tde_prefix}/share/man/man1/kile.1*

