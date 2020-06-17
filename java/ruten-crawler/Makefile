all:
	gradle build
	tar xvf build/distributions/ruten-crawler.tar
clean:
	rm -rf ruten-crawler
	gradle clean
test:	clean all
	ruten-crawler/bin/ruten-crawler 21534405681616
timeout-test:
	for i in {1..10}; do ruten-crawler/bin/ruten-crawler 21534405681616; done
