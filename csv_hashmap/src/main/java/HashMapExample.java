import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

/**
 * Created by jazz on 2016/06/08.
 * 
 * Ref: http://stackoverflow.com/questions/20068383/convert-csv-values-to-a-hashmap-key-value-pairs-in-java
 */
public class HashMapExample {
  public static void main (String[] args)
  {
    try {
      BufferedReader br = new BufferedReader(new FileReader("/tmp/product_category.csv"));
      String line = null;
      HashMap<String,String> map = new HashMap<String, String>();

      while((line = br.readLine()) != null) {
        String str[] = line.split(",");
        map.put(str[0],str[1]);
      }

      System.out.println(map.toString());
      System.out.println("Size of HashMap = " + map.size());
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
