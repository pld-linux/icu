Summary:	International Components for Unicode
Summary(pl):	Mi�dzynarodowe komponenty dla unikodu
Name:		icu
Version:	3.0
Release:	1
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

%prep
%setup -q -n %{name}

%build
cd source
%configure2_13 \
    --disable-samples

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
%{_mandir}/man1/*
%{_mandir}/man8/*


%files -n libicu
%{_libdir}/*


%files -n libicu-devel
%dir %{_includedir}/unicode
%dir %{_includedir}/layout
%{_includedir}/unicode/*.h
%{_includedir}/layout/*.h
%{_libdir}/%{name}/%{version}/Makefile.inc
%{_datadir}/%{name}/%{version}/config
