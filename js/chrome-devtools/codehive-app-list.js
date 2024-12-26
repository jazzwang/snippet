// Instruction:
// Visit https://www.codehive.app/ and paste the following code in Chrome DevTools Console

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

for ( let i = 1; i < 50; i++ ) {
    await sleep(2000); // sleep 2 second
    window.scrollTo(0, document.body.scrollHeight);
}

// Ref: https://g.co/gemini/share/c6368c3d9e3c
var apps="";
var cards=$$('.card');
cards.map(card => {
  link=card.getAttribute('hx-get');
  title=card.querySelector('.card__title')?.textContent.trim();
  description=card.querySelector('.card__descr')?.textContent.trim();
  apps += "https://www.codehive.app" + link + ';' + title  + ';' + description + "\n";
});

var a = document.createElement('a');
var file = new Blob([ apps.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'codehive-app-list.txt';
a.click();
