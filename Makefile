# SPDX-License-Identifier: BSD-2-Clause-Patent
# Copyright (c) 2020-2024 Intel Corporation

NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := 978ed4f8b14815671362e1d05914282a12b4a619
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
