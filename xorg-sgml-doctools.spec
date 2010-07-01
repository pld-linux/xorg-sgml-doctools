Summary:	Shared entity definitions for XFree86/X.org documentation
Summary(pl.UTF-8):	Współdzielone definicje encji dla dokumentacji XFree86/X.org
Name:		xorg-sgml-doctools
Version:	1.5
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.bz2
# Source0-md5:	1cd2d8213ee71ebdbefce45c9da54762
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	xorg-util-util-macros >= 1.3
# just for dir
Requires:	sgml-common
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
%setup -q -n %{name}-%{version}

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
%doc COPYING ChangeLog README
%{_datadir}/sgml/X11
%{_npkgconfigdir}/xorg-sgml-doctools.pc
