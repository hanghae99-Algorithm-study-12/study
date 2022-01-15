def findPalin(str):
    i = 1

    palin = ''
    if len(str) % 2 !=0:
        for i in range(int(len(str)/2)):
            x = int(len(str)/2) - i
            y = int(len(str)/2) + i
            if str[x] != str[y]:
                palin = str[x+1:y]
                break
            elif x == 0:
                palin = str[x:len(str)]
    elif len(str) % 2 == 0:
        for i in range(int(len(str) / 2)):
            x = int(len(str) / 2) - i
            y = int(len(str) / 2) + i - 1
            if str[x] != str[y]:
                palin = str[x + 1:y]
                break
            elif x == 0:
                palin = str[x:len(str)]

    print(palin)

if __name__ == "__main__":
    findPalin('apple')