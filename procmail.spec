%define	name	procmail
%define	release	%mkrel 9
%define	version	3.22

Summary:	The procmail mail processing program.
Name:		procmail
Version:	%{version}
Release:	%{release}
License:	GPL/Artistic
Group:		System/Servers
URL:		http://www.procmail.org
Source0:	ftp://ftp.procmail.org/pub/procmail/%{name}-%{version}.tar.bz2
Patch1:		%{name}-3.22-lockf.patch
Patch2:		%{name}-3.22-pixelpb.patch
Patch3:		%{name}-3.22-benchmark.patch
BuildRoot:	%{_tmppath}/%{name}-root
Provides:	MailTransportAgent

%description
The procmail program is used by Mandriva Linux for all local mail
delivery. In addition to just delivering mail, procmail can be used
for automatic filtering, presorting and other mail handling jobs.
Procmail is also the basis for the SmartList mailing list processor.

%prep

%setup -q
%patch1 -p1 -b .lockf
%patch2 -p1 -b .warly
%patch3 -p1 -b .bench

find . -type d -exec chmod 755 {} \;

%build
echo -n -e "\n"|  %make CFLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/{man1,man5}

make \
    BASENAME=%{buildroot}%{_prefix} \
    install.bin install.man

#move the man pages
mv %{buildroot}/usr/man/man1/* %{buildroot}%{_mandir}/man1/
mv %{buildroot}/usr/man/man5/* %{buildroot}%{_mandir}/man5/

## duplicate in /usr/bin
rm -f examples/mailstat

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc FAQ HISTORY README KNOWN_BUGS FEATURES examples
%attr(6755,root,mail) %{_bindir}/procmail
%attr(2755,root,mail) %{_bindir}/lockfile
%{_bindir}/formail
%{_bindir}/mailstat
%{_mandir}/man1/*1*
%{_mandir}/man5/*5*


