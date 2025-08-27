from bfs.bfs import BFS
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
        print("*"*15)
        path = dfs.get_path(start=maze.startNode, end=maze.endNode)
        print(f"It took {len(path)} steps to reach the goal.")
        for step in path:
            print(f"[{step.x}, {step.y}]", end="")
            print(" -> ", end="")
        print("END")
        print("\n")

    maze.reader.reconstruct_text(maze.mazeGraph, "BFS")

    print("*"*20)
    print("\n")
    maze.load()
    bfs = BFS(maze=maze)
    result = bfs.search(start=maze.startNode)
    print(f"BFS result: {result}")
    print(f"Number of visited nodes: {len(bfs.visited)}")
    if result:
        print("*"*15)
        path = bfs.get_path(start=maze.startNode, end=maze.endNode)
        print(f"It took {len(path)} steps to reach the goal.")
        for step in path:
            print(f"[{step.x}, {step.y}]", end="")
            print(" -> ", end="")
        print("END")
        print("\n")

    maze.reader.reconstruct_text(maze.mazeGraph, "BFS")


if __name__ == "__main__":
    main()
