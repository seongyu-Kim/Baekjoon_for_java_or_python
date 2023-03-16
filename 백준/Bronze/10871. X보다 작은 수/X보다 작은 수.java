import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int X = sc.nextInt();
		
		int[] array = new int[N];
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < N; i++) {
			array[i] = sc.nextInt();
			
			if(array[i] < X) {
				sb.append(array[i]+ " ");
			}
		}
		System.out.println(sb);
	}
}