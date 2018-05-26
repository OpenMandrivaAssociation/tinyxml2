%define major 6
%define libname %mklibname %{name}_ %{major}
%define develname %mklibname %{name} -d

Summary:	A small and simple XML parser
Name:		tinyxml2
Version:	6.0.0
Release:	1
License:	zlib
Group:		System/Libraries
Url:		http://www.grinninglizard.com/tinyxml/
#Source0:  https://github.com/leethomason/%{name}/archive/%{version}.tar.gz
Source0:  %{name}-&{version}.tar.gz
Source1:	FindTinyXML2.cmake
# https://github.com/leethomason/tinyxml2/pull/587
Patch0:		0001-CMake-Respect-libdir-for-config-files.patch
BuildRequires:	cmake

%description
TinyXML2 is a simple, small, C++ XML parser

%package -n %{libname}
Summary:	A small and simple XML parsing library
Group:		System/Libraries

%description -n %{libname}
TinyXML is a simple, small, C++ XML parser that can be easily 
integrating into other programs. Have you ever found yourself 
writing a text file parser every time you needed to save human 
readable data or serialize objects? TinyXML solves the text I/O 
file once and for all.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q
%patch0 -p0

%build
%cmake
%make

%install

cd build
%makeinstall_std

# Install CMake find module
install -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/cmake/Modules/FindTinyXML2.cmake

%files -n %{libname}
%{_libdir}/libtinyxml2.so.%{major}*

%files -n %{develname}
%doc readme.md
%{_datadir}/cmake/Modules/FindTinyXML2.cmake
%{_libdir}/cmake/%{name}/
%{_includedir}/*.h
%{_libdir}/libtinyxml2.so
%{_libdir}/pkgconfig/*.pc
