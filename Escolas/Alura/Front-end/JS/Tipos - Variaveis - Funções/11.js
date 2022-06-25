function MensagemBomDia () {
	console.log('Bom dia');
};

MensagemBomDia()

function MensagemBomDia02 (Texto) {
	console.log(Texto);
};

MensagemBomDia02('Bom dia')


const soma = function (num1, num2) {return num1 + num2}
console.log(soma(2, 2))


const subtracao = (n1, n2) => n1 - n2;
console.log(subtracao(2, 2))


const comparaNumero = (numero1, numero2) => {
	if (numero1 >= 10 && numero2 >= 10) {
        return `Somente numeros menores que 10 são aceitos!`;
    }else{
        return `Os números ${numero1} e ${numero2} são aceitos!`
    }
}

console.log(comparaNumero(10, 10))