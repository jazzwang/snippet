function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

for ( let i = 1; i < 100; i++ ) {
    await sleep(1000); // sleep 1 second
    window.scrollTo(0, document.body.scrollHeight);
}

count = $$("div.mh4 a.app-aware-link").length

var links = []
for (let i=0; i < count; i++) {
    links.push($$("div.mh4 a.app-aware-link")[i].href.split('?')[0]);
}

var a = document.createElement('a');
var file = new Blob([ links.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'linkedin-saved-posts.txt';
a.click();
