# Install Cmder

```
mkdir cmder
mkdir cmder\bin
cd cmder\bin
$client = new-object System.Net.WebClient
$client.DownloadFile("https://eternallybored.org/misc/wget/1.20.3/64/wget.exe","wget.exe")
cd ..
.\bin\wget.exe curl https://github.com/cmderdev/cmder/releases/download/v1.3.12/cmder.zip
unzip cmder.zip
del cmder.zip
```