Summary:	Open Source implementation of Audio Processing Technology codec (aptX)
Summary(pl.UTF-8):	Otwarta implementacja kodeka Audio Processing Technology (aptX)
Name:		libopenaptx
Version:	0.2.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/pali/libopenaptx/releases
Source0:	https://github.com/pali/libopenaptx/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	07c36ca8597195081a8c11ed258fdbbc
Patch0:		%{name}-norpath.patch
URL:		https://github.com/pali/libopenaptx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Open Source implementation of Audio Processing Technology
codec (aptX) derived from ffmpeg 4.0 project and licensed under LGPL
v2.1+. This codec is mainly used in Bluetooth A2DP profile.

%description -l pl.UTF-8
Ten pakiet zawiera mającą otwarte źródła implementację kodeka Audio
Processing Technology (aptX), wywodzącą się z projektu ffmpeg 4.0 i
udostępnioną na licencji LGPL w wersji 2.1+. Kodek jest używany
głównie w profilu Bluetooth A2DP.

%package devel
Summary:	Header files for openaptx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki openaptx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for openaptx library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki openaptx.

%package static
Summary:	Static openaptx library
Summary(pl.UTF-8):	Statyczna biblioteka openaptx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static openaptx library.

%description static -l pl.UTF-8
Statyczna biblioteka openaptx.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -W -Wall" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/openaptxdec
%attr(755,root,root) %{_bindir}/openaptxenc
%attr(755,root,root) %{_libdir}/libopenaptx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenaptx.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenaptx.so
%{_includedir}/openaptx.h
%{_pkgconfigdir}/libopenaptx.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenaptx.a
