%define		module	webassets
Summary:	Media asset management for python
Name:		python-%{module}
Version:	0.12.1
Release:	2
License:	BSD
Group:		Development/Libraries
Source0:	https://pypi.python.org/packages/source/w/webassets/%{module}-%{version}.tar.gz
# Source0-md5:	429401824556e6e0868e437f9e561ba6
URL:		http://github.com/miracle2k/webassets
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Suggests:	python-jsmin
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jspacker or CSS tidy.
Also supports URL rewriting in CSS files.

%prep
%setup -q -n %{module}-%{version}
%undos README.rst docs/{*.rst,Makefile}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

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

%dir %{py_sitescriptdir}/%{module}/filter
%{py_sitescriptdir}/%{module}/filter/cssrewrite
%{py_sitescriptdir}/%{module}/filter/jspacker
%{py_sitescriptdir}/%{module}/filter/rjsmin
%{py_sitescriptdir}/%{module}/filter/__init__.py[co]
%{py_sitescriptdir}/%{module}/filter/autoprefixer.py[co]
%{py_sitescriptdir}/%{module}/filter/babel.py[co]
%{py_sitescriptdir}/%{module}/filter/cleancss.py[co]
%{py_sitescriptdir}/%{module}/filter/clevercss.py[co]
%{py_sitescriptdir}/%{module}/filter/closure.py[co]
%{py_sitescriptdir}/%{module}/filter/closure_stylesheets.py[co]
%{py_sitescriptdir}/%{module}/filter/closure_templates.py[co]
%{py_sitescriptdir}/%{module}/filter/coffeescript.py[co]
%{py_sitescriptdir}/%{module}/filter/compass.py[co]
%{py_sitescriptdir}/%{module}/filter/cssmin.py[co]
%{py_sitescriptdir}/%{module}/filter/cssprefixer.py[co]
%{py_sitescriptdir}/%{module}/filter/cssutils.py[co]
%{py_sitescriptdir}/%{module}/filter/datauri.py[co]
%{py_sitescriptdir}/%{module}/filter/dust.py[co]
%{py_sitescriptdir}/%{module}/filter/handlebars.py[co]
%{py_sitescriptdir}/%{module}/filter/jade.py[co]
%{py_sitescriptdir}/%{module}/filter/jinja2.py[co]
%{py_sitescriptdir}/%{module}/filter/jsmin.py[co]
%{py_sitescriptdir}/%{module}/filter/jst.py[co]
%{py_sitescriptdir}/%{module}/filter/less.py[co]
%{py_sitescriptdir}/%{module}/filter/less_ruby.py[co]
%{py_sitescriptdir}/%{module}/filter/libsass.py[co]
%{py_sitescriptdir}/%{module}/filter/node_sass.py[co]
%{py_sitescriptdir}/%{module}/filter/pyscss.py[co]
%{py_sitescriptdir}/%{module}/filter/replace.py[co]
%{py_sitescriptdir}/%{module}/filter/requirejs.py[co]
%{py_sitescriptdir}/%{module}/filter/sass.py[co]
%{py_sitescriptdir}/%{module}/filter/slimit.py[co]
%{py_sitescriptdir}/%{module}/filter/slimmer.py[co]
%{py_sitescriptdir}/%{module}/filter/spritemapper.py[co]
%{py_sitescriptdir}/%{module}/filter/stylus.py[co]
%{py_sitescriptdir}/%{module}/filter/typescript.py[co]
%{py_sitescriptdir}/%{module}/filter/uglifyjs.py[co]
%{py_sitescriptdir}/%{module}/filter/yui.py[co]

%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
