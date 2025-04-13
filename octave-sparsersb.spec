%global octpkg sparsersb

# use explicit requires
%global __requires_exclude /usr/bin/octave

Summary:	Interface to the librsb package for Octvae
Name:		octave-sparsersb
Version:	1.0.9
Release:	4
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/sparsersb/
Source0:	https://downloads.sourceforge.net/octave/sparsersb-%{version}.tar.gz
BuildRequires:  octave-devel >= 4.4.0
BuildRequires:	pkgconfig(librsb)
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%patchlist
sparsersb-1.0.9-clang.patch
octave-sparsersb-1.0.9-no_c++11.patch
# (debian)
honor-cxxflags.patch
# https://savannah.gnu.org/bugs/?61320
bug61320-sparsersb-no-internal-mex-fcns.patch
#`https://savannah.gnu.org/bugs/index.php?65292
deprecated-dot-minus.patch

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

