import pytest

import seafarers


def test_ship_should_have_xy():
    sut = seafarers.Ship()
    assert sut.x == 0
    assert sut.y == 0


def test_ship_should_have_heading():
    sut = seafarers.Ship()
    assert sut.heading == 0


@pytest.mark.parametrize("given_heading, expected_heading", [(32, 0), (33, 1), (-1, 31)])
def test_ship_should_set_heading(given_heading, expected_heading):
    sut = seafarers.Ship()
    sut.set_heading(given_heading)
    assert sut.heading == expected_heading


@pytest.mark.parametrize("initial_heading, given_turn, expected_heading", [(0, 1, 1), (0, -1, 31)])
def test_ship_should_turn(initial_heading, given_turn, expected_heading):
    sut = seafarers.Ship()
    sut.set_heading(initial_heading)
    sut.turn(given_turn)
    assert sut.heading == expected_heading


def test_ship_should_have_speed():
    sut = seafarers.Ship()
    assert sut.speed == 1


@pytest.mark.parametrize("given_speed, expected_speed", [(0, 0), (2, 1), (-1, 0)])
def test_ship_should_test_speed(given_speed, expected_speed):
    sut = seafarers.Ship()
    sut.set_speed(given_speed)
    assert sut.speed == expected_speed


@pytest.mark.parametrize("given_heading, expected_x, expected_y", [
    (0, 0, 1),
    (1, 0.1951, 0.9808),
    (27, -0.8315, 0.5556),
    ])
def test_ship_should_move(given_heading, expected_x, expected_y):
    sut = seafarers.Ship()
    sut.set_heading(given_heading)
    sut.move()
    assert sut.x == expected_x
    assert sut.y == expected_y


@pytest.mark.parametrize("given_heading, expected_x, expected_y", [
    (0, 0, 1/2),
    (1, 0.1951/2, 0.9808/2),
    (27, -0.8315/2, 0.5556/2),
    ])
def test_ship_should_move_half(given_heading, expected_x, expected_y):
    sut = seafarers.Ship()
    sut.set_speed(0.5)
    sut.set_heading(given_heading)
    sut.move()
    assert sut.x == expected_x
    assert sut.y == expected_y


def test_islands_should_exist():
    sut = seafarers.Island(0, 0)
    assert sut.x == 0
    assert sut.y == 0


@pytest.mark.parametrize("given_island_x, given_island_y, expected_distance", [(0, 0, 0)])
def test_ship_should_determine_distance_to_island(given_island_x, given_island_y, expected_distance):
    sut = seafarers.Ship()
    island = seafarers.Island(given_island_x, given_island_y)
    assert sut.distance_to(island) == expected_distance


@pytest.mark.parametrize("given_island_x, given_island_y, expected_visibility", [
    (0, 0, True),
    (11, 0, False),
])
def test_ship_should_check_island_visibility(given_island_x, given_island_y, expected_visibility):
    sut = seafarers.Ship()
    island = seafarers.Island(given_island_x, given_island_y)
    assert sut.is_island_visible(island) == expected_visibility


def test_ship_should_filter_islands_by_visibility():
    sut = seafarers.Ship()
    islands = [seafarers.Island(0, 0), seafarers.Island(11, 0)]
    actual_visible_islands = sut.filter_visible_islands(islands)
    assert len(actual_visible_islands) == 1
    assert actual_visible_islands[0].x == 0
    assert actual_visible_islands[0].y == 0


@pytest.mark.parametrize("given_island_x, given_island_y, expected_dockworthiness", [
    (0, 0, True),
    (2, 0, False),
])
def test_ship_should_check_island_dockworthiness(given_island_x, given_island_y, expected_dockworthiness):
    sut = seafarers.Ship()
    island = seafarers.Island(given_island_x, given_island_y)
    assert sut.can_dock(island) == expected_dockworthiness


def test_ship_should_filter_islands_by_dockworthiness():
    sut = seafarers.Ship()
    islands = [seafarers.Island(0, 0), seafarers.Island(2, 0)]
    actual_dockworthy_islands = sut.filter_dockworthy_islands(islands)
    assert len(actual_dockworthy_islands) == 1
    assert actual_dockworthy_islands[0].x == 0
    assert actual_dockworthy_islands[0].y == 0


def test_ship_should_initially_not_be_docked():
    sut = seafarers.Ship()
    assert sut.docked_at is None


def test_ship_can_dock():
    sut = seafarers.Ship()
    island = seafarers.Island(0, 0)
    sut.dock(island)
    assert sut.docked_at == island


def test_ship_cannot_move_when_docked():
    sut = seafarers.Ship()
    island = seafarers.Island(0, 0)
    sut.dock(island)
    sut.move()
    assert sut.x == 0
    assert sut.y == 0


@pytest.mark.parametrize("island_x, island_y, expected_rough_heading", [
    (0, 1, 0),
    (1, 1, 4),
    (2, 2, 4),
    (1, -1, 12),
    (1, 0, 8),
    (0, -1, 16),
    (-1, -1, 20),
    (-1, 1, 28),
    (-1, 0, 24),
    (0, 0, 0),
])
def test_ship_should_know_rough_heading_towards_island(island_x, island_y, expected_rough_heading):
    sut = seafarers.Ship()
    island = seafarers.Island(island_x, island_y)
    actual_rough_heading = sut.rough_heading_to(island)
    assert actual_rough_heading == expected_rough_heading


def test_ship_has_move_count():
    sut = seafarers.Ship()
    assert sut.moves == 0


def test_ship_counts_moves():
    sut = seafarers.Ship()
    sut.move()
    assert sut.moves == 1


def test_ship_docking_counts_as_move():
    sut = seafarers.Ship()
    island = seafarers.Island(0, 0)
    sut.dock(island)
    assert sut.moves == 1


def test_ship_undocking_counts_as_move():
    sut = seafarers.Ship()
    sut.dock(None)
    assert sut.moves == 1
