import os, sys

def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "read":
        print(read_file(sys.argv[2]))
