# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:25:53 2026

@author: Paulina
"""

import matplotlib.pyplot as plt
import numpy as np

# Parámetros del caso ideal (D = 5" = 0.12819 m)
D = 0.12819  # m
epsilon = 0.00015  # m
e_D = epsilon / D
Re = 1.19e5


# Formulación de Colebrook como F(f) = 0
def F(f):
  term = (e_D / 3.7) + (2.51 / (Re * np.sqrt(f)))
  return (1.0 / np.sqrt(f)) + 2.0 * np.log10(term)


# Rango de evaluación para el factor de fricción f
f_vals = np.linspace(0.015, 0.035, 500)
F_vals = F(f_vals)

# Graficación
plt.figure(figsize=(8, 5))
plt.plot(f_vals, F_vals, "b-", linewidth=2, label=r"$F(f)$")
plt.axhline(
    0, color="red", linestyle="--", linewidth=1.2, label=r"Eje $F(f) = 0$"
)

# Marcado de la raíz aproximada (f ≈ 0.0224)
plt.plot(
    0.0224,
    0,
    "ro",
    markersize=8,
    label=r"Raíz aproximada ($f \approx 0.0224$)",
)

plt.title(
    r"$F(f)$ Identificación de la raíz",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel(r"Factor de fricción ($f$)", fontsize=11)
plt.ylabel(r"$F(f)$", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(loc="upper right")
plt.tight_layout()

plt.show()