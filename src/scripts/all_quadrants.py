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

data1 = np.loadtxt(paths.data / "1pos2pos_mismatch.dat")
data2 = np.loadtxt(paths.data / "q148_1neg2pos_region_f.dat")
data3 = np.loadtxt(paths.data / "1neg2neg_mismatch.dat")
data4 = np.loadtxt(paths.data / "q148_1pos2neg_region_f.dat")

data1_q148_ = np.loadtxt(paths.data / "q148.dat")
data1_q148 = np.array([data1_q148_[i] for i in range(len(data1_q148_[:,0])) if data1_q148_[i,2] > 0 and data1_q148_[i,3] > 0])
data2_q148 = np.loadtxt(paths.data / "q148_1neg2pos_all_f.dat")
data3_q148_ = np.loadtxt(paths.data / "q148.dat")
data3_q148 = np.array([data3_q148_[i] for i in range(len(data3_q148_[:,0])) if data3_q148_[i,2] < 0 and data3_q148_[i,3] < 0])
data4_q148 = np.loadtxt(paths.data / "q148_1pos2neg_all_f.dat")

bins = np.linspace(-5, -1, 15)

fig, ax = plt.subplots(2, 2, figsize=(12, 10), sharex=True)
plt.subplots_adjust(hspace=0.05)
plt.subplots_adjust(wspace=0.04)

ax[0, 0].hist(np.log10(data1[:, 4]), bins=bins, alpha=0.2, color=c1)
ax[0, 0].hist(np.log10(data1[:, 4]), bins=bins, label="Original", color=c1, lw=2, histtype="step")
ax[0,0].axvline(x=np.log10(np.median(data1[:, 4])), color=c1,zorder=-20,lw=2,alpha=1.0,linestyle=(0, (1, 1.3)))

ax[0, 0].hist(np.log10(data1[:, 5]),bins=bins,label="Optimized (Split Regions)",histtype="step",color=c3,linewidth=2)
ax[0, 0].hist(np.log10(data1[:, 5]),bins=bins,color=c3,alpha=0.2)
ax[0, 0].axvline(x=np.log10(np.median(data1[:, 5])),color=c3,lw=2,alpha=1.0,linestyle=(0, (1, 1.3)))

ax[0, 0].hist(np.log10(data1_q148[:, 5]), bins=bins, alpha=0.2, color=c2)
ax[0, 0].hist(np.log10(data1_q148[:, 5]), bins=bins, label="Optimized (All Regions)", color=c2, lw=2, histtype="step")
ax[0, 0].axvline(x=np.log10(np.median(data1_q148[:, 5])),color=c2,lw=2,alpha=1.0,linestyle=(0, (1, 1.3)))

ax[0, 0].set_ylabel("Count")
ax[0, 0].legend(loc="upper left")
ax[0, 0].set_xlim(-5, -0.5)
ax[0, 1].set_ylim(0, 45)
ax[0, 0].yaxis.set_ticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])


ax[0, 1].hist(np.log10(data3[:, 4]), bins=bins, alpha=0.2, color=c1)
ax[0, 1].hist(np.log10(data3[:, 4]), bins=bins, color=c1, lw=2, histtype="step")
ax[0, 1].axvline(x=np.log10(np.median(data3[:, 4])),color=c1,zorder=-20,lw=2,alpha=1.0,linestyle=(0, (1, 1.3)),)

ax[0, 1].hist(np.log10(data3[:, 5]),bins=bins,histtype="step",color=c3,linewidth=2)
ax[0, 1].hist(np.log10(data3[:, 5]),bins=bins,color=c3,alpha=0.2)
ax[0, 1].axvline(x=np.log10(np.median(data3[:, 5])),color=c3,lw=2,alpha=1.0,linestyle=(0, (1, 1.3)))

ax[0, 1].hist(np.log10(data3_q148[:, 5]), bins=bins, alpha=0.2, color=c2)
ax[0, 1].hist(np.log10(data3_q148[:, 5]), bins=bins,color=c2, lw=2, histtype="step")
ax[0, 1].axvline(x=np.log10(np.median(data3_q148[:, 5])),color=c2,lw=2,alpha=1.0,linestyle=(0, (1, 1.3)))

ax[0, 1].set_xlim(-5, -0.5)
ax[0, 1].set_ylim(0, 45)
ax[0, 1].yaxis.set_ticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
plt.setp(ax[0, 1].get_yticklabels(), visible=False)


ax[1, 0].hist(np.log10(data2[:, 4]), bins=bins, alpha=0.2, color=c1)
ax[1, 0].hist(np.log10(data2[:, 4]), bins=bins, histtype="step", color=c1, lw=2)
ax[1, 0].axvline(x=np.log10(np.median(data2[:, 4])),color=c1,zorder=-20,lw=2,alpha=1.0,linestyle=(0, (1, 1.3)))

ax[1, 0].hist(np.log10(data2[:, 5]), bins=bins, histtype="step", color=c3, lw=2)
ax[1, 0].hist(np.log10(data2[:, 5]), bins=bins, color=c3, alpha=0.2)
ax[1, 0].axvline(x=np.log10(np.median(data2[:, 5])),color=c3,lw=2,alpha=1.0,linestyle=(0, (1, 1.3)))

ax[1, 0].hist(np.log10(data2_q148[:, 5]), bins=bins, alpha=0.2, color=c2)
ax[1, 0].hist(np.log10(data2_q148[:, 5]), bins=bins, color=c2, lw=2, histtype="step")
ax[1, 0].axvline(x=np.log10(np.median(data2_q148[:, 5])), color=c2, lw=2, alpha=1.0, linestyle=(0, (1, 1.3)))

ax[1, 0].set_xlabel("$\log_{10}(\mathcal{M})$")
ax[1, 0].set_ylabel("Count")
ax[1, 0].set_xlim(-5, -0.5)
ax[1, 0].set_ylim(0, 21)
ax[1, 0].yaxis.set_ticks([0, 5, 10, 15, 20])


ax[1, 1].hist(np.log10(data4[:, 4]), bins=bins, alpha=0.2, color=c1)
ax[1, 1].hist(np.log10(data4[:, 4]), bins=bins, histtype="step", color=c1, lw=2)
ax[1, 1].axvline(x=np.log10(np.median(data4[:, 4])), color=c1, zorder=-20, lw=2, alpha=1.0, linestyle=(0, (1, 1.3)))

ax[1, 1].hist(np.log10(data4[:, 5]), bins=bins, histtype="step", color=c3, lw=2)
ax[1, 1].hist(np.log10(data4[:, 5]), bins=bins, color=c3, alpha=0.2)
ax[1, 1].axvline(x=np.log10(np.median(data4[:, 5])), color=c3, lw=2, alpha=1.0, linestyle=(0, (1, 1.3)))

ax[1, 1].hist(np.log10(data4_q148[:, 5]), bins=bins, alpha=0.2, color=c2)
ax[1, 1].hist(np.log10(data4_q148[:, 5]), bins=bins, color=c2, lw=2, histtype="step")
ax[1, 1].axvline(x=np.log10(np.median(data4_q148[:, 5])), color=c2, lw=2, alpha=1.0, linestyle=(0, (1, 1.3)))

ax[1, 1].set_xlabel("$\log_{10}(\mathcal{M})$")
ax[1, 1].set_xlim(-5, -0.5)
ax[1, 1].set_ylim(0, 21)
ax[1, 1].yaxis.set_ticks([0, 5, 10, 15, 20])
plt.setp(ax[1, 1].get_yticklabels(), visible=False)

ax[0, 0].text(-1.5, 42.8, r'$\chi_1,\chi_2>0$',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=14, bbox=dict(facecolor='none', edgecolor='black', pad=3.0))
ax[0, 1].text(-1.5, 42.8, r'$\chi_1,\chi_2<0$',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=14, bbox=dict(facecolor='none', edgecolor='black', pad=3.0))
ax[1, 0].text(-1.62, 20, r'$\chi_1<0<\chi_2$',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=14, bbox=dict(facecolor='none', edgecolor='black', pad=3.0))
ax[1, 1].text(-1.62, 20, r'$\chi_1>0>\chi_2$',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=14, bbox=dict(facecolor='none', edgecolor='black', pad=3.0))

plt.savefig(paths.figures / "all_quadrants.pdf", bbox_inches="tight")
