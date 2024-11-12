import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int t = scanner.nextInt();  

        while (t-- > 0) {
            long n = scanner.nextLong();  
            
            long l = 1;  
            long r = 2018; 
            long ans = -1;  

            while (l <= r) {
                long mid = (l + r) / 2;  
                long tt = (long) Math.sqrt(mid);  

                while (tt * tt > mid) tt--;  
                while ((tt + 1) * (tt + 1) <= mid) tt++;  

                long cnt = tt;  

                if (cnt == n) {  
                    ans = mid;  
                    r = mid - 1;  
                } else {
                    l = mid + 1;  
                }
            }

            System.out.println(ans);  
        }

        scanner.close();  
    }
}
