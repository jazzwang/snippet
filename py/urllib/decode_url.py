# coding: utf-8
import argparse
from urllib.parse import unquote

def decode_url(enc_url: str):
    return unquote(enc_url)

sample_url = "https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e585277-7fe3-4cd4-b257-f14edbbb4fc7_1280x1664.gif"

def main():
    # parsing CLI arguments
    parser = argparse.ArgumentParser(description="Decode URL")
    parser.add_argument("enc_url", help="encoded url")
    args = parser.parse_args()

    enc_url = args.enc_url
    dec_url = decode_url(enc_url)

    print(f"encoded url: {enc_url}")
    print(f"decoded url: {dec_url}")

if __name__ == "__main__":
    main()