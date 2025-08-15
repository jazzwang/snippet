// 1. open https://www.cloudskillsboost.google/paths
// 2. paste the following into DevTool console

card=$$('ql-activity-card')

var script = "";
for (let i=0; i < card.length; i++) {
    script += 'https://www.cloudskillsboost.google' + card[i].getAttribute("path") + ';' + card[i].getAttribute("name") + '\n';
}

var a = document.createElement('a');
var file = new Blob([ script.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'gcp-cloudskillsboost-list.txt';
a.click();