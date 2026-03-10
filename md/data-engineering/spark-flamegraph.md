# Apache Spark Performance Optimization / Distributed Profiler / Flamegraph

## JVM / Spark

- Uber jvm-profiler (JVM & Spark profiling)
  - Blog: https://www.uber.com/en-TW/blog/jvm-profiler/
  - Repo: https://github.com/uber-common/jvm-profiler
- PayPal Tech: Spark in Flames (article) 
  - https://medium.com/paypal-tech/spark-in-flames-profiling-spark-applications-using-flame-graphs-71e77b26516e
- CERN slides: Flame Graphs for Spark 
  - https://canali.web.cern.ch/docs/Spark_Summit_2016_Flame_Graphs_Spark_Luca_CERN.pdf
- Conversant spark-profiler
  - https://github.com/conversant/spark-profiler
- Spark flame graphs (Git)
  - https://github.com/mispecto/spark-flamegraph
- Google Cloud Dataproc Serverless profiling guide 
  - https://docs.cloud.google.com/dataproc-serverless/docs/guides/profiling

## Flame Graph Fundamentals & Tools

- Brendan Gregg: Flame Graphs (canonical)
  - https://www.brendangregg.com/flamegraphs.html
- Netflix FlameScope (explore traces)
  - https://github.com/Netflix/flamescope
- d3-flame-graph (interactive D3 component)
  - https://github.com/spiermar/d3-flame-graph
- VS Code Flamegraph extension
  - https://marketplace.visualstudio.com/items?itemName=rafaelha.vscode-flamegraph
  - GitHub — https://github.com/rafaelha/vscode-flamegraph

## Python

- py-spy (sampling profiler)
  - https://github.com/benfred/py-spy
- pyinstrument (profiler & flamegraphs) 
  — Reddit: https://www.reddit.com/r/Python/comments/1g1az6i/pyinstrument_v50_flamegraphs_for_python/
  - Repo: https://github.com/joerick/pyinstrument
  - Blog: https://joerick.me/posts/2024/10/3/pyinstrument-5/
  - Demo GIF: https://joerick.s3.amazonaws.com/pyi+video+1.gif
- Bloomberg memray flamegraph docs
  - https://bloomberg.github.io/memray/flamegraph.html
- evanhempel/python-flamegraph
  - https://github.com/evanhempel/python-flamegraph
- pyflame (older sampling profiler)
  - https://pypi.org/project/pyflame/
- Perforator (profiling system) 
  - https://perforator.tech/docs/en/explanation/architecture/overview
- Peter McConnell perf/py resources
  - Site: https://www.petermcconnell.com/posts/perf_eng_with_py12/
  - GitHub: https://github.com/peter-mc-connell/

## 同場加映 Go

- Flame graphs in Go (blog) 
  - https://lemire.me/blog/2025/10/26/flame-graphs-in-go/
- Debugging memory leaks in Go w/ pprof + flame graphs
  - https://medium.com/@siddharthnarayan/debugging-memory-leaks-in-go-using-pprof-and-flame-graphs-f60ef9b8944d
- Flame graphs for Go with pprof
  - https://www.benburwell.com/posts/flame-graphs-for-go-with-pprof/

## Cloud/Service Profilers

- AWS CodeGuru Profiler
  - https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html