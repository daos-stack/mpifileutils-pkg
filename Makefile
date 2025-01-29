# SPDX-License-Identifier: BSD-2-Clause-Patent
# Copyright (c) 2020-2024 Intel Corporation

NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := f69dae3d8e4ddd167dc9aa324e1ddcf8db8c5a64
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
