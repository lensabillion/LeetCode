# https://leetcode.com/problems/path-with-maximum-probability/
"""
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        visited = set()
       
        for i in range(len(edges)):
            edges[i].append(succProb[i])
                
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
       
        q = [(-1, start)]
        while q:
            curr_prob, curr_node = heapq.heappop(q)
            
            if curr_node == end:
                return -1 * curr_prob
            if curr_node in visited:
                continue

            for next_node, prob in graph[curr_node]:
                new_prob = curr_prob * prob
                if next_node not in visited:
                    heapq.heappush(q,(new_prob, next_node))
<<<<<<< HEAD
            visited.add(curr_node)
                    
      
        return 0
=======
        
        if direction[end] > 0:
            return direction[end]
        else:
            return 0
    """
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        visited = set()
       
        for i in range(len(edges)):
            edges[i].append(succProb[i])
                
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
       
        q = [(-1, start)]
        while q:
            curr_prob, curr_node = heapq.heappop(q)
            
            if curr_node == end:
                return -1 * curr_prob
            if curr_node in visited:
                continue

            for next_node, prob in graph[curr_node]:
                new_prob = curr_prob * prob
                if next_node not in visited:
                    heapq.heappush(q,(new_prob, next_node))
            visited.add(curr_node)
        return 0
                
                
                
                
>>>>>>> cb5a914ac7f1220a25abae5292f0316d81e7bf86
                
                
