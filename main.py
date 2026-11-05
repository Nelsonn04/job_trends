from datasets import load_dataset
import pandas as pd
import duckdb

ds = load_dataset("brusic/hacker-news-who-is-hiring-posts", split="train")
df = ds.to_pandas()

print(df.columns)
print(df.head())
df.to_csv("hn_who_is_hiring.csv", index=False)
df.to_parquet()
df = pd.read_parquet("hf://datasets/brusic/hacker-news-who-is-hiring-posts/data/hiring.parquet")



