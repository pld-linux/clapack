Summary:	The CLAPACK libraries for numerical linear algebra
Summary(pl.UTF-8):	Biblioteki numeryczne CLAPACK do algebry liniowej
Name:		clapack
Version:	3.0
Release:	4
License:	freely distributable
Group:		Development/Libraries
Source0:	http://www.netlib.org/clapack/%{name}.tgz
# Source0-md5:	1b6d89b3352d0c678e50a03724458053
#Source1:	http://www.netlib.org/clapack/manpages.tgz
Patch0:		%{name}-automake_support.patch
URL:		http://www.netlib.org/clapack/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-g77
BuildRequires:	libtool >= 1:1.4.2-9
Requires:	cblas = %{version}-%{release}
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

%package -n cblas
Summary:	The CBLAS (Basic Linear Algebra Subprograms) library for Linux
Summary(pl.UTF-8):	Biblioteka CBLAS (Basic Linear Algebra Subprograms) dla Linuksa
Group:		Development/Libraries

%description -n cblas
CBLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. CBLAS provides a number of basic algorithms for
linear algebra. CBLAS is fast and well-tested, was written in FORTRAN
77.

%description -n cblas -l pl.UTF-8
CBLAS (Basic Linear Algebra Subprograms) jest standardową biblioteką
numeryczną algebry. Dostarcza wiele podstawowych algorytmów dla
algebry liniowej. Jest szybka i dobrze przetestowana, została napisana
w Fortranie 77.

%package -n cblas-devel
Summary:	CBLAS header files
Summary(pl.UTF-8):	Pliki nagłówkowe CBLAS
Group:		Development/Libraries
Requires:	cblas = %{version}-%{release}

%description -n cblas-devel
CBLAS header files.

%description -n cblas-devel -l pl.UTF-8
Pliki nagłówkowe CBLAS.

%package -n cblas-static
Summary:	Static CBLAS libraries
Summary(pl.UTF-8):	Biblioteki statyczne CBLAS
Group:		Development/Libraries
Requires:	cblas-devel = %{version}-%{release}

%description -n cblas-static
Static CBLAS libraries.

%description -n cblas-static -l pl.UTF-8
Biblioteki statyczne CBLAS.

%prep
%setup -q -n CLAPACK
%patch0 -p1
# directory INSTALL conflicts with file INSTALL needed by automake
mv -f INSTALL install

%build
rm -f ltmain.sh missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install BLAS/WRAP/cblas.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n cblas -p /sbin/ldconfig
%postun	-n cblas -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_libdir}/libclapack.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libclapack.so
%{_libdir}/libclapack.la
%{_includedir}/clapack.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libclapack.a

%files -n cblas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcblas.so.*.*.*

%files -n cblas-devel
%defattr(644,root,root,755)
%{_libdir}/libcblas.so
%{_libdir}/libcblas.la
%{_includedir}/cblas.h

%files -n cblas-static
%defattr(644,root,root,755)
%{_libdir}/libcblas.a
