let frutas = ['Maçã', 'Banana', 'Açaí'];
console.log(frutas);
console.log(frutas[0]);
console.log(frutas[1]);
console.log(frutas[2]); //Veja que cada objeto tem um indice dentro do array

//Métodos do Array
let pessoas = [];

//.push()
//pessoas.push('Marcus', 'Caio')
pessoas.push('Marcus'); //Foi adicionado ao array e seu indice é 0
pessoas.push('Caio'); //Foi adicionado ao array e seu indice é 1
console.log(pessoas) //Dessa forma mostramos o array completo
console.log(pessoas[1]) //Dessa forma mostramos apenas "Caio"

//.pop()
let cidade = ['São Paulo', 'Rio de Janeiro', 'Curitiba']
cidade.pop() //Remove o ultimo elemento do Array, no caso, Curitiba.
