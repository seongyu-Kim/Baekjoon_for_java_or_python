import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int h = sc.nextInt();
		int m = sc.nextInt();
		int time = sc.nextInt();
		
		if ( (m+time) >= 60) {
			h = h + ((m+time)/60);
			m = (m+time)-((m+time)/60)*60;
			
			if ( h >= 24 ) {
				h = h-24;
			}
		}else {
			m = time+m;
		}
		System.out.printf("%d %d", h, m);
	}
}