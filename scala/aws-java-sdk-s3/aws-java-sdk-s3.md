# Development Notes

## 2020-12-14

- ( 2020-12-14 10:51:45 )
- https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-objects.html#upload-object
- https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/java/example_code/s3/src/main/java/aws/example/s3/PutObject.java
- https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-s3/1.11.918
```sbt
// https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-s3
libraryDependencies += "com.amazonaws" % "aws-java-sdk-s3" % "1.11.918"
```
```bash
~/git/snippet/scala/aws-java-sdk-s3$ git gi sbt,scala > .gitignore
~/git/snippet/scala/aws-java-sdk-s3$ sbt --sbt-create
sbt:aws-java-sdk-s3> set libraryDependencies += "com.amazonaws" % "aws-java-sdk-s3" % "1.11.918"
sbt:aws-java-sdk-s3> update
sbt:aws-java-sdk-s3> session save
sbt:aws-java-sdk-s3> exit
```