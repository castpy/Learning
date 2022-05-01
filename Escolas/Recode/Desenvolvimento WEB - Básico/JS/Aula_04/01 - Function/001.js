let dataHoraAtual = new Date();
    console.log(dataHoraAtual)

function dataHoraAgora(){
    let data = new Date();
    
    let hora = data.getHours();
    let min = data.getMinutes();
    let sec = data.getSeconds();

    let horaFormatada = hora + ':' + min + ":" + sec;
    console.log(horaFormatada);
}

while (true){
    dataHoraAgora();
}