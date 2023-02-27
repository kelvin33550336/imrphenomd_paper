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
q148_fl = np.loadtxt(paths.data / "q148_fl.dat")
bins = np.arange(-5, -1, 0.2)

plt.hist(np.log10(q148[:,4]), bins=bins, alpha=0.3, color="C0")
plt.hist(np.log10(q148[:,4]), bins=bins, label="Original", histtype="step", color="C0")
plt.hist(np.log10(q148[:,5]), bins=bins, alpha=0.05, color="C1")
plt.hist(np.log10(q148[:,5]), bins=bins, label="$\mathcal{L}_{\mathrm{mean}}$", histtype="step", color="C1")
plt.hist(np.log10(q148_fl[:,5]), bins=bins, alpha=0.05, color="C3")
plt.hist(np.log10(q148_fl[:,5]), bins=bins, label="$\mathcal{L}_{\mathrm{fl}}$", histtype="step", color="C3")
plt.legend()
plt.ylabel('Count')
plt.xlabel('$\log(\mathrm{mismatch})$')
plt.savefig(paths.figures / "q148.pdf", bbox_inches="tight")