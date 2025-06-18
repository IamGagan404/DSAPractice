''''
BLUEPRINT
example of sudoku solver
Choice
what are choices can be made at every step of algorithm

Constraints
can we know if this path does not meet our end goal? if not can we "backtrack" to last "good" choice made

Goals
can we know our path has reached out goal

'''


def count_path(r,c):
    if r == 1 or c == 1:
        return 1
    left = count_path(r-1,c)
    right = count_path(r,c-1)
    return left+right

# print(count_path(3,3))


def print_path(path,r,c):
    if r == 1 and c == 1:

        return [path]
    li = []
    if r > 1:
        li.extend(print_path(path+'D',r-1,c))
    if c > 1:
        li.extend(print_path(path+"R",r,c-1))
    # if r > 1 and c > 1:
    #     li.extend(print_path(path+"d",r-1,c-1))
    return li
# print(print_path("",3,3))

def pathObstacle(path,maze,r,c):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return [path]

    if maze[r][c] == 0:
        return [None]
    li = []
    if r < len(maze) - 1:
        li.extend(pathObstacle(path+'D',maze,r+1,c))
    if c < len(maze[0]) - 1:
        li.extend(pathObstacle(path+"R",maze,r,c+1))
    return li
maze = [[1,1,1],[1,0,1],[1,1,1]]
# print(pathObstacle("",maze,0,0))


# 22 Generate parenthesis
def gen_para(n):
    # choice take ( or )
    # constraints len = n*2 check if count of ) greater than (
    # goal valid parenthesis and len n*2

    def valid_para(s):
        stack = []
        s = list(s)
        for i in range(len(s)):
            # print(stack,s[i])
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                if stack and stack[-1] == "(":
                    stack = stack[:-1]
                else:
                    return False

        return True if len(stack) == 0 else False
    re = []
    def helper(s,re,n):
        if len(s) == n*2 and valid_para(s):
            re.append(s)
            return
        if len(s) == n*2 and not valid_para(s) :

            return
        helper(s+"(",re,n)
        helper(s+")",re,n)
    helper("",re,n)
    return re
# print(gen_para(1))

# 78 subsets, 90 subsets 2
def subsets(nums):
    def helper(re,temp,nums,start):
        re.append(list(temp))
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1] : continue # for duplicates case
            temp.append(nums[i])
            helper(re,temp,nums,i+1)
            temp.pop()
    re = []
    nums.sort()
    helper(re,[],nums,0)
    return re
# print(subsets([1,2,2,3]))

# 46 permutations
def perm(nums):
    def helper(re,perm,nums):
        if len(perm) == len(nums):
            re.append(list(perm))
        else:
            for i in range(len(nums)):
                if nums[i] in perm: continue
                perm.append(nums[i])
                helper(re,perm,nums)
                perm.pop()
    re = []
    helper(re,[],nums)
    return re
# print(perm([1,2,2]))

# 47 permutation 2
def perm2(nums):
    def helper(re,perm,used,nums):
        if len(perm) == len(nums):
            re.append(list(perm))
        else:
            for i in range(len(nums)):
                if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
                used[i] = True
                perm.append(nums[i])
                helper(re,perm,used,nums)
                used[i] = False
                perm.pop()
    re = []
    used = [False] * len(nums)
    nums.sort()
    helper(re,[],used,nums)
    return re
# print(perm2([3,3,2,3]))

# 39 combination sum
def comb_sum(nums,target):
    def helper(re,temp,nums,start,target):
        if sum(temp) > target:
            return
        if sum(temp) == target:
            re.append(list(temp))
            return

        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1]: continue
            temp.append(nums[i])
            helper(re,temp,nums,i+1,target)
            temp.pop()
    re = []
    nums.sort()
    helper(re,[],nums,0,target)
    return re
# print(comb_sum(nums = [10,1,2,7,6,1,5], target = 8))


# 131 palindrome partitioning
def partition(input_string):
    list_of_partitions = []
    backtrack(list_of_partitions, [], input_string, 0)
    return list_of_partitions

def backtrack(list_of_partitions, temporary_list, input_string, start):
    if start == len(input_string):
        list_of_partitions.append(temporary_list[:])
    else:
        for index in range(start, len(input_string)):
            if is_palindrome(input_string, start, index):
                temporary_list.append(input_string[start:index + 1])
                backtrack(list_of_partitions, temporary_list, input_string, index + 1)
                temporary_list.pop()



def is_palindrome(input_string, low, high):
    while low < high:
        if input_string[low] != input_string[high]:
            return False
        low += 1
        high -= 1
    return True

# print(partition("aab"))


# 77 combinations
def coms(n,k):
    def helper(re,temp,k,start):
        if len(temp) == k:
            re.append(list(temp))
            return
        for i in range(start,len(nums)):
            temp.append(nums[i])
            helper(re,temp,k,i+1)
            temp.pop()
    nums = [i for i in range(1,n+1)]
    re = []
    helper(re,[],k,0)
    return re
# print(coms(4,2))

#
# 216 combination sum 3
def comb_sum3(k,n):
    def helper(re,temp,n,k,nums,start):
        if sum(temp) == n and len(temp) == k:
            re.append(list(temp))
            return
        if len(temp) > k or sum(temp) > n:
            return

        for i in range(start,len(nums)):
            temp.append(nums[i])
            helper(re,temp,n,k,nums,i+1)
            temp.pop()
    nums = [i for i in range(1,10)]
    re = []
    helper(re,[],n,k,nums,0)
    return re
# print(comb_sum3(3,9))

# 257 binary tree path

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_path(root):
    def helper(re,temp,node):
        if not node.left and not node.right:
            temp = temp  + str(node.val)
            re.append(temp)
            return
        temp = temp  + str(node.value)+ "->"
        if node.left:
            helper(re,temp,node.left)
        if node.right:
            helper(re,temp,node.right)
    re = []
    helper(re,[],root)
    return re

# 282 expression add operators
def exp_opr(nums, target): # complete this
    def helper(re,temp1,temp2,nums,target,exp):
        temp1 = temp1 + exp + temp2[0]
        temp2 = temp2[1:]
        if len(temp1) == (len(nums)*2)-1 and eval(temp1) == target:
            re.append(temp1)
            print(re)
            return
        if len(temp1) == (len(nums)*2)-1 and eval(temp1) != target:
            return

        helper(re,temp1,temp2,nums,target,"+")
        helper(re,temp1,temp2,nums,target,"-")
        helper(re,temp1,temp2,nums,target,"*")

    re= []
    helper(re,"",nums,nums,target)
    return re
# print(exp_opr(nums = "123", target = 6))


# 93 restore IP address
def restore_ip(s):
#     choice : put . on 1,2,3 locations
#     constraints less than 255 no leading zero
#     goal  if valid add to result

    def helper(re,temp,start,used):
        if used == 4 and start == len(s):
            re.append(temp[:-1])
            return
        if used > 4 :
            return
        for i in range(start,min(len(s),start+3)):
            if int(s[start:i+1]) < 256 and (i == start or s[start] != "0"):
                helper(re,temp+s[start:i+1]+".",i+1,used+1)
    re = []
    if len(s) > 12:
        return re
    helper(re,"",0,0)
    return re
# print(restore_ip("25525511135"))












