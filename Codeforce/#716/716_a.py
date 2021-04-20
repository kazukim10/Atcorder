# A
def problem_A(n,a):
    
    for i in range(len(a)):
        for j in range(i,len(a)):
            tmp = a[i]*a[j]

        if int(tmp**0.5)**2 != tmp:
            return 'YES'

    return 'NO'

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))

        print(problem_A(n,a))