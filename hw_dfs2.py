class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
        
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x_root, y_root = find(x), find(y)
            if x_root == y_root:
                return False
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1
            return True
        
        for u, v in connections:
            union(u, v)
        
        components = set(find(x) for x in range(n))
        cables_needed = len(components) - 1
        
        return cables_needed

import unittest
from hw_dfs2 import Solution

class TestMakeConnected(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_make_connected_1(self):
        n = 4
        connections = [[0,1],[0,2],[1,2]]
        self.assertEqual(self.s.makeConnected(n, connections), 1)

    def test_make_connected_2(self):
        n = 6
        connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
        self.assertEqual(self.s.makeConnected(n, connections), 2)

    def test_make_connected_3(self):
        n = 6
        connections = [[0,1],[0,2],[0,3],[1,2]]
        self.assertEqual(self.s.makeConnected(n, connections), -1)

    def test_make_connected_4(self):
        n = 5
        connections = [[0,1],[1,2],[2,3],[3,4],[0,4]]
        self.assertEqual(self.s.makeConnected(n, connections), 0)

if __name__ == '__main__':
    unittest.main()
