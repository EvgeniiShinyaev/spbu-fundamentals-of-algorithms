import queue
from time import perf_counter


class Maze:
    def __init__(self, list_view: list[list[str]]) -> None:
        self.list_view = list_view
        self.start_j = None
        self.end_pos = None
        for j, sym in enumerate(self.list_view[0]):
            if sym == "O":
                self.start_j = j
        for j, sym in enumerate(self.list_view[-1]):
            if sym == "X":
                self.end_pos = (len(list_view) - 1, j)

    @classmethod
    def from_file(cls, filename):
        list_view = []
        with open(filename, "r") as f:
            for l in f.readlines():
                list_view.append(list(l.strip()))
        obj = cls(list_view)
        return obj

    def is_valid(self, i: int, j: int) -> bool:
        if not (0 <= i < len(self.list_view)) or not (
                0 <= j < len(self.list_view[0])
        ):
            return False
        elif (
                self.list_view[i][j] == "#"
        ):
            return False
        return True

    def print(self, path="") -> None:
        # Find the path coordinates
        i = 0  # in the (i, j) pair, i is usually reserved for rows and j is reserved for columns
        j = self.start_j
        path_coords = set()
        for move in path:
            i, j = _shift_coordinate(i, j, move)
            path_coords.add((i, j))
        # Print maze + path
        for i, row in enumerate(self.list_view):
            for j, sym in enumerate(row):
                if (i, j) in path_coords:
                    print("+ ", end="")  # NOTE: end is used to avoid linebreaking
                else:
                    print(f"{sym} ", end="")
            print()  # linebreak


def solve(maze: Maze):
    q = queue.Queue()
    path_model = {"value": "", "coords": (0, maze.start_j)}
    path = path_model.copy()
    q.put(path)
    while path["coords"] != maze.end_pos:
        path = q.get()
        for move in _possible_moves(path["value"]):
            new_path = path_model.copy()
            new_path["value"] = path["value"] + move
            new_path["coords"] = _shift_coordinate(path["coords"][0], path["coords"][1], move)
            if maze.is_valid(new_path["coords"][0], new_path["coords"][1]):
                q.put(new_path)
    res = path["value"]
    print(f"Found: {res}")
    maze.print(res)


def _shift_coordinate(i: int, j: int, move: str) -> tuple[int, int]:
    if move == "L":
        j -= 1
    elif move == "R":
        j += 1
    elif move == "U":
        i -= 1
    elif move == "D":
        i += 1
    return i, j

def _possible_moves(path: str) -> list[str]:
    moves = ["L", "R", "U", "D"]
    if not path:
        return moves
    last_move = path[-1]
    if last_move == "L":
        moves.remove("R")
    elif last_move == "R":
        moves.remove("L")
    elif last_move == "U":
        moves.remove("D")
    elif last_move == "D":
        moves.remove("U")
    return moves


if __name__ == "__main__":
    maze = Maze.from_file("./maze_2.txt")
    t_start = perf_counter()
    solve(maze)
    t_end = perf_counter()
    print(f"Elapsed time: {t_end - t_start} sec")
