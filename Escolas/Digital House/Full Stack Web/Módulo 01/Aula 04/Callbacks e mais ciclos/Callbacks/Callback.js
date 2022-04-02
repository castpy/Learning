//const somar = (numeroA, numeroB) => numeroA + numeroB; 
//Criamos uma função que recebe dois numeros como parametro, essa função é usada para somar.

//const calculadora = (numeroA, numeroB, operacao) => operacao (numeroA, numeroB); 
//Criamos uma função para calcular esses valores! Como parametro, a função calcular recebe o valor A e B que definimos em "somar", e em seguida ela recebe como parametro o nome da função que herdou os valores A e B. Em seguida a função "operação" é executada já com os parametros.

//console.log(calculadora(10, 20, somar)) 
//Aqui executamos a função "calculadora" definindo seus paramentros como: numeroA = 10, numeroB = 20 e chamamos a função "somar".



//Funções filho
const somar = (numeroA, numeroB) => numeroA + numeroB;
const subtrair = (numeroA, numeroB) => numeroA - numeroB;
const multiplicar = (numeroA, numeroB) => numeroA * numeroB;
//===========================================================

//Funções Pai
const calculadora = (numeroA, numeroB, operacao) => operacao(numeroA, numeroB);
console.log(calculadora(15, 40, somar)) //aqui você pode mudar o terceiro paramentro por qualquer função filho