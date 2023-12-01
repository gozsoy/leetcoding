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
    
    
# ---------------------------------------------------
# 740. Delete and Earn
# DP
# time: O(n), space: O(n)

# sol 1: bottom up (tabulation) + 2 variables
def deleteAndEarn(self, nums: List[int]) -> int:
    
    scores = [0] * (max(nums)+1)

    for num in nums:
        scores[num] += num
    
    prev_prev = scores[0]
    prev = scores[1]

    for idx in range(2, len(scores)):

        temp = prev
        prev = max(prev, scores[idx]+prev_prev)
        prev_prev = temp

    return prev

# sol 2: bottom up (tabulation) + memo
def deleteAndEarn(self, nums: List[int]) -> int:
    
    scores = [0] * (max(nums)+1)

    for num in nums:
        scores[num] += num
    
    memo = [0] * len(scores)
    memo[0] = scores[0]
    memo[1] = scores[1]

    for idx in range(2, len(scores)):

        memo[idx] = max(memo[idx-1], scores[idx]+memo[idx-2])

    return memo[-1]

# sol 3: top down (memoization) + memo
def deleteAndEarn(self, nums: List[int]) -> int:

    scores = [0] * (max(nums)+1)

    for num in nums:
        scores[num] += num
    
    memo = [-1] * len(scores)

    def aux(n):

        if n==0 or n==1:
            memo[n] = scores[n]
            return memo[n]
        else:
            if memo[n]>=0:
                return memo[n]
            else:
                result = max(scores[n]+aux(n-2), aux(n-1))
                memo[n] = result
                return memo[n]
    
    return aux(len(scores)-1)


# ---------------------------------------------------
# 5. Longest Palindromic Substring
# DP
# time: O(n^2), space: O(n^2)

# sol 1: 1d solution. time limit exceeds. bottom-up (tabulation)
def longestPalindrome(self, s: str) -> str:

    def check(s):

        for i in range(0, len(s)//2):

            if s[i]!=s[len(s)-1-i]:
                return False
        
        return True
    
    memo = {} # str: str's longest substr

    def aux(s):
    
        if memo.get(s, None) is None:
        
            if check(s):
                memo[s] = s
                return memo.get(s)
            else:
                res1 = aux(s[1:])
                res2 = aux(s[:-1])

                if len(res1)>=len(res2):
                    memo[s] = res1
                else:
                    memo[s] = res2
                return memo.get(s)
        
        else:
            return memo.get(s)

    return aux(s)


# sol 2: 2d solution. bottom-up (tabulation)
def longestPalindrome(self, s: str) -> str:
    
    n = len(s)
    curr_pal = s[0]

    memo = [[False]*n for _ in range(n)]

    for i in range(n):
        memo[i][i] = True
    
    for i in range(n-1):

        if s[i]==s[i+1]:
            memo[i][i+1]=True
            curr_pal = s[i:i+2]
    
    for sub_len in range(3, n+1):

        for i in range(n-sub_len+1):

            j = i + sub_len - 1

            if memo[i+1][j-1] and s[i]==s[j]:
                memo[i][j]=True
                curr_pal = s[i:j+1]

    return curr_pal


# ---------------------------------------------------
# 1143. Longest Common Subsequence
# DP
# time: O(n^2), space: O(n^2)

# sol1: 2d solution.
def longestCommonSubsequence(self, text1: str, text2: str) -> int:

    l1, l2 = len(text1), len(text2)

    memo = [[0]*(l2+1) for _ in range(l1+1)]

    
    for i in range(1, l1+1):
        for j in range(1, l2+1):

            if text1[i-1]==text2[j-1]:
                memo[i][j] = memo[i-1][j-1]+1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    
    return memo[-1][-1]

# ---------------------------------------------------
# 1143. 2140. Solving Questions With Brainpower
# DP
# time: O(n^2), space: O(n^2)

# sol1: plain recursion. time limit exceeds
def mostPoints(self, questions: List[List[int]]) -> int:

    def aux(curr, idx):
    
        if len(questions)<=idx:
            return curr
        else:
            score, jump = questions[idx]
            
            return max(aux(curr+score,idx+jump+1), aux(curr, idx+1))
            
    return aux(0, 0)

# sol2: ?? TODO


# ---------------------------------------------------
#1980. Find Unique Binary String
# backtracking
# time: O(2^n), space: O(2^n)

# sol 1: 
def findDifferentBinaryString(self, nums: List[str]) -> str:

    from collections import Counter

    c = Counter(nums)
    n = len(nums)

    def aux(curr_str):

        if len(curr_str)==n:
            if not c.get(curr_str):
                return [curr_str]
            else:
                return []
        else:
            return aux(curr_str+'0') + aux(curr_str+'1')

    return aux('')[0]

# sol 2:
def findDifferentBinaryString(self, nums: List[str]) -> str:

    from collections import Counter

    c = Counter(nums)
    n = len(nums)

    def aux(curr_str):

        if len(curr_str)==n:
            if not c.get(curr_str):
                return curr_str
        else:
            
            res1 = aux(curr_str+'0')
            if res1:
                return res1

            return aux(curr_str+'1')

    return aux('')


# ---------------------------------------------------
#981. Time Based Key-Value Store
# binary search, hashmap
# time: O(logn), space: O(n)

class TimeMap:

    def __init__(self):
        
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if self.d.get(key):
            self.d[key]['val'].append(value)
            self.d[key]['t'].append(timestamp)
        else:
            self.d[key] = {'val':[value],'t':[timestamp]}

    def get(self, key: str, timestamp: int) -> str:

        temp_d = self.d.get(key)

        if temp_d:
            val_arr = temp_d['val']
            t_arr = temp_d['t']

            low, high = 0, len(t_arr)-1

            while low<=high:

                mid = low + (high-low)//2

                if t_arr[mid]<= timestamp:
                    low = mid+1
                else:
                    high = mid-1

            if high==-1:
                return ""
            else:
                return val_arr[high]
        else:
            return ""


# ---------------------------------------------------
# 64. Minimum Path Sum
# dynamic programming
# time: O(mn), space: O(mn)

def minPathSum(self, grid: List[List[int]]) -> int:

    m, n = len(grid), len(grid[0])

    memo = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            
            curr_min = float('inf')
            
            if i==0 and j==0:
                curr_min = 0
            else:
                if i-1>=0:
                    curr_min = memo[i-1][j]
                if j-1>=0 and curr_min>memo[i][j-1]:
                    curr_min = memo[i][j-1]
            
            memo[i][j] = curr_min + grid[i][j]

    return memo[-1][-1]

# ---------------------------------------------------
# 2192. All Ancestors of a Node in a Directed Acyclic Graph
# dynamic programming, graph traversal
# time: O(mn), space: O(mn)

def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    
    # child: [ancestors]
    d = {}
    sink_nodes = set(range(0, n))

    for edge in edges:

        source, dest = edge[0], edge[1]
        d[dest] = d.get(dest, []) + [source]
        if source in sink_nodes:
            sink_nodes.remove(source)
    

    answer = [[] for _ in range(n)]
    
    def aux(child):

        ancestor_set = []

        if not d.get(child):
            return []
        if answer[child]!=[]:
            return answer[child]

        for ancestor in d[child]:
            ancestor_set.append(ancestor)
            ancestor_set += aux(ancestor)
        
        answer[child] = sorted(set(ancestor_set))

        return ancestor_set


    for sink_node in sink_nodes:
        aux(sink_node)
    
    return answer

# ---------------------------------------------------
# 325. Maximum Size Subarray Sum Equals k
# prefix sum, hashmap
# time: O(n), space: O(n)

def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    
    psum = 0
    d = {} # psum:idx
    max_len = 0

    for idx in range(len(nums)):

        psum += nums[idx]

        if psum==k:
            max_len = idx+1
        
        if psum-k in d:
            if idx-d.get(psum-k) > max_len:
                max_len = idx-d.get(psum-k)
        
        if psum not in d:
            d[psum]=idx
    
    return max_len