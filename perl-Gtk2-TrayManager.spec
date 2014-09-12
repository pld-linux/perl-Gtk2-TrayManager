#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	TrayManager
Summary:	Gtk2::TrayManager - Perl bindings for EggTrayManager
Summary(pl.UTF-8):	Gtk2::TrayManager - Dowiązania Perla dla EggTrayManager
Name:		perl-Gtk2-TrayManager
Version:	0.05
Release:	6
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	88cf41ab0d72572ac3d2e9ab9b3ab8f0
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	perl-Glib >= 1.00
BuildRequires:	perl-Gtk2 >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk2::TrayManager allows a Perl developer to create notification area
applications.

%description -l pl.UTF-8
Gtk2::TrayManager pozwala programistom perlowym na tworzenie programów
wykorzystujących obszar powiadamiania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/TrayManager.pm
%dir %{perl_vendorarch}/Gtk2/TrayManager
%{perl_vendorarch}/Gtk2/TrayManager/Install
%dir %{perl_vendorarch}/auto/Gtk2/TrayManager
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/TrayManager/*.so
%{_mandir}/man3/*
