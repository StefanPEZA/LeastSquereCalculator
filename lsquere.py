import argparse
from interface import interface as wm
from utils.compute import LeastSquare
from utils.parser import PointsParser
from utils.plotter import Plotter


def retrieve_points_1by1():
    result = []
    count = 1
    while True:
        in_p = input(f"Point{count} (x{count}, y{count}): ")
        if not in_p:
            break
        points = PointsParser.point_from_string(in_p)
        if points is None:
            continue
        result.append(points)
        count += 1
    print("Points got from console: " + str(result))
    return result


def retrieve_points_from_console():
    result = []
    in_p = input("Points: ")
    points = PointsParser.points_from_string(in_p)
    if points is None:
        return result
    result.extend(points)
    print("Points got from console: " + str(result))
    return result


def retrieve_points_from_file(file_path: str = None):
    if not file_path:
        file_path = input("Input file path: ")
    result = list()
    while True:
        try:
            with open(file_path) as f:
                points = PointsParser.points_from_string(f.read())
                if points is None:
                    return result
                result.extend(points)
            break
        except FileNotFoundError:
            print("Input File Not Found")
            file_path = input("Input file path: ")
    print("Points got from file: " + str(result))
    return result


retrieve_points = {
    "1": retrieve_points_1by1,
    "2": retrieve_points_from_console,
    "3": retrieve_points_from_file
}


def after_compute(l_square: LeastSquare):
    plotter = Plotter(*l_square.get_points_lists(), l_square.get_function_string())
    while True:
        print("What do you want to do: ")
        print("1. Print errors table")
        print("2. Show function graph")
        print("3. Compute f(x)")
        print("4. Exit")
        choice = input(">> ")
        if choice == "1":
            print(l_square.get_errors_table())
        elif choice == "2":
            plotter.plot()
        elif choice == "3":
            func = l_square.get_function()
            while True:
                in_x = input("X = ")
                if not in_x:
                    break
                print("F(X) = " + str(func(float(in_x))))
        else:
            break


def run(points: str = None, file_path: str = None):
    print("Running in console.")
    l_square = LeastSquare([])
    if points:
        points = PointsParser.points_from_string(points)
        print("Points got from args: " + str(points))
        l_square.add_points(points)
    elif file_path:
        points = retrieve_points_from_file(file_path)
        l_square.add_points(points)
    else:
        print("Method of input: ")
        print("1. one by one: (x, y)")
        print("2. all: (x1, y1), (x2, y2), ... (x_, y_)")
        print("3. from file")
        choice = input(">> ")
        points = retrieve_points.get(choice, "1")()
        l_square.add_points(points)
    l_square.compute_function()
    print("Computed function is: " + l_square.get_function_string())
    after_compute(l_square)


if __name__ == "__main__":
    in_args = argparse.ArgumentParser()
    in_args.add_argument("-nogui", action="store_true", dest="nogui")
    in_args.add_argument("-points", type=str, dest="points", default="")
    in_args.add_argument("-file", type=str, dest="file", default="")
    in_args = in_args.parse_args()
    if in_args.nogui:
        run(points=in_args.points.strip(), file_path=in_args.file.strip())
    else:
        wm.open_window()
