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
sc = plt.scatter(data[:,0], data[:,1], c=colors, vmin=-1, vmax=1, s=30, cmap=cm, alpha=0.8)
cbar = plt.colorbar(sc)
cbar.ax.set_ylabel('$\log(MM_{\mathrm{opt}}/MM_{\mathrm{ori}})$', rotation=270, labelpad=20)
cbar.ax.set_yticklabels(['$< -1$', '$-0.75$', '$-0.5$', '$-0.25$', '$0$', '$0.25$', '$0.5$', '$0.75$', '$> 1$'])
plt.xlabel('$q$')
plt.ylabel('$\chi_{\mathrm{PN}}$')

plt.savefig(paths.figures / "ps_q148_qchi.pdf", bbox_inches="tight")