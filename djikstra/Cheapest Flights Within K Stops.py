import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        direction = {}
        graph = [[] for _ in range(n)]
        
        for u, v, c in flights:
            graph[u].append([v, c])
        for i in range(n):
            direction[i] = [float('inf'), -1]
        direction[src][0] = 0
     
       
        q = [(-1, 0, src)]
        while q:
            
            stop, curr_cost, curr_dest = heapq.heappop(q)
            if stop > direction[curr_dest][1]:
                continue
            for next_dest, cost in graph[curr_dest]:
                new_cost = curr_cost + cost
                s = stop + 1
                if new_cost < direction[next_dest][0] and k >= direction[next_dest][1] and s <= k:
                   
                    direction[next_dest][0] = new_cost
                    direction[next_dest][1] = s
                    heapq.heappush(q, (s, new_cost, next_dest))
          
        if direction[dst][0] == float('inf'):
            return -1
        return direction[dst][0]
        
        