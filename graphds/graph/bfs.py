from graphds.test.wordladder import buildGraph
from lineards.linear.queue import Queue


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = getPred()
    print(x.getId())


if __name__ == '__main__':
    wordgraph = buildGraph('')
    bfs(wordgraph, wordgraph.getVertex('FOOL'))
    traverse(wordgraph.getVertex('SAGE'))
