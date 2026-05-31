import pandas as pd

# Load Dataset
df = pd.read_csv("netflix_titles.csv")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing director
df["director"] = df["director"].fillna("Unknown")

# Fill missing cast
df["cast"] = df["cast"].fillna("Not Available")

# Fill missing country
df["country"] = df["country"].fillna("Unknown")

# Fill missing rating
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

# Remove rows with missing duration
df = df.dropna(subset=["duration"])

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("\nCleaning Complete!")