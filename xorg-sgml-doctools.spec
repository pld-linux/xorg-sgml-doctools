Summary:	Shared entity definitions for XFree86/X.org documentation
Summary(pl.UTF-8):	Współdzielone definicje encji dla dokumentacji XFree86/X.org
Name:		xorg-sgml-doctools
Version:	1.12
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	https://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.bz2
# Source0-md5:	748e4fdc384bb5ff8e7bfd82d31548c3
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	docbook-style-xsl-nons >= 1.77
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a common set of SGML entities and XML/CSS style
sheets used in building/formatting the documentation provided in other
X.Org packages. It's typically only needed by people building from
source who want to produce formatted documentation from their builds.

%description -l pl.UTF-8
Ten pakiet udostępnia wspólny zbiór encji SGML oraz arkuszy stylów
XML/CSS używanych przy budowaniu/formatowaniu dokumentacji dołączonej
do pakietów X.Org. Zwykle jest potrzebny tylko przy budowaniu ze
źródeł, jeśli w efekcie ma być utworzona sformatowana dokumentacja.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_datadir}/sgml/X11
%{_npkgconfigdir}/xorg-sgml-doctools.pc
