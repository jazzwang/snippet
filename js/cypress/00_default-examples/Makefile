all:	setup test
	@echo "Usage:"
clean:
	@rm -rf cypress/videos/
dist-clean: clean
	@rm -rf node_modules .installed package-lock.json
setup:
	@npm install
	@touch .installed
test:	.installed
	@node_modules/.bin/cypress run -s cypress/integration/1-getting-started/todo.spec.js 

