
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.*;
import org.apache.spark.api.java.function.*;
import scala.Tuple2;

import java.util.Arrays;

/**
 * Created by jazz on 2017/06/03.
 */
public class JavaWordCount {
    public static void main(String[] args) {
        JavaSparkContext sc = new JavaSparkContext(
                new SparkConf().setAppName("Word Count"));

        Function2<Integer, Integer, Integer> reduceSumFunc = (i1, i2) -> (i1+i2);

        if (args.length < 1) {
            System.out.print("Usage: JavaWordCount <input_file>");
            System.exit(1);
        }

        // read in text file and split each document into words
        JavaRDD<String> tokenized =
                sc.textFile(args[0])
                .flatMap(line -> Arrays.asList(line.split(" ")).iterator());

        JavaPairRDD<String, Integer> counts =
                tokenized.mapToPair(word -> new Tuple2(word, 1))
                .reduceByKey(reduceSumFunc);

        System.out.println(counts.collect());
    }
}
