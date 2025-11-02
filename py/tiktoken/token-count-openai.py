#!/usr/bin/env python3
# coding: utf-8

import tiktoken
import argparse

def token_count_openai(file_path, model_name="gpt-4"):
    """Counts tokens in a file using the tiktoken library."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Get the appropriate encoding for the model
        encoding = tiktoken.encoding_for_model(model_name)

        # Encode the text and count the number of resulting tokens
        tokens = encoding.encode(text)
        return len(tokens)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # parsing CLI arguments
    parser = argparse.ArgumentParser(description="Counts tokens in a file using the tiktoken library.")
    parser.add_argument("file_path", help="file path.")

    args = parser.parse_args()
    file_path = args.file_path
    
    token_count = token_count_openai(file_path)
    print(f"Token count for GPT-4: {token_count}")

if __name__ == "__main__":
    main()