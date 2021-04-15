import numpy as np

def large_array(arr):
    H,W = arr.shape

    ans = -100000
    for i in range(H-2):
        for j in range(W-2):
            s = np.sum(arr[i,j:j+3]) + arr[i+1,j+1] + np.sum(arr[i+2,j:j+3])
            print(s)
            if s > ans:
                ans = s

    return ans

if __name__ == '__main__':
    
    arr = []
    for line in open('input.txt', 'r'):
        tmp = list(map(int,line.split()))
        arr.append(tmp)

    arr = np.array(arr)

    print('Answer:',large_array(arr))