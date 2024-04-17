import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["figure.figsize"] = (15, 12)


def a_stupid(x):
    return 1 / np.sqrt(x) - 1 / np.sqrt(x + 1)


def b_stupid(x):
    return (1 - np.cos(x)) / np.sin(x)


#def c_stupid(x):
#    δ = 1e-15
#    return np.sin(x + δ) - np.sin(x)
def c_stupid(delta):
    x = 5
    return np.sin(x+delta) -np.sin(x)

def a_smart(x):
    #return (np.sqrt(x + 1) - np.sqrt(x)) / (np.sqrt(x) * np.sqrt(x + 1))
    return 1/((x+1)*np.sqrt(x)+ x*np.sqrt(x+1))


def b_smart(x):
    return np.tan(x/2)

δ = 1e-15


def c_smart(
    delta,
):
    x = 5
    #return np.cos(x) * np.sin(δ) + np.sin(x) * (np.cos(δ) - 1)
    return 2*np.sin(delta/2)*np.cos(delta/2+x)


x = np.logspace(-20, 20, num=10000, dtype=np.float64)


def make_Plot(
    x,
    f1,
    f2,
    axs,
    title,
    xlim=None,
    ylim=None,
    ylimErr=None,
):
    axs[0, 0].plot(x, f1(x), label="before")
    axs[0, 0].plot(x, f2(x), label="after", alpha=0.7)
    axs[0, 0].set_yscale("log")
    axs[0, 0].set_xscale("log")
    if xlim:
        axs[0, 0].set_xlim(xlim)
    if ylim:
        axs[0, 0].set_ylim(ylim)
    axs[0, 0].legend()
    axs[0, 0].set_ylabel(title)
    axs[0, 0].set_title("graph")
    axs[0, 1].plot(x, np.abs((f2(x) - f1(x)) / f2(x)), c="tab:green")
    axs[0, 1].set_title("rel. difference")
    axs[0, 1].set_xscale("log")
    if xlim:
        axs[0, 1].set_xlim(xlim)
    if ylimErr:
        axs[0,1].set_ylim(ylimErr)


fig, axs = plt.subplots(3, 2)
make_Plot(
    x,
    a_stupid,
    a_smart,
    axs,
    "a",
   xlim=(1e15, 1e17),# ylim=(1e-12, 1e-9))
)
make_Plot(
    x,
    b_stupid,
    b_smart,
    axs[1:, :],
    "b",
 xlim=(1e-9, 1e-6))# ylim=(1e-4, 1e-3))
make_Plot(
    x,
    c_stupid,
    c_smart,
    axs[2:, :],
    "c",
 xlim=(1e-16, 1e-14),
 ylimErr=(-0.5,1.5))
plt.tight_layout()
plt.show()
