from dataclasses import dataclass
from typing import List

@dataclass
class GraphOptions:
    pass

@dataclass
class Edge:
    src: str
    dst: str
    color: str = None
    size: float = None

@dataclass
class Node:
    name: str
    color: str = None
    size: str = None
    label: str = None
    url: str = None


@dataclass
class Graph:
    edges: List[Edge]
    nodes: List[Node]
    directed: bool = True


