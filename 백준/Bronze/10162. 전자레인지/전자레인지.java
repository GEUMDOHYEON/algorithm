import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        int A = 300;
        int B = 60;
        int C = 10;
        int a = 0;
        int b = 0;
        int c = 0;

        if(T >= A){
            a = T / A;
            T = T % (A * a);
        }
        if(T >= B){
            b = T / B;
            T = T % (B * b);
        }
        if(T >= C){
            c = T / C;
            T = T % (C * c);
        }
        if(T > 0){
            System.out.println(-1);
            return;
        }
        System.out.println(a + " " + b + " " + c);
    }
}
