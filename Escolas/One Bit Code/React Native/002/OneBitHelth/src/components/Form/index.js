import React, {useState} from "react";
import {View, Text, TextInput, Button} from "react-native"
import ResultImc from "./ResultImc";

export default function Form(){

    const [height, setHeight] = useState(null)
    const [weigth, setWeigth] = useState(null)
    const [messageImc, setMessageImc] = useState("Preencha o peso e altura!")
    const [imc, setImc] = useState(null)
    const [textButton, setTexButton] = useState("Calcular")
function imcCalculator (){
    return setImc((weigth/(height * height)).toFixed(2))
}

function validationImc(){
    if(weigth != null && height != null){
        imcCalculator()
        setHeight(null)
        setWeigth(null)
        setMessageImc("Seu IMC é: ")
        setTexButton("Calcular Novamente")
        return
    }else{
        setImc(null)
        setTexButton("Calcular")
        setMessageImc("Preencha o peso e altura")
    }
}

    return(
        <View>
            <View>
                <Text>Altura:</Text>
                <TextInput onChangeText={setHeight} value={height} placeholder="Ex: 1.75" keyboardType="numeric"></TextInput>
                <Text>Peso:</Text>
                <TextInput onChangeText={setWeigth} value={weigth} placeholder="Ex: 85.050" keyboardType="numeric"></TextInput>
                <Button onPress={() => validationImc()} title={textButton}></Button>
            </View>
            <ResultImc messageResultImc={messageImc} resultImc={imc}/>
        </View>
    );
}