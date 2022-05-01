function formataMensagem(textoEntrada){
    if (textoEntrada == undefined)
        return '...';
    
        let data = new Date();
    
        let hora = data.getHours();
        let min = data.getMinutes();
        let sec = data.getSeconds();

        let textoSaida = (hora + ':' + min + ' - ' + textoEntrada)

        return textoSaida
}

console.log(formataMensagem('Um texto qualquer'))
console.log(formataMensagem())
console.log(formataMensagem('Outr texto qualquer'))