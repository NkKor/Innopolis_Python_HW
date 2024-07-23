#home work 1 ----------------------------------------
name = input()
surname = input()
print('Привет,',name,surname+'!')

#home work 2 ----------------------------------------
student1 = input()
student2 = input()
if student1 == student2*4:
    print(True)
else:
    print(False)
    
#home work 3 ----------------------------------------
product = input()
weight = int(input())
if product == 'яблоки':
    kkal = (weight * 1000) / 100 * 52
    print(int(kkal))
elif product == 'бананы':
    kkal = (weight * 1000) / 100 * 89
    print(int(kkal))
elif product == 'помидоры':
    kkal = (weight * 1000) / 100 * 24
    print(int(kkal))
else:
    print('В базе нет такого продукта')
    
#home work 4 ----------------------------------------
num_meals = int(input())
kkal = 0
for i in range(0,num_meals):
    product = input()
    weight = int(input())
    if product == 'яблоки':
        kkal+= (weight * 1000) / 100 * 52
    elif product == 'бананы':
        kkal+= (weight * 1000) / 100 * 89
    elif product == 'помидоры':
        kkal+= (weight * 1000) / 100 * 24
    else:
        print('В базе нет такого продукта')
        continue
print(int(kkal))

#home work 5 ----------------------------------------
weight = 0
weight_sum = 0
counter = 0
while True:
    weight = int(input())
    if weight_sum + weight > 50:
        break
    weight_sum += weight
    counter += 1
print(weight_sum)
print(counter)

