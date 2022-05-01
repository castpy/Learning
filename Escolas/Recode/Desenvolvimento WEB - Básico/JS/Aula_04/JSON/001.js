let objetoJSON = {
    "Nome":"Marcus Castilho",
    "endereco": {
        "cep": "587520-000",
        "bairro":"centro",
    },
    
    "contato": {
        "email": "contato@castilho.com"
    }
}

console.log(objetoJSON.Nome + ' ' + objetoJSON.endereco.bairro)