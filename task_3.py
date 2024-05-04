def move(n, first, third, second):
    if n == 1:
        print(f"Перемістити диск з {first} на {third}: 1")
    else:
        move(n - 1, first, second, third)
        print(f"Перемістити диск з {first} на {third}: {n}")
        move(n - 1, second, third, first)

def main():
    n = int(input("Введіть кількість дисків: "))
    towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print("Початковий стан:", towers)
    move(n, 'A', 'C', 'B')
    print("Кінцевий стан:", towers)

if __name__ == "__main__":
    main()