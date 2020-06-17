# Lab 2 : local npm package @ 2020-06-17

## References

* https://docs.npmjs.com/creating-node-js-modules
* https://docs.npmjs.com/about-scopes
* https://docs.npmjs.com/creating-a-package-json-file
* https://docs.npmjs.com/creating-and-publishing-private-packages

## Steps

* Since I am trying out the npm packages, here I choose "nonscoped module" and run `npm init`
```
~$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (url2mhtml) 
version: (1.0.0) 0.0.1
description: a simple CLI program to scrap url to MHTML file
entry point: (index.js) 
test command: node test.js
git repository: 
keywords: puppeteer
author: Jazz Wang
license: (ISC) 
About to write to /Users/jazzwang/git/snippet/javascript/puppeteer/url2mhtml/package.json:

{
  "name": "url2mhtml",
  "version": "0.0.1",
  "description": "a simple CLI program to scrap url to MHTML file",
  "main": "index.js",
  "scripts": {
    "test": "node test.js"
  },
  "keywords": [
    "puppeteer"
  ],
  "author": "Jazz Wang",
  "license": "ISC"
}


Is this OK? (yes) 
```
