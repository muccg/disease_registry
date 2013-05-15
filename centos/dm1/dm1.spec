%define name dm1
%define version 1.0.12
%define unmangled_version 1.0.12
%define release 1
%define webapps /usr/local/webapps
%define installdir %{webapps}/%{name}
%define buildinstalldir %{buildroot}/%{installdir}
%define settingsdir %{buildinstalldir}/defaultsettings
%define logsdir %{buildroot}/var/logs/%{name}
%define scratchdir %{buildroot}/var/lib/%{name}/scratch
%define mediadir %{buildroot}/var/lib/%{name}/media
%define staticdir %{buildinstalldir}/static

# Turn off brp-python-bytecompile because it makes it difficult to generate the file list
# We still byte compile everything by passing in -O paramaters to python
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Summary: WardaBDR
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Vendor: Centre for Comparative Genomics <web@ccg.murdoch.edu.au>
BuildRequires: python-setuptools mysql-devel
Requires: httpd mod_wsgi mysql-libs

%description
Registry DM1

%prep
#%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
# Nothing, all handled by install

%install
NAME=%{name}

# Make sure the standard target directories exist
# These two contain files owned by the RPM
mkdir -p %{settingsdir}
mkdir -p %{staticdir}
# The rest are for persistent data files created by the app
mkdir -p %{logsdir}
mkdir -p %{scratchdir}
mkdir -p %{mediadir}


# Create a python prefix
mkdir -p %{buildinstalldir}/{lib,bin,include}

# Install package into the prefix
cd $CCGSOURCEDIR/dm1
export PYTHONPATH=%{buildinstalldir}/lib
easy_install -O1 --prefix %{buildinstalldir} --install-dir %{buildinstalldir}/lib .

# Create settings symlink so we can run collectstatic with the default settings
touch %{settingsdir}/__init__.py
ln -fs ..`find %{buildinstalldir} -path "*/$NAME/settings.py" | sed s:^%{buildinstalldir}::` %{settingsdir}/%{name}.py

# Create symlinks under install directory to real persistent data directories
ln -fs /var/logs/%{name} %{buildinstalldir}/logs
ln -fs /var/lib/%{name}/scratch %{buildinstalldir}/scratch
ln -fs /var/lib/%{name}/media %{buildinstalldir}/media

# Install WSGI configuration into httpd/conf.d
install -D ../centos/dm1/%{name}_mod_wsgi_daemons.conf %{buildroot}/etc/httpd/conf.d/%{name}_mod_wsgi_daemons.conf
install -D ../centos/dm1/%{name}_mod_wsgi.conf %{buildroot}/etc/httpd/conf.d/%{name}_mod_wsgi.conf
install -D ../centos/dm1/django.wsgi %{buildinstalldir}/django.wsgi
install -m 0755 -D ../centos/dm1/%{name}-manage.py %{buildroot}/%{_bindir}/%{name}

# At least one python package has hardcoded shebangs to /usr/local/bin/python
find %{buildinstalldir} -name '*.py' -type f | xargs sed -i 's:^#!/usr/local/bin/python:#!/usr/bin/python:'
find %{buildinstalldir} -name '*.py' -type f | xargs sed -i 's:^#!/usr/local/python:#!/usr/bin/python:'

%post
%{name} collectstatic --noinput > /dev/null
# Remove root-owned logged files just created by collectstatic
rm -rf /var/logs/%{name}/*
# Touch the wsgi file to get the app reloaded by mod_wsgi
touch ${installdir}/django.wsgi

%clean
rm -rf %{buildroot}

%files
%defattr(-,apache,apache,-)
/etc/httpd/conf.d/*
%{_bindir}/%{name}
%attr(-,apache,,apache) %{webapps}/%{name}
%attr(-,apache,,apache) /var/logs/%{name}
%attr(-,apache,,apache) /var/lib/%{name}