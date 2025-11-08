import pandas as pd

df = pd.read_csv('bestsellers.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())


df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].astype(float)

author_counts = df['Author'].value_counts()
print(author_counts)


avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)