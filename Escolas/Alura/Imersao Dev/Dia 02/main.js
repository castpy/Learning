function Converter(){
    var valorElemento = document.getElementById("valor");
    var valor = valorElemento.value;
    var valorDolarNumerico = parseFloat(valor);
    var soma = valorDolarNumerico * 5.6
    
    var valorElemento = document.getElementById("valorConvertido");
    var valorConvertido = "O resultado em real é R$ " + soma; 
    valorElemento.innerHTML = valorConvertido;
}