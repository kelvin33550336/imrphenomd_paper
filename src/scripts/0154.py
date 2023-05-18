import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 15,
    "legend.fontsize": 12,
    "legend.frameon": False,
    "axes.labelsize": 15,
    "axes.titlesize": 15,
    "xtick.labelsize": 15,
    "ytick.labelsize": 15,
    "axes.unicode_minus": False,
    "figure.figsize": (7, 5),
    "xtick.top": True,
    "ytick.right": True,
    "xtick.bottom": True,
    "ytick.left": True,
    "xtick.major.pad": 8,
    "xtick.major.size": 8,
    "xtick.minor.size": 4,
    "ytick.major.size": 8,
    "ytick.minor.size": 4,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "axes.linewidth": 1.5,
    "text.usetex": False,
    "font.family": "serif",
    "font.serif": "cmr10",
    "mathtext.fontset": "cm",
    "axes.formatter.use_mathtext": True,  # needed when using cm=cmr10 for normal text
}

MSUN = 1.988409902147041637325262574352366540e30  # kg
G = 6.67430e-11  # m^3 / kg / s^2
C = 299792458.0  # m / s
gt = G * MSUN / (C**3.0)

f_ins = 0.018
f_rd = 149.1018563859192 * (25.0 + 25.0) * gt

mpl.rcParams.update(params)

data = np.loadtxt(paths.data / "0154_compare.dat")

f_uniform = data[:, 0]
NR_amp = data[:, 1]
NR_angle = data[:, 2]
IMR_amp = data[:, 3]
IMR_angle = data[:, 4]
IMR_opt_amp = data[:, 5]
IMR_opt_angle = data[:, 6]

fig, ax = plt.subplots(2, 2, figsize=(12, 7), sharex=True)
# green = "#406a3d"
# red = "#b14a49"
# yellow = "#b0882f"
c1 = "#102F68"  # blue
c2 = "#B02423"  # red

ax[0, 0].loglog(
    f_uniform,
    NR_amp,
    label="Numerical Relativity",
    linestyle=(0, (3, 1, 1, 1)),
    color="k",
    lw=2,
)
ax[0, 0].loglog(
    f_uniform, IMR_amp, label="Original PhenomD", linestyle=(0, (3, 1)), color=c1, lw=2
)
ax[0, 0].loglog(f_uniform, IMR_opt_amp, label="Optimized PhenomD", color=c2, lw=2)
ax[0, 0].axvline(x=f_ins, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
ax[0, 0].axvline(x=f_rd, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
# ax[0, 0].set_xlabel(r"$Mf$")
ax[0, 0].set_ylabel(r"$|\tilde{h}|$")
ax[0, 0].legend()

ax[0, 1].semilogx(f_uniform, NR_angle, label="NR", color="k", lw=2)
ax[0, 1].semilogx(
    f_uniform, IMR_angle, label="IMR original", linestyle=(0, (3, 1)), color=c1, lw=2
)
ax[0, 1].semilogx(f_uniform, IMR_opt_angle, label="IMR optimized", color=c2, lw=2)
ax[0, 1].axvline(x=f_ins, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
ax[0, 1].axvline(x=f_rd, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
# ax[0, 1].set_xlabel(r"$Mf$")
ax[0, 1].set_ylabel(r"$\phi$")
# ax[0, 1].legend()

ax[1, 0].semilogx(
    f_uniform,
    (NR_amp - IMR_amp) / NR_amp,
    label="IMR original",
    linestyle=(0, (3, 1)),
    color=c1,
    lw=2,
)
ax[1, 0].semilogx(
    f_uniform, (NR_amp - IMR_opt_amp) / NR_amp, label="IMR optimized", color=c2, lw=2
)
ax[1, 0].axvline(x=f_ins, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
ax[1, 0].axvline(x=f_rd, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
ax[1, 0].set_xlabel(r"$Mf$")
ax[1, 0].set_ylabel(r"$\tilde{h}-\tilde{h}_{\mathrm{NR}}$")
# ax[1, 0].legend()

ax[1, 1].semilogx(
    f_uniform,
    (NR_angle - IMR_angle),
    label="IMR original",
    linestyle=(0, (3, 1)),
    color=c1,
    lw=2,
)
ax[1, 1].semilogx(
    f_uniform,
    (NR_angle - IMR_opt_angle),
    label="IMR optimized",
    color=c2,
    lw=2,
)
ax[1, 1].axvline(x=f_ins, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
ax[1, 1].axvline(x=f_rd, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
ax[1, 1].set_xlabel(r"$Mf$")
ax[1, 1].set_ylabel(r"$\phi-\phi_{\mathrm{NR}}$")
# ax[1, 1].legend()

plt.subplots_adjust(hspace=0.075)
plt.savefig(paths.figures / "0154.pdf", bbox_inches="tight")
