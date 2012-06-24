#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Shellish
Summary:	Regexp::Shellish Perl module - shell-like regular expressions
Summary(pl):	Modu� Perla Regexp::Shellish - wyra�enia regularne podobne do rozwini�� wykonywanych przez pow�oki
Name:		perl-Regexp-Shellish
Version:	0.93
Release:	4
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5f92bf82b3d5033518e6d2c1028ee37
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Shellish module provides shell-like regular expressions. The
wildcards provided are '?', '*' and '**', where '**' is like '*' but
matches '/'.

%description -l pl
Modu� Regexp::Shellish udost�pnia wyra�enia regularne podobne do
rozwini�� wykonywanych przez pow�oki. Dost�pne maski to: '?', '*' i
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
