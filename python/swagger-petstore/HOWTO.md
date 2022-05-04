```
~/snippet/python/swagger-petstore$ docker run --rm     -v $PWD:/local openapitools/openapi-generator-cli generate     -i https://petstore.swagger.io/v2/swagger.json   -g python-flask       -o /local
```
