%define	major	1
# this pkg is kinda messed up
%define majorminorrelease	%{version}
%define libname	%mklibname	sysactivity %{major}
%define develname	%mklibname	sysactivity -d

Summary:	Library for retrieving statistics of the system`s activity
Name:		libsysactivity
Version:	0.6.3
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://sourceforge.net/projects/libsysactivity/
Source0:	http://downloads.sourceforge.net/project/%{name}/0.6.x/%{name}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	cmake

%description
A lightweight library that retrieves statistics of the system's activity in a 
portable and thread safe way. In each OS that it supports it offers the same 
API for retrieving the activity of: hard disks, CPUs, memory, processes and 
network interfaces.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%cmake 
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*
%{_libdir}/%{name}.so.%{majorminorrelease}

%files -n %{develname}
%doc CHANGELOG COPYING
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{name}

