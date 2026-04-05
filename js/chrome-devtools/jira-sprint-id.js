options = $$("select option")
count = options.length

var script = "sprint_name,sprint_id\n"
for (let i=0; i < count; i++) {
  sprint_name=options[i].innerText
  sprint_id=options[i].value
  console.log(sprint_name + "," + sprint_id + "\n")
  script += sprint_name + "," + sprint_id + "\n"
}

var a = document.createElement('a');
var file = new Blob([ script.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'sprint-ids.csv';
a.click();