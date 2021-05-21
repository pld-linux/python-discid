#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	discid
Summary:	Python binding of Libdiscid
Name:		python-%{module}
Version:	1.2.0
Release:	1
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/discid/
Source0:	https://files.pythonhosted.org/packages/source/d/discid/%{module}-%{version}.tar.gz
# Source0-md5:	88cbe833957062f9cb163a72884931d2
URL:		https://pypi.org/project/discid/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	libdiscid >= 0.2.2
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-discid implements Python bindings for MusicBrainz Libdiscid.
Libdiscid's main purpose is the calculation of an identifier of audio
discs (disc ID) to use for the MusicBrainz database.

That identifier is calculated from the TOC of the disc, similar to the
freeDB CDDB identifier. Libdiscid can calculate MusicBrainz disc IDs
and freeDB disc IDs. Additionally the MCN of the disc and ISRCs from
the tracks can be extracted.

%package -n python3-%{module}
Summary:	Python binding of Libdiscid
Group:		Libraries/Python
Requires:	libdiscid >= 0.2.2
Requires:	python3-modules >= 1:3.1

%description -n python3-%{module}
Python-discid implements Python bindings for MusicBrainz Libdiscid.
Libdiscid's main purpose is the calculation of an identifier of audio
discs (disc ID) to use for the MusicBrainz database.

That identifier is calculated from the TOC of the disc, similar to the
freeDB CDDB identifier. Libdiscid can calculate MusicBrainz disc IDs
and freeDB disc IDs. Additionally the MCN of the disc and ISRCs from
the tracks can be extracted.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
