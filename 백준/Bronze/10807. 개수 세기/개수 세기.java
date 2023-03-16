import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] array = new int[N];
		int cnt = 0;
		
		for(int i = 0; i < N; i++) {
			array[i] = sc.nextInt();
		}
		
		int search = sc.nextInt();
		
		for(int j = 0; j < N; j++) {
			if (array[j] == search)
				cnt++;
		}
		
		System.out.println(cnt);
	}
}