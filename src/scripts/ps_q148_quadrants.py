import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 18,
    "legend.fontsize": 12,
    "legend.frameon": False,
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

c2 = "#B02423"
c3 = "#B58500"

data1 = np.loadtxt(paths.data / "1pos2pos_mismatch.dat")
data2 = np.loadtxt(paths.data / "q148_1neg2pos_region_f.dat")
data3 = np.loadtxt(paths.data / "1neg2neg_mismatch.dat")
data4 = np.loadtxt(paths.data / "q148_1pos2neg_region_f.dat")
data_region = np.concatenate((data1, data2, data3, data4))

data1 = np.loadtxt(paths.data / "1pos2pos_mismatch.dat")
data2 = np.loadtxt(paths.data / "q148_1neg2pos_all_f.dat")
data3 = np.loadtxt(paths.data / "1neg2neg_mismatch.dat")
data4 = np.loadtxt(paths.data / "q148_1pos2neg_all_f.dat")
data_q148 = np.concatenate((data1, data2, data3, data4))

logdiff = np.log10(data_region[:, 5] / data_region[:, 4])

bins = np.linspace(-5, -1, 15)

plt.figure(figsize=(6, 5))
plt.hist(np.log10(data_q148[:,5]), alpha=0.2, bins=bins, color=c2)
plt.hist(np.log10(data_q148[:,5]), histtype='step', lw=2, bins=bins, color=c2, label='Optimized (All Regions)')
plt.hist(np.log10(data_region[:,5]), alpha=0.2, bins=bins, color=c3)
plt.hist(np.log10(data_region[:,5]), histtype='step', lw=2, bins=bins, color=c3, label='Optimized (Split Regions)')
plt.axvline(x=np.log10(np.median(data_q148[:,5])), color=c2, ls='--', lw=2)
plt.axvline(x=np.log10(np.median(data_region[:,5])), color=c3, ls='--', lw=2)
plt.xlabel("$\log_{10}(\mathcal{M})$")
plt.ylabel("Count")
plt.legend(loc='upper left')

plt.savefig(paths.figures / "ps_q148_quadrants.pdf", bbox_inches="tight")
