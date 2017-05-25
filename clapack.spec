Summary:	The CLAPACK libraries for numerical linear algebra
Summary(pl.UTF-8):	Biblioteki numeryczne CLAPACK do algebry liniowej
Name:		clapack
Version:	3.2.1
Release:	4
License:	freely distributable
Group:		Development/Libraries
Source0:	http://www.netlib.org/clapack/%{name}-%{version}-CMAKE.tgz
# Source0-md5:	4fd18eb33f3ff8c5d65a7d43913d661b
Patch0:		%{name}-%{version}-fix_include_file.patch
Patch1:		%{name}-%{version}-noblasf2c.patch
Patch2:		%{name}-%{version}-hang.patch
Patch3:		%{name}-%{version}-findblas-r6.patch
URL:		http://www.netlib.org/clapack/
BuildRequires:	cmake
BuildRequires:	gcc-fortran
BuildRequires:	libf2c-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. CLAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. CLAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision. CLAPACK
is coded in Fortran77 and translated to C using f2c.

%description -l pl.UTF-8
CLAPACK (Linear Algebra PACKage) jest standardową biblioteką
numeryczną do algebry liniowej. Dostarcza funkcje rozwiązywania:
układów równań liniowych, układów równań metodą najmniejszych
kwadratów, problemów własnych. Zawiera algorytmy faktoryzacji macierzy
(LU, Cholesky'ego, QR, SVD, Schura, uogólnioną Schura) i związanych z
tym obliczeń (np. przenumerowanie w faktoryzacji Schura i estymację
uwarunkowania). CLAPACK może obsługiwać macierze blokowe i pasmowe,
ale nie rzadkie w ogólnym przypadku. Zapewnia funkcjonalność dla
macierzy rzeczywistych i zespolonych, dla liczb pojedynczej i
podwójnej precyzji. CLAPACK jest napisany w Fortranie 77 i
przetłumaczony na C przy użyciu f2c.

%package devel
Summary:	CLAPACK header files
Summary(pl.UTF-8):	Pliki nagłówkowe CLAPACK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
CLAPACK header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe CLAPACK.

%package static
Summary:	Static CLAPACK libraries
Summary(pl.UTF-8):	Biblioteki statyczne CLAPACK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CLAPACK libraries.

%description static -l pl.UTF-8
Biblioteki statyczne CLAPACK.

%prep
%setup -q -n %{name}-%{version}-CMAKE
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
install -d build
cd build
%cmake \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_libdir}/libclapack.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libclapack.so
%{_includedir}/clapack
%{_datadir}/cmake/Modules/clapack*.cmake
