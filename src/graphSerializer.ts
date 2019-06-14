import { Graph } from 'tgraph';

export class GraphSerializer
{
    static deserialize(value: any):  Graph
    {
        let g = new Graph()
        g.deserialize(value)
        return g
    }
    static serialize(value: Graph): any
    {
        return value.serialize()
    }
}