%define revision 0

Summary:	imatix GSL is a code construction tool
Name:		imatix-gsl
Version:	4.1.0
Release:	%{revision}%{?dist}
License:	LGPL v3+
Group:		Libraries
Source0:	http://download.zeromq.org/%{name}-%{version}.tar.gz
Patch0:     imatix-gsl.patch
URL:		http://zeromq.org/
BuildRequires:	pcre-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSL/4.1 is a code construction tool. It will generate code in all languages
and for all purposes. If this sounds too good to be true, welcome to 1996,
when we invented these techniques. Magic is simply technology that is twenty
years ahead of its time. In addition to code construction, GSL has been used
to generate database schema definitions, user interfaces, reports, system
administration tools and much more.

%prep
%setup -q -n %{name}-%{version}
cd src
%patch0 -p1
cd ..
%build
cd src
make 
cd ../
%install
%{__rm} -rf $RPM_BUILD_ROOT
cd src
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/gsl
%attr(755,root,root) %{_bindir}/gsl

%changelog
