Name:		libvirt-snmp
Version:	0.0.2
Release:	3%{?dist}%{?extra_release}
Summary:	SNMP functionality for libvirt

Group:		Development/Libraries
License:	GPLv2+
URL:		http://libvirt.org
Source0:	http://www.libvirt.org/sources/snmp/libvirt-snmp-%{version}.tar.gz

Patch1: libvirt-snmp-allocate-enough-space-for-trailing-NULL-in-string.patch
Patch2: libvirt-snmp-eliminate-bogus-check-for-NULL-array.patch
Patch3: libvirt-snmp-fix-startup-logic-for-selecting-stderr-vs-syslog.patch
Patch4: libvirt-snmp-Fix-off-by-one-error.patch 

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: net-snmp-perl net-snmp net-snmp-utils net-snmp-devel libvirt-devel

%description
Provides a way to control libvirt through SNMP protocol.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/libvirtMib_subagent
%{_datadir}/snmp/mibs/LIBVIRT-MIB.txt
%doc README NEWS ChangeLog AUTHORS
%{_mandir}/man1/libvirtMib_subagent.1*


%changelog
* Tue Oct 19 2011 Laine Stump <laine@redhat.com> 0.0.2-3
- fix off-by-one problem in one of patches provided with 0.0.2-2

* Tue Oct 18 2011 Laine Stump <laine@redhat.com> 0.0.2-2
- fix bugs found by Coverity run
- Resolves: rhbz#732015

* Wed Mar 23 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.2-1
- add SNMP trap/notification support

* Fri Mar 11 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-3
- remove LIBVIRT-MIB.txt from doc

* Wed Mar  9 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-2
- resolve licensing conflicts
- add unified header to sources

* Thu Feb  2 2011 Michal Privoznik <mprivozn@redhat.com> 0.0.1-1
- initial revision
