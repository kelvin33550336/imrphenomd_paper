import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 17,
    "legend.fontsize": 14,
    "legend.frameon": True,
    "axes.labelsize": 17,
    "axes.titlesize": 17,
    "xtick.labelsize": 17,
    "ytick.labelsize": 17,
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
# blue = "#102F68"
# red = "#B02423"
c1 = "#648FFF"
c2 = "#FE6100"
# c2 = "#FFB000"

train_data = np.loadtxt(paths.data / "ps_train.dat")
test_data = np.loadtxt(paths.data / "q148.dat")

q = test_data[:, 0] / test_data[:, 1]
eta = test_data[:, 0] * test_data[:, 1] / (test_data[:, 0] + test_data[:, 1]) ** 2
chi_PN = (test_data[:, 0] * test_data[:, 2] + test_data[:, 1] * test_data[:, 3]) / (
    test_data[:, 0] + test_data[:, 1]
) - 38 * eta * (test_data[:, 2] + test_data[:, 3]) / 113

# train_data = np.loadtxt('./plotting_data/ps_train.dat', delimiter=' ') # [q, chi_PN, chi1, chi2]
# test_data = np.loadtxt('./plotting_data/q148.dat', delimiter=' ') # [q, chi_PN, chi1, chi2, ori_loss, opt_loss]
plt.scatter(train_data[:, 0], train_data[:, 1], s=160, color=c1, label="Training", marker='*')
plt.scatter(q, chi_PN, s=20, color=c2, label="Validation", zorder=-20)
plt.legend()
plt.xlabel("$q$")
plt.ylabel("$\chi_{\mathrm{PN}}$")
plt.savefig(paths.figures / "intrin_space.pdf", bbox_inches="tight")
