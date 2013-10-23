Summary:	The procmail mail processing program
Name:		procmail
Version:	3.22
Release:	21
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
# patch from fedora
Patch5:		procmail-3.22-getline.patch
Provides:	MailTransportAgent
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch5 -p1 -b .readline

find . -type d -exec chmod 755 {} \;

%build
echo -n -e "\n"|  %make CFLAGS0="%{optflags}" LDFLAGS0="%{ldflags}"

%install
rm -rf %{buildroot}

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
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc FAQ HISTORY README KNOWN_BUGS FEATURES examples
%attr(6755,root,mail) %{_bindir}/procmail
%attr(2755,root,mail) %{_bindir}/lockfile
%{_bindir}/formail
%{_bindir}/mailstat
%{_mandir}/man1/*1*
%{_mandir}/man5/*5*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 3.22-17mdv2011.0
+ Revision: 667861
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.22-16mdv2011.0
+ Revision: 607221
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 3.22-15mdv2010.1
+ Revision: 519061
- rebuild

* Mon Aug 24 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.22-14mdv2010.0
+ Revision: 420297
- o add patch from fedora to fix build

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3.22-13mdv2009.1
+ Revision: 317545
- really use %%{optflags}
- use %%{ldflags}

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.22-12mdv2009.0
+ Revision: 225079
- rebuild

* Fri Mar 21 2008 Adam Williamson <awilliamson@mandriva.org> 3.22-11mdv2008.1
+ Revision: 189316
- add defsendmail.patch to fix #27484 - define the location of sendmail, as it's not installed when we build procmail so it can't detect it

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3.22-10mdv2008.1
+ Revision: 179365
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Sun Sep 16 2007 Thierry Vignaud <tv@mandriva.org> 3.22-9mdv2008.0
+ Revision: 87635
- s/Mandrake/Mandriva/


* Sun Jan 28 2007 Olivier Thauvin <nanardon@mandriva.org> 3.22-8mdv2007.0
+ Revision: 114734
- mkrel

* Tue Jan 24 2006 Warly <warly@mandriva.com> 3.22-7mdk
- Add benchmark patch from Johan Evenhuis (bug 8877)

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.22-6mdk
- Rebuild

* Tue Sep 14 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 3.22-5mdk
- rebuild
- misc spec file fixes

