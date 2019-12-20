
# pytgraph

A 3D graph visualization Jupyter Widget

[![PyPI - Wheel][pypi-image]][pypi-url]
[![Build Status][build-action-image]][build-action-url]
[![Documentation Status][doc-action-image]][doc-action-url]
[![Release Status][release-action-image]][release-action-url]
[![CodeFactor][codefactor-image]][codefactor-url]
[![Binder][binder-image]][binder-url]

## Installation

You can install using `pip`:

```bash
pip install pytgraph
```

Or if you use jupyterlab:

```bash
pip install pytgraph
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```bash
jupyter nbextension enable --py [--sys-prefix|--user|--system] pytgraph
```

[pypi-url]: https://pypi.org/project/pytgraph/
[pypi-image]: https://img.shields.io/pypi/wheel/pytgraph
[build-action-url]: https://github.com/intv0id/pytgraph/actions?query=workflow%3A%22Build%22
[build-action-image]: https://github.com/intv0id/pytgraph/workflows/Build/badge.svg
[doc-action-url]: https://github.com/intv0id/pytgraph/actions?query=workflow%3A%22Documentation%22
[doc-action-image]: https://github.com/intv0id/pytgraph/workflows/Documentation/badge.svg
[release-action-url]: https://github.com/intv0id/pytgraph/actions?query=workflow%3A%22Release%22
[release-action-image]: https://github.com/intv0id/pytgraph/workflows/Release/badge.svg
[codefactor-url]: https://www.codefactor.io/repository/github/intv0id/pytgraph
[codefactor-image]: https://www.codefactor.io/repository/github/intv0id/pytgraph/badge
[binder-image]: https://mybinder.org/badge_logo.svg
[binder-url]: https://mybinder.org/v2/gh/intv0id/pytgraph/master?filepath=examples
