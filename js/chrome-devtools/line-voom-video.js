count = $$("video").length

var script = ""
for (let i=0; i < count; i++) {
  console.log("wget -O " + i + ".mp4 '" + $$("video")[i].getAttribute('src') + "'")
  script += "wget -O " + i + ".mp4 '" + $$("video")[i].getAttribute('src') + "'\n"
}

var a = document.createElement('a');
var file = new Blob([ script.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'download-voom-video.sh';
a.click();