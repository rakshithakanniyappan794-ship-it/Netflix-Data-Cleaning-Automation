import pandas as pd

df = pd.read_csv("netflix_cleaned.csv")

print("\n===== NETFLIX REPORT =====")

print("\nTotal Records:")
print(len(df))

print("\nMovies vs TV Shows:")
print(df["type"].value_counts())

print("\nTop 10 Countries:")
print(df["country"].value_counts().head(10))

print("\nTop 10 Ratings:")
print(df["rating"].value_counts().head(10))

print("\nLatest Release Year:")
print(df["release_year"].max())