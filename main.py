def pa():  # 年金终值
    money = float(input("输入年金额"))
    rate = float(input("输入年利率"))
    year = float(input("输入年限"))
    x = (1 - (1 + rate) ** (-year)) / rate
    ans = money * x
    return ans


def fa():  # 年金现值
    money = float(input("输入年金额"))
    rate = float(input("输入年利率"))
    year = float(input("输入年限"))
    x = ((1 + rate) ** year - 1) / rate
    ans = money * x
    return ans


def pf():  # 复利现值
    money = float(input("输入终值额"))
    rate = float(input("输入年利率"))
    year = float(input("输入年限"))
    x = ((1 + rate) ** year)
    ans = money / x
    return ans


def ff():  # 复利终值
    money = float(input("输入现值额"))
    rate = float(input("输入年利率"))
    year = float(input("输入年限"))
    x = ((1 + rate) ** year)
    ans = money * x
    return ans


if __name__ == '__main__':
    choose = input("1:计算年金现值\n2:计算年金终值\n3:计算复利现值\n4:计算复利终值")
    if choose == '1':
        print(pa())
    elif choose == '2':
        print(fa())
    elif choose == '3':
        print(pf())
    else:
        print(ff())
