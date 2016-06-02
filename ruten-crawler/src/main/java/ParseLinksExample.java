import java.io.IOException;
import java.util.Map;

import org.jsoup.Connection;
import org.jsoup.Connection.Response;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class ParseLinksExample {
  public static void main(String[] args) {
    Document doc;
    try {
      Map<String, String> cookies = null;
      String url = "http://goods.ruten.com.tw/item/show?" + args[0];
      System.out.println(url);
      Response res = Jsoup.connect(url).userAgent("Mozilla").followRedirects(false).execute();
      //System.out.println("url:"+res.url());
      //System.out.println("header:"+res.header("location"));
      //System.out.println("cookie:"+cookies);
      res = Jsoup.connect(res.header("location")).userAgent("Mozilla").followRedirects(false).execute();
      cookies = res.cookies();
      //System.out.println("url:"+res.url());
      //System.out.println("header:"+res.header("location"));
      //System.out.println("cookie:"+cookies);
      doc = Jsoup.connect(url).cookies(cookies).timeout(300).get();
      // get title of the page
      String title = doc.title();
      System.out.println("Title: " + title);
      // System.out.println(doc.body());
      // get all links
      Elements links = doc.select(".rt-breadcrumb-link");
      for (Element link : links) {
        // get the value from href attribute
        if(link.text() != "")
          System.out.println(link.attr("href")+","+link.text());
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
