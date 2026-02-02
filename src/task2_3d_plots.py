import sys
import os

sys.path.append(os.path.abspath("../data"))

import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from node import nodes
from element import members

ds = xr.open_dataset("../data/xarray_data.nc")

girders = {
    "Girder 1": [13, 22, 31, 40, 49, 58, 67, 76, 81],
    "Girder 2": [14, 23, 32, 41, 50, 59, 68, 77, 82],
    "Girder 3": [15, 24, 33, 42, 51, 60, 69, 78, 83],
    "Girder 4": [16, 25, 34, 43, 52, 61, 70, 79, 84],
    "Girder 5": [17, 26, 35, 44, 53, 62, 71, 80, 85],
}

girder_colors = {
    "Girder 1": "red",
    "Girder 2": "blue",
    "Girder 3": "green",
    "Girder 4": "purple",
    "Girder 5": "orange",
}

BMD_SCALE = 0.3
SFD_SCALE = 1.0

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

for elem, (n1, n2) in members.items():
    x1, _, z1 = nodes[n1]
    x2, _, z2 = nodes[n2]
    ax.plot([x1, x2], [0, 0], [z1, z2], color="gray", alpha=0.3)

for gname, elements in girders.items():
    color = girder_colors[gname]
    for elem in elements:
        n1, n2 = members[elem]
        x1, _, z1 = nodes[n1]
        x2, _, z2 = nodes[n2]

        ef = ds["forces"].sel(Element=elem)
        Mz_i = float(ef.sel(Component="Mz_i"))
        Mz_j = float(ef.sel(Component="Mz_j"))

        ax.plot(
            [x1, x2],
            [BMD_SCALE * Mz_i, BMD_SCALE * Mz_j],
            [z1, z2],
            color=color,
            linewidth=2
        )

ax.set_title("3D Bending Moment Diagram (All Girders)")
ax.set_xlabel("X (Bridge Length)")
ax.set_ylabel("Bending Moment (Mz)")
ax.set_zlabel("Z (Bridge Width)")
plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

for elem, (n1, n2) in members.items():
    x1, _, z1 = nodes[n1]
    x2, _, z2 = nodes[n2]
    ax.plot([x1, x2], [0, 0], [z1, z2], color="gray", alpha=0.3)

for gname, elements in girders.items():
    color = girder_colors[gname]
    for elem in elements:
        n1, n2 = members[elem]
        x1, _, z1 = nodes[n1]
        x2, _, z2 = nodes[n2]

        ef = ds["forces"].sel(Element=elem)
        Vy_i = float(ef.sel(Component="Vy_i"))
        Vy_j = float(ef.sel(Component="Vy_j"))

        ax.plot(
            [x1, x2],
            [SFD_SCALE * Vy_i, SFD_SCALE * Vy_j],
            [z1, z2],
            color=color,
            linewidth=2
        )

ax.set_title("3D Shear Force Diagram (All Girders)")
ax.set_xlabel("X (Bridge Length)")
ax.set_ylabel("Shear Force (Vy)")
ax.set_zlabel("Z (Bridge Width)")
plt.tight_layout()
plt.show()
