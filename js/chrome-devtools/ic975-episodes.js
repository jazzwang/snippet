// Instruction:
//
//   Visit https://www.ic975.com/programs/11/%25E6%2599%259A%25E5%25AE%2589%25EF%25BC%258E%25E6%259C%2588%25E4%25BA%25AE%25E2%2594%2580%25E5%25BA%258A%25E9%2582%258A%25E6%2595%2585%25E4%25BA%258B 
//   and paste the following code in Chrome DevTools Console
// 

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
  
for ( let i = 1; i < 200; i++ ) {
  await sleep(2000); // sleep 2 second
  window.scrollTo(0, document.body.scrollHeight);
}

links = $$("a.title-frame")
titles = $$("a.title-frame div.title")
timestamps = $$("a.title-frame div.on-time")
count = links.length

var script = ""
for (let i=count-1; i >= 0; i--) {
  url=links[i].href
  title=titles[i].text
  timestamp=timestamps[i].text
  console.log(url + ";" + title + ";" + timestamp + "\n")
  script += url + ";" + title + ";" + timestamp + "\n"
}

var a = document.createElement('a');
var file = new Blob([ script.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'ic975-episodes.csv';
a.click();