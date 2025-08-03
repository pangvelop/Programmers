import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        String[] alphabet = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

        for (String s : alphabet) {
            if (word.contains(s)) {
                word = word.replace(s, "a");
            }
        }
        System.out.println(word.length());
    }
}