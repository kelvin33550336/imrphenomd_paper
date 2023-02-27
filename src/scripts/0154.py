import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

params = {
    "font.size": 15,
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

data = np.loadtxt(paths.data / "0154_compare.dat")

f_uniform = data[:,0]
NR_amp = data[:,1]
NR_angle = data[:,2]
IMR_amp = data[:,3]
IMR_angle = data[:,4]
IMR_opt_amp = data[:,5]
IMR_opt_angle = data[:,6]

fig, ax = plt.subplots(2, 2, figsize=(15, 10))

ax[0, 0].loglog(f_uniform, NR_amp, label='NR')
ax[0, 0].loglog(f_uniform, IMR_amp, label='IMR original')
ax[0, 0].loglog(f_uniform, IMR_opt_amp, label='IMR optimized')
ax[0, 0].set_xlabel(r'$Mf$')
ax[0, 0].set_ylabel(r'$|\tilde{h}(f)|$')
ax[0, 0].legend()

ax[0, 1].plot(f_uniform, NR_angle, label='NR')
ax[0, 1].plot(f_uniform, IMR_angle, label='IMR original')
ax[0, 1].plot(f_uniform, IMR_opt_angle, label='IMR optimized')
ax[0, 1].set_xlabel(r'$Mf$')
ax[0, 1].set_ylabel(r'$\phi$')
ax[0, 1].legend()

ax[1, 0].plot(f_uniform, np.abs(NR_amp - IMR_amp) / NR_amp, label='IMR original')
ax[1, 0].plot(f_uniform, np.abs(NR_amp - IMR_opt_amp) / NR_amp, label='IMR optimized')
ax[1, 0].set_xlabel(r'$Mf$')
ax[1, 0].set_ylabel(r'$\Delta|\tilde{h}(f)|$')
ax[1, 0].legend()

ax[1, 1].plot(f_uniform, np.abs(NR_angle - IMR_angle), label='IMR original')
ax[1, 1].plot(f_uniform, np.abs(NR_angle - IMR_opt_angle), label='IMR optimized')
ax[1, 1].set_xlabel(r'$Mf$')
ax[1, 1].set_ylabel(r'$\Delta\phi$')
ax[1, 1].legend()

plt.savefig(paths.figures / "0154.pdf", bbox_inches="tight")