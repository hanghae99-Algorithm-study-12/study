def solution(dirs):
    answer = 0
    x,y=0,0
    temp2=[]
    for i in dirs:
        temp=[]
        temp.append([x,y])
        if i == "U" and y<5:
            y+=1
        elif i == "D" and y>-5:
            y -= 1
        elif i == "R" and x<5:
            x+=1
        elif i == "L" and x>-5:
            x -= 1
        else:
            temp.pop()
            continue
        temp.append([x, y])

        temp2.append(sorted(temp))

    for i in range(len(temp2)):
        if temp2[i] not in temp2[:i]:
            print(temp2[i])
            answer += 1

    return answer

dirs ="UDU"
print(solution(dirs))