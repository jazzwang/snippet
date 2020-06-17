import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.util.HashMap;

/**
 * Created by jazz on 2016/06/11.
 */
public class HashmapExample {
    public static void main(String[] args)
    {
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader("/tmp/product_category.csv"));
            String line = null;
            HashMap<String,String> map = new HashMap<String, String>();

            while((line = br.readLine()) != null) {
                String str[] = line.split(",");
                map.put(str[0],str[1]);
            }

            Connection connection = null;
            Statement statement = null;
            ResultSet resultSet = null;
            // Case 1 : create SQLite File 'test.db'
            connection = DriverManager.getConnection("jdbc:sqlite:test.db");
            System.out.println("Open database successfully!");
            statement = connection.createStatement();
            // Case 2 : create new table 'test'
            statement.execute("CREATE TABLE test ( product_id TEXT, category_id TEXT );");
            System.out.println("Table created successfully!");
            // Case 3 : insert records into table 'test'
            for (String key : map.keySet())
            {
                statement.execute("INSERT INTO test (product_id, category_id) values ("
                        + key + ",'" + map.get(key) + "');");
            }
            System.out.println("Records created successfully!");
            // Case 4 : query records from table 'test'
            resultSet = statement.executeQuery("SELECT * from test;");
            while ( resultSet.next() )
            {
                System.out.println(resultSet.getString("product_id") + ","
                        + resultSet.getString("category_id"));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
