n, bag = map(int, input().split())
if n == 0:
    print('')
else:
    mas = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    ans = [-1] * (bag + 1)
    ans[0] = 0
    dp = [[0] * (bag + 1) for i in range(n)]
    for i in range(n):
        for j in range(bag + 1 - mas[i]):
            cur = bag + 1 - mas[i] - 1 - j
            if ans[cur] != -1:
                ans[cur + mas[i]] = max(ans[cur + mas[i]],
                                        ans[cur] + cost[i])
        for k in range(bag + 1):
            dp[i][k] = ans[k]
    solution = []
    price = max(dp[n - 1])
    ind = dp[n - 1].index(price)
    for i in range(n):
        now = n - 1 - i
        if now < 0:
            break
        if i != n - 1 and price != 0 and ind - mas[now] >= 0:
            if dp[now - 1][ind - mas[now]] == dp[now][ind] - cost[now]:
                solution.append(now + 1)
                price = dp[now][ind] - cost[now]
                ind = ind - mas[now]

        elif i == n - 1 and price != 0:
            solution.append(1)

    for i in (reversed(solution)):
        print(i)
