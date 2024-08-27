import matplotlib.pyplot as plt
import pandas as pd


#5 Pandas
#5.1
df = pd.read_csv("animals.csv", index_col ="name")
df2 = pd.read_csv("height.csv")
print(df.head())

#5.2 Цена крокодила
print("Цена крокодила: ",df.loc["crocodile", "shop_price"])

#5.3 Обитающие на земле
print("Средняя цена обитающих на земле: ",df[df["habitat"] == "land"]["shop_price"].mean())

#5.4 Максимальный iq
max_iq = df["iq_score"].max()
print("Максимальный iq: ",df[df["iq_score"] == max_iq])

#5.5 Наименее дорогие коричневые животные
min_price = df[df["color"] == "brown"]["shop_price"].min()
print("Наименее дорогие коричневые животные: ",df[(df["color"] == "brown") & (df["shop_price"] == min_price)])

#5.6
print("Среднее значение IQ по ареалу:", df.groupby("habitat")["iq_score"].mean())

#5.7
df = df.merge(df2, left_index= True, right_on= "name")
print(df.head(3))

#5.8
fig, axs = plt.subplots(1, figsize = (10,3)) # По какой то причине получаются нечитабельные данные в гистограме
axs.hist(df[df["habitat"] == "air"])
axs.set_title("Летающие животные")
axs.set_xlabel("name")
axs.set_ylabel("height")
plt.show()