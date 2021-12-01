NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := 49b04c1
GITHUB_PROJECT := hpc/$(NAME)

RPM_BUILD_OPTIONS := $(BUILD_DEFINES)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
