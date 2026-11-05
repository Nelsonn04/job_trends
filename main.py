from datasets import load_dataset

ds = load_dataset("brusic/hacker-news-who-is-hiring-posts", split="train")
df = ds.to_pandas()

print(df.columns)
print(df.head())
df.to_csv("hn_who_is_hiring.csv", index=False)
