clean:
	rm -rf ruten-crawler
	gradle clean
all:
	gradle build
	tar xvf build/distributions/ruten-crawler.tar
test:	clean all
	ruten-crawler/bin/ruten-crawler 21534405681616
