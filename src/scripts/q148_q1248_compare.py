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

c1 = "#B02423"
c2 = "#266D1F"
# c2 = "#785EF0"


q148_data = np.loadtxt(paths.data / "q148.dat")
q1248_data = np.loadtxt(paths.data / "q1248.dat")

# bins = np.arange(-2, 2, 0.2)
bins = np.linspace(-2, 2, 15)
q148_logdiff = np.log10(q148_data[:, 5] / q148_data[:, 4])
q1248_logdiff = np.log10(q1248_data[:, 5] / q1248_data[:, 4])

plt.hist(q148_logdiff, bins=bins, alpha=0.2, color=c1)
plt.hist(q148_logdiff, bins=bins, label="Without Extra Data", color=c1, histtype="step", lw=2)
plt.axvline(
    x=np.median(q148_logdiff),
    color=c1,
    zorder=-20,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)
plt.hist(
    q1248_logdiff,
    bins=bins,
    alpha=0.2,
    color=c2,
)
plt.hist(
    q1248_logdiff,
    bins=bins,
    label=f"With Extra Data",
    histtype="step",
    color=c2,
    linewidth=2,
)
plt.axvline(
    x=np.median(q1248_logdiff),
    color=c2,
    zorder=-20,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)
# plt.text(-1.6, 73, "(add. NR data)", fontsize=12)

# plt.xlim(-2.5, 2)
plt.legend()
plt.ylabel("Count")
plt.xlabel(r"$\log_{10}(\mathcal{M}_f/\mathcal{M}_i)$")
plt.savefig(paths.figures / "q148_q1248_compare.pdf", bbox_inches="tight")
