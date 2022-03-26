let jord = {
    nome: "Gay",
    idade : 45,
    endereco : "Na casa do caralho"
}

let json01 = JSON.stringify(jord);
console.log(json01)

let json02 = JSON.parse(json01) //transformando texto em lista json 
console.log(json02.nome) //acessando atraves de módulos 