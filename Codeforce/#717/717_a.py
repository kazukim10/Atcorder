# A
def problem_A(n,k,a):
    count = 0

    i = 0
    while count < k and i <= len(a)-1:

        if a[i] > 0:
            count += 1
            a[i] -= 1
            a[-1] += 1

        elif a[i] <= 0:
            i += 1
        
    return a

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))

        ans = problem_A(n,k,a)
        print(' '.join(map(str,ans)))