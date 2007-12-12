Name: netwatch 
Version: 1.0b
Release: 0.pre3.2mdk
%define realver 1.0b.pre3
Summary: Ethernet/PPP IP Packet Monitor 
License: GPL 
Group: Monitoring
Source: ftp://ftp.slctech.org/pub/netwatch-%realver.src.tar.bz2 
Patch0: %name-include.patch.bz2
URL: http://www.slctech.org/~mackay/netwatch.html
BuildRoot: %_tmppath/%name-%version-root
BuildRequires: ncurses-devel

%description 
The software enables real-time viewing of network activity.
Network usage is tracked on a per host basis. Packet
and byte counts are available for all host communication.
Router statistics and summary charts are available.
 
%prep
%setup -q
%patch0

%build
%configure
%make

%install
install -d -m 755 %buildroot%_bindir
install -d -m 755 %buildroot%_mandir/man1
install -m 755 netwatch %buildroot%_bindir
install -m 755 netresolv %buildroot%_bindir

install -m 644 netwatch.1 %buildroot%_mandir/man1

%files
%defattr(-,root,root,-)
%doc README README.performance TODO COPYING CHANGES BUGS
%_bindir/netwatch
%_bindir/netresolv
%_mandir/man1/netwatch.1*

%clean
%__rm -fr %buildroot

