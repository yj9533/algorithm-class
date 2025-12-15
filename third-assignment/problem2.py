def knapsack_solver():
    items = [("노트북", 3, 12), ("카메라", 1, 10), ("책", 2, 6), ("옷", 2, 7), ("휴대용 충전기", 1, 4)]
    try:
        W = int(input("배낭 용량을 입력 하세요 : "))
        n = len(items)
        A = [[0] * (W + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            name, wt, val = items[i-1]
            for w in range(1, W + 1):
                if wt > w: A[i][w] = A[i-1][w]
                else: A[i][w] = max(val + A[i-1][w-wt], A[i-1][w])
                
        selected = []
        curr_w = W
        for i in range(n, 0, -1):
            if A[i][curr_w] != A[i-1][curr_w]:
                selected.append(items[i-1][0])
                curr_w -= items[i-1][1]
        
        print(f"최대 만족도: {A[n][W]}")
        print(f"선택된 물건: {selected[::-1]}")
    except ValueError:
        print("유효한 숫자를 입력하세요.")

knapsack_solver()