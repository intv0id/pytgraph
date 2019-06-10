from ._version import version_info, __version__

from .tgraph import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'tgraph',
        'require': 'tgraph/extension'
    }]
