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

## 2023-08-16

- ( 2023-08-16 13:25:15 )
- add `add-pet.yaml` which keep only 1 path and remove most out of `petstore.yaml`
- ( 2023-08-16 13:27:10 )
- run `openapi-generator-cli validate -i add-pet.yaml`
```bash
~/snippet/go/petstoropenapi-generator-cli validate -i add-pet.yaml
Did set selected version to 6.6.0
Validating spec (add-pet.yaml)
Warnings:
        - Unused model: Order
        - Unused model: User
        - Unused model: ApiResponse

[info] Spec has 3 recommendation(s).
```
- ( 2023-08-16 13:29:25 )
- remove `store`, `user` from `tags`
- remove `ApiResponse`, `Order`, `User` from `schemas`
- remove `UserArray` from `requestBodies`
- ( 2023-08-16 13:36:45 )
```
~/snippet/go/petstore$ openapi-generator-cli validate -i add-pet.yaml
Validating spec (add-pet.yaml)
No validation issues detected.
```
- ( 2023-08-16 13:36:51 )
- generate code template using `go-gin-server`
```
~/snippet/go/petstore$ openapi-generator-cli generate -i add-pet.yaml -g go-gin-server -o petstore-go-gin
Did set selected version to 6.6.0
```
- ( 2023-08-16 13:40:24 )
```
~/snippet/go/petstore$ cd petstore-go-gin/
~/snippet/go/petstore/petstore-go-gin$ tree .
.
├── api
│   └── openapi.yaml
├── Dockerfile
├── go
│   ├── api_pet.go
│   ├── model_category.go
│   ├── model_pet.go
│   ├── model_tag.go
│   ├── README.md
│   └── routers.go
├── go.mod
└── main.go

2 directories, 10 files
```
- ( 2023-08-16 15:02:45 )
- remove `Category`, `Tag` from `schemas`
- remove `category`, `tags` from `schemas > Pet`