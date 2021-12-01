from tkinter import *
from tkinter import ttk


class Entries:
    def __init__(self, root=None, column=0, row=0):
        self.entries = list()
        self.root = root
        self.count = 0
        self.column = column
        self.row = row

    @staticmethod
    def set_text(entry, text):
        entry.delete(0, END)
        entry.insert(0, text)

    def get_points(self):
        points = list()
        for entry in self.entries:
            x = float(entry.get("x").get())
            y = float(entry.get("y").get())
            points.append((x, y))
        return points

    def add_entry(self, x="", y=""):
        pad = {"padx": 2, "pady": 2}
        e1 = ttk.Entry(self.root, width=20, justify='center')
        e2 = ttk.Entry(self.root, width=20, justify='center')
        e1.grid(column=self.column, row=self.row + self.count, **pad)
        e2.grid(column=self.column + 1, row=self.row + self.count, **pad)
        Entries.set_text(e1, x)
        Entries.set_text(e2, y)
        self.count += 1
        self.entries.append({"x": e1, "y": e2})

    def remove_entry(self, erase_all=False):
        if self.count <= 2 and not erase_all:
            return
        self.count -= 1
        entry_to_remove = self.entries[-1]
        entry_to_remove.get("x").destroy()
        entry_to_remove.get("y").destroy()
        self.entries.remove(entry_to_remove)

    def clear_all(self):
        while self.count > 0:
            self.remove_entry(erase_all=True)

    def add_from_points(self, points):
        for (x, y) in points:
            self.add_entry(str(x), str(y))
