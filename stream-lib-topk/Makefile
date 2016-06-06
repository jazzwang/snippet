all:
	gradle build
	tar xvf build/distributions/stream-lib-topk.tar 
test:	clean all
	stream-lib-topk/bin/stream-lib-topk
clean:
	gradle clean
	rm -rf stream-lib-topk
