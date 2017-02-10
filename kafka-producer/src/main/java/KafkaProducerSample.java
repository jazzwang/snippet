import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

/**
 * Created by jazz on 2017/02/09.
 *
 * Reference:
 * [1] https://github.com/apache/kafka/blob/trunk/examples/src/main/java/kafka/examples/Producer.java
 * [2] https://kafka.apache.org/0100/javadoc/index.html?org/apache/kafka/clients/producer/KafkaProducer.html
 * https://github.com/bigdatabiginsight/kafka/blob/master/kafka-producer2/src/main/java/com/learningstorm/kafka/WordsProducer.java
 */
public class KafkaProducerSample {
    public static void main(String[] args)
    {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        KafkaProducer<String,String> producer = new KafkaProducer<>(props);
        for (int i = 1; i <= 50_000; i++) {
            producer.send(new ProducerRecord<String, String>("test", Integer.toString(i), Integer.toString(i)));
            System.out.println("Sending to topic 'test' with key '" + i + "' and payload '" + i + "'");
        }
        producer.flush();
        producer.close();
    }
}