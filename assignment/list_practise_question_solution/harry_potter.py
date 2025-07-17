#Harry Potter problem
def harry_potter_stone():
    n = int(input())
    coins = list(map(int, input().split()))
    q, x = map(int, input().split())
    instructions = [input().strip() for _ in range(q)]

    stack = []
    index = 0
    total = 0

    for ins in instructions:
        if ins == "Harry":
            if index < n:
                coin = coins[index]
                stack.append(coin)
                total += coin
                index += 1
        elif ins == "Remove":
            if stack:
                total -= stack.pop()

        if total == x:
            print(len(stack))
            return

    print(-1)