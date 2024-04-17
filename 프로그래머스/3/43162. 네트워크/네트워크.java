import java.io.*;
import java.util.*;

class Solution {
    public void DFS(int node, int[] visited, int[][] computers){
        visited[node] = 1;
    
        for(int i = 0; i < computers.length; i++){
            if(visited[i] == 0  && computers[node][i] == 1){
                DFS(i,visited,computers);
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n+1];
        
        for(int i = 0; i < computers.length; i++){
            if(visited[i] == 0){
                answer++;
                DFS(i,visited,computers);
            }   
        }
        
        return answer;
    }
}