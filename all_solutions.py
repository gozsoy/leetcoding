# 133. Clone Graph
# dfs, graph
# time: O(V+E), space: O(V)
# E: edge cnt, V: node cnt
from typing import Optional

def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    
    d = {}
    queue = [node]

    while len(queue) > 0:

        temp_node = queue.pop(0)

        if temp_node:

            if len(d) == 0:
                d[temp_node.val] = Node(temp_node.val, [])
            
            for n in temp_node.neighbors:
                
                if not d.get(n.val):
                    queue.append(n)
                    d[n.val] = Node(n.val)

                d[temp_node.val].neighbors.append(d[n.val])

    if len(d) == 0:
        return None
    else:
        return d[1]

# ---------------------------------------------------
# 501. Find Mode in Binary Search Tree
# dfs, BST
# time: O(V+E), space=O(1) excluding recursion stack

def findMode(self, root: Optional[TreeNode]) -> List[int]:
    
    max_freq = 0
    modes = []
    curr_val = None
    curr_freq = 0   

    def aux(node):

        nonlocal max_freq, curr_freq, curr_val, modes

        if node:

            aux(node.left)

            if curr_val is None:
                curr_val = node.val
                curr_freq = 1
            elif node.val == curr_val:
                curr_freq += 1
            else:
                curr_val = node.val
                curr_freq = 1

            if curr_freq > max_freq:
                modes = []
                max_freq = curr_freq
            
            if curr_freq==max_freq:
                modes.append(curr_val)
            
            aux(node.right)
    
    aux(root)

    return modes

# ---------------------------------------------------
# 46. Permutations
# backtracking, dfs
# time: O(n^n)?, space: O(n^3)?

def permute(self, nums: List[int]) -> List[List[int]]:

    res = []
    
    def aux(curr, rem):

        if len(rem)==0:
            res.append(curr)
        else:

            for idx in range(len(rem)):

                aux(curr+[rem[idx]], rem[:idx]+rem[idx+1:])

    aux([], nums)

    return res
    
# ---------------------------------------------------
# 797. All Paths From Source to Target
# dfs, graph
# time: O(n^n)?, space: O(n^3)?

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

    n = len(graph)
    res = []

    def aux(curr):
        
        last_node = curr[-1]

        if last_node==n-1:
            res.append(curr)
        elif graph[last_node]!=[]:

            for next_node in graph[last_node]:
                aux(curr+[next_node])
    aux([0])
    
    return res

# ---------------------------------------------------
# 1288. Remove Covered Intervals
# array, sorting
# time: O(nlogn+n), space: O(1)

def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    
    intervals.sort()

    idx = 0

    while idx<len(intervals)-1:

        l = intervals[idx]
        r = intervals[idx+1]

        if l[0] < r[0]:
            if l[1]>=r[1]:
                intervals.pop(idx+1)
            else:
                idx+=1
        elif l[0]==r[0]:
            if l[1]<=r[1]:
                intervals.pop(idx)
            else:
                print('should not be here 2.')
        
        else:
            print('should not be here at all.')
    
    return len(intervals)

# ---------------------------------------------------
# 2265. Count Nodes Equal to Average of Subtree
# backtracking, dfs, graph
# time: O(n), space: O(n), n: node count in tree

def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    
    cnt = 0

    def aux(node):
        nonlocal cnt

        curr_sum = 0
        curr_cnt = 0

        if not node:
            return (0, 0)
        else:

            l_sum, l_cnt = aux(node.left)
            r_sum, r_cnt = aux(node.right)

            curr_sum += (l_sum+r_sum+node.val)
            curr_cnt += (l_cnt+r_cnt+1)

            if int(floor(curr_sum/curr_cnt))==node.val:
                cnt += 1

            return (curr_sum, curr_cnt)
    
    aux(root)
    return cnt

# ---------------------------------------------------
# 34. Find First and Last Position of Element in Sorted Array
# BS
# time: O(logn), space: O(logn)

def searchRange(self, nums: List[int], target: int) -> List[int]:
    
    found = []

    def aux(low, high):

        if low>high:
            return
        
        mid = low + (high-low)//2

        if nums[mid]==target:
            found.append(mid)
            aux(low, mid-1)
            aux(mid+1, high)
        elif nums[mid]>target:
            aux(low, mid-1)
        else:
            aux(mid+1, high)
    
    aux(0, len(nums)-1)

    if len(found)==0:
        return [-1,-1]
    else:
        return [min(found), max(found)]