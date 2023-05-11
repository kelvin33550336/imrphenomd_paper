import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 18,
    "legend.fontsize": 12,
    "legend.frameon": True,
    "axes.labelsize": 18,
    "axes.titlesize": 18,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
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

mpl.rcParams.update(params)

q148 = np.loadtxt(paths.data / "q148.dat")
bins = np.linspace(-5, -1, 15)

plt.hist(np.log10(q148[:,4]), bins=bins, alpha=0.2, color="C0", label="Original")
plt.axvline(x=np.log10(np.median(q148[:,4])), color="C0", zorder=-20, alpha=0.4, ls=":")

plt.hist(np.log10(q148[:,5]), bins=bins, label="$\mathcal{L}_{\mathrm{mean}}$", histtype="step", color="C1", linewidth=3)
plt.axvline(x=np.log10(np.median(q148[:,5])), color="C1", zorder=-20, alpha=0.4, ls=":")

plt.legend()
plt.ylabel('Count')
plt.xlabel('$\log(\mathcal{M})$')
plt.savefig(paths.figures / "q148.pdf", bbox_inches="tight")