import os
import subprocess
import sys
import unittest

# /path/to/demos/graph-partitioning/tests/test_graph_partitioning.py
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDemo(unittest.TestCase):
    def test_smoke(self):
        """run graph_partitioning.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'graph_partitioning.py')
        subprocess.check_output([sys.executable, demo_file])
