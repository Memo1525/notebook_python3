#there are several ways of implementing a queue
#Basically a queue is FIFO structure so first in first out
# in python the built in structure is called LIST and this is more a stack but we can emulate a queue like in the above problem

# if the problem requieres processing elements in the exact same order
# they arrive


#BFS is a good example of it

#process elements as they arrive
#useful on sliding window problems

#when to avoid a queue
#if the problem requires access to elements at arbitrary order
# or requieres sorting and rearranging the data frequentlu

# now 2 examples of problems that use queues

def validParentheses(s: str) -> bool:
    queue = []
    valid_couples = ["()", "[]", "{}"]
    opens = ["(","[", "{"]
    for i in range(len(s)):
        if s[i] in opens:
            queue.append(s[i])
        else:
            last = queue.pop(0)
            if last + s[i] in valid_couples:
                continue
            else:
                return False
    return len(queue) == 0


