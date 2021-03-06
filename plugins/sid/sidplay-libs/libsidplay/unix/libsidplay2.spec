%define major    2
%define oname    libsidplay
%define name     %{oname}%{major}
%define version  2.1.0
%define frelease 1
%define release  %{frelease}
%define resid    0.13
%define residbld 1.0.0
%define builders %{_libdir}/sidplay/builders

Summary:        A Commodore 64 music player and SID chip emulator library.
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         %{oname}-%{version}-%{frelease}.tar.bz2
Source1:        resid-%{resid}.tar.bz2
Source2:        resid-builder-%{residbld}-1.tar.bz2
Patch:          resid-%{resid}-p1.patch.bz2
Copyright:      GPL
Group:          System/Libraries
URL:            http://sidplay2.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-buildroot
Prefix:         %{_prefix}

%description
This is a cycle-based version of a C64 music playing library
developed by Simon White. This library provides no internal
SID emulation. Instead a means to drive any external SID hardware or
emulation has been provided using the SID Builder Classes.

An ReSID Builder Class using a modified version of ReSID %{resid}
is included in this package. Alternative/updated classes can be
obtained from the SIDPlay2 homepage.

%package devel
Summary:        Development headers and libraries for %{name}
Group:          Development/C++
Requires:       %{name} = %{version}
Provides:       %{oname}-devel = %{version}

%description devel
This package includes the header and library files necessary
for developing applications to use %{name}.

%prep
%setup -q -n %{oname}-%{version} -a 1 -a 2
%patch -p0
touch resid-%{resid}/*

%build
%configure --with-sidbuilders=%{builders}
%make
cd resid-%{resid}
%configure --libdir=%{builders} --disable-shared
%make
cd ..
cd resid-builder-%{residbld}
%configure --with-resid=$PWD/../resid-%{resid} --libdir=%{builders} --with-sidplay2=$PWD/..
%make
cd ..

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall
cd resid-builder-%{residbld}
%makeinstall libdir=$RPM_BUILD_ROOT%{builders}

%clean
rm -rf $RPM_BUILD_ROOT

%postun -p /sbin/ldconfig

%post -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc COPYING
%{_includedir}/sidplay/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{builders}/*.la
%{builders}/*.a

%changelog
* Fri Nov 23 2001 Simon White <s_a_white@email.com> 2.1.0-1
- New interface using sidbuilder classes.  GCC3 and PSID 2NG
  support.
- Merged in Mandrake spec file changes.  Just set the release
  define accordingly.
  
* Wed Nov 7 2001 Simon White <s_a_white@email.com> 2.0.7-5
- Performance fix.

* Mon May 7 2001 Simon White <s_a_white@email.com> 2.0.7-4
- Fix for endian functions under gcc 2.96.

* Wed Apr 10 2001 Simon White <s_a_white@email.com> 2.0.7-3
- Use non Mandrake specific release number.

* Wed Apr 4 2001 Simon White <s_a_white@email.com> 2.0.7-2mdk
- Updated --prefix and make install so la file does not end up with
  a bad install path.

* Sun Apr 1 2001 Simon White <s_a_white@email.com> 2.0.7-1mdk
- First spec file.

# end of file
