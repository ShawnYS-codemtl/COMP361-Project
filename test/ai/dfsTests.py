import unittest
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(os.path.join(project_root, 'src/ai-algos'))

from MapHandler import MapHandler
from DFS import DFS
from Location import Location
from Rover import Rover

class DfsTests(unittest.TestCase):
    def test_goToSimple1(self):
        md = [[[0, 0, 0], [1, 1, 0]]]
        mh = MapHandler(md)
        dfs = DFS()
        fromLoc = Location(0, 0, 0, 0, 0)
        toLoc = Location(0, 1, 1, 1, 0)
        rover = Rover(30)
        path = dfs.goTo(fromLoc, toLoc, rover, mh)
        self.assertEqual(len(path), 2)
        self.assertEqual(path[0].y, 0)
        self.assertEqual(path[1].y, 1)

    def test_goToSimple2(self):
        md = [[[0, 0, 0], [1, 1, 0], [2, 2, 0], [3, 3, 0]]]
        mh = MapHandler(md)
        dfs = DFS()
        fromLoc = Location(0, 1, 1, 1, 0)
        toLoc = Location(0, 3, 3, 3, 0)
        rover = Rover(30)
        path = dfs.goTo(fromLoc, toLoc, rover, mh)
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0].y, 1)
        self.assertEqual(path[1].y, 2)
        self.assertEqual(path[2].y, 3)
        
    def test_visitAllSimple1(self):
        md = [[[0, 0, 0], [1, 1, 0]]]
        mh = MapHandler(md)
        dfs = DFS()
        fromLoc = Location(0, 0, 0, 0, 0)
        toLoc = Location(0, 1, 1, 1, 0)
        rover = Rover(30)
        path = dfs.visitAll(fromLoc, [toLoc], rover, mh)
        self.assertEqual(len(path), 2)
        self.assertEqual(path[0].y, 0)
        self.assertEqual(path[1].y, 1)
        
    def test_visitAllSimple2(self):
        md = [[[0, 0, 0], [1, 1, 0], [2, 2, 0], [3, 3, 0]]]
        mh = MapHandler(md)
        dfs = DFS()
        fromLoc = Location(0, 1, 1, 1, 0)
        toLoc = Location(0, 3, 3, 3, 0)
        rover = Rover(30)
        path = dfs.visitAll(fromLoc, [toLoc], rover, mh)
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0].y, 1)
        self.assertEqual(path[1].y, 2)
        self.assertEqual(path[2].y, 3)
        
    def test_visitAllSimple3(self):
        md = [[[0, 0, 0], [1, 1, 0], [2, 2, 0], [3, 3, 0]]]
        mh = MapHandler(md)
        dfs = DFS()
        fromLoc = Location(0, 1, 1, 1, 0)
        toLoc1 = Location(0, 3, 3, 3, 0)
        toLoc2 = Location(0, 0, 0, 0, 0)
        rover = Rover(30)
        path = dfs.visitAll(fromLoc, [toLoc2, toLoc1], rover, mh)
        self.assertEqual(len(path), 5)
        self.assertEqual(path[0].y, 1)
        self.assertEqual(path[1].y, 0)
        self.assertEqual(path[2].y, 1)
        self.assertEqual(path[3].y, 2)
        self.assertEqual(path[4].y, 3)

    def test_dfsComplexGraph(self):
        # Test with a more complex graph where DFS and BFS might produce different paths
        md = [[[0, 0, 0], [1, 1, 0], [2, 2, 0]],
              [[3, 3, 0], [4, 4, 0], [5, 5, 0]],
              [[6, 6, 0], [7, 7, 0], [8, 8, 0]]]
        mh = MapHandler(md)
        dfs = DFS()
        fromLoc = Location(0, 0, 0, 0, 0)
        toLoc = Location(2, 2, 8, 8, 0)
        rover = Rover(30)
        path = dfs.goTo(fromLoc, toLoc, rover, mh)
        # We just check that a valid path is found
        self.assertGreater(len(path), 0)
        self.assertEqual(path[0].x, 0)
        self.assertEqual(path[0].y, 0)
        self.assertEqual(path[-1].x, 2)
        self.assertEqual(path[-1].y, 2)

if __name__ == '__main__':
    unittest.main()