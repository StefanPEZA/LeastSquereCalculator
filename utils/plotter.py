import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, xs: list, ys: list, fys: list, title: str = ""):
        self.title = title
        self.xs = xs
        self.ys = ys
        self.fys = fys
        self.labels = [f"({x}, {y})" for x, y in zip(self.xs, self.ys)]

    def plot(self):
        print("Plotting... ")
        plt.clf()
        plt.cla()
        plt.title("Least Square Function: " + self.title)

        plt.plot(self.xs, self.ys, color="green", linewidth=1, alpha=0.5)

        if self.fys is not None:
            xy1 = (self.xs[0], self.fys[0])
            xy2 = (self.xs[-1], self.fys[-1])
            plt.axline(xy1, xy2, color="red")
            for i in range(len(self.xs)):
                plt.vlines(self.xs[i], ymin=self.ys[i], ymax=self.fys[i], color="green", linestyles=":", alpha=0.5)

        plt.scatter(self.xs, self.ys, marker="o", color="green", alpha=0.8)
        for i in range(len(self.xs)):
            plt.annotate(self.labels[i], (self.xs[i], self.ys[i] + 0.2))

        x_max = max(max(self.xs), max(self.ys))
        x_min = min(min(self.xs), min(self.ys))
        plt.xlim((x_min - 1, x_max + 1))
        plt.ylim((x_min - 1, x_max + 1))
        plt.show()
