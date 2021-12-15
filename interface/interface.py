from tkinter import *
from tkinter import ttk
from interface.components.entries import Entries
from utils.compute import LeastSquare
from interface.components.actions import try_get_points, load_from_file, \
    load_from_string, open_filedialog
from utils.plotter import Plotter

l_square = LeastSquare([])

root = Tk()
entries = Entries(root)
info_label = Label(root)


def config_root():
    global root
    root.title("Least Square Calculator")
    root.resizable(False, False)
    root.minsize(width=640, height=500)
    frm = Frame(root)
    frm.grid(padx=50, pady=10)
    return frm


def update_info_label(text, fg="black"):
    global info_label
    info_label.config(text=text, fg=fg)


def compute_func():
    global l_square, entries, info_label
    points = try_get_points(entries)
    if not points:
        update_info_label(text="Invalid arguments!", fg="red")
        print("Invalid arguments!")
        return
    l_square = LeastSquare(points)
    l_square.compute_function()
    update_info_label(text="Compute was successful!", fg="green")
    print("Compute was successful!")


def show_graph():
    global l_square, info_label
    xs, ys, fys = l_square.get_points_lists()
    plotter = Plotter(xs, ys, fys, l_square.get_function_string())
    plotter.plot()


def load_points_from_file():
    global root, info_label, entries
    file_path = open_filedialog()
    points = load_from_file(file_path)
    if not points:
        update_info_label(text="Input File Not Found!", fg="red")
        print("Input File Not Found!")
        return
    entries.clear_all()
    entries.add_from_points(points)
    update_info_label(text="Points loaded successfully!", fg="green")
    print("Points loaded successfully!")


def load_points_from_string():
    global info_label, entries
    points = load_from_string()
    if not points:
        update_info_label(text="Not correct format!", fg="red")
        print("Not correct format!")
        return
    entries.clear_all()
    entries.add_from_points(points)
    update_info_label(text="Points loaded successfully!", fg="green")
    print("Points loaded successfully!")


def calculate_function(entry: ttk.Entry, label: Label):
    try:
        global l_square
        func = l_square.get_function()
        x = float(entry.get())
        if func is None:
            result = "constant"
        else:
            result = round(func(x), 4)
        label.config(text=str(result))
    except ValueError:
        return


def print_error_table():
    global l_square
    print(l_square.get_errors_table())


def parse_args(points: str, file_path: str):
    global info_label
    result = []
    if points:
        result = load_from_string(points)
    elif file_path:
        result = load_from_file(file_path)
        if not result:
            update_info_label(text="Input File Not Found!", fg="red")
            print("Input File Not Found!")
            result = []
    return result


def render_left_side(frm, pad):
    load_file_button = ttk.Button(frm, cursor='hand2', text="Load from file", command=load_points_from_file, width=40)
    load_file_button.grid(column=2, row=1, **pad)

    load_str_button = ttk.Button(frm, cursor='hand2', text="Load From String", command=load_points_from_string, width=40)
    load_str_button.grid(column=2, row=2, **pad)

    add_button = ttk.Button(frm, text="Add Point", command=entries.add_entry, width=40)
    add_button.grid(column=2, row=3, **pad)

    remove_button = ttk.Button(frm, cursor='hand2', text="Remove Point", command=entries.remove_entry, width=40)
    remove_button.grid(column=2, row=4, **pad)

    compute_button = ttk.Button(frm, cursor='hand2', text="Compute", command=compute_func, width=40)
    compute_button.grid(column=2, row=5, **pad)

    show_button = ttk.Button(frm, cursor='hand2', text="Show Function Graph", command=show_graph, width=40)
    show_button.grid(column=2, row=6, **pad)

    show_button = ttk.Button(frm, cursor='hand2', text="Print Errors Table", command=print_error_table, width=40)
    show_button.grid(column=2, row=7, **pad)

    calculate_frm = Frame(frm)
    calculate_frm.grid(column=2, row=8, **pad)
    calculate_label = Label(calculate_frm, text="X:", width=1)
    calculate_entry = ttk.Entry(calculate_frm, width=12, justify='center')
    result_label = Label(calculate_frm, text="Y", width=15, bg="white", fg='black', font=("Courier", 11))
    calculate_button = ttk.Button(calculate_frm, cursor='hand2', text="=", width=3,
                                  command=lambda: calculate_function(calculate_entry, result_label))

    calculate_label.grid(row=0, column=0)
    calculate_entry.grid(row=0, column=1)
    calculate_button.grid(row=0, column=2)
    result_label.grid(row=0, column=3)


def open_window(points: str = None, file_path: str = None):
    global entries, l_square, info_label, root
    print("Opening GUI")

    frm = config_root()

    pad = {"padx": 2, "pady": 2}

    info_label = Label(frm, text="", justify="center", width=40)
    info_label.grid(column=2, row=0, padx=2, pady=2)

    Label(frm, text="X").grid(column=0, row=0, **pad)
    Label(frm, text="Y").grid(column=1, row=0, **pad)
    entries = Entries(frm, column=0, row=1)

    points = parse_args(points, file_path)
    entries.clear_all()
    entries.add_from_points(points)

    l_square = LeastSquare(points)

    while entries.count < 2:
        entries.add_entry()

    render_left_side(frm, pad)

    root.mainloop()
