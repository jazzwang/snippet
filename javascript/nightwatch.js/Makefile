all:	.installed
	npm run test-e2e | tee test.log
clean:
	@rm -rf reports selenium-debug.log package-lock.json test.log
dist-clean: clean
	@rm -rf bin node_modules .installed
setup:
	@./setup.sh
	@touch .installed
