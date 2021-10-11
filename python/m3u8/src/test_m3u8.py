#!/usr/bin/python

## https://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys, getopt
import m3u8

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

def check_url(url):
  playlist = m3u8.load(uri=url, headers=headers)
  print(playlist.data)

def main(argv):
  url = ''
  output = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:")
  except getopt.GetoptError:
    print(sys.argv[0] + ' -i <m3u8_url> -o <m3u8_file>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print(sys.argv[0] + ' -i <m3u8_url> -o <m3u8_file>')
      sys.exit()
    elif opt in ("-i"):
      url = arg
    elif opt in ("-o"):
      output = arg
  check_url(url)

if __name__ == "__main__":
   main(sys.argv[1:])