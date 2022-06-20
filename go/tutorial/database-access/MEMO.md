# Tutorial: Accessing a relational database

[TOC]

## 2022-06-20

- ( 2022-06-20 21:35:40 )
```bash
~/git/snippet/go/tutorial/database-access$ go mod init example/data-access
go: creating new go.mod: module example/data-access
```
- ( 2022-06-20 21:38:01 )
- In the tutorial, it uses the MySQL database. I will use SQLite instead.
```bash
~/git/snippet/go/tutorial/database-access$ sqlite3 test.db
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
sqlite>
```
- ( 2022-06-20 21:40:51 )
- create database `recordings`
- https://www.tutorialspoint.com/sqlite/sqlite_attach_database.htm
```bash
sqlite> ATTACH DATABASE 'test.db' as 'recordings';
sqlite> .databases
main: /Users/jazzwang/git/snippet/go/tutorial/database-access/test.db
recordings: /Users/jazzwang/git/snippet/go/tutorial/database-access/test.db
```
- ( 2022-06-20 21:46:22 )
- create table `album`
```sql
sqlite> DROP TABLE IF EXISTS album;
sqlite> CREATE TABLE album (
   ...>   id         INT AUTO_INCREMENT NOT NULL,
   ...>   title      VARCHAR(128) NOT NULL,
   ...>   artist     VARCHAR(255) NOT NULL,
   ...>   price      DECIMAL(5,2) NOT NULL,
   ...>   PRIMARY KEY (`id`)
   ...> );
sqlite>
sqlite> INSERT INTO album
   ...>   (title, artist, price)
   ...> VALUES
   ...>   ('Blue Train', 'John Coltrane', 56.99),
   ...>   ('Giant Steps', 'John Coltrane', 63.99),
   ...>   ('Jeru', 'Gerry Mulligan', 17.99),
   ...>   ('Sarah Vaughan', 'Sarah Vaughan', 34.98);
Error: NOT NULL constraint failed: album.id
sqlite> .schema
CREATE TABLE album (
  id         INT AUTO_INCREMENT NOT NULL,
  title      VARCHAR(128) NOT NULL,
  artist     VARCHAR(255) NOT NULL,
  price      DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE recordings.album (
  id         INT AUTO_INCREMENT NOT NULL,
  title      VARCHAR(128) NOT NULL,
  artist     VARCHAR(255) NOT NULL,
  price      DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`id`)
);
```
- ( 2022-06-20 21:50:32 )
- https://www.sqlite.org/autoinc.html
- drop table `album` and create again using SQLite Auto-increment.
```sql
sqlite> detach database 'recordings';
sqlite> .database
main: /Users/jazzwang/git/snippet/go/tutorial/database-access/test.db
sqlite> drop table album;
sqlite> create table album (
   ...>   id       INTEGER PRIMARY KEY NOT NULL,
   ...>   title    CHAR(128) NOT NULL,
   ...>   artist   CHAR(255) NOT NULL,
   ...>   price    DECIMAL(5,2) NOT NULL
   ...> );
```
- ( 2022-06-20 22:05:45 )
- I'll use https://github.com/mattn/go-sqlite3
```
SQLite (uses cgo): https://github.com/mattn/go-sqlite3 [*]
```
- ( 2022-06-20 22:07:16 )
- sample code from https://github.com/mattn/go-sqlite3
- https://github.com/mattn/go-sqlite3/blob/master/_example/simple/simple.go

- ( 2022-06-20 22:17:17 )
```bash
~/git/snippet/go/tutorial/database-access$ code access-mysql.go
```
```go
package main

import (
    "database/sql"
    "fmt"
    "log"
    "os"

    "github.com/go-sql-driver/mysql"
)

var db *sql.DB

type Album struct {
    ID     int64
    Title  string
    Artist string
    Price  float32
}

func main() {
    // Capture connection properties.
    cfg := mysql.Config{
        User:   os.Getenv("DBUSER"),
        Passwd: os.Getenv("DBPASS"),
        Net:    "tcp",
        Addr:   "127.0.0.1:3306",
        DBName: "recordings",
    }
    // Get a database handle.
    var err error
    db, err = sql.Open("mysql", cfg.FormatDSN())
    if err != nil {
        log.Fatal(err)
    }

    pingErr := db.Ping()
    if pingErr != nil {
        log.Fatal(pingErr)
    }
    fmt.Println("Connected!")

    albums, err := albumsByArtist("John Coltrane")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Albums found: %v\n", albums)

    // Hard-code ID 2 here to test the query.
    alb, err := albumByID(2)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Album found: %v\n", alb)

    albID, err := addAlbum(Album{
        Title:  "The Modern Sound of Betty Carter",
        Artist: "Betty Carter",
        Price:  49.99,
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("ID of added album: %v\n", albID)
}

// albumsByArtist queries for albums that have the specified artist name.
func albumsByArtist(name string) ([]Album, error) {
    // An albums slice to hold data from returned rows.
    var albums []Album

    rows, err := db.Query("SELECT * FROM album WHERE artist = ?", name)
    if err != nil {
        return nil, fmt.Errorf("albumsByArtist %q: %v", name, err)
    }
    defer rows.Close()
    // Loop through rows, using Scan to assign column data to struct fields.
    for rows.Next() {
        var alb Album
        if err := rows.Scan(&alb.ID, &alb.Title, &alb.Artist, &alb.Price); err != nil {
            return nil, fmt.Errorf("albumsByArtist %q: %v", name, err)
        }
        albums = append(albums, alb)
    }
    if err := rows.Err(); err != nil {
        return nil, fmt.Errorf("albumsByArtist %q: %v", name, err)
    }
    return albums, nil
}

// albumByID queries for the album with the specified ID.
func albumByID(id int64) (Album, error) {
    // An album to hold data from the returned row.
    var alb Album

    row := db.QueryRow("SELECT * FROM album WHERE id = ?", id)
    if err := row.Scan(&alb.ID, &alb.Title, &alb.Artist, &alb.Price); err != nil {
        if err == sql.ErrNoRows {
            return alb, fmt.Errorf("albumsById %d: no such album", id)
        }
        return alb, fmt.Errorf("albumsById %d: %v", id, err)
    }
    return alb, nil
}

// addAlbum adds the specified album to the database,
// returning the album ID of the new entry
func addAlbum(alb Album) (int64, error) {
    result, err := db.Exec("INSERT INTO album (title, artist, price) VALUES (?, ?, ?)", alb.Title, alb.Artist, alb.Price)
    if err != nil {
        return 0, fmt.Errorf("addAlbum: %v", err)
    }
    id, err := result.LastInsertId()
    if err != nil {
        return 0, fmt.Errorf("addAlbum: %v", err)
    }
    return id, nil
}
```
- ( 2022-06-20 22:21:52 )
- test on GCP Cloud Shell with MySQL docker running
- https://shell.cloud.google.com/?show=ide%2Cterminal
```bash
~/snippet/go/tutorial/database-access$ cloudshell open-workspace .
~/snippet/go/tutorial/database-access$ cloudshell edit docker-compose.yml
```
- ( 2022-06-20 22:30:06 )
```docker
version: '2'

services:
  mysql:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: recordings
      MYSQL_USER: sample
      MYSQL_PASSWORD: CHANGME
      MYSQL_RANDOM_ROOT_PASSWORD: '1'
    volumes:
      - ./mysql:/var/lib/mysql
    ports:
      - 3306:3306
```
```bash
~/snippet/go/tutorial/database-access$ docker-compose up -d
~/snippet/go/tutorial/database-access$ docker-compose exec mysql /bin/bash
root@0b2e7f9f3435:/# mysql -u sample -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.38 MySQL Community Server (GPL)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database recordings;
ERROR 1007 (HY000): Can't create database 'recordings'; database exists

mysql> use recordings;
Database changed

mysql> DROP TABLE IF EXISTS album;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> CREATE TABLE album (
    ->   id         INT AUTO_INCREMENT NOT NULL,
    ->   title      VARCHAR(128) NOT NULL,
    ->   artist     VARCHAR(255) NOT NULL,
    ->   price      DECIMAL(5,2) NOT NULL,
    ->   PRIMARY KEY (`id`)
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql>
mysql> INSERT INTO album
    ->   (title, artist, price)
    -> VALUES
    ->   ('Blue Train', 'John Coltrane', 56.99),
    ->   ('Giant Steps', 'John Coltrane', 63.99),
    ->   ('Jeru', 'Gerry Mulligan', 17.99),
    ->   ('Sarah Vaughan', 'Sarah Vaughan', 34.98);
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> select * from album;
+----+---------------+----------------+-------+
| id | title         | artist         | price |
+----+---------------+----------------+-------+
|  1 | Blue Train    | John Coltrane  | 56.99 |
|  2 | Giant Steps   | John Coltrane  | 63.99 |
|  3 | Jeru          | Gerry Mulligan | 17.99 |
|  4 | Sarah Vaughan | Sarah Vaughan  | 34.98 |
+----+---------------+----------------+-------+
4 rows in set (0.01 sec)

mysql> quit
Bye
root@0b2e7f9f3435:/# exit
exit

~/snippet/go/tutorial/database-access$ 
~/snippet/go/tutorial/database-access$ go get .
go: downloading github.com/go-sql-driver/mysql v1.6.0
go: added github.com/go-sql-driver/mysql v1.6.0

~/snippet/go/tutorial/database-access$ export DBUSER=sample
~/snippet/go/tutorial/database-access$ export DBPASS=CHANGME

~/snippet/go/tutorial/database-access$ go run .
[mysql] 2022/06/20 14:38:35 connector.go:95: could not use requested auth plugin 'mysql_native_password': this user requires mysql native password authentication.
2022/06/20 14:38:35 this user requires mysql native password authentication.
exit status 1

~/snippet/go/tutorial/database-access$ docker ps -a
CONTAINER ID   IMAGE       COMMAND                  CREATED              STATUS              PORTS                               NAMES
8f0483590b79   mysql:5.7   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:3306->3306/tcp, 33060/tcp   database-access_mysql_1
~/snippet/go/tutorial/database-access$ mysql -u sample -p
Enter password:
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
```

## References

- https://go.dev/doc/tutorial/getting-started -  Tutorial: Get started with Go
- https://go.dev/doc/database/index - The `database/sql` package - see **Accessing databases**
- https://go.dev/doc/modules/managing-dependencies - Managing dependencies
- https://go.dev/doc/tutorial/index.html - other Tutorials
- https://github.com/golang/go/wiki/SQLDrivers - visit the **SQLDrivers** wiki page to identify a driver you can use.
- https://github.com/go-sql-driver/mysql/ - For accessing MySQL in this tutorial, you’ll use Go-MySQL-Driver.
- https://go.dev/doc/effective_go - Effective Go
- https://go.dev/doc/code - How to write Go code
- https://go.dev/tour/ - Go Tour