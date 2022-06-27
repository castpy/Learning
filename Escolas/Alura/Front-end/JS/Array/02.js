//.push

let notas = [5, 6.7, 8.5]
notas.push(10)
let média = (notas[0] + notas[1] + notas[2] + notas[3]) / notas.length
console.log(média.toFixed(1))

//.pop

let notas2 = [5, 6.7, 8.5, 10]
notas2.pop()
console.log(notas2)

//.slice

const nomes = ['Marcus', 'Castilho', 'Mateus', 'Henrrique', 'João', 'Carlos']
const grupoA = nomes.slice(0, nomes.length/2)
const grupoB = nomes.slice(nomes.length/2)
console.log(`Na turma atual, temos dois grupos! Grupo A: ${grupoA} e Grupo B: ${grupoB}`)


//
