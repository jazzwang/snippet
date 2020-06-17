all:
	gradle build
	cp src/main/resources/product_category.csv /tmp/.
	tar xvf build/distributions/hashmap-sqlite.tar
test:	clean all
	hashmap-sqlite/bin/hashmap-sqlite
clean:
	gradle clean
	rm -rf test.db hashmap-sqlite /tmp/product_category.csv
