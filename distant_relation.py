import random

def distant_relation(range_number):
  parson = ["母","父","兄","弟","姉","妹","友達","いとこ","知り合い","となりの家"]

  for i in range(range_number - 1):
    random_parson = parson[random.randint(0,len(parson) - 1)]

    print(random_parson + "の",end=" ")
  print(random_parson)

test = int(input("関係の遠さの値を入力(数が大きいほど遠くなる):"))
distant_relation(test)
