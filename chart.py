import matplotlib.pyplot as plt

# --- Replace these three numbers with whatever metric you prefer ---
models   = ["Ridge (α=0.01)", "SVR (PCA, C=1)", "Neural Net (L2=0.01)"]
val_mse  = [2.91, 3.95, 0.0095]          # ← e.g. best-validation MSE

plt.figure(figsize=(6, 4))
bars = plt.bar(models, val_mse)
plt.ylabel("Validation MSE")
plt.title("Best-Validation MSE by Model")

# annotate bars
for bar, mse in zip(bars, val_mse):
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             y + max(val_mse)*0.02,
             f"{mse:.3f}",
             ha="center", va="bottom")

plt.xticks(rotation=15)
plt.tight_layout()
plt.show()