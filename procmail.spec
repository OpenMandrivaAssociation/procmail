Summary:	The procmail mail processing program
Name:		procmail
Version:	3.24
Release:	2
License:	GPLv2/Artistic
Group:		System/Servers
Url:		http://www.procmail.org
Source0:	https://github.com/BuGlessRB/procmail/archive/refs/tags/v%{version}.tar.gz
Patch1:		%{name}-3.22-lockf.patch
# Fix #27484:	explictly define sendmail's location as it's not
# installed when we build procmail so it can't detect it - AdamW
# 2008/03 (thanks Snowbat)
Patch4:		procmail-3.22-defsendmail.patch
Provides:	MailTransportAgent
BuildRequires:	gcc

%description
The procmail program is used by Mandriva Linux for all local mail
delivery. In addition to just delivering mail, procmail can be used
for automatic filtering, presorting and other mail handling jobs.
Procmail is also the basis for the SmartList mailing list processor.

%prep
%autosetup -p1
find . -type d -exec chmod 755 {} \;

%build
make CC=gcc CFLAGS0="%{optflags}" LDFLAGS0="%{ldflags}" LOCKINGTEST=. 

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/{man1,man5}

make \
    BASENAME=%{buildroot}%{_prefix} \
    LOCKINGTEST=. \
    install.bin install.man

#move the man pages
mv %{buildroot}/usr/man/man1/* %{buildroot}%{_mandir}/man1/
mv %{buildroot}/usr/man/man5/* %{buildroot}%{_mandir}/man5/

## duplicate in /usr/bin
rm -f examples/mailstat

%files
%doc FAQ HISTORY README KNOWN_BUGS FEATURES examples
%attr(6755,root,mail) %{_bindir}/procmail
%attr(2755,root,mail) %{_bindir}/lockfile
%{_bindir}/formail
%{_bindir}/mailstat
%{_mandir}/man1/*1*
%{_mandir}/man5/*5*

