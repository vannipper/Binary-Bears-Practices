def getSessionCount(timeout, userIds, timestamps):
    sessioncount = 0
    users = {}
    for i, userId in enumerate(userIds):
        if users.get(userId) == None:
            users[userId] = ""
            
        users[userId] += str(timestamps[i]) + ' '
    
    for val in users.values():
        # sort
        val = sorted(list(map(int, val.split())))
        if len(val) > 0:
            sessioncount += 1
        for i in range(len(val)):
            if val[i] - val[i - 1] > timeout:
                sessioncount += 1
    
    return sessioncount

if __name__ == '__main__':
    timeout = int(input().strip())
    print(timeout)
    userIds_count = int(input().strip())
    print(userIds_count)
    userIds = []

    for _ in range(userIds_count):
        userIds_item = input().strip()
        userIds.append(userIds_item)
    print(userIds)
    timestamps_count = int(input().strip())

    timestamps = []

    for _ in range(timestamps_count):
        timestamps_item = int(input().strip())
        timestamps.append(timestamps_item)
    print(timestamps)

    result = getSessionCount(timeout, userIds, timestamps)
    print(result)