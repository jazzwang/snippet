all:
	gradle build
	cp src/main/resources/product_category.csv /tmp/.
	tar xvf build/distributions/csv_hashmap.tar
clean:
	rm -rf csv_hashmap /tmp/product_category.csv
	gradle clean
test:	clean all
	csv_hashmap/bin/csv_hashmap
