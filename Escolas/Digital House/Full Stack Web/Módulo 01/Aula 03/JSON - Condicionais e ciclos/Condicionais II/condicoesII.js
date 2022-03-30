//          If ternario
let dia = "Quarta"; //Definindo a váriavel dia como domingo
let resultado = dia == "Domingo" ? "Hoje é domingo":"Hoje não é domingo! Estamos na " + dia;
//  Váriavel   |    Condição    |       true                false
console.log(resultado)


//          SWITCH
switch (dia) { //Definimos que para fazer a analise de condição, iremos verificar a variavel dia
    case "Segunda": //Caso o dia for igual segunda (dia == "Segunda")
        console.log("Dia de ir à faculdade!"); //o valor retornado será esse
        break; //e logo após irá interromper o caso
    case "Terça":
        console.log("Dia de ir ao cinema");
        break;
    case "Quarta":
        console.log("Dia de assistir ao jogo de futeboll");
        break;
    case "Quinta":
        console.log("Dia de resolver os trabalhos da faculdade")
        break;
    case "Sexta":
        console.log("Dia de ir à academia");
        break;
    case "Sabado":
        console.log("Dia de ir na casa da tia");
        break;
    case "Domingo":
        console.log("Dia de descançar e ligar pra familía!")
        break
}