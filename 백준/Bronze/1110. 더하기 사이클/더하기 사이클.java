import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int count = 0;
		int N = sc.nextInt();
		int T = N;
		
		while(true) {
			N = ((N%10)*10) + (((N/10)+(N%10))%10);
			count++;
			
			if (N == T)
				break;
		}
		System.out.println(count);
	}
}