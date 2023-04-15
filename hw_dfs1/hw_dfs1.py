class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n
        visited[0] = True

        def dfs(curr):
            for key in rooms[curr]:
                if not visited[key]:
                    visited[key] = True
                    dfs(key)

        dfs(0)
        return all(visited)
        
import unittest
from hw_dfs1 import Solution

class TestCanVisitAllRooms(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_all_rooms_unlocked(self):
        rooms = [[1], [2], [3], []]
        self.assertTrue(self.s.canVisitAllRooms(rooms))

    def test_some_rooms_locked(self):
        rooms = [[1,3], [3,0,1], [2], [0]]
        self.assertFalse(self.s.canVisitAllRooms(rooms))

    def test_single_room(self):
        rooms = [[]]
        self.assertTrue(self.s.canVisitAllRooms(rooms))

    def test_two_rooms(self):
        rooms = [[1], []]
        self.assertTrue(self.s.canVisitAllRooms(rooms))

if __name__ == '__main__':
    unittest.main()
