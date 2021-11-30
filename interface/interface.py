from tkinter import *
from tkinter import ttk
from interface.components.entries import Entries
from utils.parser import PointsParser
from utils.compute import LeastSquare
from interface.components.actions import try_get_points
from utils.plotter import Plotter

l_square = None
entries = None
info_label = None


def compute_func():
    global l_square, entries, info_label
    points = try_get_points(entries)
    if not points:
        info_label.config(text="Argumente invalide")
        return
    l_square = LeastSquare(points)
    l_square.compute_function()
    info_label.config(text="Compute was successful!")
    print("Compute was successful!")


def show_graph():
    global l_square, info_label
    xs, ys, fys = l_square.get_points_lists()
    plotter = Plotter(xs, ys, fys, l_square.get_function_string())
    plotter.plot()


def parse_args(points: str, file_path: str):
    result = []
    if points:
        result = PointsParser.points_from_string(points)
    elif file_path:
        try:
            with open(file_path) as f:
                result = PointsParser.points_from_string(f.read())
        except FileNotFoundError:
            print("Input File Not Found")
    return result


def open_window(points: str = None, file_path: str = None):
    global entries, l_square, info_label
    print("Opening GUI")

    root = Tk()
    root.wm_title("Least Square Calculator")
    root.wm_minsize(width=640, height=480)
    frm = Frame(root)
    frm.grid()

    pad = {"padx": 2, "pady": 2}

    info_label = Label(frm, text="", justify="center", padx=5, width=40)
    info_label.grid(column=2, row=0, **pad)

    Label(frm, text="X").grid(column=0, row=0, **pad)
    Label(frm, text="Y").grid(column=1, row=0, **pad)

    entries = Entries(frm, column=0, row=1)

    points = parse_args(points, file_path)
    entries.add_from_points(points)

    l_square = LeastSquare(points)

    while entries.count < 2:
        entries.add_entry()

    add_button = Button(frm, text="Add Point", command=entries.add_entry, width=40, padx=5)
    add_button.grid(column=2, row=1, **pad)
    remove_button = Button(frm, text="Remove Point", command=entries.remove_entry, width=40, padx=5)
    remove_button.grid(column=2, row=2, **pad)
    compute_button = Button(frm, text="Compute", command=compute_func, width=40, padx=5)
    compute_button.grid(column=2, row=3, **pad)
    show_button = Button(frm, text="Show Function Graph", command=show_graph, width=40, padx=5)
    show_button.grid(column=2, row=4, **pad)

    root.mainloop()
