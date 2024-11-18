// Sélectionner l'input et la table
const searchInput = document.getElementById('table-search');
const table = document.getElementById('emissionTable');
const rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

// Ajouter un écouteur d'événements sur l'input pour réagir aux changements
searchInput.addEventListener('keyup', function() {
    const filter = searchInput.value.toLowerCase();  // Récupérer la valeur du champ de recherche en minuscule

    // Parcourir toutes les lignes du tableau
    for (let i = 0; i < rows.length; i++) {
        let match = false;
        // Parcourir toutes les cellules de la ligne actuelle
        const cells = rows[i].getElementsByTagName('td');

        // Vérifier si au moins une cellule de la ligne contient le texte recherché
        for (let j = 0; j < cells.length; j++) {
            const cellContent = cells[j].textContent.toLowerCase();
            if (cellContent.includes(filter)) {
                match = true;
                break;
            }
        }

        // Si une correspondance est trouvée, afficher la ligne, sinon la masquer
        if (match) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
});
