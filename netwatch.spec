Name:		netwatch 
Summary:	Ethernet/PPP IP Packet Monitor 
Version:	1.3.0
Release:	%{mkrel 1}
# Headers suggest some code is from 'statnet' which is GPLv2
License:	GPLv2
Group:		Monitoring
Source0:	http://www.slctech.org/~mackay/NETWATCH/%{name}-%{version}-1.tgz
Patch0:		netwatch-1.3.0-1-include.patch
# Fix a bug which causes build to fail - misc 2008/09
Patch1:		netwatch-1.3.0-1-fix_build_open.patch 
URL:		http://www.slctech.org/~mackay/netwatch.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	ncurses-devel

%description 
The software enables real-time viewing of network activity.
Network usage is tracked on a per host basis. Packet
and byte counts are available for all host communication.
Router statistics and summary charts are available.
 
%prep
%setup -q
%patch0 -p0
%patch1

%build
%configure2_5x
%make

%install
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 netwatch %{buildroot}%{_sbindir}
install -m 755 netresolv %{buildroot}%{_sbindir}
install -m 644 netwatch.1 %{buildroot}%{_mandir}/man1

%clean
%__rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
%doc README README.performance TODO CHANGES BUGS
%{_sbindir}/%{name}
%{_sbindir}/netresolv
%{_mandir}/man1/%{name}.1*

