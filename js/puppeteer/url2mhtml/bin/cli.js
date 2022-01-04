#!/usr/bin/env node
// inspired by: 
// [1] https://github.com/yargs/yargs/blob/master/example/line_count.js
// [2] https://github.com/nodejs/examples/blob/master/cli/yargs/countEntriesInDirectory/bin/cli.js

const puppeteer = require('puppeteer');

var argv = require('yargs')
    .usage('Save specified URL to MHTML file.\nUsage: $0 ')
    .demand('url')
    .alias('url', 'i')
    .describe('url', 'source URL')
    .demand('outfile')
    .alias("outfile","o")
    .describe('outfile', 'output file name')
    .argv
;

// https://nodejs.org/en/knowledge/file-system/how-to-write-files-in-nodejs/
var fs = require('fs');

(async() => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(argv.url);
    const session = await page.target().createCDPSession();
    await session.send('Page.enable');
    const {data} = await session.send('Page.captureSnapshot');
    fs.writeFile(argv.outfile, data, function (err) {
        if (err) return console.log(err);
      });
    await browser.close();
  })();