//Atibuindo valor inteiro
let x = 2;

//Atibuindo valor Real
let y = 2.5;

//Atribuindo uma string
let nome = 'Marcus';

//atribuindo valor boleano
let binario = false;

//Perceba que no código  acima ocorrem algumas atribuições básicas, o que possibilita o armazenamento dos valores em suas variáveis. Até aqui, nada novo. Porém, podemos fazer mais do que isso com os operadores de atribuição, realizando um atalho para algumas operações matemáticas: adição, subtração. multiplicação e divisão.

//Atribuição de Adição
let a1 = 2;
let a2 = 5;
//Operação 1
a1 = a1 + a2;
//Operação 2
a1 += a2;


//Atribuição de Subtração
let b1 = 5;
let b2 = 2;
//Operação 1
b1 = b1 - b2;
//Operação 2
b1 -= b2;


//Atribuição de Multiplicação
let c1 = 7;
let c2 = 2;
//Operação 1
c1 = c1 * c2;
//Operação 2
c1 *= c2;


//Atribuição de Multiplicação
let d1 = 10;
let d2 = 2;
//Operação 1
d1 = d1 / d2;
//Operação 2
d1 /= d2;


//Incremento
let contador = 0;
contador += 1; //O valor é 1
contador += 1; //O valor é 2
contador += 1; //O valor é 3
//Ou pode ser feito usando ++
contador ++; //O valor é 1
contador ++; //O valor é 2
contador ++; //O valor é 3

//Decremento
let tentativas = 3;
tentativas --; //Numero de tentativas: 2
tentativas --; //Numero de tentativas: 1
tentativas --; //Numero de tentativas: 0


//Pré e Pós incremento/Decremento
let contador02 = 10;
console.log(contador02++)//exibe o valor 10
console.log(++contador)//exibe o valor 12


//OPERADORES    DE      COMPARAÇÃO

//Igual             ==
//Identico          ===     Nesse caso, comparamos não só seus valores, mas também seus tipos. 
//Diferente         !=      Comparações com o operador não igual só retornam true se os valores comparados forem diferentes.

//Super diferente   !==     Caso seja estritamente não igual, ou seja, se não for idêntico retorna true, caso seja idêntico retorna false.

//Maior que         >       Se o valor da esquerda for maior do que o da direita, o retorno é true.
//Maior ou igual    >=      Se o valor da esquerda for maior do que ou igual ao da direita, o retorno é true.
//Menor que         <       Se o valor da esquerda for menor que o da direita, o retorno é true. 
//Menor ou igual    <=      Se o valor da esquerda for menor que ou igual ao da direita, o retorno é true.


//OPERADORES    LÓGICOS

//and(e)            &&
//or(ou)            ||
//not(negação)      !

// AND
let escolha01 = 15; //Primeira escolha do usuario
console.log(escolha01 >= 10 && escolha01 <=20); //Retorna TRUE

escolha01 = 23; //Segunda escolha do usuario
console.log(escolha01 >=10 && escolha01 <=20); //Retorna FALSE