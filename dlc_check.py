import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para obter a lista de pastas (DLCs) no diretório
def get_valid_dlcs():
    dlc_directory = os.path.dirname(os.path.abspath(__file__))  # Diretório do script
    dlcs = [folder for folder in os.listdir(dlc_directory) if os.path.isdir(os.path.join(dlc_directory, folder))]
    return dlcs

@app.route('/check_dlc', methods=['GET'])
def check_dlc():
    dlc_name = request.args.get('dlc')
    valid_dlcs = get_valid_dlcs()  # Obtém a lista atual de DLCs do diretório

    # Verifica se a DLC está na lista de DLCs válidas
    if dlc_name in valid_dlcs:
        return jsonify({"exists": True})
    else:
        return jsonify({"exists": False})

if __name__ == '__main__':
    app.run(debug=True)
