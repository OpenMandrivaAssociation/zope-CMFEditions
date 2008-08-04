%define Product CMFEditions
%define product cmfeditions
%define name    zope-%{Product}
%define version 1.1.4
%define release %mkrel 3

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Versioning component integrated into Plone
License:    GPL
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tgz
Requires:   zope >= %{zope_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
In the eyes of a lot of users a major drawback of Plone was the missing
"versioning" feature. This was especially true for intranet deployments and
document management based on Plone.

Plone since Plone 3.0 has a consistent, core solution for simple versioning
tasks. This is expected of modern CMS packages.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
