from module import sum1, prod1, __counter


if __name__ == "__main__":
    zeroes=[0 for i in range(5)]
    ones=[1 for i in range (5)]
    print(sum1(zeroes))
    print(prod1(ones))
    print(__counter)