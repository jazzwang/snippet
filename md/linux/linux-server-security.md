# Linux Server Security

- ( 2023-09-08 23:33:39 )
- 記錄一下兩個常用的服務：
  - SSL Server Test - https://www.ssllabs.com/ssltest/index.html
    - 可以用來看 Nginx 或 Apache 設定 SSL 是否足夠安全
  - https://hostedscan.com/risks
    - 會產生 OpenVAS，Nmap 跟 OWASP_ZAP 的弱點掃描報告，還算方便易懂
  - ( 2024-02-27 23:57:49 )
  - https://observatory.mozilla.org/
    - 可以做多種檢查
  
  - ( 2024-08-19 20:17:16 )
  - 反查 IP 與 Geolocation 的服務：
    - https://ipinfo.io/
    - https://ifconfig.co
      - https://ifconfig.me
      - https://ifconfig.io
        - https://github.com/georgyo/ifconfig.io/
    - geofind.me
```bash
~$ curl https://ipinfo.io/
{
  "ip": "36.229.56.183",
  "hostname": "36-229-56-183.dynamic-ip.hinet.net",
  "city": "Banqiao",
  "region": "Taipei",
  "country": "TW",
  "loc": "25.0143,121.4672",
  "org": "AS3462 Data Communication Business Group",
  "timezone": "Asia/Taipei",
  "readme": "https://ipinfo.io/missingauth"
}
```
```bash
~$ curl geofind.me
36.229.56.183
Data Communication Business Group
Xindian District, , New Taipei, Taiwan
```