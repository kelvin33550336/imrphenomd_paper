import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 18,
    "legend.fontsize": 12,
    "legend.frameon": True,
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

mpl.rcParams.update(params)

data = np.loadtxt(paths.data / "q148.dat")

logdiff = np.log10(data[:,5] / data[:,4])
cm = plt.cm.get_cmap('RdYlBu')
colors = logdiff
sc = plt.scatter(data[:,2], data[:,3], c=colors, vmin=-1, vmax=1, s=30, cmap=cm, alpha=0.8)
cbar = plt.colorbar(sc, ticks=[-1, -0.5, 0, 0.5, 1])
cbar.ax.set_ylabel('$\log(\mathcal{M}/\mathcal{M}_i)$', rotation=270, labelpad=20)
cbar.ax.set_yticklabels(['$<-1$', '$-0.5$', '$0$', '$0.5$', '$>1$'])
plt.xlabel('$\chi_1$')
plt.ylabel('$\chi_2$')

plt.savefig(paths.figures / "ps_q148_chi1chi2.pdf", bbox_inches="tight")