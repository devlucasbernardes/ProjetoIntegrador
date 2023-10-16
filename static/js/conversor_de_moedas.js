let quantia = document.querySelector(".quantia");
let botaoConverter = document.querySelector("button");
let resultado = document.querySelector(".resultado");

async function converterMoeda(){
    let requestURL = `https://economia.awesomeapi.com.br/last/USD-BRL`;

    try {
        let response = await fetch(requestURL);
        let data = await response.json();
        resultado.textContent = Number(data.USDBRL.high).toFixed(2)*Number(quantia.value);
      } catch (error) {
        console.log(error);
<<<<<<< Updated upstream
      }
      
=======
        // Expected output: ReferenceError: nonExistentFunction is not defined
        // (Note: the exact output may be browser-dependent)
      }
      

>>>>>>> Stashed changes
}

botaoConverter.addEventListener("click", (e) => {
    e.preventDefault();
    converterMoeda();
});