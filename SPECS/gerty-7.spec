%global service_name %{name}

Name:             %{name}
Version:          %{ver}
Release:          %{rel}%{?dist}
Summary:          gerty for RHEL/CENTOS %{os_rel}
BuildArch:        %{arch}
Group:            Application/Internet
License:          commercial
URL:              https://github.com/unpofession-al/gerty
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source1:        gerty.bin
Source2:        gerty.service
Source3:        gerty.sysconfig

%define appdir /opt/%{name}
%define systemd_dest /usr/lib/systemd/system/
%define sysconfig /etc/sysconfig/

%description
gerty for RHEL/CENTOS %{os_rel}

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{appdir}
mkdir -p $RPM_BUILD_ROOT/%{systemd_dest}
mkdir -p $RPM_BUILD_ROOT/%{sysconfig}
%{__install} -p -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/%{appdir}/gerty
%{__install} -p -m 0755 %{SOURCE2} $RPM_BUILD_ROOT/%{systemd_dest}/gerty.service
%{__install} -p -m 0755 %{SOURCE3} $RPM_BUILD_ROOT/%{sysconfig}/gerty

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) %{appdir}
%attr(0755,root,root) %{appdir}/*
%attr(0755,root,root) %{systemd_dest}/gerty.service
%config(noreplace) %{sysconfig}/gerty

%changelog
* Fri May 27 2016 Daniel Menet <daniel.menet@swisstxt.ch> - 1-2
Binary Update, better default config
* Fri May 20 2016 Daniel Menet <daniel.menet@swisstxt.ch> - 1-2
Binary update
* Thu Jan 12 2015 Daniel Menet <daniel.menet@swisstxt.ch> - 1-1
Initial creation
