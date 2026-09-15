# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 23:56:14 2026

@author: Paulina
"""

import matplotlib.pyplot as plt

# Datos de tu tabla
diametros_in = [2, 3, 4, 5, 6]
hf_m = [241.6005, 30.6801, 7.4694, 2.3095, 0.8928]

plt.figure(figsize=(8, 5))
plt.plot(diametros_in, hf_m, "b-o", linewidth=2, markersize=6)
plt.axhline(
    y=5.0,
    color="r",
    linestyle="--",
    linewidth=1.2,
    label=r"Pérdida máxima (hf = 5\text{ m}$)",
)

plt.title(
    r"Pérdida de carga por fricción en función del diámetro (D vs. hf)",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Diámetro (pulgadas)", fontsize=11)
plt.ylabel(r"Pérdida de carga hf (m)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(loc="upper right")
plt.tight_layout()

plt.show()