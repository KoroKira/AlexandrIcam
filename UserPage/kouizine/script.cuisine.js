// Fonction pour charger les recettes depuis un fichier texte
function chargerRecettes() {
    fetch('recettes.json')
        .then(response => response.json())
        .then(recettes => afficherRecettes(recettes))
        .catch(error => console.error('Erreur de chargement des recettes :', error));
}

// Fonction pour afficher les recettes sur la page HTML
function afficherRecettes(recettes) {
    const sectionRecettes = document.getElementById('recettes');

    recettes.forEach(recette => {
        const divRecette = document.createElement('div');
        divRecette.classList.add('recette');
        divRecette.onclick = function() {
            afficherRecette(recette);
        };

        const imgRecette = document.createElement('img');
        imgRecette.src = recette.image;
        imgRecette.alt = recette.nom;

        const h2Recette = document.createElement('h2');
        h2Recette.textContent = recette.nom;

        divRecette.appendChild(imgRecette);
        divRecette.appendChild(h2Recette);

        sectionRecettes.appendChild(divRecette);
    });
}

// Fonction pour afficher les détails d'une recette spécifique
function afficherRecette(recette) {
    const sectionRecettes = document.getElementById('recettes');
    sectionRecettes.style.display = 'none';

    const sectionRecetteDetail = document.getElementById('recette-detail');
    sectionRecetteDetail.innerHTML = `
        <button id="retour" onclick="retourRecettes()">Retour</button>
        <h2>${recette.nom}</h2>
        <p><strong>Nombre de personnes :</strong> ${recette.personnes}</p>
        <p><strong>Temps de préparation :</strong> ${recette.temps_preparation}</p>
        <p><strong>Temps de cuisson :</strong> ${recette.temps_cuisson}</p>
        
        <h3>Ingrédients :</h3>
        <ul>
            ${recette.ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
        </ul>
        
        <h3>Ustensiles :</h3>
        <ul>
            ${recette.ustensiles.map(ustensile => `<li>${ustensile}</li>`).join('')}
        </ul>
        
        <h3>Instructions :</h3>
        <ol>
            ${recette.instructions.map(instruction => `<li>${instruction}</li>`).join('')}
        </ol>
    `;
    sectionRecetteDetail.style.display = 'block';
}

// Fonction pour revenir à la liste des recettes
function retourRecettes() {
    document.getElementById("recette-detail").style.display = "none";
    document.getElementById("retour").style.display = "none";
    document.getElementById("recettes").style.display = "flex";
}

// Charger les recettes lors du chargement de la page
window.onload = chargerRecettes;
