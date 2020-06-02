exports.command = function(url, job_name){
  var browser = this;
  var date = new Date();
  browser
      .url(url)
      .waitForElementVisible('#scene', 30000)
      .saveScreenshot('reports/' + job_name + '_' + date.toISOString().replace(/:/g,'-') + '.png')
  return this;
};
