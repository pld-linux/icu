Summary:	International Components for Unicode
Summary(pl):	Miêdzynarodowe komponenty dla unikodu
Name:		icu
Version:	3.2
Release:	1
License:	X License
Group:		Libraries
Source0:	ftp://www-126.ibm.com/pub/icu/%{version}/%{name}-%{version}.tgz
# Source0-md5:	55a85d2365338ece483d275119fd990c
URL:		http://oss.software.ibm.com/icu/
BuildRequires:	automake
BuildRequires:	libstdc++-devel
Requires:	libicu = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides
calendar support, conversions for many character sets, language
sensitive collation, date and time formatting, support for many
locales, message catalogs and resources, message formatting,
normalization, number and currency formatting, time zones support,
transliteration, word, line and sentence breaking, etc.

This package contains the Unicode character database and derived
properties, along with converters and time zones data.

%description -l pl
ICU jest grup± bibliotek C i C++, które dostarczaj± kompletn± i pe³n±
obs³ugê Unikodu i lokalizacji. Biblioteka dostarcza obs³ugê
kalendarza, konwersje dla wielu zestawów znaków, sortowanie zale¿ne od
jêzyka, formatowanie daty i czasu, wsparcie dla wielu lokalizacji,
katalogów komunikatów i zasobów, formatowanie komunikatów,
normalizacjê, formatowanie liczb i walut, obs³ugê stref czasowych,
transliteracjê, ³amanie s³ów, linii i zdañ itp.

Ten pakiet zawiera bazê znaków unikodowych i pochodne w³asno¶ci wraz
z konwerterami i danymi stref czasowych.

%package -n libicu
Summary:	International Components for Unicode (libraries)
Summary(pl):	Miêdzynarodowe Komponenty dla Unikodu (biblioteki)
Group:		Development/Libraries
Obsoletes:	libicu30

%description -n libicu
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the runtime
libraries for ICU. It does not contain any of the data files needed at
runtime and present in the `icu' and `icu-locales` packages.

%description -n libicu -l pl
ICU jest grup± bibliotek C i C++, które dostarczaj± kompletn± i pe³n±
obs³ugê Unikodu i lokalizacji. Ten pakiet zawiera biblioteki
uruchomieniowe ICU. Nie zawiera ¿adnych plików z danymi potrzebnymi w
czasie dzia³ania i obecnymi w pakietach "icu" i "icu-locales".

%package -n libicu-devel
Summary:	International Components for Unicode (development files)
Summary(pl):	Miêdzynarodowe komponenty dla Unikodu (pliki dla programistów)
Group:		Development/Libraries
Requires:	libicu = %{version}-%{release}

%description -n libicu-devel
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the development
files for ICU.

%description -n libicu-devel -l pl
ICU jest grup± bibliotek C i C++, które dostarczaj± kompletn± i pe³n±
obs³ugê Unikodu i lokalizacji. Ten pakiet zawiera pliki
programistyczne ICU.

%prep
%setup -q -n %{name}

%build
cd source
cp -f /usr/share/automake/config.* .
%configure2_13 \
	--disable-samples

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT

# help rpm to generate deps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libicu -p /sbin/ldconfig
%postun	-n libicu -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc license.html readme.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/mkinstalldirs
%{_mandir}/man1/*
%{_mandir}/man8/*

%files -n libicu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/icu
%dir %{_libdir}/icu/current
%dir %{_libdir}/icu/%{version}

%files -n libicu-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/unicode
%dir %{_includedir}/layout
%{_includedir}/unicode/*.h
%{_includedir}/layout/*.h
%{_libdir}/%{name}/Makefile.inc
%{_libdir}/%{name}/%{version}/Makefile.inc
%{_datadir}/%{name}/%{version}/config
