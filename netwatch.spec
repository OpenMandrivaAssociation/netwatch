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



%changelog
* Sat Mar 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.0-1mdv2010.1
+ Revision: 525419
- rediff patches (patch0 was partially applied, so rediff too)
- update to 1.3.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Sep 07 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-1mdv2009.0
+ Revision: 282054
- comment misc's patch
- install binaries to sbindir as they can only work as root
- tabs not spaces
- clean spec
- new release 1.2.0 (doesn't build yet, compile error i'm hoping to get fixed)

  + Michael Scherer <misc@mandriva.org>
    - fix build, asked by adamw, patch 1
    - remove old bz2 patch

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import netwatch


* Wed Nov 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0b-0.pre3.2mdk
-Fix BuildRequires

* Fri Feb 27 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0b-0.pre3.1mdk
- 1st mdk rpm (thx to Zborg)
