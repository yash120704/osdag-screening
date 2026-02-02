import xarray as xr
import matplotlib.pyplot as plt


ds = xr.open_dataset("../data/xarray_data.nc")

central_elements = [15, 24, 33, 42, 51, 60, 69, 78, 83]

x_bmd = []
bmd_vals = []

for i, elem in enumerate(central_elements):
    ef = ds["forces"].sel(Element=elem)

    Mz_i = float(ef.sel(Component="Mz_i"))
    Mz_j = float(ef.sel(Component="Mz_j"))

    Mz_avg = (Mz_i + Mz_j) / 2

    x_bmd.append(i)
    bmd_vals.append(Mz_avg)

plt.figure(figsize=(10, 4))
plt.plot(x_bmd, bmd_vals, color="red", linewidth=2)
plt.fill_between(x_bmd, bmd_vals, 0, color="red", alpha=0.3)
plt.title("Bending Moment Diagram (Central Longitudinal Girder)")
plt.xlabel("Bridge Length (Element Index)")
plt.ylabel("Bending Moment (Mz)")
plt.grid(True)
plt.tight_layout()
plt.show()

x_sfd = []
sfd_vals = []

pos = 0
for elem in central_elements:
    ef = ds["forces"].sel(Element=elem)

    Vy_i = float(ef.sel(Component="Vy_i"))
    Vy_j = float(ef.sel(Component="Vy_j"))

    x_sfd.extend([pos, pos + 1])
    sfd_vals.extend([Vy_i, Vy_j])

    pos += 1

plt.figure(figsize=(10, 4))
plt.step(x_sfd, sfd_vals, where="post", color="blue", linewidth=2)
plt.fill_between(x_sfd, sfd_vals, 0, step="post", color="blue", alpha=0.3)
plt.title("Shear Force Diagram (Central Longitudinal Girder)")
plt.xlabel("Bridge Length (Element Index)")
plt.ylabel("Shear Force (Vy)")
plt.grid(True)
plt.tight_layout()
plt.show()
