class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DLLNode:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

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


# head = make_ll([1,2,3,4,5])

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
# print_ll(reverse_ll(head))

#################### Striver's Linked List Series ##############################
# Given the head of a linked list, print the length of the linked list.
def get_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

# Given the head of a linked list and an integer value, find out whether the integer is present 
# in the linked list or not. Return true if it is present, or else return false.
def search_element(head,num):
    temp = head
    while temp:
        if temp.val == num:
            return True
        temp = temp.next
    return False

# Given a doubly linked list of size ‘N’ consisting of positive integers, 
# your task is to reverse it and return the head of the modified doubly linked list.
def reverse_dll(head):
    cur = head
    prev = None
    while cur:
        prev = cur.prev
        cur.prev = cur.next
        cur.next = prev
        cur = cur.prev
    return prev.prev

# Given two non-empty linked lists l1 and l2 which represent two non-negative integers. 
# The digits are stored in reverse order with each node storing one digit.Add two numbers and 
# return the sum as a linked list.
def addTwoNumbers(l1, l2):
    def get_num(head):
        re = 0
        count = 0
        while head:
            re = re + head.val*(pow(10,count))
            head = head.next
            count += 1
        print(re)
        return re
    sum_num = get_num(l1) + get_num(l2)
    print(sum_num)
    dummy = ListNode(0)
    head = dummy
    while sum_num > 0:
        data = sum_num % 10
        sum_num = sum_num // 10
        new_node = ListNode(data)
        dummy.next = new_node
        dummy = new_node
    return head.next

def addTwoNumbers2(l1,l2):
    dummy = ListNode(0,None)
    head = dummy
    carry = 0
    while l1 or l2:

        if l1:
            l1_val = l1.val
        else:
            l1_val = 0
        if l2:
            l2_val = l2.val
        else:
            l2_val = 0
            
        node_sum = l1_val + l2_val + carry
        carry = node_sum % 10
        node_sum = node_sum // 10
        NewNode = ListNode(carry)
        head.next = NewNode
        head = head.next
        if l1: 
            l1 = l1.next
        
        if l2: l2 = l2.next
    return dummy.next

#
l1 = make_ll([5,4])
l2 = make_ll([4])
print_ll(addTwoNumbers2(l1,l2))


# 328. Odd Even Linked List
def even_odd(head):
    dummy = head
    last_odd = head
    last_even = head.next
    og_even = head.next
    while last_even or last_odd:
        new_odd = last_even.next
        if new_odd == None:
            return dummy
        new_even = new_odd.next
        last_odd.next = new_odd
        last_even.next = new_even
        new_odd.next = og_even
        last_odd = new_odd
        last_even = new_even
    return dummy
# print_ll(even_odd(make_ll([1,2,3,4,5,6,7,8])))


# add one to linked list
def addone(head):
    cur = head
    num = 0
    while cur:
        num = num*10 + cur.val
        cur = cur.next
    num = num + 1
    nums = [int(x) for x in list(str(num))]
    for a in range(len(nums)):
        nums[a] = ListNode(nums[a])
    for i in range(len(nums)-1):
        nums[i].next = nums[i+1]
    return nums[0]
# l = make_ll([1,2,3])
# print_ll(addone(l))

# Reverse linked list in k gropus
def reverse_k_grps(head,k):
    def find_k_node(node,k):
        k -= 1
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def reverse_list(node):
        temp = node
        prev = None
        while temp:
            fut = temp.next
            temp.next = prev
            prev = temp
            temp = fut
        return prev

    temp = head
    prev = None
    while temp:
        knode = find_k_node(temp,k)
        if knode == None:
            if prev: prev.next = temp
            break
        nextnode = knode.next
        knode.next = None
        reverse_list(temp)
        if temp == head:
            head = knode
        else:
            prev.next = knode
        prev = temp
        temp = nextnode
    return head
head = make_ll([1,2,3,4,5,6,7,8,9,10])
print_ll(reverse_k_grps(head,3))



