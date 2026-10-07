"""Generates figures/cooling-curves.pdf from ../cooling.csv.

Not needed during the workshop -- the PDF is shipped with the template.
Kept here so the figure can be regenerated if you want to change it.

NOTE ON THE DATA
cooling.csv is SYNTHETIC. It is Newton's law of cooling evaluated for
three plausible time constants, plus simulated thermometer noise. No
actual coffee was harmed. The report is a realistic-looking example to
write LaTeX around, not a real measurement.
"""

import csv
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

T_0 = 85.0      # degC, temperature at t = 0
T_env = 21.0    # degC, ambient temperature

# label, column in cooling.csv, fitted time constant / min, colour, marker
vessels = [
    ("Ceramic mug",  "mug_degC",    24.0, "#1f4e79", "o"),
    ("Glass",        "glass_degC",  18.0, "#c0392b", "s"),
    ("Vacuum flask", "flask_degC", 310.0, "#2e7d32", "^"),
]

# ---------------------------------------------------------------------
#  Read the measurements. Lines starting with # are comments.
# ---------------------------------------------------------------------
with open("cooling.csv", newline="") as f:
    rows = list(csv.DictReader(line for line in f if not line.startswith("#")))

t_meas = np.array([float(r["time_min"]) for r in rows])

fig, ax = plt.subplots(figsize=(5.4, 3.3))

# The band in which the drink is considered drinkable.
ax.axhspan(50.0, 65.0, color="#f0c419", alpha=0.18, zorder=0)
ax.text(58.0, 57.5, "drinkable", fontsize=8, color="#8a6d00",
        ha="right", va="center")

t_model = np.linspace(0.0, 60.0, 400)
every = 15      # plot a marker every 15th reading, else they merge

for label, column, tau, colour, marker in vessels:
    ax.plot(t_model, T_env + (T_0 - T_env) * np.exp(-t_model / tau),
            color=colour, lw=1.5, zorder=2)
    T_meas = np.array([float(r[column]) for r in rows])
    ax.plot(t_meas[::every], T_meas[::every], marker, ms=4.0, color=colour,
            mfc="none", mew=1.2, label=label, zorder=3)

ax.axhline(T_env, color="0.55", lw=0.9, ls="--", zorder=1)
ax.text(1.0, T_env - 3.5, "ambient", fontsize=8, color="0.4", ha="left")

ax.set_xlabel("Time $t$ / min")
ax.set_ylabel(r"Temperature $T$ / $^\circ$C")
ax.set_xlim(0, 60)
ax.set_ylim(15, 90)
ax.grid(True, lw=0.4, color="0.9", zorder=0)
ax.legend(frameon=False, loc="upper right", fontsize=9)
fig.tight_layout()

fig.savefig("cooling-curves.pdf")
print("written: cooling-curves.pdf")
