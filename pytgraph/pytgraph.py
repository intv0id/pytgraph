#!/usr/bin/env python
# coding: utf-8

from ipywidgets import DOMWidget
from traitlets import Unicode, Instance
from ._frontend import module_name, module_version

from .model import Graph


class pytgraphWidget(DOMWidget):
    _model_name = Unicode('pytgraphModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('pytgraphView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    graph = Instance(klass=Graph).tag(sync=True)