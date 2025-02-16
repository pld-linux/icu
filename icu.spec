#
# Conditional build:
%bcond_without	static_libs	# static libraries

%define		ver	%(echo %{version} | tr . _)
%define		basever	%(echo %{version} | cut -d. -f1)
Summary:	International Components for Unicode
Summary(pl.UTF-8):	Międzynarodowe komponenty dla unikodu
Name:		icu
Version:	76.1
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	https://github.com/unicode-org/icu/releases/download/release-76-1/icu4c-%{ver}-src.tgz
# Source0-md5:	857fdafff8127139cc175a3ec9b43bd6
Patch0:		icudata-stdlibs.patch
Patch1:		timezone.patch
URL:		https://icu.unicode.org/
BuildRequires:	autoconf >= 2.72
BuildRequires:	autoconf-archive
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	python3
BuildRequires:	python3-modules
Requires:	libicu%{?_isa} = %{version}-%{release}
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
Summary(pl.UTF-8):	Międzynarodowe Komponenty dla Unikodu (biblioteki)
Group:		Libraries
Obsoletes:	libicu30 < 3.2

%description -n libicu
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the runtime
libraries for ICU. It does not contain any of the data files needed at
runtime and present in the `icu' package.

%description -n libicu -l pl.UTF-8
ICU jest grupą bibliotek C i C++, które dostarczają kompletną i pełną
obsługę Unikodu i lokalizacji. Ten pakiet zawiera biblioteki
uruchomieniowe ICU. Nie zawiera żadnych plików z danymi potrzebnymi w
czasie działania i obecnymi w pakietach "icu".

%package -n libicu-devel
Summary:	International Components for Unicode (development files)
Summary(pl.UTF-8):	Międzynarodowe komponenty dla Unikodu (pliki dla programistów)
Group:		Development/Libraries
Requires:	libicu%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel%{?_isa} >= 6:8

%description -n libicu-devel
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the development
files for ICU.

%description -n libicu-devel -l pl.UTF-8
ICU jest grupą bibliotek C i C++, które dostarczają kompletną i pełną
obsługę Unikodu i lokalizacji. Ten pakiet zawiera pliki
programistyczne ICU.

%package -n libicu-static
Summary:	International Components for Unicode (static libraries)
Summary(pl.UTF-8):	Międzynarodowe komponenty dla Unikodu (biblioteki statyczne)
Group:		Development/Libraries
Requires:	libicu-devel%{?_isa} = %{version}-%{release}

%description -n libicu-static
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode support. This package contains the static
libraries for ICU.

%description -n libicu-static -l pl.UTF-8
ICU jest grupą bibliotek C i C++, które dostarczają kompletną i pełną
obsługę Unikodu i lokalizacji. Ten pakiet zawiera statyczne
biblioteki programistyczne ICU.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p2

%build
cd source
%{__autoconf}
%configure \
	--sbindir=%{_bindir} \
	--with-data-packaging=library \
	%{?with_static_libs:--enable-static} \
	--disable-samples

%{__make} \
	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT

for f in icu-i18n icu-io icu-uc ; do
sed -i \
	-e 's/\$(THREADSCXXFLAGS)//' \
	-e 's/\$(THREADSCFLAGS)//' \
	-e 's/\$(THREADSCPPFLAGS)/-D_REENTRANT/' $RPM_BUILD_ROOT%{_pkgconfigdir}/${f}.pc
done

# help rpm to generate deps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

# rpm is too stupid sometimes and fails on symlinks to symlinked resources
# (reporting unresolved dependency at install time)
for f in Makefile.inc pkgdata.inc ; do
	ln -sf %{version}/${f} $RPM_BUILD_ROOT%{_libdir}/%{name}/${f}
done

%{__rm} $RPM_BUILD_ROOT%{_datadir}/icu/%{version}/LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libicu -p /sbin/ldconfig
%postun	-n libicu -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc license.html readme.html
%attr(755,root,root) %{_bindir}/derb
%attr(755,root,root) %{_bindir}/escapesrc
%attr(755,root,root) %{_bindir}/gen*
%attr(755,root,root) %{_bindir}/icuexportdata
%attr(755,root,root) %{_bindir}/icuinfo
%attr(755,root,root) %{_bindir}/icupkg
%attr(755,root,root) %{_bindir}/makeconv
%attr(755,root,root) %{_bindir}/pkgdata
%attr(755,root,root) %{_bindir}/uconv
%{_mandir}/man1/derb.1*
%{_mandir}/man1/gen*.1*
%{_mandir}/man1/icuexportdata.1*
%{_mandir}/man1/makeconv.1*
%{_mandir}/man1/pkgdata.1*
%{_mandir}/man1/uconv.1*
%{_mandir}/man8/gen*.8*
%{_mandir}/man8/icupkg.8*

%files -n libicu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libicu*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libicu*.so.%{basever}

%files -n libicu-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/icu-config
%attr(755,root,root) %{_libdir}/libicu*.so
%{_pkgconfigdir}/icu-i18n.pc
%{_pkgconfigdir}/icu-io.pc
%{_pkgconfigdir}/icu-uc.pc
%{_includedir}/unicode
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.inc
%{_libdir}/%{name}/current
%dir %{_libdir}/%{name}/%{version}
%{_libdir}/%{name}/%{version}/*.inc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/config
%attr(755,root,root) %{_datadir}/%{name}/%{version}/install-sh
%attr(755,root,root) %{_datadir}/%{name}/%{version}/mkinstalldirs
%{_mandir}/man1/icu-config.1*

%if %{with static_libs}
%files -n libicu-static
%defattr(644,root,root,755)
%{_libdir}/libicu*.a
%endif
