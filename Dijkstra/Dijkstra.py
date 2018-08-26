import heapq
import collections
def Dijkstra(start,graph):
    visited={start:0}
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,cur=heapq.heappop(q)
        for l,nnd in graph[cur]:
            if nnd not in visited or visited[nnd]>l+dist:
                visited[nnd]=l+dist
                heapq.heappush(q,(l+dist,nnd))
    return visited

if __name__ == '__main__':
    graph=collections.defaultdict(set)
    raw=input("type in the edge information follow the format: weight1.edge_a1.edge_b1,weight2.edge_a2.edge_b2")
    raw=raw.split(",")
    for tmp in raw:
        w,a,b=tmp.split(".")
        w=int(w)
        graph[a].add((w,b))
        graph[b].add((w,a))
    start=input("type in the start node")
    print("*"*15)
    print("\n")
    print(f"visited: {Dijkstra(start,graph)}")



