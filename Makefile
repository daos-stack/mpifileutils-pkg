NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
#PKG_GIT_COMMIT := 09193358a53ad55e041be7d778d1932a27dda7ff
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
