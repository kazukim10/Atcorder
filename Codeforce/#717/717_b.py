# B
def problem_B(n,a):
    
    l = len(a)
    while l > 2:
        x = a[0]
        y = a[1]
        z = x^y
        a = a[2:]+[z]
        print(a,set(a))
        l = len(a)

        if len(set(a))==1:
            return 'YES'
 
    else:
        return 'NO'

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))

        print(problem_B(n,a))