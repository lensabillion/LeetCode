# https://leetcode.com/problems/path-with-maximum-probability/
"""
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        direction = {}
        for i in range(n):
            graph[i] = []
            direction[i] = float('-inf')
        for i in range(len(edges)):
            edges[i].append(succProb[i])
        direction[start] = -1
        
        for u, v, w in edges:
            graph[u].append([v,w])
            graph[v].append([u, w])
       
        q = [(-1, start)]
        while q:
            curr_prob, curr_node = heapq.heappop(q)
            if -1 * curr_prob < direction[curr_node]:
                continue
            for next_node, prob in graph[curr_node]:
                new_prob = curr_prob * prob
                
                if -1 * new_prob > direction[next_node]:
                    direction[next_node] = -1 * new_prob
                    heapq.heappush(q,(new_prob, next_node))
        
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
                
                
                
                
                
                
