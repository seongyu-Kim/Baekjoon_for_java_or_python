import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int price;
		
		
		if (a == b && b == c) {
			price = 10000 + (a * 1000);
		} else if ( a == b && b != c ) {
			price = 1000 + ( a * 100 );
		} else if ( a == c && c != b ) {
			price = 1000 + ( a * 100 );
		}else if ( b == c && c != a) {
			price = 1000 + ( b * 100 );
		} else {
			int max1 = Math.max(a, b);
			int max2 = Math.max(b, c);
			price = Math.max(max1, max2) * 100;
		}
		
		System.out.println(price);
	}
}