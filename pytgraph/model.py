from dataclasses import dataclass
from typing import List

class Graph():
    nodes: Node = []
    edges: Edge = []
    directed: bool = True


class Node():
    name: str
    labels: List[str] = []
    color: str = ""
    size: float = 1.0
    url: str = ""

    

class Edge():
    src: str 
    dst: str
    label: str = ""
    color: str = ""
    size: float = 1.0

    