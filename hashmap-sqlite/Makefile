all:
	gradle build
	tar xvf build/distributions/hashmap-sqlite.tar
test:	clean all
	hashmap-sqlite/bin/hashmap-sqlite
clean:
	gradle clean
	rm -rf test.db hashmap-sqlite
