import os
from flask import Flask, request, jsonify

directory_path = "code_blocks"

def load_code_blocks_from_directory(directory_path):
    """
    Load all Python code blocks from a given directory and its subdirectories.
    
    Args:
    - directory_path (str): Path to the directory containing code blocks.
    
    Returns:
    - dict: A dictionary with filenames (without extension) as keys and code content as values.
    """
    code_blocks = {}

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), 'r') as f:
                    # Use the filename (without extension) as the key
                    key = os.path.splitext(file)[0]
                    code_blocks[key] = f.read()

    return code_blocks

app = Flask(__name__)
@app.route('/blender_code', methods=['GET'])
def get_code():
    command = request.args.get('command')
    if command == "all":        
        code_blocks = load_code_blocks_from_directory(directory_path)        
        code = ""
        for key, value in code_blocks.items():
            code += value
    else:
        return jsonify({"error": "Unknown command"}), 400

    return jsonify({"code": code})


if __name__ == '__main__':
    app.run(debug=True, port=6001)
