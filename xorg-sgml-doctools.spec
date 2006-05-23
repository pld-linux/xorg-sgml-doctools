Summary:	Shared entity definitions for XFree86/X.org documentation
Summary(pl):	Wspó³dzielone definicje encji dla dokumentacji XFree86/X.org
Name:		xorg-sgml-doctools
Version:	1.1
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.bz2
# Source0-md5:	b4166e6638c506fd886aaf25c3777a3d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared entity definitions for XFree86/X.org documentation.

%description -l pl
Wspó³dzielone definicje encji dla dokumentacji XFree86/X.org.

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
%doc ChangeLog
%{_datadir}/X11/sgml
