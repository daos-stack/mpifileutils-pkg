NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := 356cb83d36a9243e30fe8a1bbc83e81fc46d2be2
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
