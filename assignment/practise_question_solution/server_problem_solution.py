
no_of_request= int(input("Enter the number of requests: "))
request= list(map(int, input("Enter the requests: ").split(',')))
all_server_1=[]
deall_server_1=[]
all_server_2=[]
deall_server_2=[]
for i in range(len(request)):
    if i % 2 == 0:
        if request[i] == -1:
            deall_server_1.append(request[i])
        else:
            all_server_1.append(request[i])
    else:
        if request[i] == -1:
            deall_server_2.append(request[i])
        else:
            all_server_2.append(request[i])
print("tottal allocation by server 1 is:", len(all_server_1))
print("tottal deallocation by server 1 is:", len(deall_server_1))