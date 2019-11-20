#!env python
# -*- coding: utf-8 -*-

import feedparser
d = feedparser.parse('https://confluence.atlassian.com/activity?streams=user+IS+dvdsmpsn')
type(d)
print("------ Feed Dict Keys----")
d.keys()
type(d['entries'])
d['entries'][0]
type(d['entries'][0])
d['entries'][0].keys()
d['entries'][0]['id']
d['entries'][0]['guidislink']
d['entries'][0]['link']
d['entries'][0]['title']
d['entries'][0]['summary']
d['entries'][0]['authors']
d['entries'][0]['author_detail']
d['entries'][0]['author']
d['entries'][0]['links']