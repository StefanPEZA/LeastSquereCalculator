class PointsParser:
    @staticmethod
    def points_from_string(points_string: str = ""):
        """

        :param points_string: "(x1, y1), (x2, y2), ... (x_, y_)"
        :return:
        """
        try:
            result = eval(f"[{points_string.strip('[]')}]")
            return result
        except SyntaxError:
            return []

    @staticmethod
    def point_from_string(point_string: str = ""):
        """

        :param point_string: "(x, y)"
        :return:
        """
        try:
            result = eval(f"{point_string.strip('[]')}")
            return result
        except SyntaxError:
            return None
