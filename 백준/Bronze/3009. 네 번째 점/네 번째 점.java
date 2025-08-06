import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list_x = new ArrayList<>();
        List<Integer> list_y = new ArrayList<>();
        int x, y;
        for (int i = 0; i < 3; i++) {
            x = sc.nextInt();
            y = sc.nextInt();
            if (list_x.contains(x)) {
                list_x.remove(list_x.indexOf(x));
                x = 0;
            }
            if (list_y.contains(y)) {
                list_y.remove(list_y.indexOf(y));
                y = 0;
            }
            list_x.add(x);
            list_y.add(y);
        }

        while (list_x.remove(Integer.valueOf(0)));
        while (list_y.remove(Integer.valueOf(0)));
        System.out.println(list_x.get(0) + " " + list_y.get(0));
    }
}