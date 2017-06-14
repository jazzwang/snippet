exports.command = function(username, password){
  var browser = this;
  browser
      .url('https://portal.azure.com')
      .waitForElementVisible('#cred_userid_inputtext', 30000)
      .setValue('#cred_userid_inputtext', username)
      .setValue('#cred_password_inputtext', password)
      .submitForm('#credentials')
      .waitForElementVisible('#web-container', 60000)
  return this;
};
