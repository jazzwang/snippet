module.exports = {
  'google maps test' : function (browser) {
    var url = "https://goo.gl/maps/4xY4ZX3cZrS2";

    browser.resizeWindow(1280, 1024);
    browser
      .google_maps(url,"Taipei-HsinChu")
      .pause(5000)
      .end();
  }
};
