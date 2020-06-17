all:
	gradle build
	tar xvf build/distributions/java-sqlite.tar 
test:	clean all
	java-sqlite/bin/java-sqlite
clean:
	gradle clean
	rm -rf test.db java-sqlite
