import argparse
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



if __name__ == "__main__":
    t = np.linspace(0, 1, num=1000)
    f = 1
    y = np.sin(2*np.pi*f*t)
    plt.figure()
    plt.plot(t, y, color="black")
    plt.axis("off")
    plt.savefig("output.svg", transparent=True)

