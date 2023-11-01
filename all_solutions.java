// 133. Clone Graph
// time: O(V+E), space: O(V)
// E: edge cnt, V: node cnt
import java.util.*;

class Solution {
    public Node cloneGraph(Node node) {
        
        HashMap<Integer, Node> d = new HashMap<>();
        ArrayDeque<Node> queue = new ArrayDeque<>();
        if (node==null){
            return null;
        }
        queue.add(node);

        while (!queue.isEmpty()){

            Node temp_node = queue.removeFirst();

            if (temp_node!=null){

                if (d.isEmpty()){
                    d.put(temp_node.val, new Node(temp_node.val));
                }

                for (Node n: temp_node.neighbors){

                    if (!d.containsKey(n.val)){
                        queue.add(n);
                        d.put(n.val, new Node(n.val));
                    }
                    d.get(temp_node.val).neighbors.add(d.get(n.val));
                }
            }
        }
        return d.get(1);
    }
}

// ---------------------------------------------------
// 501. Find Mode in Binary Search Tree
// time: O(V+E), space=O(1) excluding recursion stack

class Solution {

    public int max_freq = 0;
    public ArrayList<Integer> modes = new ArrayList<>();
    public int curr_val;
    public int curr_freq = 0;

    public void aux(TreeNode node){

        if (node!=null){
            aux(node.left);

            if (node.val==curr_val){
                curr_freq += 1;
            }
            else{
                curr_val = node.val;
                curr_freq = 1;
            }

            if (curr_freq>max_freq){
                modes.clear();
                max_freq = curr_freq;
            }
            if (curr_freq==max_freq){
                modes.add(curr_val);
            }

            aux(node.right);

        }

    }
    public int[] findMode(TreeNode root) {

        aux(root);
        return modes.stream().mapToInt(i->i).toArray();
    }
}

// ---------------------------------------------------
// 797. All Paths From Source to Target
// backtracking, dfs, graph
// time: O(n^n)?, space: O(n^3)?

class Solution {

    public void aux(List<Integer> curr, int[][] graph, List<List<Integer>> res){

        int n = graph.length;
        int last_node = curr.get(curr.size()-1);

        if (last_node==n-1){
            res.add(new ArrayList<>(curr));
        }
        else if (graph[last_node].length!=0){

            for (int next_node: graph[last_node]){
                curr.add(next_node);
                aux(curr, graph, res);
                curr.remove(curr.size()-1);
            }
        }
    }

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        
        List<List<Integer>> res = new ArrayList<>();

        List<Integer> curr = new ArrayList();
        curr.add(0);
        aux(curr, graph, res);

        return res;
    }
}