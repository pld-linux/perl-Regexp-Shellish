#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Regexp
%define		pnam	Shellish
Summary:	Regexp::Shellish Perl module - shell-like regular expressions
Summary(pl.UTF-8):	Moduł Perla Regexp::Shellish - wyrażenia regularne podobne do rozwinięć wykonywanych przez powłoki
Name:		perl-Regexp-Shellish
Version:	0.93
Release:	5
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5f92bf82b3d5033518e6d2c1028ee37
URL:		http://search.cpan.org/dist/Regexp-Shellish/
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Shellish module provides shell-like regular expressions. The
wildcards provided are '?', '*' and '**', where '**' is like '*' but
matches '/'.

%description -l pl.UTF-8
Moduł Regexp::Shellish udostępnia wyrażenia regularne podobne do
rozwinięć wykonywanych przez powłoki. Dostępne maski to: '?', '*' i
'**', gdzie '**' jest podobna do '*', ale obejmuje znaki '/'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
