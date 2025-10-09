# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0
"""Define files to be checked by the pratidoc."""

from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class File:
    """Container with file name and optional link to documentation."""

    name: str
    link: str | None = None


FILES = [
    File(
        "Readme",
        "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes",
    ),
    File(
        "Security",
        "https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository",
    ),
    File(
        "License",
        "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository",
    ),
    File("Changelog", "https://keepachangelog.com/en/1.1.0/"),
    File(
        "Citation",
        "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files",
    ),
    File("DCO", "https://wiki.linuxfoundation.org/dco"),
    File("Adopters"),
    File(
        "Code_Of_Conduct",
        "https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project",
    ),
    File("Roadmap"),
    File(
        "Codeowners",
        "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners",
    ),
    File("Governance"),
    File(
        "Contributing",
        "https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors",
    ),
    File(
        "Support",
        "https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-support-resources-to-your-project",
    ),
]
"""Set of files to be checked by the pratidoc."""
