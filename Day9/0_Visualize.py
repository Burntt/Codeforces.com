import sys
import threading
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict


def visualizeGraph(adjMatrix):
    A = np.asarray(adjMatrix)
    G = nx.from_numpy_matrix(A)

    labels = []
    for i in range(A.shape[0]):
        labels.append(str(i))

    labelMap = dict(zip(G.nodes(), labels))
    nx.draw(G, labels=labelMap, with_labels=True)
    plt.show()


def readLine():
    return list(map(int, input().split()))


############################################################################


n, a, b = readLine()
gM = []
for i in range(n):
    line = readLine()
    gM.append(line)

visualizeGraph(gM)


