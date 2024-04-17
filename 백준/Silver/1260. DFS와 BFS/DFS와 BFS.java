import java.util.*;

public class Main {
    static int N,M,V;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] visited;

    public static void BFS(int V){
        Queue q = new LinkedList();
        q.add(V);
        visited[V] = 1;

        while(!q.isEmpty()){
            int tmp = (int) q.poll();
            System.out.print(tmp + " ");
            for(int next: graph.get(tmp)){
                if(visited[next] == 0){
                    q.add(next);
                    visited[next] = 1;
                }
            }
        }
    }

    public static void DFS(int V){
        visited[V] = 1;
        System.out.print(V + " ");
        for (int v : graph.get(V)){
            if(visited[v] == 0){
                DFS(v);
            }
        }
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt(); // 노드의 수
        M = scanner.nextInt(); // 간선의 수
        V = scanner.nextInt(); // 시작 노드
        
        graph = new ArrayList<ArrayList<Integer>>();
        for(int i = 0; i < N+1; i++){
            graph.add(new ArrayList<Integer>());
        }

        visited = new int[N+1];

        for(int i = 0; i < M; i++){
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        for(int i = 1; i <= N; i++){
            Collections.sort(graph.get(i));
        }
        DFS(V);
        visited = new int[N+1];
        System.out.println();
        BFS(V);
    }
}
