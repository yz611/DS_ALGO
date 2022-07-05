from LinkedList import LinkedList

def partition(ll, x):
    curNode = ll.head
    ll.tail = curNode

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = ll.tail.next
        curNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 50)
print(customLL)
