document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggleButton");
  
    // Ajoute un gestionnaire d'événements pour le bouton
    toggleButton.addEventListener("click", function () {
      // Vérifie si le cookie est déjà présent
      const isCookieSet = document.cookie.includes("redFilter=true");
  
      // Crée ou supprime le cookie en fonction de sa présence
      if (isCookieSet) {
        document.cookie = "redFilter=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      } else {
        document.cookie = "redFilter=true; expires=Fri, 31 Dec 9999 23:59:59 UTC; path=/;";
      }
  
      // Active ou désactive le filtre en fonction de la présence du cookie
      setRedFilter(!isCookieSet);
    });
  
    // Fonction pour activer ou désactiver le filtre rouge
    function setRedFilter(isActive) {
      const body = document.body;
  
      if (isActive) {
        body.classList.add("red-filter-active");
      } else {
        body.classList.remove("red-filter-active");
      }
    }
  });
  