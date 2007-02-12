Summary:	International Components for Unicode
Summary(pl.UTF-8):   Międzynarodowe komponenty dla unikodu
Name:		icu
Version:	3.4.1
Release:	2
License:	X License
Group:		Libraries
Source0:	ftp://ftp.software.ibm.com/software/globalization/icu/%{version}/%{name}-%{version}.tgz
# Source0-md5:	2a16f58bcb26e5010c946dca9ec08d5f
URL:		http://www.ibm.com/software/globalization/icu/
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

%description -l pl.UTF-8
ICU jest grupą bibliotek C i C++, które dostarczają kompletną i pełną
obsługę Unikodu i lokalizacji. Biblioteka dostarcza obsługę
kalendarza, konwersje dla wielu zestawów znaków, sortowanie zależne od
języka, formatowanie daty i czasu, wsparcie dla wielu lokalizacji,
katalogów komunikatów i zasobów, formatowanie komunikatów,
normalizację, formatowanie liczb i walut, obsługę stref czasowych,
transliterację, łamanie słów, linii i zdań itp.

Ten pakiet zawiera bazę znaków unikodowych i pochodne własności wraz z
konwerterami i danymi stref czasowych.

%package -n libicu
Summary:	International Components for Unicode (libraries)
Summary(pl.UTF-8):   Międzynarodowe Komponenty dla Unikodu (biblioteki)
Group:		Development/Libraries
Obsoletes:	libicu30

%description -n libicu
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the runtime
libraries for ICU. It does not contain any of the data files needed at
runtime and present in the `icu' and `icu-locales` packages.

%description -n libicu -l pl.UTF-8
ICU jest grupą bibliotek C i C++, które dostarczają kompletną i pełną
obsługę Unikodu i lokalizacji. Ten pakiet zawiera biblioteki
uruchomieniowe ICU. Nie zawiera żadnych plików z danymi potrzebnymi w
czasie działania i obecnymi w pakietach "icu" i "icu-locales".

%package -n libicu-devel
Summary:	International Components for Unicode (development files)
Summary(pl.UTF-8):   Międzynarodowe komponenty dla Unikodu (pliki dla programistów)
Group:		Development/Libraries
Requires:	libicu = %{version}-%{release}

%description -n libicu-devel
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the development
files for ICU.

%description -n libicu-devel -l pl.UTF-8
ICU jest grupą bibliotek C i C++, które dostarczają kompletną i pełną
obsługę Unikodu i lokalizacji. Ten pakiet zawiera pliki
programistyczne ICU.

%prep
%setup -q -n %{name}

%build
cd source
cp -f /usr/share/automake/config.* .
%configure2_13 \
	--sbindir=%{_bindir} \
	--disable-samples

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT

# help rpm to generate deps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

rm -f $RPM_BUILD_ROOT%{_datadir}/icu/%{version}/license.html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libicu -p /sbin/ldconfig
%postun	-n libicu -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc license.html readme.html
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/icu-config
%{_mandir}/man1/*
%{_mandir}/man8/*
%exclude %{_mandir}/man1/icu-config.1*

%files -n libicu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files -n libicu-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/icu-config
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/unicode
%dir %{_includedir}/layout
%{_includedir}/unicode/*.h
%{_includedir}/layout/*.h
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/Makefile.inc
%dir %{_libdir}/%{name}/current
%dir %{_libdir}/%{name}/%{version}
%{_libdir}/%{name}/%{version}/Makefile.inc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/config
%attr(755,root,root) %{_datadir}/%{name}/%{version}/mkinstalldirs
%{_mandir}/man1/icu-config.1*
