# MEMO

## 2023-08-15

- test environment: https://shell.cloud.google.com
- ( 2023-08-15 00:32:04 )
- https://openapi-generator.tech/docs/installation
```bash
~$ npm install @openapitools/openapi-generator-cli -g
```
- ( 2023-08-15 00:34:42 )
- download sample
```
~/git/snippet/go$ mkdir petstore
~/git/snippet/go$ cd petstore
~/snippet/go/petstore$ wget -q https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml
~/snippet/go/petstore$ git add petstore.yaml
~/snippet/go/petstore$ openapi-generator-cli validate -i petstore.yaml
Did set selected version to 6.6.0
Validating spec (petstore.yaml)
No validation issues detected.
```