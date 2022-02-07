from utils.lsquere_error import LSquereError


class LeastSquare:
    def __init__(self, points: list):
        self.points = set(points)
        self.m = None
        self.b = 0

    def get_points(self) -> list:
        return sorted(list(self.points))

    def add_point(self, x: float, y: float):
        self.points.add((x, y))

    def add_points(self, points: list):
        self.points.update(points)

    def get_function(self):
        if self.m is None:
            return None

        def func(x: float):
            return self.m * x + self.b

        return func

    def get_points_lists(self):
        xs, ys = zip(*self.get_points())
        func = self.get_function()

        if func is None:
            return xs, ys, None

        fys = [func(x) for x in xs]
        return xs, ys, fys

    def get_errors_table(self):
        xs, ys, fys = self.get_points_lists()
        table = "X\t Y\t F(X)\t ERR"
        table += "\n---\t ---\t ---\t ---"
        for x, y, fy in zip(xs, ys, fys):
            x = round(x, 3)
            y = round(y, 3)
            fy = round(fy, 3)
            table += f"\n{x}\t {y}\t {fy}\t {round(fy - y, 3)}"
        return table + "\n"

    def get_function_string(self):
        if self.m is None:
            func_str = f"x = {self.get_points()[0][0]} (constant)"
        else:
            func_str = f"y = {round(self.m, 4)} * x + {round(self.b, 4)}"
        return func_str

    def compute_function(self):
        if len(self.get_points()) < 2:
            raise LSquereError("You need to provide at least 2 points!")
        x2, xy = self.__compute_step1()
        sum_x, sum_y, sum_x2, sum_xy = self.__compute_step2(x2, xy)
        try:
            self.m = self.__compute_slope(sum_x, sum_y, sum_x2, sum_xy)
            self.b = self.__compute_intercept(sum_x, sum_y)
        except ZeroDivisionError:
            pass

    def __compute_step1(self):
        x2 = list()
        xy = list()
        for (x, y) in self.get_points():
            x2.append(x * x)
            xy.append(x * y)
        return x2, xy

    def __compute_step2(self, x2, xy):
        sum_x = sum_y = sum_x2 = sum_xy = 0
        xs, ys = zip(*self.get_points())
        for i in range(len(xs)):
            sum_x += xs[i]
            sum_y += ys[i]
            sum_x2 += x2[i]
            sum_xy += xy[i]
        return sum_x, sum_y, sum_x2, sum_xy

    def __compute_slope(self, sum_x, sum_y, sum_x2, sum_xy):
        n = len(self.get_points())
        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
        return m

    def __compute_intercept(self, sum_x, sum_y):
        n = len(self.get_points())
        b = (sum_y - self.m * sum_x) / n
        return b
