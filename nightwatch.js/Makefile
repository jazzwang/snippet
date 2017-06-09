clean:
	@rm -rf reports selenium-debug.log package-lock.json
dist-clean: clean
	@rm -rf bin node_modules
setup:
	@./setup.sh
all:
	npm run test-e2e
