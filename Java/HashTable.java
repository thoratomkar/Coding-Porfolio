import java.util.HashMap;
import java.util.Map;
import java.nio.ByteBuffer;


public class HashTable {
    public static void main(String[] args) {
        String str = "aabcdaccbdaf";
        int length = str.length();
        HashMap<Character, Integer> h = new HashMap<>();
        for (int i = 0; i <= length - 1; i++)
        {
            char c = str.charAt(i);
            if (h.containsKey(c)) {
                int m = h.get(c);
                m++;
                h.put(c, m);
            } else
                h.put(c, 1);
        }




    }
}