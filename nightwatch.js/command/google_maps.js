exports.command = function(url, job_name){
  var browser = this;
  var date = new Date();
  browser
      .url(url)
      .waitForElementVisible('#scene', 30000)
      .saveScreenshot('reports/' + job_name + '_' + date.toISOString().substring(0, 10) + '_' + date.getHours() + '.png')
  return this;
};
