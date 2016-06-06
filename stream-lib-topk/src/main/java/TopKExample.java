import com.clearspring.analytics.stream.Counter;
import com.clearspring.analytics.stream.StreamSummary;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

/**
 * Created by jazz on 2016/06/06.
 *
 * Reference: https://github.com/addthis/stream-lib/blob/master/src/main/java/com/clearspring/analytics/util/TopK.java
 */
public class TopKExample {
    public static void main(String[] args) {
        int capacity = 1000;
        StreamSummary<String> topk = new StreamSummary<String>(capacity);
        BufferedReader input = new BufferedReader(new InputStreamReader(
                TopKExample.class.getClassLoader().getResourceAsStream("local_data.log")));
        String line = null;

        // Step 1: Feed input data into `StreamSummary` object
        try {
            while ((line = input.readLine()) != null) {
                topk.offer(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Step 2: count Top-K
        List<Counter<String>> counters = topk.topK(topk.getCapacity());

        // Step 3: print Top-K
        for (Counter<String> counter : counters) {
            System.out.println(counter.getItem()+"\t"+counter.getCount()+"\t"+counter.getError());
        }
    }
}
