import requests
import json

def consultar_cep(cep, numero_casa):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        data = json.loads(response.text)

        if 'erro' not in data:
            endereco_completo = data.get("logradouro", "")
            if numero_casa:
                endereco_completo += f", {numero_casa}"
            if 'bairro' in data:
                endereco_completo += f", {data['bairro']}"
            if 'localidade' in data:
                endereco_completo += f", {data['localidade']}"

            data["endereco_completo"] = endereco_completo
            return data
        else:
            return None
    except Exception as e:
        return None
