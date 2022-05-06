var n1 = 5
var n2 = 5
var soma01 = (Number(n2) + Number(n2)) / 2
console.log(soma01)


//Auto-atribuição
var n = 3
n = n * 3
// n *= 3
console.log(n)

//Operadores relacionais
var numero1 = 4
var numero2 = 4
console.log(numero1 > numero2) //Resultado: False
console.log(numero1 < numero2) //Resultado: False
console.log(numero1 >= numero2)//Resultado: True
console.log(numero1 <= numero2)//Resultado: True
console.log(numero1 == numero2)//Resultado: True
console.log(numero1 != numero2)//Resultado: False

//Operadores de Identidade
console.log(`${numero1} == '4' -> A penas o valor é verificado. TRUE`)
console.log(`${numero1} === '4' -> O valor e o tipo é verificado. FALSE`)