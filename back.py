import numpy as np
from random import randint


class Array:
    def __init__(self, n_column, n_row):
        self.array = np.zeros((n_column, n_row), dtype=bool)
        self.n_column, self.n_row = n_column, n_row
        self.birth_list, self.death_list = [], []

    def random_filling(self):
        for i in range(self.n_row):
            for j in range(self.n_column):
                self.fill_array(j, i, randint(0,1))
    def fill_array(self, x, y, value):
        self.array[y][x] = value

    def turn(self):
        self.birth_list, self.death_list = [], []
        self.birth_death_append()
        self.change_cells_status()

    def birth_death_append(self):
        for i in range(self.n_row):
            for j in range(self.n_column):
                if self.is_alive(j, i):
                    if self.will_die(j, i):
                        self.death_list.append((j, i))
                else:
                    if self.will_born(j, i):
                        self.birth_list.append((j, i))

    def change_cells_status(self):
        for e in self.birth_list:
            self.array[e[1], e[0]] = True
        for e in self.death_list:
            self.array[e[1], e[0]] = False

    def _how_many_neighbours_alive(self, x, y):
        alive_neighbours = 0

        for i in range(max(0, y - 1), min(len(self.array), y + 2)):
            for j in range(max(0, x - 1), min(len(self.array[0]), x + 2)):
                alive_neighbours += self.array[i, j]
        alive_neighbours -= self.array[y, x]
        return alive_neighbours

    def is_alive(self, x, y):
        return self.array[y, x]

    def will_die(self, x, y):
        neighbours_alive = self._how_many_neighbours_alive(x, y)
        if neighbours_alive < 2 or neighbours_alive > 3:
            return True

    def will_born(self, x, y):
        if self._how_many_neighbours_alive(x, y) == 3:
            return True

    def __iter__(self):
        return iter(self.array)


if __name__ == "__main__":
    array = Array(10, 10)
    array.random_filling()
    for row in array:
        for column in row:
            if column:
                print("-", end="")
            else:
                print(" ", end="")
        print("")
    print("")
    array.turn()
    for row in array:
        for column in row:
            if column:
                print("-", end="")
            else:
                print(" ", end="")
        print("")
