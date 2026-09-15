# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:38:52 2026

@author: Paulina
"""

import matplotlib.pyplot as plt
import numpy as np

Q = 0.012  # m^3/s
D = np.linspace(0.05, 0.15, 200)
V = (4 * Q) / (np.pi * D**2)

plt.figure(figsize=(7, 4.5))
plt.plot(D, V, color="blue", label="Velocidad V(D)")
plt.title("Diámetro vs Velocidad ")
plt.xlabel("Diámetro ")
plt.ylabel("Velocidad ")
plt.grid(True, )
plt.legend()
plt.tight_layout()
plt.show()