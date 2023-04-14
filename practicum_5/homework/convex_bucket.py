from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def check_orientation(a: NDArray, b: NDArray, c: NDArray) -> bool:
    return (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1]) >= 0

def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    lower_bucket = []

    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))  # Sort points by X and Y axes

    # Adding 2 very first points
    lower_bucket.append(sorted_points[0])
    lower_bucket.append(sorted_points[1])

    for point in sorted_points[2:]:
        # Checking orientation and array's len
        while len(lower_bucket) > 1 and check_orientation(lower_bucket[-2], lower_bucket[-1], point):
            lower_bucket.pop()

        # Adding next point
        lower_bucket.append(point)

    lower_bucket += lower_bucket[-2::-1]  # Avoiding connection of last and first point on graph

    return np.array(lower_bucket)


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"../points_{i}.txt"
        curr_points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(curr_points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(curr_points, convex_hull=ch, markersize=20)
        print()
