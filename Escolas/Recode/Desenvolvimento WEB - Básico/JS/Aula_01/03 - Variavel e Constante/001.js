function exibeMensagem(){
    var escopoDaFuncao = 'Mensagem fora do IF';
        if (true){
            var escopoDoIf = '"Mensagem do IF"'; //isso deve aparecer só dentro do IF
        }
        alert(escopoDaFuncao);
        alert('A mensagem ' + escopoDoIf + ' Não poderia aparecer, pois representa uma falha de segurança e que deveria ser acessada apenas dentro do IF e não fora do seu escopo');
};

function exibeMensagemLet(){
    var escopoDaFuncao = 'Mensagem fora do IF';
    if (true){
        let escopoDoIf = '"Mensagem do IF"'; //isso deve aparecer só dentro do IF
    }
    alert(escopoDaFuncao);
    alert('A váriavel "escopoDoIf" não será exibida pois foi criada com LET e o problema de segurança de escopo foi resolvido.');
};

function exibeMensagemConst(){
    const tempo = {"hora": 60, "dia": 10, "minuto": 1005};
    alert("A hora é " + tempo.hora);
    let opcao = prompt('Hora')
    alert('A hora antiga era ' + tempo.hora + ' e você alterou para ' + opcao)
};