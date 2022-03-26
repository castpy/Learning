let meuPais = {
    nome: "Brasil",
    populacao: 2329873,
    capital: "Brasilia",
    maiorCidade: "São Paulo",

    nacionalidade:function(){
        return "Brasileiro"
    }
}
console.log("O meu país se chama " + meuPais.nome + ", ele tem uma população de " + meuPais.populacao + ", sua capital é " + meuPais.capital + " e a maior cidade se chama " + meuPais.maiorCidade);
console.log("No " + meuPais.nome + " a nacionalidade de cada cidadão é " + meuPais.nacionalidade())

function Carro (nomeCarro, anoCarro) {
    this.nome = nomeCarro;
    this.ano = anoCarro;
}

let civic = new Carro("Civic", "2019");
console.log(civic)