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

q148_data = np.loadtxt(paths.data / "q148.dat")
q1248_data = np.loadtxt(paths.data / "q1248.dat")

bins = np.arange(-2, 2, 0.2)
q148_logdiff = np.log10(q148_data[:,5]/q148_data[:,4])
q1248_logdiff = np.log10(q1248_data[:,5]/q1248_data[:,4])

plt.hist(q148_logdiff, bins=bins, alpha=0.3, color="C0")
plt.hist(q1248_logdiff, bins=bins, label="q1248", histtype="step", color="C1", linewidth=3)

plt.legend()
plt.ylabel('Count')
plt.xlabel('$\log(\mathcal{M_f}/\mathcal{M_i})$')
plt.savefig(paths.figures / "q148_q1248_compare.pdf", bbox_inches="tight")