%global with_mpich 1
%if (0%{?rhel} >= 8)
%global with_openmpi 1
%global with_openmpi3 0
%else
%global with_openmpi 0
%global with_openmpi3 1
%endif

%if (0%{?suse_version} >= 1500)
%global module_load() if [ "%{1}" == "openmpi3" ]; then MODULEPATH=/usr/share/modules module load gnu-openmpi; else MODULEPATH=/usr/share/modules module load gnu-%{1}; fi
%else
%global module_load() module load mpi/%{1}-%{_arch}
%endif

%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif
%if %{with_openmpi3}
%if 0%{?fedora}
# this would be nice to use but causes issues with linting
# since that is done on Fedora
#{error: openmpi3 doesn't exist on Fedora}
%endif
%global mpi_list %{?mpi_list} openmpi3
%endif

%if (0%{?suse_version} >= 1500)
%global mpi_libdir %{_libdir}/mpi/gcc
%global mpi_lib_ext lib64
%global mpi_includedir %{_libdir}/mpi/gcc
%global mpi_include_ext /include
%else
%global mpi_libdir %{_libdir}
%global mpi_lib_ext lib
%global mpi_includedir %{_includedir}
%global mpi_include_ext -%{_arch}
%endif

%if (0%{?suse_version} >= 1500)
%global cmake cmake
%else
%global cmake cmake3
%endif

%global shortcommit %(c=%{commit};echo ${c:0:7})

Name:		mpifileutils
Version:	0.11.1
Release:	3%{?commit:.g%{shortcommit}}%{?dist}
Summary:	File utilities designed for scalability and performance.

Group:		System Environment/Libraries
License:	Copyright and BSD License
URL:		https://hpc.github.io/mpifileutils
Source:		https://github.com/hpc/%{name}/archive/v%{version}.tar.gz
%if "%{?commit}" != ""
Patch1: %{version}..%{commit}.patch
%endif
BuildRoot:	%_topdir/BUILDROOT
%if (0%{?suse_version} >= 1500)
BuildRequires: cmake >= 3.1
BuildRequires: lua-lmod
BuildRequires: libbz2-devel
BuildRequires: libopenssl-devel
%else
BuildRequires: cmake3 >= 3.1
BuildRequires: Lmod
BuildRequires: bzip2-devel
BuildRequires: openssl-devel
%endif
BuildRequires: gcc-c++
BuildRequires: libuuid-devel
BuildRequires: libattr-devel


%if (0%{?suse_version} >= 1500)
BuildRequires: libfabric1 >= 1.12.0
%endif

%description
File utilities designed for scalability and performance.

%if %{with_openmpi}
%package openmpi
Summary:	File utilities designed for scalability and performance.
BuildRequires: openmpi-devel
BuildRequires: dtcmp-openmpi-devel
BuildRequires: libcircle-openmpi-devel
BuildRequires: hdf5-vol-daos-openmpi-devel

%description openmpi
File utilities designed for scalability and performance.


%package openmpi-devel
Summary:	File utilities designed for scalability and performance.
Requires: %{name}-openmpi%{_isa} = %version-%release

%description openmpi-devel
Development files for %{name}-openmpi.
%endif

%if %{with_openmpi3}
%package openmpi3
Summary:	File utilities designed for scalability and performance.
BuildRequires: openmpi3-devel
BuildRequires: dtcmp-openmpi3-devel
BuildRequires: libcircle-openmpi3-devel
BuildRequires: hdf5-vol-daos-openmpi3-devel

%description openmpi3
File utilities designed for scalability and performance.

%if (0%{?suse_version} >= 1500)
%package -n libmfu0-openmpi3
Summary:	File utilities designed for scalability and performance.

%description -n libmfu0-openmpi3
Shared libraries for %{name}-openmpi3.
%endif

%package openmpi3-devel
Summary:	File utilities designed for scalability and performance.
%if (0%{?suse_version} >= 1500)
Requires: libmfu0-openmpi3%{_isa} = %version-%release
%else
Requires: %{name}-openmpi3%{_isa} = %version-%release
%endif

%description openmpi3-devel
Development files for %{name}-openmpi3.
%endif

%if %{with_mpich}
%package mpich
Summary:	File utilities designed for scalability and performance.
BuildRequires: mpich-devel
BuildRequires: dtcmp-mpich-devel
BuildRequires: libcircle-mpich-devel
BuildRequires: hdf5-vol-daos-mpich-devel

%description mpich
File utilities designed for scalability and performance.

%if (0%{?suse_version} >= 1500)
%package -n libmfu0-mpich
Summary:	File utilities designed for scalability and performance.

%description -n libmfu0-mpich
Shared libraries for %{name}-mpich.
%endif

%package mpich-devel
Summary:	File utilities designed for scalability and performance.
%if (0%{?suse_version} >= 1500)
Requires: libmfu0-mpich%{_isa} = %version-%release
%else
Requires: %{name}-mpich%{_isa} = %version-%release
%endif

%description mpich-devel
Development files for %{name}-mpich.
%endif


%prep
%autosetup -p1

%build
for mpi in %{?mpi_list}; do
  mkdir $mpi
  pushd $mpi
  %module_load $mpi
  %cmake ../ -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}"                                   \
             -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}"                                 \
             -DENABLE_DAOS=ON                                                     \
             -DENABLE_LIBARCHIVE=OFF                                              \
             -DENABLE_HDF5=ON                                                     \
             -DDTCMP_INCLUDE_DIRS=%{mpi_includedir}/$mpi%{mpi_include_ext}        \
             -DDTCMP_LIBRARIES=%{mpi_libdir}/$mpi/%{mpi_lib_ext}/libdtcmp.so      \
             -DLibCircle_INCLUDE_DIRS=%{mpi_includedir}/$mpi%{mpi_include_ext}    \
             -DLibCircle_LIBRARIES=%{mpi_libdir}/$mpi/%{mpi_lib_ext}/libcircle.so \
             -DHDF5_INCLUDE_DIRS=%{mpi_includedir}/$mpi%{mpi_include_ext}         \
             -DHDF5_LIBRARIES=%{mpi_libdir}/$mpi/%{mpi_lib_ext}/libhdf5.so        \
             -DWITH_DAOS_PREFIX=/usr                                              \
             -DCMAKE_INSTALL_INCLUDEDIR=%{mpi_includedir}/$mpi%{mpi_include_ext}  \
             -DCMAKE_INSTALL_PREFIX=%{mpi_libdir}/$mpi                            \
             -DCMAKE_INSTALL_LIBDIR=%{mpi_lib_ext}

  make
  module purge
  popd
done

%install
rm -rf %{buildroot}
for mpi in %{?mpi_list}; do
  %module_load $mpi
  make install -C $mpi DESTDIR=%{buildroot}
  module purge
done

%if %{with_openmpi}
%files openmpi
%defattr(-,root,root,-)
%{mpi_libdir}/openmpi/bin/*
%{mpi_libdir}/openmpi/share/man/*
%{mpi_libdir}/openmpi/%{mpi_lib_ext}/libmfu.so.*

%files openmpi-devel
%{mpi_includedir}/openmpi%{mpi_include_ext}/*
%{mpi_libdir}/openmpi/%{mpi_lib_ext}/lib*.so
%{mpi_libdir}/openmpi/%{mpi_lib_ext}/lib*.a
%endif

%if %{with_openmpi3}
%files openmpi3
%defattr(-,root,root,-)
%{mpi_libdir}/openmpi3/bin/*
%{mpi_libdir}/openmpi3/share/man/*
%if (0%{?suse_version} >= 1500)
%files -n libmfu0-openmpi3
%endif
%{mpi_libdir}/openmpi3/%{mpi_lib_ext}/libmfu.so.*

%files openmpi3-devel
%{mpi_includedir}/openmpi3%{mpi_include_ext}/*
%{mpi_libdir}/openmpi3/%{mpi_lib_ext}/lib*.so
%{mpi_libdir}/openmpi3/%{mpi_lib_ext}/lib*.a
%endif

%if %{with_mpich}
%files mpich
%defattr(-,root,root,-)
%{mpi_libdir}/mpich/bin/*
%{mpi_libdir}/mpich/share/man/*
%if (0%{?suse_version} >= 1500)
%files -n libmfu0-mpich
%endif
%{mpi_libdir}/mpich/%{mpi_lib_ext}/libmfu.so.*

%files mpich-devel
%{mpi_includedir}/mpich%{mpi_include_ext}/*
%{mpi_libdir}/mpich/%{mpi_lib_ext}/lib*.so
%{mpi_libdir}/mpich/%{mpi_lib_ext}/lib*.a
%endif

%changelog
* Fri Oct 21 2022 Dalton A. Bohning <dalton.bohning@intel.com> - 0.11.1-3
- Rebuilt for breaking DAOS API change

* Mon Mar 14 2022 Mohamad Chaarawi <mohamad.chaarawi@intel.com> - 0.11.1-2
- Update to build with HDF5 1.13.1

* Thu Feb 24 2022 Dalton A. Bohning <daltonx.bohning@intel.com> - 0.11.1-1
- Update to v0.11.1 + patch 356cb83d36a9243e30fe8a1bbc83e81fc46d2be2
- Remove patch2, which was merged into v0.11.1
- Remove unused WITH_CART_PREFIX
- Add libattr-devel dependency - now required for xattrs

* Fri Nov 12 2021 Wang Shilong <shilong.wang@intel.com> - 0.11-10
- Rebuilt for breaking DAOS API change
- Add patch to work with libdaos.so.2

* Wed Sep 29 2021 Danielle M. Sikich <danielle.sikich@intel.com> - 0.11-9
- Update to patch bdc379b

* Fri Aug 20 2021 Danielle M. Sikich <danielle.sikich@intel.com> - 0.11-8
- Update to patch 588e665

* Fri Jul 16 2021 Danielle M. Sikich <danielle.sikich@intel.com> - 0.11-7
- Update to patch 67f44ad

* Wed Jun 16 2021 Dalton A. Bohning <daltonx.bohning@intel.com> - 0.11-6
- Update to patch 3746c05

* Mon May 17 2021 Brian J. Murrell <brian.murrell@intel.com> - 0.11-5
- Package for openmpi on EL8

* Mon May 03 2021 Dalton A. Bohning <daltonx.bohning@intel.com> - 0.11-4
- Update to patch bdf06d4

* Tue Apr 06 2021 Dalton A. Bohning <daltonx.bohning@intel.com> - 0.11-3
- Update to patch 5525560

* Fri Mar 12 2021 Dalton A. Bohning <daltonx.bohning@intel.com> - 0.11-2
- Update to patch b0d402d
- Added libuuid-devel dependency
- Build with HDF5 support

* Thu Feb 04 2021 Dalton A. Bohning <daltonx.bohning@intel.com> - 0.11-1
- Update to version 0.11
- Remove libarchive dependency

* Wed Jan 20 2021 Kenneth Cain <kenneth.c.cain@intel.com> - 0.10.1-6
- update to daos major version 1 for libdaos API update

* Sat Dec 19 2020 Dalton A. Bohning <daltonx.bohning@intel.com> - 0.10.1-5
- Update to 1ed76ea, now that daos is ready

* Tue Dec 15 2020 Brian J. Murrell <brian.murrell@intel.com> - 0.10.1-4
- Revert update to 7c32b9c as it breaks compatibility

* Mon Dec 14 2020 Dalton A. Bohning <daltonx.bohning@intel.com> - 0.10.1-3
- Updated to latest patch file 0.10.1...7c32b9c
- Include relval in Release

* Tue Nov 10 2020 Dalton A. Bohninc <daltonx.bohning@intel.com> - 0.10.1-2
- Moved Provides from libmfu* to <mpi>*

* Tue Sep 29 2020 Brian J. Murrell <brian.murrell@intel.com> - 0.10.1-1
- Initial package

PR-repos: daos@PR-3347:212- Package for multiple MPI stacks and multiple distros
- Updated to latest patch file 0.10.1...4ec7841.patch
