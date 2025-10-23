# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""Pratidoc CLI entrypoint."""

from __future__ import annotations

import pathlib
import typing

from importlib.metadata import version

import lintkit
import loadfig

from pratidoc._files import FILES

if typing.TYPE_CHECKING:
    from collections.abc import Iterable

NAME = "pratidoc"

lintkit.settings.name = NAME.upper()

# Import all rules to register them (side-effect)
from pratidoc._rule import (  # noqa: E402
    rule,  # noqa: F401  # pyright: ignore[reportUnusedImport]
)


def _files() -> Iterable[pathlib.Path]:
    """Files to lint.

    Note:
        The files listed __may not exist__, therefore
        only the ones existing will be yielded.

    Yields:
        Small set of files to be checked against the rules.

    """
    # Empty extensions checked as well, e.g. DCO or CODEOWNERS
    extensions = {"", ".md", ".rst", ".txt", ".cff"}

    for f in FILES:
        for e in extensions:
            if (
                p := pathlib.Path(f.name.upper()).resolve().with_suffix(e)
            ).exists():
                yield p


def main(
    args: list[str] | None = None,
    include_codes: Iterable[int] | None = None,
    exclude_codes: Iterable[int] | None = None,
) -> None:
    """Run the CLI."""
    config = loadfig.config(NAME.lower())

    lintkit.registry.inject("config", config)

    if include_codes is None:  # pragma: no cover
        include_codes = config.get("include_codes")
    if exclude_codes is None:  # pragma: no cover
        exclude_codes = config.get("exclude_codes")

    lintkit.cli.main(
        version=version(NAME),
        files_default=_files(),
        include_codes=include_codes,
        exclude_codes=exclude_codes,
        end_mode=config.get("end_mode", "all"),
        pass_files=False,
        args=args,
        description="pratidoc - ensure essential documentation is present.",
    )
