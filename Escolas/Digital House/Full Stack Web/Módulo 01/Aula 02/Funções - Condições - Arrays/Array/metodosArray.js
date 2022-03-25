let giriasParaene = [
    "Égua",
    "Dirrocha",
    "Mais ulha",
    "Me rouba logo",
];

console.log(giriasParaene); //Chamando o array e o objeto 1 - "Dirrocha".
giriasParaene.push("Laricado"); //Adiciona o objeto "Laricado" ao final do array.
giriasParaene.pop(); //Remove o ultimo objeto do array "Laricado".
giriasParaene.shift(); //Remove o primeiro objeto do array "Égua".
giriasParaene.unshift("Ispia", "O cavalo mordeu tua cabeça?"); //Adiciona 1 ou mais objetos ao final do array.
giriasParaene.indexOf("Égua") //Procura dentro do array, pela string que foi passada como parametro.
giriasParaene.lastIndexOf("Égua") //Procura dentro do array, pela string que foi passada como parametro, porem do final para o inicio
let join = giriasParaene.join(" - ") //Junta todos os elementos do array em uma unica string e os separa com o valor passado como parametro
console.log(giriasParaene);
console.log(join)