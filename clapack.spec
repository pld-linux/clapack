Summary:	The CLAPACK libraries for numerical linear algebra
Summary(pl):	Biblioteki numeryczne CLAPACK do algebry liniowej
Name:		clapack
Version:	3.0
Release:	1
License:	Freely distributable
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Source0:	http://www.netlib.org/clapack/%{name}.tgz
#Source1:	http://www.netlib.org/clapack/manpages.tgz
Patch0:		%{name}-automake_support.patch
URL:		http://www.netlib.org/lapack/
BuildRequires:	gcc-g77
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	cblas

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

%description -l pl
CLAPACK (Linear Algebra PACKage) jest standardow± bibliotek± numeryczn±
do algebry liniowej. Dostarcza funkcje rozwi±zywania: uk³adów równañ
liniowych, uk³adów równañ metod± najmniejszych kwadratów, problemów
w³asnych. Zawiera algorytmy faktoryzacji macierzy (LU, Cholesky'ego,
QR, SVD, Schura, uogólnion± Schura) i zwi±zanych z tym obliczeñ (np.
przenumerowywanie w faktoryzacji Schura i estymacjê uwarunkowania).
CLAPACK mo¿e obs³ugiwaæ macierze blokowe i pasmowe, ale nie rzadkie w
ogólnym przypadku. Zapewnia funkcjonalno¶æ dla macierzy rzeczywistych
i zespolonych, dla liczb pojedynczej i podwójnej precyzji. CLAPACK jest
napisany w Fortranie 77 i przetlumaczony na C przy urzyciu f2c.

%package devel
Summary:	CLAPACK header files
Summary(pl):	Pliki nag³ówkowe CLAPACK
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
CLAPACK header files.

%description devel -l pl
Pliki nag³ówkowe CLAPACK.

%package static
Summary:	Static CLAPACK libraries
Summary(pl):	Biblioteki statyczne CLAPACK
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static CLAPACK libraries.

%description -l pl static
Biblioteki statyczne CLAPACK.

%package -n cblas
Summary:	The CBLAS (Basic Linear Algebra Subprograms) library for Linux
Summary(pl):	Biblioteka CBLAS (Basic Linear Algebra Subprograms) dla Linuksa
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ

%description -n cblas
CBLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. CBLAS provides a number of basic algorithms for
linear algebra. CBLAS is fast and well-tested, was written in FORTRAN
77.

%description -n cblas -l pl
CBLAS (Basic Linear Algebra Subprograms) jest standardow± bibliotek±
numeryczn± algebry. Dostarcza wiele podstawowych algorytmów dla
algebry liniowej. Jest szybka i dobrze przetestowana, zosta³a napisana
w Fortranie 77.

%package -n cblas-devel
Summary:	CBLAS header files
Summary(pl):	Pliki nag³ówkowe CBLAS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	blas = %{version}

%description -n cblas-devel
CBLAS header files.

%description -n cblas-devel -l pl
Pliki nag³ówkowe CBLAS.

%package -n cblas-static
Summary:	Static CBLAS libraries
Summary(pl):	Biblioteki statyczne CBLAS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	cblas-devel = %{version}

%description -n cblas-static
Static CBLAS libraries.

%description -n cblas-static -l pl
Biblioteki statyczne CBLAS.

%prep
%setup -q -n CLAPACK
%patch0 -p1
# directory INSTALL conflicts with file INSTALL needed by automake
mv -f INSTALL install
>INSTALL
>AUTHORS
>ChangeLog
>NEWS
>COPYING
#>config.h.in

%build
rm -f ltmain.sh
libtoolize --copy --force
aclocal
autoheader
automake --add-missing
autoconf
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#workaround libtool
ed SRC/libclapack.la <<EOF
s/relink_command=.*/relink_command=''/
w
q
EOF
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post           -p /sbin/ldconfig
%postun         -p /sbin/ldconfig

%post   -n cblas -p /sbin/ldconfig
%postun -n cblas -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_libdir}/libclapack.so.*.*.*

%files devel 
%defattr(644,root,root,755)
%{_libdir}/libclapack.so
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

%files -n cblas-static
%defattr(644,root,root,755)
%{_libdir}/libcblas.a
