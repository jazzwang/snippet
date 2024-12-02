#!/usr/bin/python

## https://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys, getopt
import m3u8
import requests
from Crypto.Cipher import AES


# url='https://d3c7rimkq79yfu.cloudfront.net/12638/1/v1/480/12638-eps-1_480p.m3u8'


print(playlist.keys[0])
print(playlist.keys[0].uri
)
print(playlist.keys[0].iv)
print(playlist.keys[0].method)
iv=playlist.keys[0].iv
key=playlist.lyes[0].uri
key=playlist.keys[0].uri
key
key = requests.get(playlist.keys[-1].uri, headers=headers).content
enumerate(playlist.segments, 1)
a = enumerate(playlist.segments, 1)
a
a[0]
playlist.segments
playlist.segments[0]
playlist.segments[0]
print(playlist.segments[0])
print(playlist.segments[0].absolute_uri)
data = requests.get(playlist.segments[0].absolute_uri, headers=headers).content

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

def download_video(url, output):
  playlist = m3u8.load(uri=url, headers=headers)
  key = requests.get(playlist.keys[-1].uri, headers=headers).content
  for i in range(len(playlist.segments)):
    data = requests.get(playlist.segments[i].absolute_uri, headers=headers).content

def main(argv):
  url = ''
  output = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:")
  except getopt.GetoptError:
    print(sys.argv[0] + ' -i <m3u8_url> -o <output_video_file>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print(sys.argv[0] + ' -i <m3u8_url> -o <output_video_file>')
      sys.exit()
    elif opt in ("-i"):
      url = arg
    elif opt in ("-o"):
      output = arg
  download_video(url, output)

if __name__ == "__main__":
   main(sys.argv[1:])