import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 17,
    "legend.fontsize": 14,
    "legend.frameon": False,
    "axes.labelsize": 17,
    "axes.titlesize": 17,
    "xtick.labelsize": 17,
    "ytick.labelsize": 17,
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

c1 = "#0562ED"
c2 = "#FE6100"

train_data = np.loadtxt(paths.data / "train_waveform_loss.txt")
validation_data = np.loadtxt(paths.data / "validation_waveform_loss.txt")

fig, ax1 = plt.subplots(figsize=(6, 5))

ax2 = ax1.twinx()
ax1.plot(train_data[:, 0], train_data[:, 1], color=c1, linewidth=2, label="Training")
ax2.plot(
    validation_data[:, 0],
    validation_data[:, 1],
    color=c2,
    linewidth=2,
    label="Validation",
    linestyle=(0, (3, 1)),
)
ax1.axvline(x=12000, alpha=0.5, color="k", linestyle=(0, (1, 1.05)))

ax1.set_xlabel("Iteration")
ax1.set_ylabel("Training Loss")
ax2.set_ylabel("Validation Loss")
fig.legend(loc="upper right", bbox_to_anchor=(0.89, 0.875))

plt.savefig(paths.figures / "loss.pdf", bbox_inches="tight")
