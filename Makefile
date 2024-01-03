NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := 3975d8483c2471c59c599d87516c7cea24bcc032
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
