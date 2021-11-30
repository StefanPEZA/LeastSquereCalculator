from utils.lsquere_error import LSquereError


class LeastSquare:
    def __init__(self, points: list):
        self.points = set(points)
        self.m = 1
        self.b = 0

    def get_points(self) -> list:
        return list(self.points)

    def add_point(self, x: float, y: float):
        self.points.add((x, y))

    def add_points(self, points: list):
        self.points.update(points)

    def get_function(self):
        def func(x: float):
            return self.m * x + self.b
        return func

    def get_errors_table(self):
        xs, ys = zip(*self.get_points())
        func = self.get_function()
        fys = [func(x) for x in xs]
        table = "X\tY\tF(X)\tERR"
        for x, y, fy in zip(xs, ys, fys):
            table += f"\n{x}\t{y}\t{fy}\t{fy - y}"
        return table

    def get_function_string(self):
        func_str = f"y = {self.m} * x + {self.b}"
        return func_str

    def compute_function(self):
        if len(self.get_points()) < 2:
            raise LSquereError("You need to provide at least 2 points!")

