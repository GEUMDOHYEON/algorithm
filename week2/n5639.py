import sys

sys.setrecursionlimit(10 ** 9)

tree = []

while True:
    try:
        tree.append(int(sys.stdin.readline().rstrip())) # 연속적으로 값을 받아와 리스트에 추가됨.
    except:
        break # 빈 값에 엔터하면 입력 끝.

def bsTree(rootIdx,endIdx):
    global tree

    if rootIdx > endIdx:
        return
    
    midIdx = endIdx + 1

    for i in range(rootIdx + 1, endIdx + 1):
        if tree[rootIdx] < tree[i]:
            midIdx = i
            break
    
    bsTree(rootIdx + 1,midIdx - 1)

    bsTree(midIdx,endIdx)    

    print(tree[rootIdx])

bsTree(0,len(tree)-1)

# def bsTree(trees):
    # tmpTree = []

    # for i in range(len(trees)):
    #     if trees[0] > trees[i]:
    #         tmpTree.append(trees[i])

    # if tmpTree:
    #     bsTree(tmpTree)
    # else:
    #     return
    
    # print(tmpTree)
    
# bsTree(tree)
