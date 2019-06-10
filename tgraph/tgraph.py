from ipywidgets import register, DOMWidget
from traitlets import Unicode

@register
class tgraph(DOMWidget):
    """A 3D graph view widget"""
    _view_name = Unicode('tgraphView').tag(sync=True)
    _model_name = Unicode('tgraphModel').tag(sync=True)
    _view_module = Unicode('tgraph').tag(sync=True)
    _model_module = Unicode('tgraph').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    value = Unicode('Hello World!').tag(sync=True)
