%bcond clang 1

# TDE variables
%define tde_pkg kile
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		14.1.6
Release:		1
Summary:		TDE Integrated LaTeX Environment [Trinity]
Group:			Applications/Publishing
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/office/%{tarball_name}-%{version}.tar.xz

BuildSystem:  	cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:  trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes: %{name}-i18n-ar < %{EVRD}
Obsoletes: %{name}-i18n-bg < %{EVRD}
Obsoletes: %{name}-i18n-br < %{EVRD}
Obsoletes: %{name}-i18n-ca < %{EVRD}
Obsoletes: %{name}-i18n-cs < %{EVRD}
Obsoletes: %{name}-i18n-cy < %{EVRD}
Obsoletes: %{name}-i18n-da < %{EVRD}
Obsoletes: %{name}-i18n-de < %{EVRD}
Obsoletes: %{name}-i18n-el < %{EVRD}
Obsoletes: %{name}-i18n-engb < %{EVRD}
Obsoletes: %{name}-i18n-es < %{EVRD}
Obsoletes: %{name}-i18n-et < %{EVRD}
Obsoletes: %{name}-i18n-eu < %{EVRD}
Obsoletes: %{name}-i18n-fi < %{EVRD}
Obsoletes: %{name}-i18n-fr < %{EVRD}
Obsoletes: %{name}-i18n-ga < %{EVRD}
Obsoletes: %{name}-i18n-gl < %{EVRD}
Obsoletes: %{name}-i18n-hi < %{EVRD}
Obsoletes: %{name}-i18n-hu < %{EVRD}
Obsoletes: %{name}-i18n-is < %{EVRD}
Obsoletes: %{name}-i18n-it < %{EVRD}
Obsoletes: %{name}-i18n-ja < %{EVRD}
Obsoletes: %{name}-i18n-lt < %{EVRD}
Obsoletes: %{name}-i18n-ms < %{EVRD}
Obsoletes: %{name}-i18n-mt < %{EVRD}
Obsoletes: %{name}-i18n-nb < %{EVRD}
Obsoletes: %{name}-i18n-nds < %{EVRD}
Obsoletes: %{name}-i18n-nl < %{EVRD}
Obsoletes: %{name}-i18n-nn < %{EVRD}
Obsoletes: %{name}-i18n-pa < %{EVRD}
Obsoletes: %{name}-i18n-pl < %{EVRD}
Obsoletes: %{name}-i18n-pt < %{EVRD}
Obsoletes: %{name}-i18n-ptbr < %{EVRD}
Obsoletes: %{name}-i18n-ro < %{EVRD}
Obsoletes: %{name}-i18n-ru < %{EVRD}
Obsoletes: %{name}-i18n-rw < %{EVRD}
Obsoletes: %{name}-i18n-sk < %{EVRD}
Obsoletes: %{name}-i18n-sr < %{EVRD}
Obsoletes: %{name}-i18n-srlatin < %{EVRD}
Obsoletes: %{name}-i18n-sv < %{EVRD}
Obsoletes: %{name}-i18n-ta < %{EVRD}
Obsoletes: %{name}-i18n-th < %{EVRD}
Obsoletes: %{name}-i18n-tr < %{EVRD}
Obsoletes: %{name}-i18n-uk < %{EVRD}
Obsoletes: %{name}-i18n-zhcn < %{EVRD}


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

