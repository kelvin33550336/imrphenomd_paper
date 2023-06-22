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
    "figure.figsize": (11, 5),
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

c1 = "#102F68"
c2 = "#B02423"
c3 = "#FFB300"

data2 = np.loadtxt(paths.data / "1neg2pos_mismatch.dat")
data4 = np.loadtxt(paths.data / "1pos2neg_mismatch.dat")

data = np.loadtxt(paths.data / "q148.dat")
data2_q148 = np.array([data[i, 5] for i in range(len(data[:,0])) if data[i, 2] < 0 and data[i, 3] > 0])
data4_q148 = np.array([data[i, 5] for i in range(len(data[:,0])) if data[i, 2] > 0 and data[i, 3] < 0])

bins = np.linspace(-5, -1, 15)

fig, ax = plt.subplots(2, figsize=(6, 10), sharex=True)
plt.subplots_adjust(hspace=0.05)

ax[0].hist(
    np.log10(data2[:, 4]), 
    bins=bins, 
    alpha=0.2, 
    color=c1
)
ax[0].hist(
    np.log10(data2[:, 4]), 
    bins=bins, 
    label="Original", 
    color=c1, 
    lw=2, 
    histtype="step"
)
ax[0].axvline(
    x=np.log10(np.median(data2[:, 4])),
    color=c1,
    zorder=-20,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)
ax[0].hist(
    np.log10(data2[:, 5]),
    bins=bins,
    label="Optimized",
    histtype="step",
    color=c3,
    linewidth=2,
)
ax[0].hist(
    np.log10(data2[:, 5]),
    bins=bins,
    color=c3,
    alpha=0.2,
)
ax[0].axvline(
    x=np.log10(np.median(data2[:, 5])),
    color=c3,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)
ax[0].hist(
    np.log10(data2_q148), 
    bins=bins, 
    alpha=0.2, 
    color=c2
)
ax[0].hist(
    np.log10(data2_q148), 
    bins=bins, 
    label="Optimized $(\mathcal{L}_{\mathrm{ave}})$", 
    color=c2, 
    lw=2, 
    histtype="step"
)
ax[0].axvline(
    x=np.log10(np.median(data2_q148)),
    color=c2,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)
ax[0].set_ylabel("Count")
ax[0].legend(loc="upper left")

ax[1].hist(
    np.log10(data4[:, 4]), 
    bins=bins, 
    alpha=0.2, 
    color=c1
)
ax[1].hist(
    np.log10(data4[:, 4]), 
    bins=bins, 
    histtype="step", 
    color=c1, 
    lw=2
)
ax[1].axvline(
    x=np.log10(np.median(data4[:, 4])),
    color=c1,
    zorder=-20,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)
ax[1].hist(
    np.log10(data4[:, 5]), 
    bins=bins, 
    histtype="step", 
    color=c3, 
    lw=2
)
ax[1].hist(
    np.log10(data4[:, 5]), 
    bins=bins, 
    color=c3, 
    alpha=0.2
)
ax[1].axvline(
    x=np.log10(np.median(data4[:, 5])),
    color=c3,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)
ax[1].hist(
    np.log10(data4_q148), 
    bins=bins, 
    alpha=0.2, 
    color=c2
)
ax[1].hist(
    np.log10(data4_q148), 
    bins=bins, 
    color=c2, 
    lw=2, 
    histtype="step"
)
ax[1].axvline(
    x=np.log10(np.median(data4_q148)),
    color=c2,
    lw=2,
    alpha=1.0,
    linestyle=(0, (1, 1.3)),
)
ax[1].set_xlabel("$\log_{10}(\mathcal{M})$")
ax[1].set_ylabel("Count")

plt.savefig(paths.figures / "all_quadrants.pdf", bbox_inches="tight")
