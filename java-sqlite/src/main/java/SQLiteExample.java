/*
Reference:
[1] http://www.tutorialspoint.com/sqlite/sqlite_java.htm
 */

import java.sql.*;

public class SQLiteExample
{
  public static void main( String args[] )
  {
    try {
      Connection connection = null;
      Statement statement = null;
      // Case 1 : create SQLite File 'test.db'
      connection = DriverManager.getConnection("jdbc:sqlite:test.db");
      System.out.println("Open database successfully!");
      statement = connection.createStatement();
      // Case 2 : create new table 'test'
      statement.execute("CREATE TABLE test ( id INT, name CHAR[50] );");
      System.out.println("Table created successfully!");
      // Case 3 : insert records into table 'test'
      statement.execute("INSERT INTO test (id, name) values (1,'jazz');");
      statement.execute("INSERT INTO test (id, name) values (2,'john');");
      statement.execute("INSERT INTO test (id, name) values (3,'joe');");
      System.out.println("Records created successfully!");
      // Case 4 : query records from table 'test'
      ResultSet resultSet = statement.executeQuery("SELECT * from test where id = 1 ;");
      System.out.println(resultSet.toString());
      // Case N : delete table 'test'
      statement.execute("Drop table test;");
      System.out.println("Table deleted successfully!");
      statement.close();
      connection.close();
    } catch (SQLException e) {
      e.printStackTrace();
    }
  }
}
