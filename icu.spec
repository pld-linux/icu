%define		ver	%(echo %{version} | tr . _)
Summary:	International Components for Unicode
Summary(pl.UTF-8):	Międzynarodowe komponenty dla unikodu
Name:		icu
Version:	4.2.1
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	http://download.icu-project.org/files/icu4c/%{version}/%{name}4c-%{ver}-src.tgz
# Source0-md5:	e3738abd0d3ce1870dc1fd1f22bba5b1
Patch0:		pkgconfig.patch
Source1:	%{name}-config
URL:		http://www.icu-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
Summary(pl.UTF-8):	Międzynarodowe Komponenty dla Unikodu (biblioteki)
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
Summary(pl.UTF-8):	Międzynarodowe komponenty dla Unikodu (pliki dla programistów)
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
%patch0 -p1

%build
cd source
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--sbindir=%{_bindir} \
	--disable-samples

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT

install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}-config
sed -i 's/\$(THREADSCXXFLAGS)//' $RPM_BUILD_ROOT%{_libdir}/pkgconfig/icu.pc
sed -i 's/\$(THREADSCPPFLAGS)/-D_REENTRANT/' $RPM_BUILD_ROOT%{_libdir}/pkgconfig/icu.pc

# help rpm to generate deps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

# rpm is too stupid sometimes and fails on symlinks to symlinked resources
# (reporting unresolved dependency at install time)
ln -sf %{version}/Makefile.inc $RPM_BUILD_ROOT%{_libdir}/%{name}/Makefile.inc

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
%attr(755,root,root) %{_libdir}/libicu*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libicu*.so.42

%files -n libicu-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/icu-config
%attr(755,root,root) %{_libdir}/libicu*.so
%{_pkgconfigdir}/icu.pc
%{_includedir}/unicode
%{_includedir}/layout
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.inc
%dir %{_libdir}/%{name}/current
%dir %{_libdir}/%{name}/%{version}
%{_libdir}/%{name}/%{version}/*.inc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/config
%attr(755,root,root) %{_datadir}/%{name}/%{version}/install-sh
%attr(755,root,root) %{_datadir}/%{name}/%{version}/mkinstalldirs
%{_mandir}/man1/icu-config.1*
