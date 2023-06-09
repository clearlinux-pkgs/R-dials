#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-dials
Version  : 1.2.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/dials_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dials_1.2.0.tar.gz
Summary  : Tools for Creating Tuning Parameter Values
Group    : Development/Tools
License  : MIT
Requires: R-DiceDesign
Requires: R-cli
Requires: R-dplyr
Requires: R-glue
Requires: R-hardhat
Requires: R-lifecycle
Requires: R-pillar
Requires: R-purrr
Requires: R-rlang
Requires: R-scales
Requires: R-tibble
Requires: R-vctrs
Requires: R-withr
BuildRequires : R-DiceDesign
BuildRequires : R-cli
BuildRequires : R-dplyr
BuildRequires : R-glue
BuildRequires : R-hardhat
BuildRequires : R-kernlab
BuildRequires : R-lifecycle
BuildRequires : R-pillar
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-scales
BuildRequires : R-tibble
BuildRequires : R-vctrs
BuildRequires : R-withr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
cannot be directly estimated from the data). These tools can be used
    to define objects for creating, simulating, or validating values for
    such parameters.

%prep
%setup -q -n dials

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681754542

%install
export SOURCE_DATE_EPOCH=1681754542
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dials/DESCRIPTION
/usr/lib64/R/library/dials/INDEX
/usr/lib64/R/library/dials/LICENSE
/usr/lib64/R/library/dials/Meta/Rd.rds
/usr/lib64/R/library/dials/Meta/features.rds
/usr/lib64/R/library/dials/Meta/hsearch.rds
/usr/lib64/R/library/dials/Meta/links.rds
/usr/lib64/R/library/dials/Meta/nsInfo.rds
/usr/lib64/R/library/dials/Meta/package.rds
/usr/lib64/R/library/dials/Meta/vignette.rds
/usr/lib64/R/library/dials/NAMESPACE
/usr/lib64/R/library/dials/NEWS.md
/usr/lib64/R/library/dials/R/dials
/usr/lib64/R/library/dials/R/dials.rdb
/usr/lib64/R/library/dials/R/dials.rdx
/usr/lib64/R/library/dials/doc/dials.R
/usr/lib64/R/library/dials/doc/dials.Rmd
/usr/lib64/R/library/dials/doc/dials.html
/usr/lib64/R/library/dials/doc/index.html
/usr/lib64/R/library/dials/help/AnIndex
/usr/lib64/R/library/dials/help/aliases.rds
/usr/lib64/R/library/dials/help/dials.rdb
/usr/lib64/R/library/dials/help/dials.rdx
/usr/lib64/R/library/dials/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/dials/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/dials/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/dials/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/dials/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/dials/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/dials/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/dials/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/dials/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/dials/help/figures/logo.png
/usr/lib64/R/library/dials/help/paths.rds
/usr/lib64/R/library/dials/html/00Index.html
/usr/lib64/R/library/dials/html/R.css
/usr/lib64/R/library/dials/tests/testthat.R
/usr/lib64/R/library/dials/tests/testthat/_snaps/aaa_unknown.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/aaa_values.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/constructors.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/encode_unit.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/extract.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/finalize.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/grids.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/misc.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/parameters.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/pull_dials_object.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/space_filling.md
/usr/lib64/R/library/dials/tests/testthat/_snaps/validation.md
/usr/lib64/R/library/dials/tests/testthat/helper-s3.R
/usr/lib64/R/library/dials/tests/testthat/helper-skip_if_below_r_version.R
/usr/lib64/R/library/dials/tests/testthat/test-aaa_ranges.R
/usr/lib64/R/library/dials/tests/testthat/test-aaa_unknown.R
/usr/lib64/R/library/dials/tests/testthat/test-aaa_values.R
/usr/lib64/R/library/dials/tests/testthat/test-compat-dplyr-old-parameters.R
/usr/lib64/R/library/dials/tests/testthat/test-compat-dplyr-parameters.R
/usr/lib64/R/library/dials/tests/testthat/test-compat-vctrs-helpers-parameters.R
/usr/lib64/R/library/dials/tests/testthat/test-compat-vctrs-parameters.R
/usr/lib64/R/library/dials/tests/testthat/test-constructors.R
/usr/lib64/R/library/dials/tests/testthat/test-encode_unit.R
/usr/lib64/R/library/dials/tests/testthat/test-extract.R
/usr/lib64/R/library/dials/tests/testthat/test-finalize.R
/usr/lib64/R/library/dials/tests/testthat/test-grids.R
/usr/lib64/R/library/dials/tests/testthat/test-misc.R
/usr/lib64/R/library/dials/tests/testthat/test-parameters.R
/usr/lib64/R/library/dials/tests/testthat/test-params.R
/usr/lib64/R/library/dials/tests/testthat/test-pull_dials_object.R
/usr/lib64/R/library/dials/tests/testthat/test-space_filling.R
/usr/lib64/R/library/dials/tests/testthat/test-type_sum.R
/usr/lib64/R/library/dials/tests/testthat/test-validation.R
