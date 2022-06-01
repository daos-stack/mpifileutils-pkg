NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := 6230ed293c69f818aac5a47a0ce3665fc3fafba6
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
