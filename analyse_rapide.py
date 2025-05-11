import pandas as pd

df = pd.read_csv("nombre_collaborations.csv")
print("=== Top 3 des collaborations ===")
print(df.sort_values("nombre_publications", ascending=False).head(3))

print("\n=== Répartition par pays ===")
print(df.groupby("pays").sum())
