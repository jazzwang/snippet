# Webhint

- Git Repo
  - https://github.com/webhintio/hint
- Website
  - https://webhint.io/

## 2026-07-07

> Use webhint to improve your website
> webhint helps you improve your site's accessibility, speed, cross-browser compatibility, and more by checking your code for best practices and common errors.

- 文件上寫 Try it
```bash
$ npx hint https://webhint.io
```
- 實測：
```bash
~/git/snippet/js/webhint$ npx hint https://webhint.io
Need to install the following packages:
hint@7.1.13
Ok to proceed? (y) 
Using the built-in configuration.
Visit https://webhint.io/docs/user-guide/ to learn how to create your own configuration.
✖ Finishing...
You can view the HTML report in "C:\Users\jazzw\git\snippet\js\webhint\hint-report\https-webhint-io.html"
compat-api/html            1 warning
ssllabs                    2 warnings
content-type               9 warnings
http-compression           4 warnings   10 hints
no-disallowed-headers      18 warnings
strict-transport-security  18 errors
x-content-type-options     18 errors
http-cache                 37 warnings  4 hints
× Found a total of 36 errors, 71 warnings, 14 hints and 0 informations
```
- 緣起：
  - 在 Edge DevTool 看到這個置頂通知
  - ![](edge-webhint-warning.png)