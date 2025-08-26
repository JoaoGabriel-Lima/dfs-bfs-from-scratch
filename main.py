from maze.maze import Maze


def main():
    maze = Maze("1.maze.example.txt")
    maze.load()
    print(maze.startNode)
    print("-"*10)
    print(maze.startNode.left)
    print(maze.startNode.right)
    print(maze.startNode.down)
    print(maze.startNode.up)
    print("-"*10)
    print(maze.endNode)
    print("-"*10)
    print(maze.endNode.left)
    print(maze.endNode.right)
    print(maze.endNode.up)
    print(maze.endNode.down)
    maze.reader.reconstruct_text(maze.mazeGraph)


if __name__ == "__main__":
    main()