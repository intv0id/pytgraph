pytgraph
===============================

A 3D graph visualization jupyter widget using [tgraph](https://github.com/intv0id/tgraph)

Installation
------------

To install use pip:

``` bash
pip install pytgraph
jupyter nbextension enable --py --sys-prefix pytgraph
```

For a development installation (requires npm),

``` bash
git clone https://github.com/pytgraph.git
cd pytgraph
pip install -e .
jupyter nbextension install --py --symlink --sys-prefix pytgraph
jupyter nbextension enable --py --sys-prefix pytgraph
```
