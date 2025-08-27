# SPDX-License-Identifier: BSD-2-Clause-Patent
# Copyright (c) 2020-2024 Intel Corporation

NAME      := mpifileutils
SRC_EXT   := gz
REPO_NAME := mpifileutils-pkg
PKG_GIT_COMMIT := 11ac26436606ac8dbfac2e51ecd23f73243f415c
GITHUB_PROJECT := hpc/$(NAME)

TEST_PACKAGES := $(NAME)-mpich-devel $(NAME)-openmpi3-devel

include packaging/Makefile_packaging.mk
