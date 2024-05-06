import pytest
from back import Array


@pytest.fixture(scope="module")
def array_10_x_10_empty():
    return Array(10, 10)


@pytest.fixture(scope="module")
def array_10_x_10_even_numbers_true():
    array = Array(10, 10)
    for i in range(10):
        for j in range(10):
            if not j % 2:
                array.fill_array(j, i, True)
    return array


@pytest.fixture(scope="module")
def array_5_x_5_first_column_true():
    array = Array(5, 5)
    for i in range(5):
        array.fill_array(0, i, True)
    return array


def test_create_array(array_10_x_10_empty):
    assert array_10_x_10_empty.array.size == 100
    assert not array_10_x_10_empty.array.all()


def test_fill_array(array_10_x_10_empty):
    array_10_x_10_empty.fill_array(2, 1, True)
    assert array_10_x_10_empty.array[1][2]


def test_is_alive(array_10_x_10_even_numbers_true):
    assert array_10_x_10_even_numbers_true.is_alive(0, 0)
    assert not array_10_x_10_even_numbers_true.is_alive(1, 0)


def test_how_many_neighbours_alive_border(array_10_x_10_even_numbers_true):
    assert array_10_x_10_even_numbers_true._how_many_neighbours_alive(1, 0) == 4


def test_how_many_neighbours_alive_center(array_10_x_10_even_numbers_true):
    assert array_10_x_10_even_numbers_true._how_many_neighbours_alive(3, 2) == 6


def test_will_die(array_10_x_10_even_numbers_true):
    assert not array_10_x_10_even_numbers_true.will_die(0, 1)
    assert array_10_x_10_even_numbers_true.will_die(1, 1)


def test_will_born(array_5_x_5_first_column_true):
    assert array_5_x_5_first_column_true.will_born(1, 1)
    assert not array_5_x_5_first_column_true.will_born(2, 1)


def birth_death_append(array_5_x_5_first_column_true):
    array_5_x_5_first_column_true.birth_death_append()
    assert array_5_x_5_first_column_true.birth_list == [(1, 1), (2, 1), (3, 1)]
    assert array_5_x_5_first_column_true.death_list == [(0, 0), (4, 0)]


def test_change_cells_status(array_5_x_5_first_column_true):
    array_5_x_5_first_column_true.birth_list = [(1, 1), (1, 2), (1, 3)]
    array_5_x_5_first_column_true.death_list = [(0, 0), (0, 4)]
    array_5_x_5_first_column_true.change_cells_status()
    assert not array_5_x_5_first_column_true.array[0, 0] and not array_5_x_5_first_column_true.array[4, 0]
    assert (array_5_x_5_first_column_true.array[1, 1] and array_5_x_5_first_column_true.array[2, 1] and
            array_5_x_5_first_column_true.array[3, 1])


