class PointsForPlace:

    @staticmethod
    def get_points_for_place(place: int) -> int:
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0
        else:
            points = 101 - place
            return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters: int) -> float:
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        else:
            points = meters * 0.5
            return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()

    def get_total_points(self, meters: int, place: int):
        points_place = self.get_points_for_place(place)
        points_meters = self.get_points_for_meters(meters)
        total_points = points_place + points_meters
        return total_points

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(-1))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(-1))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))