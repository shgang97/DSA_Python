from graphds.graph.graph import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time=0
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setColor(-1)
        for aVertex in self:
            if aVertex.getColor():
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time+=1
        startVertex.setDiscover(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor()=='white':
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time+=1
        startVertex.setFinish(self.time)

                
                