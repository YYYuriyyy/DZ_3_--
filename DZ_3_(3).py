##1. сума трьох чисел або добуток трьох чисел

n = float(input("Перше число: "))
n1 = float(input("Друге число: "))
n2 = float(input("Трете число: "))

print(n*n1*n2, n+n1+n2, n-n1-n2, n/n1/n2)

##2. максимум із трьох, мінімум із трьох, або середньоарифметичне трьох чисел

n = int(input("Перше число: "))
n1 = int(input("Друге число: "))
n2 = int(input("Трете число: "))

print(f"Максимальне число: {max(n,n1,n2)}")
print(f"Мінімальне число: {min(n,n1,n2)}")
print(f"Середнє арифм. трьох чисел: {(n+n1+n2) / 3 }")

##3. конвертація метри в милі, дюйми та ярди

m = float(input("Введіть кількість метрів: "))

print(f"Милі: ={0.000621*m}mi.", f"Дюйми: ={39.370078*m}in.", f"Ярди: ={1.09361*m}yd.")