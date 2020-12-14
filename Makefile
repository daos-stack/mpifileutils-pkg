NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
GIT_SHORT := 7c32b9c

BUILD_DEFINES := --define "relval .g$(GIT_SHORT)"

RPM_BUILD_OPTIONS := $(BUILD_DEFINES)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
