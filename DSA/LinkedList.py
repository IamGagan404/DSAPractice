class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_ll(head):
    while head:
        print(head.val,end='->')
        head = head.next
    print('\n')

def swapPairs(head):
    cur = head
    dummy = ListNode(next=head)
    prev = dummy
    while cur and cur.next:
        fut = cur.next.next
        sec = cur.next

        sec.next = cur
        cur.next = fut
        prev.next = sec

        prev = cur
        cur = fut
    return print_ll(dummy.next)

def make_ll(nums):
    for a in range(len(nums)):
        nums[a] = ListNode(nums[a])
    for i in range(len(nums)-1):
        nums[i].next = nums[i+1]
    return nums[0]


head = make_ll([1,2,3,4,5])

def reverse_ll(head):
    prev = None
    pres = head
    if head.next:
        fut = head.next
    while fut:
        pres.next = prev
        pres = fut
        prev = pres
        if fut.next:
            fut = fut.next
    return pres
print_ll(reverse_ll(head))









