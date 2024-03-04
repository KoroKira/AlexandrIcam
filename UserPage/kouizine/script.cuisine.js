function afficherRecette(nomRecette) {
    // Vérifiez la recette sélectionnée
    if (nomRecette === 'pate_carbonara') {
        // Remplacez le contenu du détail de la recette avec la recette spécifique
        document.getElementById("recette-detail").innerHTML = `
            <h2>Pâtes à la Carbonara</h2>
            <p><strong>Nombre de personnes :</strong> 4</p>
            <p><strong>Temps de préparation :</strong> 10 minutes</p>
            <p><strong>Temps de cuisson :</strong> 15 minutes</p>
            
            <h3>Ingrédients :</h3>
            <ul>
                <li>400g de pâtes (spaghetti de préférence)</li>
                <li>150g de guanciale ou de pancetta, coupé en dés</li>
                <li>3 œufs</li>
                <li>100g de fromage Pecorino Romano râpé</li>
                <li>Poivre noir fraîchement moulu</li>
            </ul>
            
            <h3>Ustensiles :</h3>
            <ul>
                <li>Une grande casserole pour cuire les pâtes</li>
                <li>Une poêle pour faire revenir la pancetta</li>
                <li>Un bol pour mélanger les œufs et le fromage</li>
            </ul>
            
            <h3>Instructions :</h3>
            <ol>
                <li>Faites cuire les pâtes dans de l'eau salée selon les instructions de l'emballage.</li>
                <li>Pendant ce temps, faites revenir la pancetta dans une poêle jusqu'à ce qu'elle soit croustillante.</li>
                <li>Dans un bol, battez les œufs et mélangez-les avec le fromage Pecorino Romano.</li>
                <li>Égouttez les pâtes et ajoutez-les à la poêle avec la pancetta. Mélangez bien.</li>
                <li>Retirez la poêle du feu et ajoutez le mélange d'œufs et de fromage. Remuez rapidement pour enrober les pâtes.</li>
                <li>Assaisonnez avec du poivre noir fraîchement moulu.</li>
                <li>Servez immédiatement et ajoutez du fromage supplémentaire si désiré.</li>
            </ol>
        `;

        // Affiche le détail de la recette
        document.getElementById("recette-detail").style.display = "block";
        document.getElementById("recettes").style.display = "none";
    }
    // Ajoutez des conditions pour d'autres recettes si nécessaire
}
