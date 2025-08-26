class MazeNode:
    def __init__(self, x: int, y: int, is_start: bool = False, is_goal: bool = False, is_wall: bool = False):
        self.x = x
        self.y = y

        self.visited = False
        self.visited_from = None

        self.is_goal = is_goal
        self.is_start = is_start
        self.is_path = False
        self.is_wall = is_wall

        self.left: MazeNode = None
        self.right: MazeNode = None
        self.up: MazeNode = None
        self.down: MazeNode = None

    def __repr__(self):
        return f"MazeNode({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        if not isinstance(other, MazeNode):
            return False
        return self.x == other.x and self.y == other.y

    def get_neighbors(self):
        neighbors = []
        if self.left:
            neighbors.append(self.left)
        if self.right:
            neighbors.append(self.right)
        if self.up:
            neighbors.append(self.up)
        if self.down:
            neighbors.append(self.down)
        return neighbors