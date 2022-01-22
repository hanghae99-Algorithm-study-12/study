# 2에서 9 까지 숫자가 주어졌을 때 전화번호로 조합가능한 모든 문자를 출력하라.
def number(s):

    def dfs(index,path):
        if len(path)==len(s):
            answer.append(path)
            return

        for i in range(index,len(s)):
            for j in dic[s[i]]:
                dfs(i+1,path+j)

    if not s:
        return[]
    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    answer = []
    dfs(0, "")

    return answer

a = "234"
print((number(a)))
