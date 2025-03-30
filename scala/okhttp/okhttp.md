
## RESTful Client Framework Survey

- ( 2021-04-16 12:43:17 )
- https://www.javacodegeeks.com/2012/09/simple-rest-client-in-java.html
  - 2012 年左右，Java 要處理 RESTful API 可以用 [Apache HttpClient](https://hc.apache.org/httpclient-legacy/) 或 [Jersey](https://eclipse-ee4j.github.io/jersey/)

- 2018:
  - http://www.mastertheboss.com/other/java-stuff/top-solutions-for-java-http-clients
  - [OkHttp](http://square.github.io/okhttp/)
  - [Unirest](http://unirest.io/java.html)
  - [Apache HttpComponents HttpClient](http://hc.apache.org/)
  - Java 9's new HttpClient API
  - Java built-in HttpURLConnection
- 2020
  - https://www.mocklab.io/blog/which-java-http-client-should-i-use-in-2020/
```
However, all things being equal Square’s OkHttpClient would be our recommendation for teams choosing a new client library. It’s feature-rich, highly configurable and works well in production out of the box.
```
  - https://zh.codeprj.com/blog/bc26d31.html
  - Java’s [HttpURLConnection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/HttpURLConnection.html) and [HttpsURLConnection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/net/ssl/HttpsURLConnection.html)
  - The new [HttpClient](https://docs.oracle.com/en/java/javase/11/docs/api/java.net.http/java/net/http/HttpClient.html), introduced in Java 11
  - [Apache HTTPClient](https://hc.apache.org/httpcomponents-client-5.0.x/index.html)
  - [OkHttp](https://square.github.io/okhttp/)
  - [AsyncHttpClient](https://github.com/AsyncHttpClient/async-http-client)
  - [Jetty HttpClient](https://www.eclipse.org/jetty/documentation/current/http-client.html)

## Ranking

- 初步看起來，okhttp ~= retrofit > async-http-client > jetty-http > unirest-java > google volley

- https://ithelp.ithome.com.tw/articles/10188660
- https://ithelp.ithome.com.tw/articles/10188600

| libarary | libraries.io SourceRank |Git  Repository | Description | Website |
|----------|--------------|--------|-------------|-------------|
| okhttp | [26](https://libraries.io/maven/com.squareup.okhttp3:okhttp) | https://github.com/square/okhttp | https://square.github.io/okhttp/ |
| retrofit | [26](https://libraries.io/maven/com.squareup.retrofit2:retrofit) | https://github.com/square/retrofit | A type-safe HTTP client for Android and the JVM | https://square.github.io/retrofit/ |
| async-http-client | [24](https://libraries.io/maven/org.asynchttpclient:async-http-client) | https://github.com/AsyncHttpClient/async-http-client |
Asynchronous Http and WebSocket Client library for Java | http://github.com/AsyncHttpClient/async-http-client |
| jetty-http | [22](https://libraries.io/maven/org.eclipse.jetty:jetty-http) | https://github.com/eclipse/jetty.project | https://eclipse.org/jetty |
| unirest-java | [14](https://libraries.io/maven/com.konghq:unirest-java) | https://github.com/Kong/unirest-java | Unirest in Java: Simplified, lightweight HTTP client library. | http://kong.github.io/unirest-java/ |
| volley | ? | https://github.com/google/volley | | |