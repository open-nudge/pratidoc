# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""Pratidoc specific files definition.

Note:
    Rules are created dynamically by iterating over mixins
    defining type of existence and specific file.

"""

from __future__ import annotations

import typing

from pratidoc._files import FILES
from pratidoc._rule import _base, _existence


def binding(what: str | None) -> typing.Callable[[typing.Any], str | None]:
    """Create link or what method for the rule."""

    def method(_: _base.Base) -> str | None:
        """Link or what method from _base.Base."""
        return what

    return method


_existence_mixins = ["No", "Multiple"]

code: int = 0
for f in FILES:
    # Create a file class dynamically feeding it data from _files.py.
    # This approach centralizes potential check additions in _files.py file
    file_type = type(f.name, (_base.Base,), {})
    file_type.what = binding(f.name.upper())  # pyright: ignore[reportAttributeAccessIssue]
    file_type.link = binding(f.link)  # pyright: ignore[reportAttributeAccessIssue]

    # Create No<FILE> and Multiple<FILE> rules
    for e in _existence_mixins:
        _ = type(
            f"{e}{f}",
            (getattr(_existence, e), file_type),
            {},
            code=code,
        )
        code += 1
