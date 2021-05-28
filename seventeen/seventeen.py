from helpers import ReadLines
from functools import lru_cache


class Cube:
    def __init__(self, coordinates: list[int], state: bool = False):
        self.state = state
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

    def __repr__(self):
        return (
            f"This cube is {'active' if self.state else 'inactive'} and has "
            f"coordinates {self.x, self.y, self.z}"
        )

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def coords(self):
        return self.x, self.y, self.z


class Space(ReadLines):
    def __init__(self, file_input):
        super(Space, self).__init__("seventeen", file_input)
        self.cubes = []
        self.process_initial(self.inputs)

    def process_initial(self, initial_state: list[str]):
        initial_state.reverse()
        rows = initial_state
        for y, row in enumerate(rows):
            for x, cell in enumerate(row):
                state = True if cell == "#" else False
                self.cubes.append(Cube([x, y, 0], state))

        return None

    def get_neighbours(self, cube: Cube) -> list[Cube]:
        neighbours = []
        for x in range(cube.x - 1, cube.x + 2):
            for y in range(cube.y - 1, cube.y + 2):
                for z in range(cube.z - 1, cube.z + 2):
                    if (x, y, z) == (cube.x, cube.y, cube.z):
                        pass
                    else:
                        neighbours.append(self.find_cube(x, y, z))
        return neighbours

    def find_cube(self, x: int, y: int, z: int) -> Cube:
        next_cube = filter(
            lambda cube: cube.x == x and cube.y == y and cube.z == z, self.cubes
        )
        try:
            cube = next(next_cube)
        except StopIteration:
            cube = Cube([x, y, z])
        return cube

    def iterate(self):
        current_cubes = set()
        new_cubes = set()
        for cube in self.cubes:
            current_cubes.update(self.get_neighbours(cube))
        for cube in current_cubes:
            new_cubes.add(
                Cube(list(cube.coords()), self.active_in_next_iteration(cube))
            )
        self.cubes = list(set(new_cubes))

    def active_in_next_iteration(self, target: Cube):
        neighbours = self.get_neighbours(target)
        active_neighbours = [cube for cube in neighbours if cube.state]
        if (target.state and 3 >= len(active_neighbours) >= 2) or (
            not target.state and len(active_neighbours) == 3
        ):
            return True
        else:
            return False
