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

## 2023-08-17

- ( 2023-08-17 09:23:46 )
- Here is the [mustache](https://mustache.github.io/) templates that `openapi-generator-cli` used for generating golang codes
- https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/go
- https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/go-echo-server
- https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/go-gin-server
- https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/go-server
```
go
├── api_doc.mustache
├── api.mustache
├── api_test.mustache
├── client.mustache
├── configuration.mustache
├── gitignore.mustache
├── git_push.sh.mustache
├── go.mod.mustache
├── go.sum.mustache
├── model_anyof.mustache
├── model_doc.mustache
├── model_enum.mustache
├── model.mustache
├── model_oneof.mustache
├── model_simple.mustache
├── nullable_model.mustache
├── openapi.mustache
├── partial_header.mustache
├── README.mustache
├── response.mustache
├── signing.mustache
└── utils.mustache
go-gin-server
├── controller-api.mustache
├── Dockerfile.mustache
├── go.mod.mustache
├── main.mustache
├── model.mustache
├── openapi.mustache
├── partial_header.mustache
├── README.mustache
└── routers.mustache
go-echo-server
├── api.mustache
├── Dockerfile.mustache
├── go-mod.mustache
├── handler-container.mustache
├── hello-world.mustache
├── main.mustache
├── model.mustache
├── openapi.mustache
└── README.mustache
go-server
├── api.mustache
├── controller-api.mustache
├── Dockerfile.mustache
├── error.mustache
├── go.mod.mustache
├── helpers.mustache
├── impl.mustache
├── logger.mustache
├── main.mustache
├── model.mustache
├── openapi.mustache
├── partial_header.mustache
├── README.mustache
├── routers.mustache
└── service.mustache

0 directories, 55 files
```