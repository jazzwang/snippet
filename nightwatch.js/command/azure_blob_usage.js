exports.command = function(subscription, resourceGroup, storageAccount){
  var browser = this;
  var usage = "";

  //console.log('https://portal.azure.com/#resource/subscriptions/' + subscription + '/resourceGroups/' + resourceGroup + '/providers/Microsoft.Storage/storageAccounts/' + storageAccount + '/containersUsage');

  browser
      .url('https://portal.azure.com/#resource/subscriptions/' + subscription + '/resourceGroups/' + resourceGroup + '/providers/Microsoft.Storage/storageAccounts/' + storageAccount + '/containersUsage')
      .waitForElementVisible('#web-container > div.fxs-portal-main > main > div.fxs-journey-target.fxs-journey > div > div.fxs-blade.fxs-stacklayout-child.fxs-bladesize-menu.fxs-menublade.fxs-blade-maximized > div > div.fxs-blade-content-container-details.fxs-blade-border.fxs-portal-border.fxs-bladecontent.fx-rightClick.fxs-bladestyle-default.fxs-bladesize-medium.fxs-bladecontent-unlocked.fxs-blade-maximized > div.fxs-blade-content-wrapper > div.fxs-blade-content > div > div > div.fxs-lens-layout > div.fxs-tile.fxs-portal-bg-txt-br.fxs-tilesize-herowide.fx-rightClick > div.fxs-part.fxs-part-part-title-visible.fxs-part-clickable > div.fxs-part-content.css-scope-Microsoft_Azure_Insights > div > div.fxc-base.fxc-base-fill-container-width.fxc-base-fill-container-height.fxc-chart > div.fxc-base.azc-control.azc-metrics.azc-metrics-sizeLarge > ul > li > div.azc-metrics-singleSetting.fxc-base.azc-control.azc-singleSetting > div.azc-singleSetting-data > div.azc-singleSetting-value', 10000, false)
      .getText('#web-container > div.fxs-portal-main > main > div.fxs-journey-target.fxs-journey > div > div.fxs-blade.fxs-stacklayout-child.fxs-bladesize-menu.fxs-menublade.fxs-blade-maximized > div > div.fxs-blade-content-container-details.fxs-blade-border.fxs-portal-border.fxs-bladecontent.fx-rightClick.fxs-bladestyle-default.fxs-bladesize-medium.fxs-bladecontent-unlocked.fxs-blade-maximized > div.fxs-blade-content-wrapper > div.fxs-blade-content > div > div > div.fxs-lens-layout > div.fxs-tile.fxs-portal-bg-txt-br.fxs-tilesize-herowide.fx-rightClick > div.fxs-part.fxs-part-part-title-visible.fxs-part-clickable > div.fxs-part-content.css-scope-Microsoft_Azure_Insights > div > div.fxc-base.fxc-base-fill-container-width.fxc-base-fill-container-height.fxc-chart > div.fxc-base.azc-control.azc-metrics.azc-metrics-sizeLarge > ul > li > div.azc-metrics-singleSetting.fxc-base.azc-control.azc-singleSetting > div.azc-singleSetting-data > div.azc-singleSetting-value', function(result) { 
	  console.log('{"resource_group":"%s","storage_account":"%s","usage":"%s",', resourceGroup, storageAccount, result.value);
       })
      .getText('#web-container > div.fxs-portal-main > main > div.fxs-journey-target.fxs-journey > div > div.fxs-blade.fxs-stacklayout-child.fxs-bladesize-menu.fxs-menublade.fxs-blade-maximized > div > div.fxs-blade-content-container-details.fxs-blade-border.fxs-portal-border.fxs-bladecontent.fx-rightClick.fxs-bladestyle-default.fxs-bladesize-medium.fxs-bladecontent-unlocked.fxs-blade-maximized > div.fxs-blade-content-wrapper > div.fxs-blade-content > div > div > div.fxs-lens-layout > div.fxs-tile.fxs-portal-bg-txt-br.fxs-tilesize-herowide.fx-rightClick > div.fxs-part.fxs-part-part-title-visible.fxs-part-clickable > div.fxs-part-content.css-scope-Microsoft_Azure_Insights > div > div.fxc-base.fxc-base-fill-container-width.fxc-base-fill-container-height.fxc-chart > div.fxc-base.azc-control.azc-metrics.azc-metrics-sizeLarge > ul > li > div.azc-metrics-singleSetting.fxc-base.azc-control.azc-singleSetting > div.azc-singleSetting-data > div.azc-singleSetting-unit > span', function(result) { console.log('"unit":"%s"}', result.value); })
      .saveScreenshot('reports/' + resourceGroup + '_' + storageAccount + '.png')
      .pause(1000);

  return this;
};
