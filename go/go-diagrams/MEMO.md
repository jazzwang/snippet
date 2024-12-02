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
- ( 2024-12-02 20:08:25 )
- test with `gore`
```bash
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ gore -autoimport
gore version 0.5.7  :help for help
gore> :print
package main

import "github.com/k0kubun/pp/v3"

func __gore_p(xs ...any) {
    for _, x := range xs {
        pp.Println(x)
    }
}
func main() {}

gore> :import "github.com/blushft/go-diagrams"
gore> :print
package main

import (
    "github.com/k0kubun/pp/v3"
    "github.com/blushft/go-diagrams"
)

func __gore_p(xs ...any) {
    for _, x := range xs {
        pp.Println(x)
    }
}
func main() {}

gore> d, err := diagram.New(diagram.Filename("app"), diagram.Label("App"), diagram.Direction("LR"))
&diagram.Diagram{
  options: diagram.Options{
    Name:       "go-diagrams",
    FileName:   "app",
    OutFormat:  "dot",
    Direction:  "LR",
    CurveStyle: "ortho",
    Show:       true,
    Label:      "App",
    Pad:        2.000000,
    Splines:    "ortho",
    NodeSep:    0.600000,
    RankSep:    0.750000,
    Font:       diagram.Font{
      Name:  "Sans-Serif",
      Size:  13.000000,
      Color: "#2D3436",
    },
    Attributes: map[string]string{},
  },
  g: &gographviz.Escape{
    Graph: &gographviz.Graph{
      Attrs: gographviz.Attrs{
        "fontcolor": "\"#2D3436\"",
        "fontname":  "\"Sans-Serif\"",
        "fontsize":  "13",
        "label":     "App",
        "nodesep":   "0.6",
        "pad":       "2",
        "rankdir":   "LR",
        "ranksep":   "0.75",
        "splines":   "ortho",
      },
      Name:     "root",
      Directed: true,
      Strict:   false,
      Nodes:    &gographviz.Nodes{
        Lookup: map[string]*gographviz.Node{},
        Nodes:  []*gographviz.Node{},
      },
      Edges: &gographviz.Edges{
        SrcToDsts: map[string]map[string][]*gographviz.Edge{},
        DstToSrcs: map[string]map[string][]*gographviz.Edge{},
        Edges:     []*gographviz.Edge{},
      },
      SubGraphs: &gographviz.SubGraphs{
        SubGraphs: map[string]*gographviz.SubGraph{},
      },
      Relations: &gographviz.Relations{
        ParentToChildren: map[string]map[string]bool{},
        ChildToParents:   map[string]map[string]bool{},
      },
    },
  },
  root: &diagram.Group{
    idx:     0,
    id:      "root",
    options: diagram.GroupOptions{
      Label:           "",
      LabelJustify:    "l",
      Direction:       "LR",
      PenColor:        "#AEB6BE",
      BackgroundColor: "#E5F5FD",
      Shape:           "box",
      Style:           "rounded",
      Font:            diagram.Font{
        Name:  "Sans-Serif",
        Size:  12.000000,
        Color: "#2D3436",
      },
      Attributes: map[string]string{},
    },
    parent:   (*diagram.Group)(nil),
    children: map[string]*diagram.Group{},
    nodes:    map[string]*diagram.Node{},
    edges:    map[string]*diagram.Edge{},
  },
}
nil
gore> 
gore> if err != nil {
.....         log.Fatal(err)
..... }
gore> 
gore> dns := gcp.Network.Dns(diagram.NodeLabel("DNS"))
&diagram.Node{
  id:      "iqargyhp",
  conn:    nil,
  Options: diagram.NodeOptions{
    Name:          "node",
    Label:         "DNS",
    Provider:      "gcp",
    Image:         "assets/gcp/network/dns.png",
    ImageScale:    true,
    Shape:         "none",
    Style:         "rounded",
    FixedSize:     true,
    Width:         1.400000,
    Height:        1.400000,
    LabelLocation: "b",
    Font:          diagram.Font{
      Name:  "Sans-Serif",
      Size:  13.000000,
      Color: "#2D3436",
    },
    Attributes: map[string]string{},
  },
}
gore> lb := gcp.Network.LoadBalancing(diagram.NodeLabel("NLB"))
&diagram.Node{
  id:      "wzgbtygx",
  conn:    nil,
  Options: diagram.NodeOptions{
    Name:          "node",
    Label:         "NLB",
    Provider:      "gcp",
    Image:         "assets/gcp/network/load-balancing.png",
    ImageScale:    true,
    Shape:         "none",
    Style:         "rounded",
    FixedSize:     true,
    Width:         1.400000,
    Height:        1.400000,
    LabelLocation: "b",
    Font:          diagram.Font{
      Name:  "Sans-Serif",
      Size:  13.000000,
      Color: "#2D3436",
    },
    Attributes: map[string]string{},
  },
}
gore> cache := gcp.Database.Memorystore(diagram.NodeLabel("Cache"))
&diagram.Node{
  id:      "argfrrdx",
  conn:    nil,
  Options: diagram.NodeOptions{
    Name:          "node",
    Label:         "Cache",
    Provider:      "gcp",
    Image:         "assets/gcp/database/memorystore.png",
    ImageScale:    true,
    Shape:         "none",
    Style:         "rounded",
    FixedSize:     true,
    Width:         1.400000,
    Height:        1.400000,
    LabelLocation: "b",
    Font:          diagram.Font{
      Name:  "Sans-Serif",
      Size:  13.000000,
      Color: "#2D3436",
    },
    Attributes: map[string]string{},
  },
}
gore> db := gcp.Database.Sql(diagram.NodeLabel("Database"))
&diagram.Node{
  id:      "ppavwvrb",
  conn:    nil,
  Options: diagram.NodeOptions{
    Name:          "node",
    Label:         "Database",
    Provider:      "gcp",
    Image:         "assets/gcp/database/sql.png",
    ImageScale:    true,
    Shape:         "none",
    Style:         "rounded",
    FixedSize:     true,
    Width:         1.400000,
    Height:        1.400000,
    LabelLocation: "b",
    Font:          diagram.Font{
      Name:  "Sans-Serif",
      Size:  13.000000,
      Color: "#2D3436",
    },
    Attributes: map[string]string{},
  },
}
gore> dc := diagram.NewGroup("GCP")
gore> dc.NewGroup("services").
.....     Label("Service Layer").
.....     Add(
.....             gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 1")),
.....             gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 2")),
.....             gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 3")),
.....     ).
.....     ConnectAllFrom(lb.ID(), diagram.Forward()).
.....     ConnectAllTo(cache.ID(), diagram.Forward())
gore> dc.NewGroup("data").Label("Data Layer").Add(cache, db).Connect(cache, db)
&diagram.Group{
  idx:     1,
  id:      "clusterdata",
  options: diagram.GroupOptions{
    Label:           "Data Layer",
    LabelJustify:    "l",
    Direction:       "LR",
    PenColor:        "#AEB6BE",
    BackgroundColor: "#EBF3E7",
    Shape:           "box",
    Style:           "rounded",
    Font:            diagram.Font{
      Name:  "Sans-Serif",
      Size:  12.000000,
      Color: "#2D3436",
    },
    Attributes: map[string]string{},
  },
  parent: &diagram.Group{
    idx:     0,
    id:      "cluster_GCP",
    options: diagram.GroupOptions{
      Label:           "",
      LabelJustify:    "l",
      Direction:       "LR",
      PenColor:        "#AEB6BE",
      BackgroundColor: "#E5F5FD",
      Shape:           "box",
      Style:           "rounded",
      Font:            diagram.Font{
        Name:  "Sans-Serif",
        Size:  12.000000,
        Color: "#2D3436",
      },
      Attributes: map[string]string{},
    },
    parent:   (*diagram.Group)(nil),
    children: map[string]*diagram.Group{
      "clusterdata":     &diagram.Group{...},
      "clusterservices": &diagram.Group{
        idx:     1,
        id:      "clusterservices",
        options: diagram.GroupOptions{
          Label:           "Service Layer",
          LabelJustify:    "l",
          Direction:       "LR",
          PenColor:        "#AEB6BE",
          BackgroundColor: "#EBF3E7",
          Shape:           "box",
          Style:           "rounded",
          Font:            diagram.Font{
            Name:  "Sans-Serif",
            Size:  12.000000,
            Color: "#2D3436",
          },
          Attributes: map[string]string{},
        },
        parent:   &diagram.Group{...},
        children: map[string]*diagram.Group{},
        nodes:    map[string]*diagram.Node{
          "fgseyadp": &diagram.Node{
            id:      "fgseyadp",
            conn:    nil,
            Options: diagram.NodeOptions{
              Name:          "node",
              Label:         "Server 2",
              Provider:      "gcp",
              Image:         "assets/gcp/compute/compute-engine.png",
              ImageScale:    true,
              Shape:         "none",
              Style:         "rounded",
              FixedSize:     true,
              Width:         1.400000,
              Height:        1.400000,
              LabelLocation: "b",
              Font:          diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Attributes: map[string]string{},
            },
          },
          "gdomwrod": &diagram.Node{
            id:      "gdomwrod",
            conn:    nil,
            Options: diagram.NodeOptions{
              Name:          "node",
              Label:         "Server 1",
              Provider:      "gcp",
              Image:         "assets/gcp/compute/compute-engine.png",
              ImageScale:    true,
              Shape:         "none",
              Style:         "rounded",
              FixedSize:     true,
              Width:         1.400000,
              Height:        1.400000,
              LabelLocation: "b",
              Font:          diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Attributes: map[string]string{},
            },
          },
          "pchcrvxb": &diagram.Node{
            id:      "pchcrvxb",
            conn:    nil,
            Options: diagram.NodeOptions{
              Name:          "node",
              Label:         "Server 3",
              Provider:      "gcp",
              Image:         "assets/gcp/compute/compute-engine.png",
              ImageScale:    true,
              Shape:         "none",
              Style:         "rounded",
              FixedSize:     true,
              Width:         1.400000,
              Height:        1.400000,
              LabelLocation: "b",
              Font:          diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Attributes: map[string]string{},
            },
          },
        },
        edges: map[string]*diagram.Edge{
          "17c2b59b-7622-4ab2-b620-93cf99a2a8cd": &diagram.Edge{
            id:      "17c2b59b-7622-4ab2-b620-93cf99a2a8cd",
            start:   "fgseyadp",
            end:     "suulghie",
            Options: diagram.EdgeOptions{
              Label:   "",
              Color:   "#7B8894",
              Forward: true,
              Reverse: false,
              Font:    diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Style:      "",
              Attributes: map[string]string{},
            },
          },
          "3ab44a27-d3f5-4592-966a-c70f7ffe7683": &diagram.Edge{
            id:      "3ab44a27-d3f5-4592-966a-c70f7ffe7683",
            start:   "qdtcfjis",
            end:     "pchcrvxb",
            Options: diagram.EdgeOptions{
              Label:   "",
              Color:   "#7B8894",
              Forward: true,
              Reverse: false,
              Font:    diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Style:      "",
              Attributes: map[string]string{},
            },
          },
          "a16e25f4-b19c-481d-887f-08b10274e52d": &diagram.Edge{
            id:      "a16e25f4-b19c-481d-887f-08b10274e52d",
            start:   "qdtcfjis",
            end:     "fgseyadp",
            Options: diagram.EdgeOptions{
              Label:   "",
              Color:   "#7B8894",
              Forward: true,
              Reverse: false,
              Font:    diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Style:      "",
              Attributes: map[string]string{},
            },
          },
          "b7e800f5-89d4-45bf-becf-1f6dd3ea72ad": &diagram.Edge{
            id:      "b7e800f5-89d4-45bf-becf-1f6dd3ea72ad",
            start:   "qdtcfjis",
            end:     "gdomwrod",
            Options: diagram.EdgeOptions{
              Label:   "",
              Color:   "#7B8894",
              Forward: true,
              Reverse: false,
              Font:    diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Style:      "",
              Attributes: map[string]string{},
            },
          },
          "e730ac98-afe0-461a-9b53-1116840a73ed": &diagram.Edge{
            id:      "e730ac98-afe0-461a-9b53-1116840a73ed",
            start:   "pchcrvxb",
            end:     "suulghie",
            Options: diagram.EdgeOptions{
              Label:   "",
              Color:   "#7B8894",
              Forward: true,
              Reverse: false,
              Font:    diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Style:      "",
              Attributes: map[string]string{},
            },
          },
          "ea6b185c-9a37-4eb3-81c4-78774490002b": &diagram.Edge{
            id:      "ea6b185c-9a37-4eb3-81c4-78774490002b",
            start:   "gdomwrod",
            end:     "suulghie",
            Options: diagram.EdgeOptions{
              Label:   "",
              Color:   "#7B8894",
              Forward: true,
              Reverse: false,
              Font:    diagram.Font{
                Name:  "Sans-Serif",
                Size:  13.000000,
                Color: "#2D3436",
              },
              Style:      "",
              Attributes: map[string]string{},
            },
          },
        },
      },
    },
    nodes: map[string]*diagram.Node{},
    edges: map[string]*diagram.Edge{},
  },
  children: map[string]*diagram.Group{},
  nodes:    map[string]*diagram.Node{
    "rxiawoke": &diagram.Node{
      id:      "rxiawoke",
      conn:    nil,
      Options: diagram.NodeOptions{
        Name:          "node",
        Label:         "Database",
        Provider:      "gcp",
        Image:         "assets/gcp/database/sql.png",
        ImageScale:    true,
        Shape:         "none",
        Style:         "rounded",
        FixedSize:     true,
        Width:         1.400000,
        Height:        1.400000,
        LabelLocation: "b",
        Font:          diagram.Font{
          Name:  "Sans-Serif",
          Size:  13.000000,
          Color: "#2D3436",
        },
        Attributes: map[string]string{},
      },
    },
    "suulghie": &diagram.Node{
      id:      "suulghie",
      conn:    nil,
      Options: diagram.NodeOptions{
        Name:          "node",
        Label:         "Cache",
        Provider:      "gcp",
        Image:         "assets/gcp/database/memorystore.png",
        ImageScale:    true,
        Shape:         "none",
        Style:         "rounded",
        FixedSize:     true,
        Width:         1.400000,
        Height:        1.400000,
        LabelLocation: "b",
        Font:          diagram.Font{
          Name:  "Sans-Serif",
          Size:  13.000000,
          Color: "#2D3436",
        },
        Attributes: map[string]string{},
      },
    },
  },
  edges: map[string]*diagram.Edge{
    "f6a61513-550e-4b7a-a194-a12641ae8c92": &diagram.Edge{
      id:      "f6a61513-550e-4b7a-a194-a12641ae8c92",
      start:   "suulghie",
      end:     "rxiawoke",
      Options: diagram.EdgeOptions{
        Label:   "",
        Color:   "#7B8894",
        Forward: true,
        Reverse: false,
        Font:    diagram.Font{
          Name:  "Sans-Serif",
          Size:  13.000000,
          Color: "#2D3436",
        },
        Style:      "",
        Attributes: map[string]string{},
      },
    },
  },
}
gore> 
gore> d.Connect(dns, lb, diagram.Forward()).Group(dc)
&diagram.Diagram{
  options: diagram.Options{
    Name:       "go-diagrams",
    FileName:   "app",
    OutFormat:  "dot",
    Direction:  "LR",
    CurveStyle: "ortho",
    Show:       true,
    Label:      "App",
    Pad:        2.000000,
    Splines:    "ortho",
    NodeSep:    0.600000,
    RankSep:    0.750000,
    Font:       diagram.Font{
      Name:  "Sans-Serif",
      Size:  13.000000,
      Color: "#2D3436",
    },
    Attributes: map[string]string{},
  },
  g: &gographviz.Escape{
    Graph: &gographviz.Graph{
      Attrs: gographviz.Attrs{
        "fontcolor": "\"#2D3436\"",
        "fontname":  "\"Sans-Serif\"",
        "fontsize":  "13",
        "label":     "App",
        "nodesep":   "0.6",
        "pad":       "2",
        "rankdir":   "LR",
        "ranksep":   "0.75",
        "splines":   "ortho",
      },
      Name:     "root",
      Directed: true,
      Strict:   false,
      Nodes:    &gographviz.Nodes{
        Lookup: map[string]*gographviz.Node{},
        Nodes:  []*gographviz.Node{},
      },
      Edges: &gographviz.Edges{
        SrcToDsts: map[string]map[string][]*gographviz.Edge{},
        DstToSrcs: map[string]map[string][]*gographviz.Edge{},
        Edges:     []*gographviz.Edge{},
      },
      SubGraphs: &gographviz.SubGraphs{
        SubGraphs: map[string]*gographviz.SubGraph{},
      },
      Relations: &gographviz.Relations{
        ParentToChildren: map[string]map[string]bool{},
        ChildToParents:   map[string]map[string]bool{},
      },
    },
  },
  root: &diagram.Group{
    idx:     0,
    id:      "root",
    options: diagram.GroupOptions{
      Label:           "",
      LabelJustify:    "l",
      Direction:       "LR",
      PenColor:        "#AEB6BE",
      BackgroundColor: "#E5F5FD",
      Shape:           "box",
      Style:           "rounded",
      Font:            diagram.Font{
        Name:  "Sans-Serif",
        Size:  12.000000,
        Color: "#2D3436",
      },
      Attributes: map[string]string{},
    },
    parent:   (*diagram.Group)(nil),
    children: map[string]*diagram.Group{
      "cluster_GCP": &diagram.Group{
        idx:     0,
        id:      "cluster_GCP",
        options: diagram.GroupOptions{
          Label:           "",
          LabelJustify:    "l",
          Direction:       "LR",
          PenColor:        "#AEB6BE",
          BackgroundColor: "#E5F5FD",
          Shape:           "box",
          Style:           "rounded",
          Font:            diagram.Font{
            Name:  "Sans-Serif",
            Size:  12.000000,
            Color: "#2D3436",
          },
          Attributes: map[string]string{},
        },
        parent:   &diagram.Group{...},
        children: map[string]*diagram.Group{
          "clusterdata": &diagram.Group{
            idx:     1,
            id:      "clusterdata",
            options: diagram.GroupOptions{
              Label:           "Data Layer",
              LabelJustify:    "l",
              Direction:       "LR",
              PenColor:        "#AEB6BE",
              BackgroundColor: "#EBF3E7",
              Shape:           "box",
              Style:           "rounded",
              Font:            diagram.Font{
                Name:  "Sans-Serif",
                Size:  12.000000,
                Color: "#2D3436",
              },
              Attributes: map[string]string{},
            },
            parent:   &diagram.Group{...},
            children: map[string]*diagram.Group{},
            nodes:    map[string]*diagram.Node{
              "eewpaexj": &diagram.Node{
                id:      "eewpaexj",
                conn:    nil,
                Options: diagram.NodeOptions{
                  Name:          "node",
                  Label:         "Database",
                  Provider:      "gcp",
                  Image:         "assets/gcp/database/sql.png",
                  ImageScale:    true,
                  Shape:         "none",
                  Style:         "rounded",
                  FixedSize:     true,
                  Width:         1.400000,
                  Height:        1.400000,
                  LabelLocation: "b",
                  Font:          diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Attributes: map[string]string{},
                },
              },
              "rfdtcxgu": &diagram.Node{
                id:      "rfdtcxgu",
                conn:    nil,
                Options: diagram.NodeOptions{
                  Name:          "node",
                  Label:         "Cache",
                  Provider:      "gcp",
                  Image:         "assets/gcp/database/memorystore.png",
                  ImageScale:    true,
                  Shape:         "none",
                  Style:         "rounded",
                  FixedSize:     true,
                  Width:         1.400000,
                  Height:        1.400000,
                  LabelLocation: "b",
                  Font:          diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Attributes: map[string]string{},
                },
              },
            },
            edges: map[string]*diagram.Edge{
              "d9aade97-e365-4fb9-a1c0-c6104f4c407b": &diagram.Edge{
                id:      "d9aade97-e365-4fb9-a1c0-c6104f4c407b",
                start:   "rfdtcxgu",
                end:     "eewpaexj",
                Options: diagram.EdgeOptions{
                  Label:   "",
                  Color:   "#7B8894",
                  Forward: true,
                  Reverse: false,
                  Font:    diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Style:      "",
                  Attributes: map[string]string{},
                },
              },
            },
          },
          "clusterservices": &diagram.Group{
            idx:     1,
            id:      "clusterservices",
            options: diagram.GroupOptions{
              Label:           "Service Layer",
              LabelJustify:    "l",
              Direction:       "LR",
              PenColor:        "#AEB6BE",
              BackgroundColor: "#EBF3E7",
              Shape:           "box",
              Style:           "rounded",
              Font:            diagram.Font{
                Name:  "Sans-Serif",
                Size:  12.000000,
                Color: "#2D3436",
              },
              Attributes: map[string]string{},
            },
            parent:   &diagram.Group{...},
            children: map[string]*diagram.Group{},
            nodes:    map[string]*diagram.Node{
              "bpntlzaw": &diagram.Node{
                id:      "bpntlzaw",
                conn:    nil,
                Options: diagram.NodeOptions{
                  Name:          "node",
                  Label:         "Server 3",
                  Provider:      "gcp",
                  Image:         "assets/gcp/compute/compute-engine.png",
                  ImageScale:    true,
                  Shape:         "none",
                  Style:         "rounded",
                  FixedSize:     true,
                  Width:         1.400000,
                  Height:        1.400000,
                  LabelLocation: "b",
                  Font:          diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Attributes: map[string]string{},
                },
              },
              "hkgcedxq": &diagram.Node{
                id:      "hkgcedxq",
                conn:    nil,
                Options: diagram.NodeOptions{
                  Name:          "node",
                  Label:         "Server 1",
                  Provider:      "gcp",
                  Image:         "assets/gcp/compute/compute-engine.png",
                  ImageScale:    true,
                  Shape:         "none",
                  Style:         "rounded",
                  FixedSize:     true,
                  Width:         1.400000,
                  Height:        1.400000,
                  LabelLocation: "b",
                  Font:          diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Attributes: map[string]string{},
                },
              },
              "petffgqe": &diagram.Node{
                id:      "petffgqe",
                conn:    nil,
                Options: diagram.NodeOptions{
                  Name:          "node",
                  Label:         "Server 2",
                  Provider:      "gcp",
                  Image:         "assets/gcp/compute/compute-engine.png",
                  ImageScale:    true,
                  Shape:         "none",
                  Style:         "rounded",
                  FixedSize:     true,
                  Width:         1.400000,
                  Height:        1.400000,
                  LabelLocation: "b",
                  Font:          diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Attributes: map[string]string{},
                },
              },
            },
            edges: map[string]*diagram.Edge{
              "0709661b-26b4-42aa-8482-10280715e1f8": &diagram.Edge{
                id:      "0709661b-26b4-42aa-8482-10280715e1f8",
                start:   "bdihtenf",
                end:     "bpntlzaw",
                Options: diagram.EdgeOptions{
                  Label:   "",
                  Color:   "#7B8894",
                  Forward: true,
                  Reverse: false,
                  Font:    diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Style:      "",
                  Attributes: map[string]string{},
                },
              },
              "0e3b8ebd-f1c8-4c6f-aa2f-d95e89418f3a": &diagram.Edge{
                id:      "0e3b8ebd-f1c8-4c6f-aa2f-d95e89418f3a",
                start:   "bdihtenf",
                end:     "hkgcedxq",
                Options: diagram.EdgeOptions{
                  Label:   "",
                  Color:   "#7B8894",
                  Forward: true,
                  Reverse: false,
                  Font:    diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Style:      "",
                  Attributes: map[string]string{},
                },
              },
              "74a46187-4972-40bc-b184-177990c7cf0d": &diagram.Edge{
                id:      "74a46187-4972-40bc-b184-177990c7cf0d",
                start:   "petffgqe",
                end:     "rfdtcxgu",
                Options: diagram.EdgeOptions{
                  Label:   "",
                  Color:   "#7B8894",
                  Forward: true,
                  Reverse: false,
                  Font:    diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Style:      "",
                  Attributes: map[string]string{},
                },
              },
              "91c15587-5d5a-4996-af52-6924bc782595": &diagram.Edge{
                id:      "91c15587-5d5a-4996-af52-6924bc782595",
                start:   "bpntlzaw",
                end:     "rfdtcxgu",
                Options: diagram.EdgeOptions{
                  Label:   "",
                  Color:   "#7B8894",
                  Forward: true,
                  Reverse: false,
                  Font:    diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Style:      "",
                  Attributes: map[string]string{},
                },
              },
              "9ed1caf8-b9a7-4811-84a4-a665b2e97ad3": &diagram.Edge{
                id:      "9ed1caf8-b9a7-4811-84a4-a665b2e97ad3",
                start:   "bdihtenf",
                end:     "petffgqe",
                Options: diagram.EdgeOptions{
                  Label:   "",
                  Color:   "#7B8894",
                  Forward: true,
                  Reverse: false,
                  Font:    diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Style:      "",
                  Attributes: map[string]string{},
                },
              },
              "dd4d3037-a0d7-4a4e-b793-2571aa6fe3c3": &diagram.Edge{
                id:      "dd4d3037-a0d7-4a4e-b793-2571aa6fe3c3",
                start:   "hkgcedxq",
                end:     "rfdtcxgu",
                Options: diagram.EdgeOptions{
                  Label:   "",
                  Color:   "#7B8894",
                  Forward: true,
                  Reverse: false,
                  Font:    diagram.Font{
                    Name:  "Sans-Serif",
                    Size:  13.000000,
                    Color: "#2D3436",
                  },
                  Style:      "",
                  Attributes: map[string]string{},
                },
              },
            },
          },
        },
        nodes: map[string]*diagram.Node{},
        edges: map[string]*diagram.Edge{},
      },
    },
    nodes: map[string]*diagram.Node{
      "bdihtenf": &diagram.Node{
        id:      "bdihtenf",
        conn:    nil,
        Options: diagram.NodeOptions{
          Name:          "node",
          Label:         "NLB",
          Provider:      "gcp",
          Image:         "assets/gcp/network/load-balancing.png",
          ImageScale:    true,
          Shape:         "none",
          Style:         "rounded",
          FixedSize:     true,
          Width:         1.400000,
          Height:        1.400000,
          LabelLocation: "b",
          Font:          diagram.Font{
            Name:  "Sans-Serif",
            Size:  13.000000,
            Color: "#2D3436",
          },
          Attributes: map[string]string{},
        },
      },
      "zttncbzx": &diagram.Node{
        id:      "zttncbzx",
        conn:    nil,
        Options: diagram.NodeOptions{
          Name:          "node",
          Label:         "DNS",
          Provider:      "gcp",
          Image:         "assets/gcp/network/dns.png",
          ImageScale:    true,
          Shape:         "none",
          Style:         "rounded",
          FixedSize:     true,
          Width:         1.400000,
          Height:        1.400000,
          LabelLocation: "b",
          Font:          diagram.Font{
            Name:  "Sans-Serif",
            Size:  13.000000,
            Color: "#2D3436",
          },
          Attributes: map[string]string{},
        },
      },
    },
    edges: map[string]*diagram.Edge{
      "c5c381c8-5d61-4958-b828-d79f8831cbd8": &diagram.Edge{
        id:      "c5c381c8-5d61-4958-b828-d79f8831cbd8",
        start:   "zttncbzx",
        end:     "bdihtenf",
        Options: diagram.EdgeOptions{
          Label:   "",
          Color:   "#7B8894",
          Forward: true,
          Reverse: false,
          Font:    diagram.Font{
            Name:  "Sans-Serif",
            Size:  13.000000,
            Color: "#2D3436",
          },
          Style:      "",
          Attributes: map[string]string{},
        },
      },
    },
  },
}
gore> 
gore> if err := d.Render(); err != nil {
.....         log.Fatal(err)
..... }
gore> 
gore> :print
package main

import (
    "log"

    "github.com/blushft/go-diagrams/diagram"
    "github.com/blushft/go-diagrams/nodes/gcp"
    "github.com/k0kubun/pp/v3"
)

func __gore_p(xs ...any) {
    for _, x := range xs {
        pp.Println(x)
    }
}
func main() {
    d, err := diagram.New(diagram.Filename("app"), diagram.Label("App"), diagram.Direction("LR"))
    if err != nil {
        log.Fatal(err)
    }
    dns := gcp.Network.Dns(diagram.NodeLabel("DNS"))
    lb := gcp.Network.LoadBalancing(diagram.NodeLabel("NLB"))
    cache := gcp.Database.Memorystore(diagram.NodeLabel("Cache"))
    db := gcp.Database.Sql(diagram.NodeLabel("Database"))
    dc := diagram.NewGroup("GCP")
    _ = dc.NewGroup("services").Label("Service Layer").Add(gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 1")), gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 2")), gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 3"))).ConnectAllFrom(lb.ID(), diagram.Forward()).ConnectAllTo(cache.ID(), diagram.Forward())
    _ = dc.NewGroup("data").Label("Data Layer").Add(cache, db).Connect(cache, db)
    _ = d.Connect(dns, lb, diagram.Forward()).Group(dc)
    if err := d.Render(); err != nil {
        log.Fatal(err)
    }
}
gore> :quit
```
- 把 `gore` `:print` 的結果，複製到 `example.go` 略做微調後，用 `go run example.go` 執行看看。
```bash
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ go run example.go 
2024/12/02 20:23:34 mkdir go-diagrams: file exists
exit status 1
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ rm -rf go-diagrams/
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ go run example.go 
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ tree go-diagrams/
go-diagrams/
├── app.dot
└── assets
    └── gcp
        ├── compute
        │   └── compute-engine.png
        ├── database
        │   ├── memorystore.png
        │   └── sql.png
        └── network
            ├── dns.png
            └── load-balancing.png

5 directories, 6 files
```
- 所以看起來是會產生 graphviz 的 `app.dot` 檔案，要用指令再產生 PNG 格式。
```bash
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ dpkg -S $(which dot)
graphviz: /usr/bin/dot
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ dot -Tpng go-diagrams/app.dot > app.png
Warning: No such file or directory while opening assets/gcp/network/dns.png
Warning: No or improper image="assets/gcp/network/dns.png" for node "mogkyyrd"
Warning: No such file or directory while opening assets/gcp/network/load-balancing.png
Warning: No or improper image="assets/gcp/network/load-balancing.png" for node "hbswhzeu"
Warning: No such file or directory while opening assets/gcp/compute/compute-engine.png
Warning: No or improper image="assets/gcp/compute/compute-engine.png" for node "nlvgtohh"
Warning: No such file or directory while opening assets/gcp/compute/compute-engine.png
Warning: No or improper image="assets/gcp/compute/compute-engine.png" for node "tsqexfmj"
Warning: No such file or directory while opening assets/gcp/compute/compute-engine.png
Warning: No or improper image="assets/gcp/compute/compute-engine.png" for node "njqakknn"
Warning: No such file or directory while opening assets/gcp/database/memorystore.png
Warning: No or improper image="assets/gcp/database/memorystore.png" for node "jibpxsod"
Warning: No such file or directory while opening assets/gcp/database/sql.png
Warning: No or improper image="assets/gcp/database/sql.png" for node "bbjehdvc"
@jazzwang ➜ /workspaces/snippet/go/go-diagrams (master) $ cd go-diagrams/
@jazzwang ➜ .../snippet/go/go-diagrams/go-diagrams (master) $ dot -Tpng app.dot > app.png
@jazzwang ➜ .../snippet/go/go-diagrams/go-diagrams (master) $ code app.png 
```