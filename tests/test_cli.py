# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""Smoke test CLI entrypoint."""

from __future__ import annotations

import pathlib

import lintkit

import pytest

from pratidoc import _cli


@pytest.mark.parametrize(
    ("directory", "should_error", "even"),
    (
        (pathlib.Path("tests/cases/fail/none"), True, True),
        (pathlib.Path("tests/cases/fail/multiple"), True, False),
        (pathlib.Path("tests/cases/pass"), False, False),  # last False not used
    ),
)
def test_cli(
    directory: pathlib.Path,
    should_error: bool,  # noqa: FBT001
    even: bool,  # noqa: FBT001
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Smoke test pynudger CLI.

    Args:
        directory:
            Test directory to use as a pseudo-root of the project.
        should_error:
            Whether this directory should error (e.g. due to multiple
                files with the same purpose defined).
        even:
            Whether the error numbers should be even (files missing) or odd
                (multiple files with the same purpose present).
        monkeypatch:
            Pytest fixture to change test's directory.
        capsys:
            Pytest system capture fixture (used for stdout/stderr analysis).

    """
    monkeypatch.chdir(pathlib.Path.cwd() / directory)
    try:
        _cli.main(args=["check"])
    except SystemExit as e:
        if should_error:
            assert e.code == 1  # noqa: PT017
            out, _ = capsys.readouterr()
            for i in (
                i
                for i in lintkit.registry.codes()
                if (even and i % 2 == 0) or (not even and i % 2 != 0)
            ):
                assert f"PRATIDOC{i}" in out
        else:
            assert e.code == 0  # noqa: PT017
