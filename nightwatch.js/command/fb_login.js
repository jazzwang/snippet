exports.command = function(username, password){
  var browser = this;
  browser
      .url('https://www.facebook.com')
      .waitForElementVisible('#email', 30000)
      .setValue('#email', username)
      .setValue('#pass', password)
      .submitForm('#login_form')
      .waitForElementVisible('#pagelet_bluebar', 60000)
  return this;
};
