var button = document.querySelector(".animateButton");
button.addEventListener("click", function() {
    button.classList.add("clicked");
    setTimeout(function(){
        button.classList.remove("clicked");
    }, 300);
});
document.getElementById("myForm").addEventListener("submit", function(event) {

    event.preventDefault(); // Empêche l'envoi du formulaire
    let mot = document.getElementById("resultTextArea").value; // Récupérer le texte du textarea
    let lg = document.getElementById("lg").value;
    let levelC = document.getElementById("comp").value;
    let temperature = document.getElementById("temp").value;
    if (lg == "" || lg == 0){
        document.getElementById("lg").innerHTML = 1;
    }
    else if (levelC == "" || Number(levelC > 100)){
        alert("Le level C dois etre inferieur a 101")
        document.getElementById("comp").innerHTML = 70;

    }
    else if (temperature == "" || Number(temperature > 1)){
        alert("la temperature est comprise entre 0.1 et 1 inclut")
        document.getElementById("temp").innerHTML= 0.3;
    }


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