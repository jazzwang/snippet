# Databricks - Batch Inference vs Streaming Inference

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
databricks batch inference streaming inference
</td></tr><tr><td>A:</td><td>

In Databricks, batch inference and streaming inference represent two different strategies for executing machine learning or large language model (LLM) predictions depending on your data latency and throughput needs. [1, 2, 3] 
Databricks unifies both paradigms, allowing you to use identical code logic (such as SQL AI functions) for both batch and streaming pipelines. [4, 5, 6, 7, 8] 

### Comparison Overview

| Feature [1, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] | Batch Inference | Streaming Inference |
|---|---|---|
| Data Source | Static Delta Tables or files | Continuous stream (e.g., Kafka[](https://www.databricks.com/blog/what-is-data-streaming), Auto Loader[](https://docs.databricks.com/aws/en/query/streaming)) |
| Core Metric | High throughput / Low cost | Low latency / Freshness |
| Execution | On-demand or scheduled jobs | Continuous or micro-batches |
| Primary Tooling | ai_query, Apache Spark, Ray Data | Structured Streaming[](https://docs.databricks.com/aws/en/structured-streaming/tutorial), Delta Live Tables |

### 1. Batch Inference (Offline / Bulk Processing)
Batch inference processes large datasets collected over time all at once. It maximizes hardware utilization to lower costs and is ideal when you do not need immediate real-time answers. [1, 3, 13] 

#### Common Use Cases

* Nightly sentiment analysis on thousands of customer reviews.
* Weekly catalog text embeddings generation.
* Bulk content generation or structured data extraction. [9, 14, 19] 

#### Recommended Implementations

* Mosaic AI & ai_query (Best for LLMs): Databricks allows you to execute batch LLM inference directly inside your [Delta Lake](https://docs.databricks.com/aws/en/machine-learning/train-model/dl-best-practices) using SQL. The underlying serverless engine automatically handles scaling and retries. [9, 18, 20, 21] 
* Spark UDFs with MLflow: For traditional ML models (e.g., scikit-learn, XGBoost), you load the model from the [MLflow Model Registry](https://community.databricks.com/t5/machine-learning/how-to-speed-up-inference/td-p/135900) and wrap it inside a Spark User Defined Function (UDF) to scale horizontally. [2, 10, 22] 
* Ray Data + vLLM: Used for hyper-scale open-source LLM inference workloads using raw cluster GPUs. [16, 23] 

#### Code Example (SQL Batch Inference)

```sql
SELECT 
  review_id, 
  ai_query('databricks-llama-3-70b-instruct', CONCAT('Analyze sentiment: ', review_text)) AS sentimentFROM 
  hive_metastore.default.customer_reviews;
``

### 2. Streaming Inference (Near Real-Time Processing)

Streaming inference processes data incrementally as it arrives. It treats data as an unbounded table, computing predictions continuously or on small micro-batches. [4, 11] 

#### Common Use Cases

* Real-time fraud detection on financial transactions.
* Live sensor/IoT data anomaly detection.
* Immediate chatbot orchestration or routing pipelines. [24, 25] 

#### Recommended Implementations

* Structured Streaming with ai_query: You can seamlessly plug the same AI query functions into a live Spark streaming pipeline.
* Delta Live Tables (DLT): Declarative framework that simplifies building and monitoring streaming inference pipelines.
* Auto Loader: Efficiently pulls incoming files from cloud storage (S3/ADLS) into your streaming engine. [5, 12, 15, 18, 26] 

#### Code Example (Python Streaming Inference)

```python
# Read streaming data from a Delta table sourcestreaming_df = spark.readStream.table("catalog.schema.live_events")
# Apply inference logic incrementallypredictions_df = streaming_df.selectExpr(
    "event_id",
    "ai_query('custom-fraud-model-endpoint', event_payload) AS is_fraud"
)
# Write results continuously to a sink tablequery = (predictions_df.writeStream
         .format("delta")
         .outputMode("append")
         .option("checkpointLocation", "/mnt/telemetry/checkpoints/")
         .start("catalog.schema.predictions"))
```

### Key Decision Factors

   1. How fast do you need predictions? If minutes or hours are acceptable, use Batch. If you need answers within seconds of data generation, use Streaming. [11, 13, 27, 28, 29] 
   2. What is your cost budget? Batch allows Databricks to scale down infrastructure to zero when done. Streaming requires continuously running or frequently triggered resources, which increases compute costs. [1, 9, 13, 30, 31] 
   3. What is the data arrival pattern? Scattered files dropping into cloud bucket storage benefit from Streaming via Auto Loader, while a database partition refreshed once a day requires Batch. [12, 32] 

If you are setting up a pipeline, please let me know:

* What type of model you are serving (e.g., an LLM like Llama, or a traditional ML model like XGBoost)?
* Where your raw data is currently stored?
* Your target latency requirement (e.g., sub-second, real-time, or batch/overnight)?

I can provide the specific syntax and cluster optimization settings for your case.

[1] [https://www.youtube.com](https://www.youtube.com/watch?v=JluYAgxoE0k&t=7)
[2] [https://docs.databricks.com](https://docs.databricks.com/aws/en/machine-learning/concepts/ml-capabilities)
[3] [https://cloud.google.com](https://cloud.google.com/discover/what-is-batch-inference)
[4] [https://www.databricks.com](https://www.databricks.com/blog/2021/09/01/infrastructure-design-for-real-time-machine-learning-inference.html)
[5] [https://databrickster.medium.com](https://databrickster.medium.com/responseformat-in-ai-batch-inference-23671c578c8f)
[6] [https://www.dataexpert.io](https://www.dataexpert.io/blog/structured-streaming-live-video-databricks)
[7] [https://shahrukh0603.medium.com](https://shahrukh0603.medium.com/day-27-of-databrickster-45636ac15ba4)
[8] [https://www.databricks.com](https://www.databricks.com/blog/what-is-data-streaming)
[9] [https://www.youtube.com](https://www.youtube.com/watch?v=YbkFXuofkrE&t=3)
[10] [https://community.databricks.com](https://community.databricks.com/t5/machine-learning/how-to-speed-up-inference/td-p/135900)
[11] [https://www.databricks.com](https://www.databricks.com/blog/what-is-data-streaming)
[12] [https://docs.databricks.com](https://docs.databricks.com/aws/en/query/streaming)
[13] [https://medium.com](https://medium.com/codetodeploy/deploying-gen-ai-on-databricks-using-batch-inference-20b89dbace6c)
[14] [https://www.youtube.com](https://www.youtube.com/watch?v=hDoQHuPKjHY&t=5)
[15] [https://docs.databricks.com](https://docs.databricks.com/gcp/en/large-language-models/batch-inference-pipelines)
[16] [https://docs.databricks.com](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/ray-batch-inference)
[17] [https://docs.databricks.com](https://docs.databricks.com/aws/en/large-language-models/ai-query)
[18] [https://www.databricks.com](https://www.databricks.com/blog/introducing-simple-fast-and-scalable-batch-llm-inference-mosaic-ai-model-serving)
[19] [https://community.databricks.com](https://community.databricks.com/t5/databricks-tv/intelligence-engineering-through-batch-inference/ba-p/124362)
[20] [https://www.databricks.com](https://www.databricks.com/blog/introducing-serverless-batch-inference)
[21] [https://docs.databricks.com](https://docs.databricks.com/aws/en/large-language-models/ai-functions)
[22] [https://community.databricks.com](https://community.databricks.com/t5/data-engineering/how-to-optimize-batch-inference-for-per-item-ml-models-in/td-p/122647)
[23] [https://medium.com](https://medium.com/@changiti/llm-batch-inference-0ad05c98c53c)
[24] [https://www.databricks.com](https://www.databricks.com/product/aws)
[25] [https://pipeline2insights.substack.com](https://pipeline2insights.substack.com/p/how-to-decide-between-batch-and-stream-processing)
[26] [https://medium.com](https://medium.com/@divyanshgoyal8989/streamlining-real-time-data-a-guide-to-delta-live-tables-in-databrickss-688ff6e35247)
[27] [https://reenbit.com](https://reenbit.com/batch-vs-stream-processing-understanding-the-trade-offs/)
[28] [https://www.linkedin.com](https://www.linkedin.com/pulse/streaming-real-time-feed-event-distribution-whats-vincent-rainardi-sxgse)
[29] [https://huggingface.co](https://huggingface.co/docs/text-generation-inference/conceptual/streaming)
[30] [https://docs.databricks.com](https://docs.databricks.com/aws/en/structured-streaming/tutorial)
[31] [https://medium.com](https://medium.com/@blakelassiter/streaming-vs-batch-what-i-learned-the-hard-way-8a8d4921a896)
[32] [https://docs.databricks.com](https://docs.databricks.com/aws/en/data-engineering/batch-vs-streaming)

</td></tr>
</table>
