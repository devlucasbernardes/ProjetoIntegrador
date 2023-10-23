let quantia = document.querySelector(".quantia");
let botaoConverter = document.querySelector("button");
let resultado = document.querySelector(".resultado");

async function converterMoeda(){
    let requestURL = `https://economia.awesomeapi.com.br/last/USD-BRL`;

    try {
        let response = await fetch(requestURL);
        let data = await response.json();
        resultado.textContent = (Number(data.USDBRL.high) * Number(quantia.value)).toFixed(2);
      } catch (error) {
        console.log(error);
      }
      
}

botaoConverter.addEventListener("click", (e) => {
    e.preventDefault();
    converterMoeda();
});