all:	.installed
	npm run test-e2e
clean:
	@rm -rf reports selenium-debug.log package-lock.json
dist-clean: clean
	@rm -rf bin node_modules .installed
setup:
	@./setup.sh
	@touch .installed
