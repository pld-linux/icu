Summary:	International Components for Unicode
Summary(pl):	Miêdzynarodowe komponenty dla unikodu
Name:		icu
Version:	3.0
Release:	0.1
License:	X License
Group:		Libraries
Source0:	ftp://www-126.ibm.com/pub/%{name}/%{version}/%{name}-%{version}.tgz
# Source0-md5:	
URL:		http://oss.software.ibm.com/icu/
Provides:	icu
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

This package contains the runtime libraries for ICU. It does not
contain any of the data files needed at runtime and present in the
`icu' and `icu-locales` packages.

%description -l pl
ICU jest grup± bibliotek C i C++ które dostarczaj± kompletne i pe³ne
wsparcie Unikodu oraz wsparcie lokalizacyjne. Biblioteka dostarcza
wsparcie dla kalendarza, konwersje dla wielu znaków, jêzykowe
zestawienia, formatowanie daty i czasu, wsparcie dla wielu jêzyków.

Pakiet zawiera baze znaków Unikodu.

%package -n libicu30
Summary:	International Components for Unicode (libraries)
Summary(pl):	Miêdzynarodowe Komponenty dla Unikodu (biblioteki)
Group:		Development/Libraries

%description -n libicu30
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the runtime
libraries for ICU. It does not contain any of the data files needed at
runtime and present in the `icu' and `icu-locales` packages.

%package -n libicu-devel
Summary:	International Components for Unicode (development files)
Summary(pl):	Miêdzynarodowe komponenty dla Unikodu (biblioteki dla programistów)
Group:		Development/Libraries

%description -n libicu-devel
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the development
files for ICU.

%package locales
Summary:	Locale data for ICU
Summary(pl):	Pliki lokalizacyjne dla ICU
Group:		Libraries
Requires:	libicu30 >= %{version}

%description locales
The locale data are used by ICU to provide localization (l10n),
internationalization (i18n) and timezone support to ICU applications.
This package also contains break data for various languages, and
transliteration data.

%prep
%setup -q -n %{name}-%{version}.orig -a 1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files subpackage
%defattr(644,root,root,755)
%doc extras/*.gz
%{_datadir}/%{name}-ext
