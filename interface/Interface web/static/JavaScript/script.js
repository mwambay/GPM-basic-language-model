var button = document.querySelector(".animateButton");
button.addEventListener("click", function() {
    button.classList.add("clicked");
    setTimeout(function(){
        button.classList.remove("clicked");
    }, 300);
});

const mySlider = document.getElementById("my-slider");
const sliderValue = document.getElementById("slider-value");

function slider(){
    valPercent = (mySlider.value / mySlider.max)*100;
    console.log(valPercent)
    mySlider.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue.textContent = mySlider.value;

}
slider();

const mySlider2 = document.getElementById("my-slider2");
const sliderValue2 = document.getElementById("slider-value2");

function slider2(){
    valPercent = (mySlider2.value / mySlider2.max)*100;
    console.log("deuxoeddkd")
    console.log(valPercent)
    mySlider2.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue2.textContent = mySlider2.value;

}
slider2();


const mySlider3 = document.getElementById("my-slider3");
const sliderValue3 = document.getElementById("slider-value3");

function slider3(){
    valPercent = (mySlider3.value / mySlider3.max);
    console.log("deuxoeddkd")
    console.log(valPercent)
    mySlider3.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue3.textContent = mySlider3.value;

}
slider3();


document.getElementById("myForm").addEventListener("submit", function(event) {

    event.preventDefault(); // Empêche l'envoi du formulaire
    let lg  = (mySlider.value / mySlider.max)*100;
    mySlider.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue.textContent = mySlider.value;
    console.log("hello");
    console.log(lg);
    let mot = document.getElementById("resultTextArea").value; // Récupérer le texte du textarea
    //let lg = document.getElementById("lg").value;

    fetch("/", { method: "POST", body: new FormData(document.getElementById("myForm")) })
      .then(response => response.json())
      .then(data => {
        console.log(data.result);
        let resultModel = data.result;

        // Insertion des elements probable
        let probabilityModel = resultModel['Probability']
        document.getElementById('resultprediction').value += "\n\n New processe\n";
        for (let index = 0; index < probabilityModel.length; index++){
            document.getElementById('resultprediction').value += `${probabilityModel[index]} \n`;
            console.log(probabilityModel[index]);
        
        };
        document.getElementById('resultprediction').value += "End";
        
        // Prediction
        let predictionModel = resultModel["Predictions"]
        document.getElementById('resultprediction').value += "\n\n New processe of prediction\n";
        for (let index = 0; index < predictionModel.length; index++){
            document.getElementById('resultprediction').value +=  predictionModel[index] + "\n";
            console.log(predictionModel[index]);
        
        };
        document.getElementById('resultprediction').value += "End";
        resultModel = resultModel['Sequence retained'];
        let textePrecedent = mot
        // Délai entre chaque ajout de caractère (en millisecondes)
        var delay = 50;
        
        // Fonction pour afficher le texte de manière incrémentielle
        function displayText(text, index) {
            if (index < text.length) {
            // Ajouter un caractère au <textarea>
            document.getElementById("resultTextArea").value += text.charAt(index);

            //
            
            // Appeler la fonction récursivement pour afficher le caractère suivant
            setTimeout(function() {
                displayText(text, index + 1);
            }, delay);
            }
        }
        
        // Appeler la fonction pour afficher le texte incrémentiellement
        displayText(resultModel, 0);
        
        //document.getElementById("resultTextArea").value = textePrecedent + " " + resultModel;
      });
   // document.getElementById("resultTextArea").value = ""; // Réinitialiser le textarea
  });

