"""
Program testing Djikstra Algorithm based ona same example graph with known shortest paths. 
"""

import unittest
from DjikstraAlgorithm import Graph

class DjiATest(unittest.TestCase):
    def test_city(self):
        european_cities_graph = [
        ("London", "Paris", 300), ("London", "Amsterdam", 400),
        ("Paris", "Berlin", 500), ("Paris", "Brussels", 300),
        ("Berlin", "Vienna", 700), ("Berlin", "Prague", 400),
        ("Rome", "Vienna", 1000), ("Rome", "Madrid", 1200),
        ("Amsterdam", "Brussels", 200), ("Brussels", "Vienna", 800)]
    
        result = Graph(european_cities_graph).dijkstar_distance("London")
        
        self.assertEquals(result['London'], 0)
        self.assertEquals(result['Paris'], 300)
        self.assertEquals(result['Amsterdam'], 400)
        self.assertEquals(result['Berlin'], 800)
        self.assertEquals(result['Brussels'], 600)
        self.assertEquals(result['Vienna'], 1400)
        self.assertEquals(result['Prague'], 1200)
        self.assertEquals(result['Rome'], 2400)
        self.assertEquals(result['Madrid'], 3600)
if __name__ == "__main__":
    unittest.main()
