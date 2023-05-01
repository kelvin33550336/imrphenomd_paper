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

q148 = np.loadtxt(paths.data / "all_quadrants.dat")
data2 = np.array([i for i in q148 if (i[2] < 0 and i[3] > 0)])
data4 = np.array([i for i in q148 if (i[2] > 0 and i[3] < 0)])

bins = np.arange(-5, -1, 0.2)

fig, ax = plt.subplots(2, figsize=(6, 10))

ax[0].hist(np.log10(data2[:,4]), bins=bins, alpha=0.3, color="C0")
ax[0].hist(np.log10(data2[:,4]), bins=bins, label="top-left original", histtype="step", color="C0", linewidth=1.3)
ax[0].axvline(x=np.log10(np.median(data2[:,4])), color="C0", ls="--")
ax[0].hist(np.log10(data2[:,5]), bins=bins, alpha=0.3, color="C1")
ax[0].hist(np.log10(data2[:,5]), bins=bins, label="top-left optimized", histtype="step", color="C1", linewidth=1.3)
ax[0].axvline(x=np.log10(np.median(data2[:,5])), color="C1", ls="--")
ax[0].set_ylabel('Count')
ax[0].legend(loc='upper left')

ax[1].hist(np.log10(data4[:,4]), bins=bins, alpha=0.3, color="C0")
ax[1].hist(np.log10(data4[:,4]), bins=bins, label="bottom-right original", histtype="step", color="C0", linewidth=1.3, alpha=0.8)
ax[1].axvline(x=np.log10(np.median(data4[:,4])), color="C0", ls="--")
ax[1].hist(np.log10(data4[:,5]), bins=bins, alpha=0.3, color="C1")
ax[1].hist(np.log10(data4[:,5]), bins=bins, label="bottom-right optimized", histtype="step", color="C1", linewidth=1.3, alpha=0.8)
ax[1].axvline(x=np.log10(np.median(data4[:,5])), color="C1", ls="--")
ax[1].set_xlabel('$\log(\mathcal{M})$')
ax[1].set_ylabel('Count')
ax[1].legend(loc='upper left')

# plt.hist(np.log10(data2[:,4]), bins=bins, label="top-left original", histtype="step", color="C0", linewidth=1.3)
# plt.hist(np.log10(data2[:,5]), bins=bins, label="top-left optimized", histtype="step", color="C0", linestyle=('dashed'), linewidth=1.3)

# plt.hist(np.log10(data4[:,4]), bins=bins, label="bottom-right original", histtype="step", color="C1", linewidth=1.3)
# plt.hist(np.log10(data4[:,5]), bins=bins, label="bottom-right optimized", histtype="step", color="C1", linestyle=('dashed'), linewidth=1.3)

# plt.legend(loc='upper left')
# plt.ylabel('Count')
# plt.xlabel('$\log(\mathrm{mismatch})$')

plt.savefig(paths.figures / "all_quadrants.pdf", bbox_inches="tight")