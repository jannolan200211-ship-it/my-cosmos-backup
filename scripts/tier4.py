#!/usr/bin/env python3
import sys
import requests
import json

def call_tier4(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "qwen-opt",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=data)
        return response.json().get("response", "Error: No response")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tier4 <prompt>")
        sys.exit(1)
    print(call_tier4(sys.argv[1]))
