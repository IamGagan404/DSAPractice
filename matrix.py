# Spiral traversal of matrix
def spiral_mat(mat):
    n = len(mat)
    m = len(mat[0])

    left = 0
    right = m-1
    top = 0
    bottom = n-1

    ans = []
    while top <= bottom and left <= right:  # to check if there are still columns and row left to traverse
        print(ans)
        for i in range(left,right+1):
            ans.append(mat[top][i])
        top += 1

        for i in range(top,bottom+1):
            ans.append(mat[i][right])
        right -= 1

        if top <= bottom: # as top is changing inside while loop, had to be checked again
            for i in range(right,left-1,-1):
                ans.append(mat[bottom][i])
            bottom -= 1
        if left <= right: # as right is changing inside while loop, had to be checked again
            for i in range(bottom,top-1,-1):
                ans.append(mat[i][left])
            left += 1
    return ans
print(spiral_mat([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))