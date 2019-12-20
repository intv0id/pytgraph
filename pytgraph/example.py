#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Clément Trassoudaine.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget, register
from traitlets import Unicode, Instance, List, Dict
from ._frontend import module_name, module_version
from .types import GraphData

@register
class GraphWidget(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('GraphModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('GraphView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    nodes = Dict(default_value={}).tag(sync=True)
    vertices = List(default_value=[]).tag(sync=True)
