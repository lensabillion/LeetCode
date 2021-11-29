import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        visited = set()
        graph = [[] for _ in range(n)]
        
        for u, v, c in flights:
            graph[u].append([v, c])
        
        _maxcost = float('inf')
        q = [(0, -1, src)]
        while q:
            
            if len(visited) >= n:
                break
            curr_cost, stop, curr_dest = heapq.heappop(q)
           
            if curr_dest == dst and stop <= k:
                _maxcost = min(_maxcost, curr_cost)
            
            for next_dest, cost in graph[curr_dest]:
                new_cost = curr_cost + cost
                s = stop + 1
                if next_dest not in visited:
                    heapq.heappush(q,(new_cost, s, next_dest))
            visited.add(curr_dest)
        
        if _maxcost == float('inf'):            
            return -1
        return _maxcost