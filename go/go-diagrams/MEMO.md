# Go Diagrams

> Create beautiful system diagrams with Go

- https://github.com/blushft/go-diagrams

## 2024-12-02

- ( 2024-12-02 16:54:11 )
- 緣起：
  - 在 ByteByteGo 的文章中看到 `go-diagrams`
  - ![](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e585277-7fe3-4cd4-b257-f14edbbb4fc7_1280x1664.gif)
- 測試：
  - 環境：Github Codespace
- 安裝：
```bash
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ go get github.com/blushft/go-diagrams
go: go.mod file not found in current directory or any parent directory.
        'go get' is no longer supported outside a module.
        To build and install a command, use 'go install' with a version,
        like 'go install example.com/cmd@latest'
        For more information, see https://golang.org/doc/go-get-install-deprecation
        or run 'go help get' or 'go help install'.
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ go install github.com/blushft/go-diagrams
go: 'go install' requires a version when current directory is not in a module
        Try 'go install github.com/blushft/go-diagrams@latest' to install the latest version
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ go install github.com/blushft/go-diagrams@latest
go: downloading github.com/blushft/go-diagrams v0.0.0-20201006005127-c78c821223d9
go: downloading github.com/awalterschulze/gographviz v0.0.0-20200901124122-0eecad45bd71
go: downloading github.com/google/uuid v1.1.2
go: downloading golang.org/x/net v0.0.0-20190620200207-3b0461eec859
package github.com/blushft/go-diagrams is not a main package
```
- 編譯：
```bash
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ cat > example.go < EOF
d, err := diagram.New(diagram.Filename("app"), diagram.Label("App"), diagram.Direction("LR"))
if err != nil {
    log.Fatal(err)
}

dns := gcp.Network.Dns(diagram.NodeLabel("DNS"))
lb := gcp.Network.LoadBalancing(diagram.NodeLabel("NLB"))
cache := gcp.Database.Memorystore(diagram.NodeLabel("Cache"))
db := gcp.Database.Sql(diagram.NodeLabel("Database"))

dc := diagram.NewGroup("GCP")
dc.NewGroup("services").
    Label("Service Layer").
    Add(
        gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 1")),
        gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 2")),
        gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 3")),
    ).
    ConnectAllFrom(lb.ID(), diagram.Forward()).
    ConnectAllTo(cache.ID(), diagram.Forward())

dc.NewGroup("data").Label("Data Layer").Add(cache, db).Connect(cache, db)

d.Connect(dns, lb, diagram.Forward()).Group(dc)

if err := d.Render(); err != nil {
    log.Fatal(err)
}
EOF
```
```bash
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ go run example.go 
example.go:1:1: expected 'package', found d
```
- install Go REPL `gore` and autocomplete `gocode`
```bash
@jazzwang ➜ /workspaces/snippet/go (master) $ go install github.com/x-motemen/gore/cmd/gore@latest
go: downloading github.com/x-motemen/gore v0.5.7
go: downloading github.com/motemen/go-quickfix v0.0.0-20230925231438-5cf0001766ff
go: downloading github.com/peterh/liner v1.2.2
go: downloading golang.org/x/text v0.13.0
go: downloading golang.org/x/tools v0.13.0
go: downloading github.com/mattn/go-runewidth v0.0.15
go: downloading golang.org/x/sys v0.12.0
go: downloading github.com/rivo/uniseg v0.4.4
go: downloading golang.org/x/mod v0.12.0
@jazzwang ➜ /workspaces/snippet/go (master) $ go install github.com/mdempsky/gocode@latest
go: downloading github.com/mdempsky/gocode v0.0.0-20200405233807-4acdcbdea79d
go: finding module for package golang.org/x/tools/go/gcexportdata
go: downloading golang.org/x/tools v0.27.0
go: found golang.org/x/tools/go/gcexportdata in golang.org/x/tools v0.27.0
```