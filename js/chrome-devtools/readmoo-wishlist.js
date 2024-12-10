links = $$("div.item-title-link-box a")
count = links.length

var script = ""
for (let i=0; i < count/2; i++) {
  url=links[2*i].href
  title=links[2*i].text
  console.log(url + ";" + title + "\n")
  script += url + ";" + title + "\n"
}

var a = document.createElement('a');
var file = new Blob([ script.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'readmoo-wishlist.csv';
a.click();