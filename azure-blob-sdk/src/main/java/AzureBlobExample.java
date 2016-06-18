import com.microsoft.azure.storage.CloudStorageAccount;
import com.microsoft.azure.storage.StorageException;
import com.microsoft.azure.storage.blob.CloudBlobClient;
import com.microsoft.azure.storage.blob.CloudBlobContainer;
import com.microsoft.azure.storage.blob.CloudBlockBlob;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.net.URISyntaxException;
import java.security.InvalidKeyException;

/**
 * Created by jazz on 2016/06/17.
 *
 * Reference:
 * [1] BlobBasics.java @ https://github.com/Azure/azure-storage-java/
 */
public class AzureBlobExample {
    public static void main(String[] args) {
        BufferedReader br = null;
        String connectStr = null;
        try {
            br = new BufferedReader(new FileReader("storagekeys"));
            connectStr = br.readLine();
            CloudStorageAccount account = CloudStorageAccount.parse(connectStr);
            CloudBlobClient client = account.createCloudBlobClient();
            CloudBlobContainer container = client.getContainerReference("test");
            CloudBlockBlob blob1 = container.getBlockBlobReference("sample_file1");
            // Write "Hello World" to Azure Block Blob 'sample_file1'
            blob1.uploadText("Hello World");
            // Read from Azure Block Blob 'sample_file1'
            System.out.println(blob1.downloadText());
        } catch (FileNotFoundException e) {
            System.err.println("Can not find file named by 'storagekey'!!\n" +
                               "Please put Azure Blob Container Connection String in file `storagekeys'.");
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(-1);
        } catch (URISyntaxException e) {
            System.err.println("Unkown Syntax in Connection String : " + connectStr);
            System.exit(-1);
        } catch (InvalidKeyException e) {
            System.err.println("Invalid Key in Connection String : " + connectStr);
            System.exit(-1);
        } catch (StorageException e) {
            e.printStackTrace();
        }
    }
}