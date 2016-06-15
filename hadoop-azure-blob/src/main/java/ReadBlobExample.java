import org.apache.hadoop.fs.FileSystem;

import java.io.FileNotFoundException;
import java.io.FileReader;

/**
 * Created by jazz on 2016/06/20.
 */
public class ReadBlobExample {
    public void main(String[] args) {
        String CONFIG_FILE = "storagekeys";
        try (FileReader fr = new FileReader(CONFIG_FILE)) {

        } catch (FileNotFoundException) {

        }
        FileSystem fs;
    }
}
