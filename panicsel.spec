Summary:	A package that adds additional features to the panic handler
Name:		panicsel
Version:	1.3.7
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f49299b38c77fc314da0a0132cdee772
URL:		http://panicsel.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The panicsel kernel module adds an OS Critical Stop message to the BIOS System
Event Log, sends a BMC LAN SNMP Alert, and sets the Telco Critical Alarm
LED when a panic occurs.

The panicsel component package provides utilities to view the SEL (showsel),
perform a hardware reset (hwreset), and set up the Platform Event Filter
entry to allow BMC LAN alerts from OS Critical Stop messages (pefconfig).
It requires an IPMI driver (ipmidrvr) package in order to talk to the
BMC/firmware interface.

An IPMI driver can be provided by either the Intel IPMI driver (/dev/imb)
or the valinux IPMI driver (/dev/ipmikcs).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

cp doc/UserGuide UserGuide.txt
cp README README.txt

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	mandir=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc UserGuide.txt AUTHORS README.txt TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
