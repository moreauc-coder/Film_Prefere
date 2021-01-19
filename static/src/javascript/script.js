function connection(){
    alert('connection impossible');
}

function formulaire(){
	var email = document.getElementById("email").value;
	var mdp = document.getElementById("mdp").value;
	var msg = document.getElementById("msg").value;

	if (email && mdp && msg){
        alert("c'est good");
    } else {
        alert('Veuillez remplir tout les champs');
        return false; // Permet de bloquer la soumission du formulaire
    }

}