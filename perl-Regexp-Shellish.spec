%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Shellish
Summary:	Regexp::Shellish perl module - Shell-like regular expressions
Summary(pl):	Modu³ perla Regexp::Shellish - shellopodobne wyra¿enia regularne
Name:		perl-Regexp-Shellish
Version:	0.93
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5f92bf82b3d5033518e6d2c1028ee37
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Shellish module provides shell-like regular expressions. The
wildcards provided are '?', '*' and '**', where '**' is like '*' but
matches '/'.

%description -l pl
Modu³ Regexp::Shellish udostêpnia shellopodobne wyra¿enia regularne.
Dostêpne maski to: '?', '*' i '**', gdzie '**' jest podobna do '*',
ale obejmuje znaki '/'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Regexp/Shellish.pm
%{_mandir}/man3/*
