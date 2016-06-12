import java.io.IOException;
import java.util.Map;
import java.net.SocketTimeoutException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.jsoup.Connection;
import org.jsoup.Connection.Response;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class ParseLinksExample {
  public static void main(String[] args) {
    Document doc = null;
    int count = 0;
    boolean success = false;
    Map<String, String> cookies = null;
    String pattern = ".*\\?c=(.*)";
    String url = "http://goods.ruten.com.tw/item/show?" + args[0];
    System.err.println(url);

    while ( ! success && count < 5 ) {
      try {
        Response res = Jsoup.connect(url).userAgent("Mozilla").followRedirects(false).execute();
        //System.out.println("url:"+res.url());
        //System.out.println("header:"+res.header("location"));
        //System.out.println("cookie:"+cookies);
        res = Jsoup.connect(res.header("location")).userAgent("Mozilla").followRedirects(false).execute();
        cookies = res.cookies();
        //System.out.println("url:"+res.url());
        //System.out.println("header:"+res.header("location"));
        //System.out.println("cookie:"+cookies);
        doc = Jsoup.connect(url).cookies(cookies).get();
        success = true;
      } catch (SocketTimeoutException ex) {
        count ++;
        System.err.println("Read Timed out! Retry the " + count + " times.");
      } catch (IOException e) {
          e.printStackTrace();
      }
    }
    String href = null;
    // get all links
    Elements links = doc.select(".rt-breadcrumb-link");
    String category_id = "9999";
    for (Element link : links) {
      // get the value from href attribute
      href = link.attr("href");
      if (href.contains("category.php?c=")) {
        Matcher m = Pattern.compile(pattern).matcher(href);
        if (m.find()) {
          System.err.println("category_id = " + m.group(1) + " , category = '" + link.text() + "'");
          category_id = m.group(1);
        } else {
          System.err.println(href);
        }
      }
    }
    System.out.println(args[0] + "," + category_id);
  }
}
