package example

// Reference:
// https://github.com/awslabs/aws-cloudwatch-metrics-custom-spark-listener/blob/master/src/main/scala/com/amazonaws/awslabs/sparkstreaming/listener/CloudWatchSparkListener.scala
// https://aws.amazon.com/blogs/big-data/monitor-spark-streaming-applications-on-amazon-emr/

import org.apache.spark.streaming.scheduler._
import collection.mutable.{ Map , HashMap }

class ConsoleSparkListener(appName: String = "ApplicationName") extends StreamingListener {

    val dimentionsMap = new HashMap[String,String]()

    override def onBatchCompleted(batchCompleted: StreamingListenerBatchCompleted): Unit = {
        println("CloudWatch Streaming Listener, onBatchCompleted:" + appName)
        val processingTime = if (batchCompleted.batchInfo.processingDelay.isDefined) {
            batchCompleted.batchInfo.processingDelay.get 
        }
        val schedulingDelay = if (batchCompleted.batchInfo.schedulingDelay.isDefined && batchCompleted.batchInfo.schedulingDelay.get > 0 ) {
            batchCompleted.batchInfo.schedulingDelay.get 
        } else { 0 }
        val numRecords = batchCompleted.batchInfo.numRecords
        println("Batch completed at: " + batchCompleted.batchInfo.processingEndTime.get)
        println(" was started at: " + batchCompleted.batchInfo.processingStartTime.get)
        println(" submission time: " + batchCompleted.batchInfo.submissionTime)
        println(" batch time: " + batchCompleted.batchInfo.batchTime)
        println(" batch processing delay: " + batchCompleted.batchInfo.processingDelay.get)
        println(" records : " + numRecords)
        println(" total batch delay:" + batchCompleted.batchInfo.totalDelay.get)
        println(" product prefix:" + batchCompleted.batchInfo.productPrefix)
        println(" schedulingDelay:" + schedulingDelay)
        println(" processingTime:" + processingTime)
    }
}