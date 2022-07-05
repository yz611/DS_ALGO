from LinkedList import LinkedList, Node

def intersect(ll1, ll2):
    if ll1.tail != ll2.tail:
        return False

    n1 = ll1.head
    n2 = ll2.head
    if len(ll1)>=len(ll2):
        shift = len(ll1)-len(ll2)
        for _ in range(shift):
            if n1.next is not None:
                n1 = n1.next
    else:
        shift = len(ll2) - len(ll1)
        for _ in range(shift):
            if n2.next is not None:
                n2 = n2.next
    
    while n1 or n2:
        if n1.value != n2.value:
            n1 = n1.next
            n2 = n2.next
        else:
            return n1

# Helper addition method
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3,0,10)


llB = LinkedList()
llB.generate(4,0,10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)
print(intersect(llA, llB))


    
    