NAME            := mpifileutils
SRC_EXT         := gz
TEST_PACKAGES   := $(NAME)-mpich-devel $(NAME)-openmpi3-devel
REPO_NAME       := mpifileutils-pkg
SOURCE_COMMIT   := 7c32b9cf6143776d798ab8134696b5f4e38916e9
SOURCE          = $(SOURCE_COMMIT).tar.$(SRC_EXT)
GIT_SHORT       := $(shell git rev-parse --short $(SOURCE_COMMIT))
BUILD_DEFINES   := --define "%relval .g$(GIT_SHORT)" --define "%source_commit $(SOURCE_COMMIT)"
RPM_BUILD_OPTIONS := $(BUILD_DEFINES)

$(SOURCE_COMMIT).tar.$(SRC_EXT):
	curl -f -L -O https://github.com/hpc/mpifileutils/archive/$(SOURCE_COMMIT).tar.$(SRC_EXT)

include packaging/Makefile_packaging.mk
