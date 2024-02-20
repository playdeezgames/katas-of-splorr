import math


class Island:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    MAXIMUM_VISIBILITY = 10
    MAXIMUM_DOCK_DISTANCE = 1

    def set_heading(self, new_heading):
        self.heading = self.__normalize_heading(new_heading)

    @staticmethod
    def __normalize_heading(new_heading):
        return new_heading - (new_heading // 360) * 360

    def set_speed(self, new_speed):
        self.speed = min(max(new_speed, 0), 1)

    def move(self):
        if self.docked_at is None:
            self.moves += 1
            self.y += math.cos(self.__to_radians()) * self.speed
            self.x += math.sin(self.__to_radians()) * self.speed

    def __to_radians(self):
        return self.heading * math.pi / 180

    def can_see(self, island):
        return self.distance_to(island) <= Ship.MAXIMUM_VISIBILITY

    def distance_to(self, island):
        return math.sqrt(
            (self.x - island.x) * (self.x - island.x) +
            (self.y - island.y) * (self.y - island.y))

    def can_dock(self, island):
        return self.distance_to(island) <= Ship.MAXIMUM_DOCK_DISTANCE

    def dock(self, island):
        self.visits.append((island, self.moves))
        self.docked_at = island

    def heading_to(self, island):
        degrees = math.atan2(island.x - self.x, island.y - self.y) * 180 / math.pi
        return self.__normalize_heading(degrees)

    def count_visits(self, island):
        counter = 0
        for visit in self.visits:
            if island == visit[0]:
                counter += 1
        return counter

    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.speed = 1
        self.docked_at = None
        self.moves = 0
        self.visits = []

    def last_visit(self, island):
        counter = None
        for visit in self.visits:
            if island == visit[0]:
                if counter is None:
                    counter = visit[1]
                else:
                    counter = max(counter, visit[1])
        return counter
