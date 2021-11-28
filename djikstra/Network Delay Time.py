import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        direction = {}
        for i in range(1, n+1):
            graph[i] = []
            direction[i] = float('inf')
        direction[k] = 0
        
        for u, v, w in times:
            graph[u].append([v, w])

        q = [(0, k)]
        _maxtime = -1
        while q:
            curr_time, curr_node = heapq.heappop(q)
            if curr_time > direction[curr_node]:
                continue
            for next_node, time in graph[curr_node]:
                new_time = curr_time + time
                
                if new_time < direction[next_node]:
                    direction[next_node] = new_time
                    heapq.heappush(q, (new_time, next_node))
      
        for i in direction:
            if direction[i] == float('inf'):
                return -1
            if i!= k:
                _maxtime = max(_maxtime, direction[i])
        return _maxtime