class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def bob_dfs(curr_node, prev_node, count):
            if curr_node == 0:
                return count
            if prev_node != None and len(graph[curr_node]) == 1 and curr_node != 0:
                return -1
            
            for node in graph[curr_node]:
                if node == prev_node:
                    continue
                res = bob_dfs(node, curr_node, count + 1)
                if res != -1:
                    if count < (res + 1) // 2:
                        amount[curr_node] = 0
                    if res % 2 == 0 and res // 2 == count:
                        amount[curr_node] /= 2
                    return res
            return -1  
        
        bob_dfs(bob, None, 0)
        leafs_res = []
        
        def sum_dfs(curr_node, curr_sum, prev_node):
            if len(graph[curr_node]) == 1 and curr_node != 0:
                leafs_res.append(curr_sum + amount[curr_node])
            
            for node in graph[curr_node]:
                if node == prev_node:
                    continue
                sum_dfs(node, curr_sum + amount[curr_node], curr_node)
        
        sum_dfs(0, 0, None)
        
        res = max(leafs_res)
        if res % 1 == 0:
            return int(res)
        else:
            return res
            
            
LEETCODE SUBMISSION LINK :https://leetcode.com/problems/most-profitable-path-in-a-tree/solutions/3004051/most-profitable-path-in-a-tree-solution/
