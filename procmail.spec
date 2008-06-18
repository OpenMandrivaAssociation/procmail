%define	name	procmail
%define	version	3.22

Summary:	The procmail mail processing program
Name:		procmail
Version:	%{version}
Release:	%mkrel 12
License:	GPL/Artistic
Group:		System/Servers
URL:		http://www.procmail.org
Source0:	ftp://ftp.procmail.org/pub/procmail/%{name}-%{version}.tar.bz2
Patch1:		%{name}-3.22-lockf.patch
Patch2:		%{name}-3.22-pixelpb.patch
Patch3:		%{name}-3.22-benchmark.patch
# Fix #27484: explictly define sendmail's location as it's not
# installed when we build procmail so it can't detect it - AdamW
# 2008/03 (thanks Snowbat)
Patch4:		procmail-3.22-defsendmail.patch
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
%patch4 -p1 -b .defsendmail

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


