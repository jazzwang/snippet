# MEMO

## Reference

- **Source Code**:
  - https://github.com/simple-salesforce/simple-salesforce
- **Document**:
  - https://simple-salesforce.readthedocs.io/en/latest/
- [REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
  - Data Model - [Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm)
  - [Salesforce Object Query Language (SOQL) and Salesforce Object Search Language (SOSL) APIs](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_sosl_intro.htm)
- https://developer.salesforce.com/blogs/2021/09/how-to-automate-data-extraction-from-salesforce-using-python
- https://oktana.com/python-and-salesforce/
- https://medium.com/@noueruzzaman/connect-salesforce-to-python-c1477e9394a9

## 2022-10-06

- 動機：蒐集團隊成員的 Incident / Service Request 清單列表與時間分佈
- 參考：
  - https://developer.salesforce.com/blogs/2021/09/how-to-automate-data-extraction-from-salesforce-using-python
- ( 2022-10-06 09:14:25 )
- 準備環境：安裝 `simple-salesforce`
```
jazzwang:~$ source ~/venv/bin/activate
(venv) jazzwang:~$ pip install simple_salesforce
(venv) jazzwang:~$ ipython3
Python 3.8.9 (default, Oct 26 2021, 07:25:54)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.3.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```
- 測試登入
  - 參考：https://github.com/simple-salesforce/simple-salesforce#examples
  - 由於公司用 SAML SSO，看起來得使用 `instance_url` 的做法。

>      If you have the full URL of your instance
>      (perhaps including the schema,
>      as is included in the `OAuth2` request process),
>      you can pass that in instead using `instance_url`:

- ( 2022-10-06 10:55:34 )
- 參考：https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart_code.htm
- 確認 Salesforce 版本
```
jazzwang:~$ curl -s https://changehealthcare.my.salesforce.com/services/data/ | jq .
```