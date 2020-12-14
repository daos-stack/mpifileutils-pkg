NAME       := mpifileutils
SRC_EXT    := gz
REPO_NAME  := mpifileutils-pkg

GIT_SHORT       := $(shell git rev-parse --short=8 HEAD)
GIT_NUM_COMMITS := $(shell git rev-list HEAD --count)

BUILD_DEFINES   := --define "%relval .$(GIT_NUM_COMMITS).g$(GIT_SHORT)"

RPM_BUILD_OPTIONS := $(BUILD_DEFINES)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
