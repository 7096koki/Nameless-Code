def HQ9plus(code): #こんな簡単に再現できる言語ってあるんだ...
    code_number = 0
    accumulator = 0
    code = code.upper()
    for i in code:
        if i == "H":
            print("Hello World!")
        elif i == "Q":
            print(code)
        elif i == "9":
            n = 99
            while n != 0:
                n -= 1
                print(f"ビールが壁から落っこちた！残りのビールは{n}本だ！")
                if n == 0:
                    print("あれ?ビールが無くなった?")
        elif i == "+":
            accumulator += 1
            print("スタックに1足しました")
        else:
            print(f'CodeError "{i}" is not defined.')

while True:
    print("HQ9+に処理させたいコードを入力")
    text = input("")
    HQ9plus(text)
