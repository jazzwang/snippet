# Apache Hive

## 2024-10-22

- ( 2024-10-22 22:16:14 )
- 今天老戰友敲我，說遇到一個奇怪的狀況，重新格式化錯誤訊息如下：
```bash
2024-10-22 11:00:17,497 ERROR org.apache.hadoop.hive.ql.Driver: 
[HiveServer2-Background-Pool: Thread-119]: 
FAILED: Error in acquiring locks: Lock acquisition for LockRequest(
    component: [
        LockComponent(type: SHARED_READ, level: TABLE, dbname: test_db, tablename: test_tbl_log_file, operationType: SELECT ), 
        LockComponent(type: SHARED_READ, level: PARTITION, dbname: test_db, tablename: test_tbl_log_file, partitionname: logdays=2024-02-03, operationType: SELECT)
    ], 
    txnid: 0, 
    user: hive, 
    hostname: edge02. 
    agentInfo: hive_20241022092708_3db7f577-f484-4c9f-83e7-ac8cbf04c87d) timed out after 5588288ms.

    LockResponse (lockid: 58375, state: WAITING) 
    org.apache.hadoop.hive.ql.lockmgr.LockException: 
    Lock acquisition for LockRequest(
        component: [
            LockComponent(type: SHARED_READ, level: TABLE, dbname: test_db, tablename: test_tbl_log_file, operationType: SELECT),
            LockComponent(type: SHARED_READ, level: PARTITION, dbname: test_db, tablename: test_tbl_log_file, partitionname: logdays=2024-02-03, operationType: SELECT)
        ], 
        txnid: 0, 
        user: hive, 
        hostname: edge02, 
        agentInfo: hive_20241022092708_3db7f577-f484-4c9f-83e7-ac8cbf04c87d) timed out after 5588288ms. 
    
    LockResponse (lockid: 58875, state: WAITING) 
    org.apache.hive.service.cli.HiveSQLException: Error while processing statement: 
    FAILED: Error in acquiring locks: Lock acquisition for LockRequest(
        component: [
            LockComponent(type: SHARED_READ, level: TABLE, dbname: test_db, tablename: test_tbl_log_file, operationType: SELECT),
            LockComponent(type: SHARED_READ, level: PARTITION, dbname: test_db, tablename: test_tbl_log_file, partitionname: logdays=2024-02-03, operationType: SELECT)
        ], 
        txnid: 0, 
        user: hive,
        hostname: edge02, 
        agentInfo: hive_20241022092708_3db7f577-f484-4c9f-83e7-ac8cbf04c87d) timed out after 5588288ms. 
    
    LockResponse(lockid: 58375, state: WAITING) 
    Caused by: org.apache.hadoop.hive.ql.lockmgr.LockException: 
    Lock acquisition for LockRequest(
        component: [
            LockComponent(type: SHARED_READ, level: TABLE, d bname: test_db, tablename: test_tbl_log_file, operationType: SELECT),
            LockComponent(type: SHARED_READ, level: PARTITION, dbname: test_db, tablename: test_tbl_log_file, partitionname: logdays=2024-02-03, operationType: SELECT)
        ], 
        txnid: 0, 
        user: hive, 
        hostname: edge02,
        agentInfo: hive_20241022092708_3db7f577-f484-4c9f-88e7-ac8cbf04c87d) timed out after 5588288ms. 
```
- 症狀：SSH 從 Edge Node 進去，透過 beeline 連接 Hive Server 2，連下 `describe test_tbl_log_file` 都沒辦法執行。
- 錯誤排查：
  - 參考：https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=27362050#Locking-Debugging
  - 使用以下語法除錯：
```
SHOW LOCKS <TABLE_NAME>;
SHOW LOCKS <TABLE_NAME> EXTENDED;
SHOW LOCKS <TABLE_NAME> PARTITION (<PARTITION_DESC>);
SHOW LOCKS <TABLE_NAME> PARTITION (<PARTITION_DESC>) EXTENDED;
```
  - 結果：`SHOW LOCKS test_tbl_log_file` 竟然有 1 萬 2 千多筆。這不太尋常。
- 思路：
  - 其他 Hive Table 都可以查詢，但唯獨某個 Partition 內容值有一千多種的 `test_tbl_log_file` 不能查。會不會是因為無法寫入 LOCK 呢？
  - 怎麼手動刪除 LOCK 呢？
- 探索：
  - 根據 Perplexity 的建議，如果要手動刪除 Hive Lock，必須到 metastore 的資料庫，去查 `HIVE_LOCKS` 這個資料表。
  - 我們登入 metastore 資料庫 (MariaDB)，然後使用以下 SQL 語法判讀各資料表的 Lock 個數，發現只有兩個 Hive Table 出現千個，甚至萬個 Lock 的結果。
```sql
SELECT HL_TABLE,count(*) FROM HIVE_LOCKS GROUP BY HL_TABLE;
```
- 解法：
  - 我們把 HIVE_LOCKS 裡面，只要 `HL_TABLE` 是 `test_tbl_log_file` 的紀錄全部刪除後，就可以順利 `describe test_tbl_log_file` 甚至可以跑 `SELECT count(*) FROM test_tbl_log_file WHERE logdays="2024-02-03"` 的 HIVE 查詢。
```sql
DELETE FROM HIVE_LOCKS WHERE HL_TABLE="test_tbl_log_file";
```
- 後記：
  - https://cwiki.apache.org/confluence/display/hive/locking 
    - 這個 wiki 說明了 Hive 是怎麼用 Lock 機制來達到 Concurrent
  - https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Explain#LanguageManualExplain-TheLOCKSClause 
    - 這個 wiki 提到可以用 `EXPLAIN LOCKS 查詢子句` 來顯示該查詢會生成多少個 Lock
  - https://lists.apache.org/thread/9gqqmx41s4r7j5joh4s0337w4npx2fyx
    - 這個討論串，有參考 HIVE_LOCKS 的 Schema
  - https://cwiki.apache.org/confluence/display/Hive/Hive+Transactions#HiveTransactions-LockManager
    - 這個 wiki 提到了 Transaction 與 `LockManager` 的關係。
    - 原本在懷疑這個 Hive 3 的警告。後來證實不是 Hive 版本的原因。
    
    > Hive 3 Warning
    > 
    > Any transactional tables created by a Hive version prior to Hive 3 require Major Compaction to be run on every partition before upgrading to 3.0.  More precisely, any partition which has had any update/delete/merge statements executed on it since the last Major Compaction, has to undergo another Major Compaction.  No more update/delete/merge may happen on this partition until after Hive is upgraded to Hive 3.
