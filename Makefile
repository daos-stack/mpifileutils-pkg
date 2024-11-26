# SPDX-License-Identifier: BSD-2-Clause-Patent
# Copyright (c) 2020-2024 Intel Corporation

NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := b65c188e82f2514faafe4633586e38957755a7b1
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
