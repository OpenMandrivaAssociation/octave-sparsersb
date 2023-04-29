%global octpkg sparsersb

Summary:	Interface to the librsb package for Octvae
Name:		octave-sparsersb
Version:	1.0.9
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/sparsersb/
Source0:	https://downloads.sourceforge.net/octave/sparsersb-%{version}.tar.gz
# (debian)
Patch0:		no-internal-mex-fcns.patch
Patch1:		honor-cxxflags.patch

BuildRequires:  octave-devel >= 4.4.0
BuildRequires:	pkgconfig(librsb)
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Interface to the librsb package implementing the RSB sparse matrix
format for fast shared-memory sparse matrix computations.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
export CC=gcc
export CXX=g++
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

