NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := 4e172a6f2b31a64ec3673ddcfb870d031fa8b037
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
