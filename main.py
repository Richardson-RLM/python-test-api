from flask import Flask, jsonify
from service.cpf_service import load_blacklist, verify_cpf

app = Flask(__name__)

blacklist = load_blacklist()

@app.route('/<cpf>', methods=['GET'])
def verify_cpf_route(cpf):
    status = verify_cpf(cpf, blacklist)
    return jsonify({"status": status})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)