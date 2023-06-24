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
    "figure.figsize": (6, 5),
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

mpl.rcParams.update(params)

# c2 = "#4e7ab1"  # blue Nash

# c2 = "#406a3d"
# c1 = "#b14a49"
# c1 = "#b0882f"  # yellow nash
c1 = "#102F68"
c2 = "#B02423"


q148 = np.loadtxt(paths.data / "q148.dat")
bins = np.linspace(-5, -1, 15)

plt.hist(np.log10(q148[:, 4]), bins=bins, alpha=0.2, color=c1)
plt.hist(
    np.log10(q148[:, 4]),
    bins=bins,
    color=c1,
    histtype="step",
    linewidth=2,
    label="Original",
)
plt.axvline(
    x=np.log10(np.median(q148[:, 4])),
    color=c1,
    zorder=-20,
    alpha=1.0,
    lw=2,
    linestyle=(0, (1, 1.3)),
)

plt.hist(
    np.log10(q148[:, 5]),
    bins=bins,
    histtype="step",
    label="Optimized $(\mathcal{L}_{\mathrm{ave}})$",
    color=c2,
    linewidth=2,
)
plt.hist(
    np.log10(q148[:, 5]),
    bins=bins,
    color=c2,
    alpha=0.2,
)
plt.axvline(
    x=np.log10(np.median(q148[:, 5])),
    color=c2,
    # zorder=-20,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)

plt.legend(loc="upper left")
plt.ylabel("Count")
plt.xlabel("$\log_{10}(\mathcal{M})$")
plt.savefig(paths.figures / "q148.pdf", bbox_inches="tight")
