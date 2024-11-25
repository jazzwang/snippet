function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

for ( let i = 1; i < 200; i++ ) {
    await sleep(2000); // sleep 2 second
    window.scrollTo(0, document.body.scrollHeight);
}

count = $$("div.mh4 a").length

var links = []
for (let i=0; i < count; i++) {
    links.push($$("div.mh4 a")[i].href.split('?')[0]);
}

var a = document.createElement('a');
var file = new Blob([ links.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'linkedin-saved-posts.txt';
a.click();
