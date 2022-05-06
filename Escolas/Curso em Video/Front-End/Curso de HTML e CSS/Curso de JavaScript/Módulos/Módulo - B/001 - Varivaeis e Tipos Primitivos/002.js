var n1 = 1837.7
console.log(n1.toFixed(2).replace('.', ','))    //Formatando para duas casa decimais e trocando '.' por ','
console.log(n1.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'}))   //Formatando para formato em R$