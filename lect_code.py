"""
data = np.array([10,20,30,40,50])
np.save('my_array.npy',data)
loaded_arr = np.load("my_array.npy")
print(loaded_arr)


data = {'Имя':['Анна','Петр','Мария'],'Возраст':[25,30,22]}
df = pd.DataFrame(data)
df['Зарплата']=[50000,60000,45000]
df["Возраст"].max()
#print(df.head())
#print(df.describe())
#print(df["Возраст"].max())

#df = pd.read_csv("cameras.csv")
plt.hist(df["Возраст"])
plt.show()


image=plt.imread('image.jpg')
#plt.imshow(image)
#plt.show()

#Изменениеразмераизображения
resized_image = image[::5, ::5]
#Отображениеизображения
plt.imshow(resized_image)
plt.show()

hight = np.array([i for i in range(175, 185)])
weight = np.array([i for i in range(55, 65)])
bmi = weight / (hight/100) ** 2
normal_bmi = np.sum((bmi >= 18) & (bmi <= 25))
print(normal_bmi) """



