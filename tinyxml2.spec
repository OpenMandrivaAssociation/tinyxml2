%define major 9
%define libname %mklibname %{name}
%define develname %mklibname %{name} -d

Summary:	A small and simple XML parser
Name:		tinyxml2
Version:	9.0.0
Release:	2
License:	zlib
Group:		System/Libraries
Url:		http://www.grinninglizard.com/tinyxml/
Source0:	https://github.com/leethomason/tinyxml2/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake ninja

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
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libtinyxml2.so.%{major}*

%files -n %{develname}
%doc readme.md
%{_libdir}/cmake/%{name}/
%{_includedir}/*.h
%{_libdir}/libtinyxml2.so
%{_libdir}/pkgconfig/*.pc
