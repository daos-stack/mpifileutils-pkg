NAME       := mpifileutils
SRC_EXT    := gz
REPO_NAME  := mpifileutils-pkg

TEST_PACKAGES := $(NAME)-daos-mpich-devel $(NAME)-daos-openmpi3-devel "daos-client >= 1.1.1"

include packaging/Makefile_packaging.mk
