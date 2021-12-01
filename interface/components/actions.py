from interface.components.entries import Entries
from tkinter import *
from tkinter import ttk, filedialog, simpledialog
from utils.parser import PointsParser


def try_get_points(entries):
    try:
        points = entries.get_points()
        return points
    except ValueError:
        return None


def open_filedialog():
    filename = filedialog.askopenfile(initialdir="./", title="Select an input file!",
                                      filetypes=(("Text file ", "*.txt"),))
    return filename.name


def load_from_file(file_path):
    if not file_path:
        return None
    try:
        with open(file_path) as f:
            result = PointsParser.points_from_string(f.read())
            return result
    except FileNotFoundError:
        return None


def load_from_string(points_str=None):
    if not points_str:
        points_str = simpledialog.askstring(title="Points input!", prompt="Write down points in this format: (x1, y1), "
                                                                          "(x2, y2), ... (x_, y_)")

    return PointsParser.points_from_string(points_str)
