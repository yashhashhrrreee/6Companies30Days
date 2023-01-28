class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        students_ten = [ sum([2 ** (len(i) - 1 - j) * i[j] for j in range(len(i))]) for i in students]
        mentors_ten = [ sum([2 ** (len(i) - 1 - j) * i[j] for j in range(len(i))]) for i in mentors]
        students_ten = [[students_ten[i], i] for i in range(len(students))]
        mentors_ten = [[mentors_ten[i], i] for i in range(len(mentors))]
        
        res = [[0 for i in range(len(students))]  for j in range(len(students))]
        
        for i in range(len(students)):
            x, i1 = students_ten[i]
            for j in range(len(students)):
                y, i2 = mentors_ten[j]
                z = self.hammingWeight((x ^ y) ^ (2** (len(students[i1])) - 1))
                res[i][j] = z
        m = 0
        if len(students) == 1:
            return res[0][0]
        for i in range(len(students)):
            x = self.bfs((0, i), res, students)
            m = max(m, x)
        return m
            
    
    def hammingWeight(self, n: int) -> int:
        
        num_of_1s = 0
        
        for i in range(64):
            
            num_of_1s += (n & 1)
            
            n = n >> 1
            
        return num_of_1s
    
    def bfs(self, start, grid, students):
        m = 0
        queue = [[start, grid[start[0]][start[1]], [start[1]] ]] 
        while queue:
            index, s, col = queue.pop(0)
            x, y = index
            for i in range(len(students)):
                if i not in col and x < len(students) - 1:
                    queue.append([(x + 1, i), s + grid[x + 1][i], col + [i]])
                    m = max(m, s + grid[x + 1][i])
        return m
