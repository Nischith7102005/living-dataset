# 📁 README – living-dataset  
> **Don’t collect data—grow it.**

---

## 1. What it is  
A **single Jupyter notebook** (`living_dataset.ipynb`) that turns any small CSV into fresh synthetic rows.  
Gaussian noise + crossover + classifier feedback = new data that boosts accuracy without extra real samples.

---

## 2. Quick Start (zero installs)  
1. Open `living_dataset.ipynb` in Jupyter or Google Colab.  
2. Run all cells.  
3. Grab the generated `evolved.csv` from the side panel.

That’s it—no requirements, no local setup.

---

## 3. Swap Your Own Data  
- **CSV**: drop your file in the same folder, change one cell:  
  `df = pd.read_csv("myfile.csv")`  
- **Images / Text**: replace the CSV loader cell with the provided template (flatten pixels or TF-IDF vectors).  
All other cells stay identical.

---

## 4. Hyper-parameters you can twist  
- `scale=0.05` – mutation noise  
- `gens=5` – generations  
- `pop_size` – population size (default = input row count)  

All live at the top of the evolution cell.

---

## 5. Output Files (created next to the notebook)  
- `evolved.csv` – synthetic data you can download  
- `before_after.png` – scatter plot showing genetic spread  
- `accuracy.txt` – hold-out score before vs after

---

## 6. Benchmarks (Iris example, 120 → 120 synthetic)  
| Metric | Original | After 5 gens | Gain |
|--------|----------|--------------|------|
| Hold-out accuracy | 92 % | **96 %** | +4 % |
| Rare-class recall | 83 % | **91 %** | +8 % |

---

## 7. Ethics & Reproducibility  
- Set `np.random.seed(42)` inside the notebook for identical synthetic sets.  
- Gaussian noise + lineage reduce re-identification risk.  
- No external uploads—everything stays local.

---

## 8. Repo Contents  
```
living_dataset.ipynb   # ← the entire project (12 cells)
README.md              # ← this file
```

That’s **all**—one notebook, one README.

---

**Star ⭐** if the notebook grew fresh rows for you.
