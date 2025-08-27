from maze.node import MazeNode


class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.frontier: list[MazeNode] = []
        self.visited: list[MazeNode] = []

    def search(self, start: MazeNode):
        self.frontier.append(start)

        while self.frontier:
            current = self.frontier.pop(0)

            if current.visited:
                continue

            self.visited.append(current)
            current.visited = True

            if current.is_goal:
                return True

            for neighbor in current.get_neighbors():
                if not neighbor.visited:
                    neighbor.visited_from = current
                    self.frontier.append(neighbor)

        return False

    def get_path(self, start: MazeNode, end: MazeNode):
        path = []
        current = end
        while current and current != start:
            path.append(current)
            current = current.visited_from
            current.is_path = True
        path.append(start)
        return path[::-1]
