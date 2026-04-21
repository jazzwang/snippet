// 1. Open https://www.linkedin.com/my-items/saved-posts/
// 2. paste this snippet into Chrome Developer Tool Console

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

for ( let i = 1; i < 200; i++ ) {
    await sleep(2000); // sleep 2 second
    window.scrollTo(0, document.body.scrollHeight);
    console.log(`Iteration: ${i}, Remaining: ${199 - i}`);
}

count = $$('div[data-chameleon-result-urn]').length

var script = ""
for (let i=0; i < count; i++) {
    script += "https://www.linkedin.com/feed/update/" + $$('div[data-chameleon-result-urn]')[i].getAttribute('data-chameleon-result-urn') + "\n"
}

var a = document.createElement('a');
var file = new Blob([ script.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'linkedin-saved-posts.txt';
a.click();
