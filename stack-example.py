from arraystack import ArrayStack

# sample usage
if __name__ == '__main__':
    mystack = ArrayStack()
    print(mystack.is_empty())
    mystack.push('hello')
    mystack.push(7)
    print(mystack.__len__())
    print(mystack.pop())