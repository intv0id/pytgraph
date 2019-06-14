#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'examples'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Introduction

#%%
from pytgraph import pytgraphWidget, Graph, Node, Edge

#%%
graph = Graph(
    nodes=[Node(name="a"), Node(name="b")],
    edges=[Edge(src="a", dst="b")],
    directed = True
)

#%%
w = pytgraphWidget(g)
w


