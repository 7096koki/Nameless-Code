def collatz(number):
    result = number

    while result != 1:
        if result % 2 == 0:
            result = result / 2
        else:
            result = (result * 3) + 1

        print(int(result))


test = int(input("コラッツ予想を検証したい自然数を入力:"))
collatz(test)
