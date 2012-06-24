Summary:	International Components for Unicode
Summary(pl):	Mi�dzynarodowe komponenty dla unikodu
Name:		icu
Version:	3.0
Release:	0.1
License:	X License
Group:		Libraries
#Source0:	ftp://www-126.ibm.com/pub/%{name}/%{version}/%{name}-%{version}.tgz
Source0:	icu-3.0.tgz
# Source0-md5:	f66c1e6f4622a2d880a5f056d86b5a38
URL:		http://oss.software.ibm.com/icu/
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
ICU jest grup� bibliotek C i C++, kt�re dostarczaj� kompletn� i pe�n�
obs�ug� Unikodu i lokalizacji. Biblioteka dostarcza obs�ug�
kalendarza, konwersje dla wielu zestaw�w znak�w, sortowanie zale�ne od
j�zyka, formatowanie daty i czasu, wsparcie dla wielu lokalizacji,
katalog�w komunikat�w i zasob�w, formatowanie komunikat�w,
normalizacj�, formatowanie liczb i walut, obs�ug� stref czasowych,
transliteracj�, �amanie s��w, linii i zda� itp.

Ten pakiet zawiera baz� znak�w unikodowych i pochodne w�asno�ci wraz
z konwerterami i danymi stref czasowych.

%package -n libicu
Summary:	International Components for Unicode (libraries)
Summary(pl):	Mi�dzynarodowe Komponenty dla Unikodu (biblioteki)
Group:		Development/Libraries
Obsoletes:	libicu30

%description -n libicu
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the runtime
libraries for ICU. It does not contain any of the data files needed at
runtime and present in the `icu' and `icu-locales` packages.

%description -n libicu -l pl
ICU jest grup� bibliotek C i C++, kt�re dostarczaj� kompletn� i pe�n�
obs�ug� Unikodu i lokalizacji. Ten pakiet zawiera biblioteki
uruchomieniowe ICU. Nie zawiera �adnych plik�w z danymi potrzebnymi w
czasie dzia�ania i obecnymi w pakietach "icu" i "icu-locales".

%package -n libicu-devel
Summary:	International Components for Unicode (development files)
Summary(pl):	Mi�dzynarodowe komponenty dla Unikodu (pliki dla programist�w)
Group:		Development/Libraries
Requires:	libicu = %{version}-%{release}

%description -n libicu-devel
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the development
files for ICU.

%description -n libicu-devel -l pl
ICU jest grup� bibliotek C i C++, kt�re dostarczaj� kompletn� i pe�n�
obs�ug� Unikodu i lokalizacji. Ten pakiet zawiera pliki
programistyczne ICU.

%package locales
Summary:	Locale data for ICU
Summary(pl):	Pliki lokalizacyjne dla ICU
Group:		Libraries
Requires:	libicu = %{version}-%{release}

%description locales
The locale data are used by ICU to provide localization (l10n),
internationalization (i18n) and timezone support to ICU applications.
This package also contains break data for various languages, and
transliteration data.

%description locales -l pl
Dane lokalizacji s� u�ywane przez ICU do zapewnienia lokalizacji
(l10n), internacjonalizacji (i18n) i obs�ugi stref czasowych dla
aplikacji ICU. Ten pakiet zawiera tak�e dane dotycz�ce �amania tekstu
dla r�nych j�zyk�w oraz dane dla transliteracji.

%prep
%setup -q -n %{name}

%build
cd source
echo 'CPPFLAGS += -DICU_DATA_DIR=\"%{_datadir}/%{name}/%{version}\"' >> icudefs.mk
%configure2_13 \
    --disable-tests \
    --disable-samples \
    --with-data-packaging=files

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd source
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.html readme.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{version}/mkinstalldirs
%{_datadir}/%{name}/%{version}/icudt30l/*.cnv
%{_datadir}/%{name}/%{version}/icudt30l/*.icu
%{_datadir}/%{name}/%{version}/icudt30l/*.spp
%{_mandir}/man1/*
%{_mandir}/man8/*


%files locales
%{_datadir}/%{name}/%{version}/icudt30l/*.brk
%{_datadir}/%{name}/%{version}/icudt30l/*.res
%{_datadir}/%{name}/%{version}/icudt30l/coll/*.res


%files -n libicu
%{_libdir}/*


%files -n libicu-devel
%dir %{_includedir}/unicode
%dir %{_includedir}/layout
%{_includedir}/unicode/*.h
%{_includedir}/layout/*.h
%{_libdir}/%{name}/%{version}/Makefile.inc
%{_datadir}/%{name}/%{version}/config
