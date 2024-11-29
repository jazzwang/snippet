const { Kafka } = require('kafkajs');

const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
});

const producer = kafka.producer();

const run = async () => {
    await producer.connect();
    for (let i = 1; i <= 50000; i++) {
        await producer.send({
            topic: 'test',
            messages: [
                { key: i.toString(), value: i.toString() },
            ],
        });
        console.log(`Sending to topic 'test' with key '${i}' and payload '${i}'`);
    }
    await producer.disconnect();
};

run().catch(console.error);
