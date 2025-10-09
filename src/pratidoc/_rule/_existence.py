# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""Pratidoc rules verifying existence of files."""

from __future__ import annotations

import abc
import typing

import lintkit

from pratidoc._rule._base import Base

if typing.TYPE_CHECKING:
    import pathlib

    from collections.abc import Iterable


class _FileExists(
    lintkit.check.Check,
    lintkit.loader.File,
    lintkit.rule.All,
    Base,
    abc.ABC,
):
    """Base mixin for concrete file existence mixins below."""

    def values(self) -> Iterable[lintkit.Value[pathlib.Path]]:
        """Return value to be checked (path to file)."""
        if self.file is not None:
            yield lintkit.Value(self.file)
        else:  # pragma: no cover
            pass

    def check(self, value: lintkit.Value[pathlib.Path]) -> bool:
        """Check if the file exists.

        Returns:
            `True` if the file exists, `False` otherwise.
        """
        return value.stem == self.what()

    def _info(self, message: str) -> str:
        """Return message with optional link to documentation.

        Args:
            message:
                The message to be displayed with or without link.

        Returns:
            The message with link if available, otherwise just the message.

        """
        if (link := self.link()) is not None:
            return f"{message} Read more here: {link}"
        return message


class Multiple(_FileExists, abc.ABC):
    """Mixin to check if multiple files of the same type exist.

    An example could be multiple README files (e.g. README.md and README.rst).

    """

    def finalize(self, n_fails: int) -> bool:
        """Error out if more than one file exists.

        Args:
            n_fails:
                The number of files found.
        """
        return n_fails > 1

    def message(self) -> str:
        """Return rule error message."""
        return self._info(f"Multiple {self.what()} files exist.")

    def description(self) -> str:
        """Return rule description."""
        return self._info(f"Only one {self.what()} file should be defined.")


class No(_FileExists, abc.ABC):
    """Mixin to check if a specific file exists."""

    def finalize(self, n_fails: int) -> bool:
        """Error out if no file exists."""
        return n_fails < 1

    def message(self) -> str:
        """Return rule error message."""
        return self._info(f"File {self.what()} does not exist.")

    def description(self) -> str:
        """Return rule description."""
        return self._info(f"File {self.what()} should be defined.")
