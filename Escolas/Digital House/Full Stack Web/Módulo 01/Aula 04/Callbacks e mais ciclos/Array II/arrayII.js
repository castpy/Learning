//Usando .map();
let numeros = [2, 4, 6];
//Criamos um array

const dobroDoNumero = numeros.map(function(numeroQualquer){
    return numeroQualquer * 2;
});
//Criamso uma função que recebe a variavel "numero" com o método "".map();" e nele passamos uma variavel qualquer como parametro.
//Então criamos o nosso bloco de código, nesse caso criamos um retorno do valor multiplicado

console.log(dobroDoNumero);
//E imprimimos no console o valor que está guardado dentro da função "dobroDoNumero", nesse caso, um array com os novos valores multiplicados!
//==========================================================================================================================

//Usando .filter();
let numero02 = [10, 15, 20, 30];

const filtro = numero02.filter(function(umNumero){
    return umNumero >= 18;
});

console.log(filtro)
//==========================================================================================================================

//usando .reducer();
let numero03 = [10, 20, 30];

const reduzindo = numero03.reduce(function(acumulado, acumulador){
    return acumulado + acumulador
});

console.log(reduzindo)
//==========================================================================================================================

//usando .forEatch();
let paises = ["Brasil", "Argentina", "Colombia"]

paises.forEach(function(umpais){
    console.log(umpais)
});