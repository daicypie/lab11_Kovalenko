class QueueError(Exception):
    def __init__(self, message="Queue is empty"):
        self.message = message
        super().__init__(self.message)


class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.insert(0, elem)

    def get(self):
        if not self.list_queue:
            raise QueueError("Cannot get from an empty queue")
        else:
            elem = self.list_queue.pop()
        return elem


que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except QueueError as e:
    print(e)