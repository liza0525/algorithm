def solution(numbers):
    answer = ''.join(sorted(list(map(str, numbers)), key=lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]), reverse=True))
    return answer if int(answer) != 0 else '0'