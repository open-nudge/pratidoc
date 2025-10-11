<!--
SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
SPDX-FileContributor: szymonmaszke <github@maszke.co>

SPDX-License-Identifier: Apache-2.0
-->

# pratidoc

<!-- mkdocs remove start -->

<!-- vale off -->

<!-- pyml disable-num-lines 30 line-length-->

<p align="center">
    <em>Lint your repository docs - ensure the essentials are always there.</em>
</p>

<div align="center">

<a href="https://pypi.org/project/pratidoc">![PyPI - Python Version](https://img.shields.io/pypi/v/pratidoc?style=for-the-badge&label=release&labelColor=grey&color=blue)
</a>
<a href="https://pypi.org/project/pratidoc">![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fopen-nudge%2Fpratidoc%2Fmain%2Fpyproject.toml&style=for-the-badge&label=python&labelColor=grey&color=blue)
</a>
<a href="https://opensource.org/licenses/Apache-2.0">![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)
</a>
<a>![Coverage Hardcoded](https://img.shields.io/badge/coverage-100%25-green?style=for-the-badge)
</a>
<a href="https://scorecard.dev/viewer/?uri=github.com/open-nudge/pratidoc">![OSSF-Scorecard Score](https://img.shields.io/ossf-scorecard/github.com/open-nudge/pratidoc?style=for-the-badge&label=OSSF)
</a>

</div>

<p align="center">
✨ <a href="#features">Features</a>
🚀 <a href="#quick-start">Quick start</a>
📚 <a href="https://open-nudge.github.io/pratidoc">Documentation</a>
🤝 <a href="#contribute">Contribute</a>
👍 <a href="https://github.com/open-nudge/pratidoc/blob/main/ADOPTERS.md">Adopters</a>
📜 <a href="#legal">Legal</a>
</p>
<!-- vale on -->

______________________________________________________________________

<!-- mkdocs remove end -->

## Features

__pratidoc__ is a __documentation checker__ which verifies if your project
contains a set of essential documentation files:

- __Well-defined files__: Only the files common in large open source projects
    are searched for.
- __Comprehensive choice__: Documents from a wide range of categories
    (like legal, governance, security, community, etc.) are included.
- __Link to source__: Wherever applicable each rule points to the
    official/well-respected resource with more information regarding it.

## Table of contents

- [Quick start](#quick-start)
    - [Installation](#installation)
    - [Usage](#usage)
- [Advanced](#advanced)
    - [Configuration](#configuration)
    - [Run as a pre-commit hook](#run-as-a-pre-commit-hook)
    - [Rules](#rules)

## Quick start

### Installation

> [!TIP]
> You can use your favorite package manager like
> [`uv`](https://github.com/astral-sh/uv),
> [`hatch`](https://github.com/pypa/hatch)
> or [`pdm`](https://github.com/pdm-project/pdm)
> instead of `pip`.

```sh
> pip install pratidoc
```

### Usage

To check against the rules run the following from the command line:

```sh
> pratidoc check
```

> [!NOTE]
> The command should be ran from the directory which we want to verify
> __and no path(s) should be passed as arguments!__

an example output could be:

```sh
> ALL:-:-: PRATIDOC1 Multiple README files exist.
```

> [!NOTE]
> This is a __repo-wide linter__, therefore it will not point to a specific
> line, instead `ALL:-:-:` means that the rule was violated in
> current working directory.

## Advanced

### Configuration

You can configure `pratidoc` in `pyproject.toml` (or `.pratidoc.toml`
in the root of your project, just remove the `[tool.pratidoc]` section),
for example:

```toml
[tool.pratidoc]
# include rules by their code
include_codes = [1, 2, 5] # default: all rules included
# exclude rules by their code (takes precedence over include)
exclude_codes = [4, 5, 6] # default: no rules excluded
# whether to exit after first error or all errors
end_mode = "first" # default: "all"
```

> [!WARNING]
> You can only disable rules via include/exclude codes as shown above.

### Run as a pre-commit hook

`pratidoc` can be used as a pre-commit hook, to add as a plugin:

```yaml
repos:
-   repo: "https://github.com/open-nudge/pratidoc"
    rev: ...  # select the tag or revision you want, or run `pre-commit autoupdate`
    hooks:
    -   id: "pratidoc"
```

### Rules

> [!TIP]
> Run `pratidoc rules` to see the list of available rules.

`pratidoc` provides the following rules (links omitted for brevity):

| Name       | Enabled | Description                                      |
| ---------- | ------- | ------------------------------------------------ |
| PRATIDOC0  | True    | File README should be defined.                   |
| PRATIDOC1  | True    | Only one README file should be defined.          |
| PRATIDOC2  | True    | File SECURITY should be defined.                 |
| PRATIDOC3  | True    | Only one SECURITY file should be defined.        |
| PRATIDOC4  | True    | File LICENSE should be defined.                  |
| PRATIDOC5  | True    | Only one LICENSE file should be defined.         |
| PRATIDOC6  | True    | File CHANGELOG should be defined.                |
| PRATIDOC7  | True    | Only one CHANGELOG file should be defined.       |
| PRATIDOC8  | True    | File CITATION should be defined.                 |
| PRATIDOC9  | True    | Only one CITATION file should be defined.        |
| PRATIDOC10 | True    | File DCO should be defined.                      |
| PRATIDOC11 | True    | Only one DCO file should be defined.             |
| PRATIDOC12 | True    | File ADOPTERS should be defined.                 |
| PRATIDOC13 | True    | Only one ADOPTERS file should be defined.        |
| PRATIDOC14 | True    | File CODE_OF_CONDUCT should be defined.          |
| PRATIDOC15 | True    | Only one CODE_OF_CONDUCT file should be defined. |
| PRATIDOC16 | True    | File ROADMAP should be defined.                  |
| PRATIDOC17 | True    | Only one ROADMAP file should be defined.         |
| PRATIDOC18 | True    | File CODEOWNERS should be defined.               |
| PRATIDOC19 | True    | Only one CODEOWNERS file should be defined.      |
| PRATIDOC20 | True    | File GOVERNANCE should be defined.               |
| PRATIDOC21 | True    | Only one GOVERNANCE file should be defined.      |
| PRATIDOC22 | True    | File CONTRIBUTING should be defined.             |
| PRATIDOC23 | True    | Only one CONTRIBUTING file should be defined.    |
| PRATIDOC24 | True    | File SUPPORT should be defined.                  |
| PRATIDOC25 | True    | Only one SUPPORT file should be defined.         |

<!-- pyml disable-num-lines 16 line-length-->

You can consult the following resources to learn more about a given document
(click on the name to go to the resource):

- [`README`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [`SECURITY`](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)
- [`LICENSE`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [`CHANGELOG`](https://keepachangelog.com/en/1.1.0/)
- [`CITATION`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)
- [`DCO`](https://wiki.linuxfoundation.org/dco)
- [`CODE_OF_CONDUCT`](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)
- [`SUPPORT`](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-support-resources-to-your-project)
- [`CONTRIBUTING`](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [`CODEOWNERS`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

<!-- md-dead-link-check: off -->

<!-- mkdocs remove start -->

## Contribute

We welcome your contributions! Start here:

- [Code of Conduct](/CODE_OF_CONDUCT.md)
- [Contributing Guide](/CONTRIBUTING.md)
- [Roadmap](/ROADMAP.md)
- [Changelog](/CHANGELOG.md)
- [Report security vulnerabilities](/SECURITY.md)
- [Open an Issue](https://github.com/open-nudge/pratidoc/issues)

## Legal

- This project is licensed under the _Apache 2.0 License_ - see
    the [LICENSE](/LICENSE.md) file for details.
- This project is copyrighted by _open-nudge_ - the
    appropriate copyright notice is included in each file.

<!-- mkdocs remove end -->

<!-- md-dead-link-check: on -->
