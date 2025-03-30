# Kafka Producer Sample

This is a simple Kafka producer sample using the `kafkajs` library.

## Requirements

- Node.js (version 12 or higher)
- Kafka broker running on `localhost:9092`

## Installation

1. Clone the repository or download the files.
2. Navigate to the `js/kafkajs` directory.
3. Install the required dependencies:

   ```bash
   npm install kafkajs
   ```

## Running the Producer

To run the Kafka producer sample, execute the following command in your terminal:

```bash
node KafkaProducerSample.js
```

This will send 50,000 messages to the `test` topic in your Kafka broker, with each message having a key and value corresponding to its index.

## Notes

- Ensure that your Kafka broker is up and running before executing the producer.
- You can modify the number of messages sent by changing the loop in `KafkaProducerSample.js`.
