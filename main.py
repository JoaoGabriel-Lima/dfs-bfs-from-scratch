from dfs.dfs import DFS
from maze.maze import Maze


def main():
    maze = Maze("2.maze.example.txt")
    maze.load()

    dfs = DFS(maze=maze)

    result = dfs.search(start=maze.startNode)
    print(f"DFS result: {result}")
    print(f"Number of visited nodes: {len(dfs.visited)}")
    if result:
        print("Getting path")
        path = dfs.get_path(start=maze.startNode, end=maze.endNode)
        print(f"Path found: {path}")
        for step in path:
            print(f"[{step.x}, {step.y}]", end="")
            print(" -> ", end="")
        print("\n")

    maze.reader.reconstruct_text(maze.mazeGraph)


if __name__ == "__main__":
    main()