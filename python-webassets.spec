%define		module	webassets
Summary:	Media asset management for python
Name:		python-%{module}
Version:	0.7.1
Release:	1
License:	BSD
Group:		Development/Libraries
URL:		http://github.com/miracle2k/%{module}
# Because jsmin.py is non-free, we have to make a "clean" source tarball.
# First, get the original source:
# Source0:      http://pypi.python.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz
# Then, unpack it, and delete src/webassets/filter/jsmin/jsmin.py
# tar xf %{module}-%{version}.tar.gz
# rm -rf %{module}-%{version}/src/webassets/filter/jsmin/jsmin.py
# tar cfz %{module}-%{version}-clean.tar.gz %{module}-%{version}
Source0:	%{module}-%{version}-clean.tar.gz
# Source0-md5:	548e2a4125a11c0bf30398357059a725
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.553
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

%prep
%setup -q -n %{module}-%{version}
%undos README.rst docs/{*.rst,Makefile,django/jinja2.rst}

rm src/django_assets/models.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst CHANGES LICENSE docs
%attr(755,root,root) %{_bindir}/webassets
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]

%dir %{py_sitescriptdir}/%{module}/ext
%{py_sitescriptdir}/%{module}/ext/__init__.py[co]
%{py_sitescriptdir}/%{module}/ext/jinja2.py[co]
%{py_sitescriptdir}/%{module}/ext/werkzeug.py[co]

%dir %{py_sitescriptdir}/%{module}/filter
%{py_sitescriptdir}/%{module}/filter/__init__.py[co]
%{py_sitescriptdir}/%{module}/filter/clevercss.py[co]
%{py_sitescriptdir}/%{module}/filter/closure.py[co]
%{py_sitescriptdir}/%{module}/filter/coffeescript.py[co]
%{py_sitescriptdir}/%{module}/filter/compass.py[co]
%{py_sitescriptdir}/%{module}/filter/cssmin.py[co]
%{py_sitescriptdir}/%{module}/filter/cssprefixer.py[co]
%{py_sitescriptdir}/%{module}/filter/cssutils.py[co]
%{py_sitescriptdir}/%{module}/filter/datauri.py[co]
%{py_sitescriptdir}/%{module}/filter/dust.py[co]
%{py_sitescriptdir}/%{module}/filter/gzip.py[co]
%{py_sitescriptdir}/%{module}/filter/handlebars.py[co]
%{py_sitescriptdir}/%{module}/filter/jst.py[co]
%{py_sitescriptdir}/%{module}/filter/less.py[co]
%{py_sitescriptdir}/%{module}/filter/less_ruby.py[co]
%{py_sitescriptdir}/%{module}/filter/pyscss.py[co]
%{py_sitescriptdir}/%{module}/filter/sass.py[co]
%{py_sitescriptdir}/%{module}/filter/uglifyjs.py[co]
%{py_sitescriptdir}/%{module}/filter/yui.py[co]
%{py_sitescriptdir}/%{module}/filter/cssrewrite
%{py_sitescriptdir}/%{module}/filter/jsmin
%{py_sitescriptdir}/%{module}/filter/jspacker
%{py_sitescriptdir}/%{module}/filter/rjsmin

%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

%{py_sitescriptdir}/django_assets
