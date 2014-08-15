Summary:	Common networking utilities and servers
Name:		inetutils
Version:	1.9.2
Release:	2
License:	GPL v3+
Group:		Networking/Utilities
Source0:	http://ftp.gnu.org/gnu/inetutils/%{name}-%{version}.tar.gz
# Source0-md5:	aa1a9a132259db83e66c1f3265065ba2
URL:		http://www.gnu.org/software/inetutils/
BuildRequires:	autoconf
BuildRequires:	automake
# for config.rpath
BuildRequires:	gettext-devel
BuildRequires:	pam-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
Requires:	iana-etc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_sbindir}

%description
This is a distribution of common networking utilities and servers.
Main package currently contains only some common documentation, all
utilities are in their own packages.

%package dnsdomainname
Summary:	DNS domain name tool
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description dnsdomainname
Show domain part of the system's fully qualified host name.
The tool uses gethostname to get the host name of the system and
getaddrinfo to resolve it into a canonical name. The part after the
first period ('.') of the canonical name is shown.

%package ftp
Summary:	FTP client from GNU inetutils package
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	ftp
Obsoletes:	ftp

%description ftp
FTP client from GNU inetutils package.

%package hostname
Summary:	Showing or setting the system's host name
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description hostname
Hostname is the program that is used to either set or display the
current host, domain or node name of the system. These names are used
by many of the networking programs to identify the machine. The domain
name is also used by NIS/YP.

%package ping
Summary:	ping utility from GNU inetutils package
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	ping
Obsoletes:	iputils-ping
Obsoletes:	ping

%description ping
ping utility from GNU inetutils package.

%package rexec
Summary:	rexec client from GNU inetutils package
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Provides:	rexec
Obsoletes:	rexec

%description rexec
rexec client from GNU inetutils package.

%package rlogin
Summary:	rlogin client from GNU inetutils package
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	rlogin
Obsoletes:	rlogin

%description rlogin
rlogin client from GNU inetutils package.

%package rsh
Summary:	rsh and rcp clients from GNU inetutils package
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	rsh
Obsoletes:	rsh

%description rsh
rsh and rcp clients from GNU inetutils package.

%package talk
Summary:	talk client from GNU inetutils package
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	talk
Obsoletes:	talk

%description talk
talk client from GNU inetutils package.

%package telnet
Summary:	telnet client from GNU inetutils package
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	telnet
Obsoletes:	telnet

%description telnet
telnet client from GNU inetutils package.

%package traceroute
Summary:	Traces the route taken by packets over a TCP/IP network
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description traceroute
traceroute displays the route used by IP packets on their way to
specified host.

%package tftp
Summary:	TFTP client from GNU inetutils package
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	tftp
Obsoletes:	tftp

%description tftp
TFTP client from GNU inetutils package.

%prep
%setup -q

%build
cp -f /usr/share/gettext/config.rpath build-aux
%{__aclocal} -I m4 -I am
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure \
	--disable-ifconfig	\
	--disable-logger	\
	--disable-servers	\
	--disable-silent-rules	\
	--disable-syslogd	\
	--disable-whois		\
	--with-pam		\
	--without-wrap
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SUIDMODE="-m755"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_infodir}/inetutils.info*

%files dnsdomainname
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dnsdomainname
%{_mandir}/man1/dnsdomainname.1*

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%{_mandir}/man1/ftp.1*

%files hostname
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hostname
%{_mandir}/man1/hostname.1*

%files ping
%defattr(644,root,root,755)
%attr(4754,root,adm) %{_bindir}/ping
%attr(4754,root,adm) %{_bindir}/ping6
%{_mandir}/man1/ping.1*
%{_mandir}/man1/ping6.1*

%files rexec
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rexec
%{_mandir}/man1/rexec.1*

%files rlogin
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/rlogin
%{_mandir}/man1/rlogin.1*

%files rsh
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/rcp
%attr(4755,root,root) %{_bindir}/rsh
%{_mandir}/man1/rcp.1*
%{_mandir}/man1/rsh.1*

%files talk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/talk
%{_mandir}/man1/talk.1*

%files telnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/telnet
%{_mandir}/man1/telnet.1*

%files traceroute
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/traceroute
%{_mandir}/man1/traceroute.1*

%files tftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tftp
%{_mandir}/man1/tftp.1*

