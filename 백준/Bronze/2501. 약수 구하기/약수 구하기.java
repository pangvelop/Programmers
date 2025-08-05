import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();

        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                list.add(i);
            }
        }

        if (list.size() <= k - 1) {
            System.out.println(0);
        } else {
            System.out.println(list.get(k - 1));
        }
    }
}