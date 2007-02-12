Summary:	A package that adds additional features to the panic handler
Summary(pl.UTF-8):   Pakiet dodający dodatkowe możliwości do procedury obsługi paniki
Name:		panicsel
Version:	1.4.8
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/panicsel/%{name}-%{version}.tar.gz
# Source0-md5:	e0c580d9eec9082e6c03fc107cae5021
URL:		http://panicsel.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The panicsel kernel module adds an OS Critical Stop message to the
BIOS System Event Log, sends a BMC LAN SNMP Alert, and sets the Telco
Critical Alarm LED when a panic occurs.

The panicsel component package provides utilities to view the SEL
(showsel), perform a hardware reset (hwreset), and set up the Platform
Event Filter entry to allow BMC LAN alerts from OS Critical Stop
messages (pefconfig). It requires an IPMI driver (ipmidrvr) package in
order to talk to the BMC/firmware interface.

An IPMI driver can be provided by either the Intel IPMI driver
(/dev/imb) or the valinux IPMI driver (/dev/ipmikcs).

%description -l pl.UTF-8
Moduł jądra panicsel dodaje komunikat OS Critical Stop do loga zdarzeń
(Event Log) systemowego BIOS-u, wysyła alarm BMC LAN po SNMP i ustawia
diodę LED Critical Alarm Telco w przypadku wystąpienia paniki.

Pakiet panicsel dostarcza narzędzia do oglądania SEL (showsel),
wykonywania sprzętowego resetu (hwreset) oraz ustawiania filtra
zdarzeń (Platform Event Filter) aby zezwolić na alarmy BMC LAN z
komunikatów OS Critical Stop (pefconfig). Wymaga pakietu ze
sterownikiem IPMI (ipmidrvr), aby móc porozumieć się z interfejsem
BMC/firmware.

Sterownikiem IPMI może być sterownik Intela (/dev/imb) lub valinux
(/dev/ipmikcs).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# INSTALL is workaround for install-sh moving files
%{__make} install \
	INSTALL=install \
	mandir=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO doc/UserGuide
%attr(755,root,root) %{_sbindir}/*
%dir %{_datadir}/panicsel
%{_datadir}/panicsel/UserGuide
%{_datadir}/panicsel/bmclan*.mib
%attr(755,root,root) %{_datadir}/panicsel/checksel
%{_mandir}/man?/*
