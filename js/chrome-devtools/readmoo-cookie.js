function splitOnFirstEqual(str) {
    const index = str.indexOf('=');
    if (index === -1) {
        return [str]; // 如果沒有找到 `=`，返回整個字符串
    }
    const beforeEqual = str.substring(0, index);
    const afterEqual = str.substring(index + 1);
    return [beforeEqual, afterEqual];
}

cookies = JSON.stringify(
    document.cookie.split(';')
    .map(c => splitOnFirstEqual(c))
    .map(i => [i[0].trim(), i[1].trim()])
    .reduce((r, i) => {r[i[0]] = i[1]; return r;}, {}))

var a = document.createElement('a');
var file = new Blob([ cookies.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'readmoo-cookie.json';
a.click();