# SPDX-License-Identifier: BSD-2-Clause-Patent
# Copyright (c) 2020-2024 Intel Corporation

NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := 0a4c530bca5dc2476418a3833a15ab812d636e78
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
