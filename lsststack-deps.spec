Summary:        LSST Stack core OS provided dependencies
Name:           lsststack-deps
Version:        1.0.1
Release:        1
License:        APL 2.0
Url:            https://github.com/lsst
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       bison
Requires:       blas
Requires:       bzip2-devel
Requires:       flex
Requires:       freetype-devel
Requires:       gcc-c++
Requires:       gcc-gfortran
Requires:       libuuid-devel
Requires:       libXt-devel
Requires:       ncurses-devel
Requires:       make
Requires:       openssl-devel
Requires:       perl
Requires:       readline-devel
Requires:       zlib-devel

%description
Pulls in core OS provided packages required for building the LSST Stack as
documented at https://confluence.lsstcorp.org/display/LSWUG/Prerequisites.

# XXX an empty files section is required or the "meta" package will not be
# generated.
%files

%changelog
* Wed Jan 14 2015 Joshua Hoblitt <jhoblitt@cpan.org> 1.0.1-1
- new package built with tito

* Tue Jan 13 2015 jhoblitt@lsst.org
- first working version
