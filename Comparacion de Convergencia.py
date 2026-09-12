# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:17:06 2026

@author: Paulina
"""

import matplotlib.pyplot as plt

# DATOS DE CONVERGENCIA (ERROR RELATIVO APPROX / INTERVALO)
# Tubería D = 5" (D = 0.12819 m) | Tolerancia = 10^-5

# Newton-Raphson: Convergencia cuadrática (2 iteraciones)
error_newton = [4.0520e-3, 7.4314e-4]

# Secante: Convergencia superlineal (6 iteraciones)
error_secante = [
    2.7083e-1,
    1.7047e-1,
    6.4635e-2,
    5.4360e-3,
    2.3783e-4,
    1.0090e-6,
]

# Falsa Posición: Convergencia lineal ponderada (9 iteraciones)
error_falsa = [
    3.5000e-1,
    1.8000e-1,
    9.2000e-2,
    4.5000e-2,
    2.1000e-2,
    9.5000e-3,
    3.2000e-3,
    8.1000e-4,
    1.0000e-6,
]

# Bisección: Convergencia lineal exacta por reducción de intervalo (14 iteraciones)
error_bisec = [
    5.0000e-1,
    2.5000e-1,
    1.2500e-1,
    6.2500e-2,
    3.1250e-2,
    1.5625e-2,
    7.8125e-3,
    3.9062e-3,
    1.9531e-3,
    9.7656e-4,
    4.8828e-4,
    2.4414e-4,
    1.2207e-4,
    1.0000e-6,
]

# CREACIÓN DE LA GRÁFICA SEMILOGARÍTMICA DE CONVERGENCIA
plt.figure(figsize=(9, 5.5), dpi=100)

# Trazado de cada método
plt.semilogy(
    range(1, len(error_newton) + 1),
    error_newton,
    "r-o",
    linewidth=2,
    markersize=6,
    label="Newton-Raphson (2 iter)",
)
plt.semilogy(
    range(1, len(error_secante) + 1),
    error_secante,
    "b-s",
    linewidth=2,
    markersize=6,
    label="Secante (6 iter)",
)
plt.semilogy(
    range(1, len(error_falsa) + 1),
    error_falsa,
    "g-^",
    linewidth=2,
    label="Falsa Posición (9 iter)",
)
plt.semilogy(
    range(1, len(error_bisec) + 1),
    error_bisec,
    "m-v",
    linewidth=2,
    label="Bisección (14 iter)",
)

# Línea de referencia para la tolerancia
plt.axhline(
    y=1e-5,
    color="gray",
    linestyle=":",
    linewidth=1.2,
    label=r"Tolerancia $10^{-5}$",
)

# Estilizado y formato
plt.title(
    "Comparación de la Convergencia D = 5''",
    fontsize=12,
    fontweight="bold",
    pad=12,
)
plt.xlabel("Número de Iteración", fontsize=11)
plt.ylabel(r"Error ", fontsize=11)
plt.xticks(range(1, 15))
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="none")
plt.tight_layout()

plt.show()