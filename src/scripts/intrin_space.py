import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 18,
    "legend.fontsize": 15,
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

train_data = np.loadtxt(paths.data / "ps_train.dat")
test_data = np.loadtxt(paths.data / "q148.dat")

# train_data = np.loadtxt('./plotting_data/ps_train.dat', delimiter=' ') # [q, chi_PN, chi1, chi2]
# test_data = np.loadtxt('./plotting_data/q148.dat', delimiter=' ') # [q, chi_PN, chi1, chi2, ori_loss, opt_loss]
plt.scatter(test_data[:,0], test_data[:,1], s=30, label='testing')
plt.scatter(train_data[:,0], train_data[:,1], s=100, label='training')
plt.legend()
plt.xlabel('$q$')
plt.ylabel('$\chi_{\mathrm{PN}}$')
plt.savefig(paths.figures / "intrin_space.pdf", bbox_inches="tight")