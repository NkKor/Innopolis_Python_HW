import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sphinx.addnodes import index

#5 Pandas
#5.1
df = pd.read_csv("animals.csv", index_col ="name")
print(df.head())

#5.2 Цена крокодила
print("Цена крокодила: ",df.loc["crocodile", "shop_price"])

#5.3 Обитающие на земле
print("Средняя цена обитающих на земле: ",df[df["habitat"] == "land"]["shop_price"].mean())

#5.4 Максимальный iq
max_iq = df["iq_score"].max()
print("Максимальный iq: ",df[df["iq_score"] == max_iq])

#5.5 Наименее дорогие коричневые животные
min_price = df["shop_price"].min()
print("Наименее дорогие коричневые животные: ",df[(df["color"] == "brown") & (df["shop_price"] == min_price)])