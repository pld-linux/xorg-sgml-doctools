Summary:	Shared entity definitions for XFree86/X.org documentation
Summary(pl.UTF-8):	Współdzielone definicje encji dla dokumentacji XFree86/X.org
Name:		xorg-sgml-doctools
Version:	1.3
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.bz2
# Source0-md5:	1e3ee108688d1df91049a565813c973d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
# just for dir
Requires:	sgml-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared entity definitions for XFree86/X.org documentation.

%description -l pl.UTF-8
Współdzielone definicje encji dla dokumentacji XFree86/X.org.

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
%{_datadir}/sgml/X11
