# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    start = [0] * int(n)

    for i in range(m):
        thread = 0
        for j in range(1,n):
            if start[j] < start[thread]:
                thread = j
            if start[thread] == start[j] and j < thread:
                thread =j
        
        output.append((thread, start[thread]))
        start[thread] += data[i]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []
    data = list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pairs in result:
        print(pairs[0], pairs[1])


if __name__ == "__main__":
    main()
