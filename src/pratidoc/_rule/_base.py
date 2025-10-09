# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""Pratidoc base for all rules."""

from __future__ import annotations

import abc


class Base(abc.ABC):
    """Base class for all rules and mixins."""

    @abc.abstractmethod
    def what(self) -> str:
        """Return the stemmed name of the file this rule checks for.

        Note:
            This method is also used to conditionally skip files and provide
            rule messages/information when running `pratidoc rules`

        Returns:
            The stemmed name of the file.
        """

    def link(self) -> str | None:
        """Return link to documentation about the file this rule checks for.

        Returns:
            The link to the documentation or `None` if not available.
        """
        # This method will be dynamically assigned in ./rule.py, but kept
        # "just in case" to always return `None` by default.
        return None  # pragma: no cover
