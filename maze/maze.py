from maze.node import MazeNode
from maze.reader import MazeReader


class Maze:
    def __init__(self, file_name):
        self.mazeGraph = []
        self.reader = MazeReader(file_name)
        self.startNode = None
        self.endNode = None

    def load(self):
        lines = self.reader.read()

        self.maze = [list(line.rstrip()) for line in lines]
        self.mazeGraph = [[None for _ in range(len(row))] for row in self.maze]

        self.create_nodes()
        self.connect_nodes()

    def create_nodes(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == "A":
                    self.startNode = MazeNode(x, y, is_start=True)
                    self.mazeGraph[y][x] = self.startNode
                    continue
                elif cell == "B":
                    self.endNode = MazeNode(x, y, is_goal=True)
                    self.mazeGraph[y][x] = self.endNode
                    continue

                if cell == "#":
                    self.mazeGraph[y][x] = MazeNode(x, y, is_wall=True)
                    continue

                node = MazeNode(x, y)
                self.mazeGraph[y][x] = node

            
    def connect_nodes(self):
        for y, row in enumerate(self.mazeGraph):
            for x, node in enumerate(row):
                if node is None:
                    continue

                if x > 0 and not self.mazeGraph[y][x - 1].is_wall:
                    node.left = self.mazeGraph[y][x - 1]
                if x < len(row) - 1 and not self.mazeGraph[y][x + 1].is_wall:
                    node.right = self.mazeGraph[y][x + 1]
                if y > 0 and not self.mazeGraph[y - 1][x].is_wall:
                    node.up = self.mazeGraph[y - 1][x]
                if y < len(self.mazeGraph) - 1 and not self.mazeGraph[y + 1][x].is_wall:
                    node.down = self.mazeGraph[y + 1][x]


    def is_path_clear(self, start: MazeNode, end: MazeNode):
        for neighbor in self.get_neighbors(start):
            if neighbor == end:
                return True
        return False
    