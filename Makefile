NAME       := mpifileutils
SRC_EXT    := gz
REPO_NAME  := mpifileutils-pkg

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk