def create_circular_queue(size):
    return {
        'data': [None] * size,
        'front': -1,
        'rear': -1,
        'size': size
    }

def is_empty(queue):
    return queue['front'] == -1

def is_full(queue):
    return (queue['rear'] + 1) % queue['size'] == queue['front']

def enqueue(queue, value):
    if is_full(queue):
        print("Queue is full")
        return
    if is_empty(queue):
        queue['front'] = queue['rear'] = 0
    else:
        queue['rear'] = (queue['rear'] + 1) % queue['size']
    queue['data'][queue['rear']] = value

def dequeue(queue):
    if is_empty(queue):
        print("Queue is empty")
        return None
    value = queue['data'][queue['front']]
    if queue['front'] == queue['rear']:
        queue['front'] = queue['rear'] = -1
    else:
        queue['front'] = (queue['front'] + 1) % queue['size']
    return value