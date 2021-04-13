#!/bin/bash
sbt 'run -i nyc-tlc/yellow_v1 -o out/schema=1 -v 1'
sbt 'run -i nyc-tlc/yellow_v2 -o out/schema=2 -v 2'
sbt 'run -i nyc-tlc/yellow_v3 -o out/schema=3 -v 3'
sbt 'run -i nyc-tlc/yellow_v4 -o out/schema=4 -v 4'
sbt 'run -i nyc-tlc/yellow_v5 -o out/schema=5 -v 5'
