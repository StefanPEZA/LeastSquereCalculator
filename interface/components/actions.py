from interface.components.entries import Entries


def try_get_points(entries):
    try:
        points = entries.get_points()
        return points
    except ValueError:
        return None