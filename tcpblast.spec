Summary:	tool for measuring network bandwidth
Summary(pl.UTF-8):   narzędzie do pomiaru przepustowości sieci
Name:		tcpblast
Version:	20011111
Release:	2
License:	GPL
Vendor:		Rafal Maszkowski <rzm@icm.edu.pl>
Group:		Applications/Networking
Source0:	ftp://6bone-gw.6bone.pl/pub/blast/%{name}-%{version}.tar.gz
# Source0-md5:	7769126e5171c3745089a432a78a9e39
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcp/udpblast patched from FreeBSD and other versions; added options
for setting TCP-UDP, block and buffer size, port #, packet size, local
address/port, continuous speed display, sending random data,
bidirectionality, rate limits; units, IPv6, standalone high
performance echo/chargen/discard included

%description -l pl.UTF-8
tcp/udpblast pochodzący z FreeBSD wzbogacony o dodatkowe możliwości;
dodane opcje pozwalające ustalić TCP-UDP, wielkość bloku oraz rozmiar
bufora, port, rozmiar pakietu, lokalny i zdalny adres/port, limity,
jednostki, ipv6.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
