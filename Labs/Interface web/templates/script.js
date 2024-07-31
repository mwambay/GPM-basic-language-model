document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Empêche l'envoi du formulaire
    let mot = document.getElementById("resultTextArea").value; // Récupérer le texte du textarea
    let lg = document.getElementById("lg").value;
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