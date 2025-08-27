from maze.node import MazeNode
import os


class MazeReader:
    def __init__(self, file_name):
        self.base_path = "maze/maze-examples/"
        self.file_name: str = file_name
        self.file_path: str = self.base_path + file_name

    def read(self) -> list[str]:
        with open(self.file_path, "r") as file:
            return file.readlines()

    def reconstruct_text(self, mazeGraph, method: str):
        text = ""
        for row in mazeGraph:
            for node in row:
                if node is None:
                    text += "?"
                elif node.is_wall:
                    text += "#"
                elif node.is_start:
                    text += "A"
                elif node.is_goal:
                    text += "B"
                elif node.is_path:
                    text += "O"
                elif node.visited:
                    text += "X"
                else:
                    text += " "
            text += "\n"

        file_path = f"maze/maze-examples/reconstructed/{self.file_name.split('.txt')[0]}.{method}.reconstructed.txt"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        for line in text.splitlines():
            print(line)

        with open(file_path, "w") as file:
            file.write(text)
