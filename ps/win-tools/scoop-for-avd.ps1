Invoke-RestMethod -Uri https://raw.githubusercontent.com/ScoopInstaller/Install/master/install.ps1 -outfile install-scoop.ps1
.\install-scoop.ps1
scoop bucket add extras
$scoopCachePath = Join-Path $env:HOME 'scoop\cache'
Expand-Archive S:\Migration_Software\RCM_EE_IND\scoop-cache.zip -DestinationPath $scoopCachePath
scoop install 7zip git saml2aws k6 terraform redis golangci-lint
