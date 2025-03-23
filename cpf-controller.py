import re
from flask import Flask, jsonify

app = Flask(__name__)

def clean_cpf(cpf):
    return re.sub(r'\D', '', cpf)  


def load_blacklist():
    try:
        with open("blacklist.txt", "r") as file:
            return set(clean_cpf(line.strip()) for line in file)
    except FileNotFoundError:
        return set()

blacklist = load_blacklist()

@app.route('/<cpf>', methods=['GET'])
def verify_cpf(cpf):
    cpf = clean_cpf(cpf) 
    status = "BLOCK" if cpf in blacklist else "FREE"
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)