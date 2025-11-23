# json-schema-generator

> Generates draft v4 schema from a local file or a remote JSON url.

- NPM
  - https://www.npmjs.com/package/json-schema-generator
- Git Repo
  - https://github.com/krg7880/json-schema-generator

## 2025-09-06

- 需求：從 JSON 檔案資料轉成 JSON Schema 定義

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there command line tool to convert JSON file to JSON Schema?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, there are several command-line tools available to convert a JSON file into a JSON Schema. These tools typically work by analyzing the structure and data types within one or more sample JSON documents and then inferring a schema that would validate them.

### Popular Command-Line Tools

There are a few key options you can consider, depending on your environment and needs.

* **`json-schema-generator` (NPM Package)**: This is a popular tool for Node.js environments. It's easy to install via npm and provides a straightforward command-line interface. You can pipe a JSON file to it or specify an input file directly. The tool analyzes the JSON and outputs a draft of a schema. 

* **`quicktype`**: While `quicktype` is best known for generating code from JSON, it also has a feature to generate JSON Schema. It's a versatile tool that can be used on the command line to infer a schema from a JSON file or a directory of sample files.

* **`json-cli` (Python/Docker)**: This is a robust, multi-functional tool with a range of features beyond just schema generation, including validation, formatting, and diffing. You can use it to build a schema from a JSON instance, and it can be run directly from a Docker container, making it easy to use in various environments without a complex setup.
</td></tr></table>

- 備註：找不到 `json-cli` 這個 python 套件。（幻覺？）

## 2025-11-23

- 安裝：
```bash
~/Downloads$ npm install -g json-schema-generator
```
- 範例輸入：
```json
{
    "title": "fresh fruit schema v1",
    "type": "object",
    "required": ["skin", "colors", "taste"],
    "properties": {
        "colors": {
            "type": "array",
            "minItems": 1,
            "uniqueItems": true,
            "items": {
                "type": "string"
            }
        },
        "skin": {
            "type": "string"
        },
        "taste": {
            "type": "number",
            "minimum": 5
        }
    }
}
```
- 範例輸出：
```bash
~/Downloads$ json-schema-generator sample.json
Node
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "",
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "minLength": 1
    },
    "type": {
      "type": "string",
      "minLength": 1
    },
    "required": {
      "type": "array",
      "items": {
        "required": [],
        "properties": {}
      }
    },
    "properties": {
      "type": "object",
      "properties": {
        "colors": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "minLength": 1
            },
            "minItems": {
              "type": "number"
            },
            "uniqueItems": {
              "type": "boolean"
            },
            "items": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string",
                  "minLength": 1
                }
              },
              "required": [
                "type"
              ]
            }
          },
          "required": [
            "type",
            "minItems",
            "uniqueItems",
            "items"
          ]
        },
        "skin": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "type"
          ]
        },
        "taste": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "minLength": 1
            },
            "minimum": {
              "type": "number"
            }
          },
          "required": [
            "type",
            "minimum"
          ]
        }
      },
      "required": [
        "colors",
        "skin",
        "taste"
      ]
    }
  },
  "required": [
    "title",
    "type",
    "required",
    "properties"
  ]
}
```
- 狀況：用 STDIN 的作法反而沒有結果
```bash
~/Downloads$ cat sample.json | json-schema-generator
Node
```
- 雖然可以生成 JSON Schema，但原本我想要的結果是類似 PySpark 那種有階層的輸出。
  - 替代方案：
    - 用 `jq` 直接生成
    - https://stackoverflow.com/a/43380040
    ```bash
    ~/Downloads$ cat ~/bin/jq-schema
    #!/bin/bash
    SOURCE_FILE=$1
    ##-- https://stackoverflow.com/a/43380040
    ##-- Posted by peak, modified by community. See post 'Timeline' for change history
    ##-- Retrieved 2025-11-23, License - CC BY-SA 4.0

    jq 'paths(scalars) | map(tostring) | join(".")' $SOURCE_FILE
    ```
    ```bash
    ~/Downloads$ jq-schema sample.json
    "title"
    "type"
    "required.0"
    "required.1"
    "required.2"
    "properties.colors.type"
    "properties.colors.minItems"
    "properties.colors.uniqueItems"
    "properties.colors.items.type"
    "properties.skin.type"
    "properties.taste.type"
    "properties.taste.minimum"
    ```
    - 用 python 生成
    - https://stackoverflow.com/a/43379886
    ```bash
    ~/Downloads$ show_struct.py sample.json
    .properties
    .properties.colors
    .properties.colors.items
    .properties.colors.items.type -- string
    .properties.colors.minItems -- 1
    .properties.colors.type -- array
    .properties.colors.uniqueItems -- True
    .properties.skin
    .properties.skin.type -- string
    .properties.taste
    .properties.taste.minimum -- 5
    .properties.taste.type -- number
    .required -- (Array of 3 elements)
    .required[] -- colors .. taste (3 unique values)
    .title -- fresh fruit schema v1
    .type -- object
    ```