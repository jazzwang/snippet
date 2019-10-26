#!/usr/bin/env python3

## Reference
## [1] https://webwebpage.github.io/docs/examples/display_from_edge_list.html

from webweb import Web

# make a list of unweighted edges
# (nodes can be numbers or strings)
edge_list = [[0, 1], [1, 2], [2, 3]]

# create the web
web = Web(edge_list)

# show the visualization
web.show()