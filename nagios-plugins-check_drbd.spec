# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/


Name:    nagios-plugins-check_drbd
Version: 0.1
Release: 1.ndias%{?dist}
Summary: Nagios plugin to check the status of a DRBD device

License: GPLv3
URL:     https://github.com/ndias/check_drbd
Source0: https://github.com/ndias/check_drbd/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

Requires: /usr/bin/perl, /usr/sbin/drbdadm

%description
Nagios plugin to check the status of a DRBD device

%prep
%setup -q -n check_drbd-%{version}


%build


%install
install -p -m 755 -D check_drbd.sh %{buildroot}%{_libdir}/nagios/plugins/check_drbd.sh

%files
%doc README.md
%license LICENSE

%{_libdir}/nagios/plugins/check_drbd.sh

%changelog
* Fri Jan 21 2022 Nuno Dias <Nuno.Dias@gmail.com> - 0.1-1.ndias
- Version 0.1
