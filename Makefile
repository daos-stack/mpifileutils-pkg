NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
GIT_SHORT := b1d9591 

BUILD_DEFINES := --define "git_short $(GIT_SHORT)"

RPM_BUILD_OPTIONS := $(BUILD_DEFINES)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
