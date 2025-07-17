#captain tsubasa
T = int(input())
for _ in range(T):
    parts = input().split()
    N = int(parts[0])
    current = int(parts[1])
    history = []

    for _ in range(N):
        command = input().split()
        if command[0] == 'P':
            history.append(current)
            current = int(command[1])
        elif command[0] == 'B':
            current = history.pop()
    print("Player", current)