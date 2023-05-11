import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 18,
    "legend.fontsize": 12,
    "legend.frameon": True,
    "axes.labelsize": 16,
    "axes.titlesize": 16,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
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

train_data = np.loadtxt(paths.data / "train_waveform_loss.txt")
validation_data = np.loadtxt(paths.data / "validation_waveform_loss.txt")

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(validation_data[:,0], validation_data[:,1], color="C1", linewidth=2, label='validation')
ax2.plot(train_data[:,0], train_data[:,1], color="C0", linewidth=2, label='train')

ax1.set_xlabel('N')
ax1.set_ylabel('validation loss (dashed)')
ax2.set_ylabel('test loss')

plt.savefig(paths.figures / "loss.pdf", bbox_inches="tight")