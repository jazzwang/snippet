## ChangeLog

* 2016-06-06: add retry to handle exception 'Read timed out'
    * Reference: http://stackoverflow.com/questions/10506577/jsoup-connections-and-retries
```
java.net.SocketTimeoutException: Read timed out
	at java.net.SocketInputStream.socketRead0(Native Method)
	at java.net.SocketInputStream.socketRead(SocketInputStream.java:116)
	at java.net.SocketInputStream.read(SocketInputStream.java:170)
	at java.net.SocketInputStream.read(SocketInputStream.java:141)
	at java.io.BufferedInputStream.fill(BufferedInputStream.java:246)
	at java.io.BufferedInputStream.read1(BufferedInputStream.java:286)
	at java.io.BufferedInputStream.read(BufferedInputStream.java:345)
	at sun.net.www.http.HttpClient.parseHTTPHeader(HttpClient.java:704)
	at sun.net.www.http.HttpClient.parseHTTP(HttpClient.java:647)
	at sun.net.www.protocol.http.HttpURLConnection.getInputStream0(HttpURLConnection.java:1536)
	at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1441)
	at java.net.HttpURLConnection.getResponseCode(HttpURLConnection.java:480)
	at org.jsoup.helper.HttpConnection$Response.execute(HttpConnection.java:567)
	at org.jsoup.helper.HttpConnection$Response.execute(HttpConnection.java:540)
	at org.jsoup.helper.HttpConnection.execute(HttpConnection.java:227)
	at org.jsoup.helper.HttpConnection.get(HttpConnection.java:216)
	at ParseLinksExample.main(ParseLinksExample.java:27)
```
