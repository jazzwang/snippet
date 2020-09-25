* [動機] 想分析團隊成員有貢獻的 git repo 並且將增減行數及時間做視覺畫的呈現
* [構思] 
    * 1. 需要先能找到分析 git repo 的 python 函式庫
    * [參考]
        * 底下幾個參考連結幾乎都是靠 `git log` 的結果來做分析
        * https://pypi.org/project/gitstats/
            * https://github.com/suminb/gitstats
            * 感覺是寫成 pip 套件的指令，安裝起來相依套件很多
        * http://iguananaut.net/blog/programming/git-logs-in-pandas.html
        * https://www.feststelltaste.de/mini-tutorial-git-log-analysis-with-python-and-pandas/
        * 其次，看到比較大型的專案是 GitPython
            * https://pypi.org/project/GitPython/
            * https://github.com/gitpython-developers/GitPython
    * 2. 能計算 [Bus Factor](https://en.wikipedia.org/wiki/Bus_factor)
        * https://github.com/jerdonegan/bus-factor
        * https://github.com/zats/github_bus_factor
        * https://github.com/yamikuronue/BusFactor
        * https://pypi.org/project/mr.parker/
    * [參考]
        * https://github.com/wdm0006/gitnoc - 這個專案蠻接近最終想呈現的結果
            * 相依 [git-pandas](http://wdm0006.github.io/git-pandas/) 
            * https://github.com/wdm0006/git-pandas - 使用 gitPython 把 Git Repo 的一些屬性轉成 Pandas 的 DataFrame