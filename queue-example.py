from arrayqueue import ArrayQueue

# sample usage
if __name__ == '__main__':
    myq = ArrayQueue()
    print(myq.is_empty())
    myq.enqueue('hello')
    myq.enqueue(7)
    print(myq.__len__())
    print(myq.dequeue())