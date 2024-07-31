document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Empêche l'envoi du formulaire
    let mot = document.getElementById("resultTextArea").value; // Récupérer le texte du textarea
    let lg = document.getElementById("my-slider").value;
    fetch("/", { method: "POST", body: new FormData(document.getElementById("myForm")) })
      .then(response => response.json())
      .then(data => {
        console.log(data.result);
        let resultModel = data.result;
        resultModel = resultModel['Sequence retained'];
        let textePrecedent = mot
        document.getElementById("resultTextArea").value = textePrecedent + " " + resultModel;
      });
   // document.getElementById("resultTextArea").value = ""; // Réinitialiser le textarea
  });

  document.getElementById("myForm").addEventListener("my-slider", function(event) {
    event.preventDefault(); // Empêche l'envoi du formulaire  
    fetch("/", { method: "POST", body: new FormData(document.getElementById("myForm")) })
const mySlider = document.getElementById("my-slider");
const sliderValue = document.getElementById("slider-value");

function slider(){
    valPercent = (mySlider.value / mySlider.max)*100;
    console.log(valPercent)
    mySlider.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue.textContent = mySlider.value;
}
slider();
  });