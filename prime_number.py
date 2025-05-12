def is_prime_number(number):
    if number <= 1:
        return False

    prime_bool = True
    counter = 2
    while counter * counter <= number:
        if number % counter == 0:
            prime_bool = False
            break
        counter += 1
    return prime_bool

test = int(input("素数かどうか調べたい正の数を入力:"))
print(is_prime_number(test))