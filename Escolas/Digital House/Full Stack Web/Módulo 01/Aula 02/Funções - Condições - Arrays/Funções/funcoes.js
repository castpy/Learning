//numero global
let numero = 32

//modo declarativo
function somar(a, b){
    console.log(numero)
    //código
    console.log('Estou somando....')
    return a + b
}

//modo expressão
const multiplicar = function(a, b){
    //código
    console.log("Estou multiplicando...")
    return a * b
}

//chamando a função
let resultadoSoma = somar(1, 2);
let resultadoMultiplicar = multiplicar(1, 10);

console.log(resultadoSoma)
console.log(resultadoMultiplicar)