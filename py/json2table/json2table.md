# json2table

- 套件：https://github.com/latture/json2table
- 測試：想拿 CMS [Price Transparency Guide](https://github.com/CMSgov/price-transparency-guide.git) 的 example JSON 來做實驗。

## 第一版:

- 一個小 CLI 程式，目標語法：
```bash
~$ python3 json-to-table.py input.json output.html
```
- 實作：[json-to-table.py](json-to-table.py)
- 實驗：
    - 理解資料格式 - 從 https://github.com/latture/json2table/blob/master/tests/test_json2table.py 的 test case 來看，輸入會是 dict 型別。
```
In [3]: simple_json = {"key" : "value"}

In [4]: type(simple_json)
Out[4]: dict
```