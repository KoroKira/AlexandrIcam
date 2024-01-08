// Fonction pour définir un cookie
function setCookie(name, value, days) {
  var expires = "";
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + value + expires + "; path=/";
}

// Fonction pour récupérer la valeur d'un cookie
function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

// Fonction pour supprimer un cookie
function eraseCookie(name) {
  document.cookie = name + '=; Max-Age=-99999999; path=/';
}

// Fonction pour activer/désactiver le filtre rouge
function toggleRedFilter() {
  var body = document.body;
  var redFilter = document.getElementById("red-filter");

  // Vérifier si le filtre rouge est actif
  var isRedFilterActive = body.classList.contains("red-filter-active");

  // Inverser l'état du filtre
  if (isRedFilterActive) {
    body.classList.remove("red-filter-active");
    eraseCookie("redFilter");
  } else {
    body.classList.add("red-filter-active");
    setCookie("redFilter", "active", 365);
  }
}

// Vérifier le cookie lors du chargement de la page
document.addEventListener("DOMContentLoaded", function () {
  var body = document.body;
  var redFilter = document.getElementById("red-filter");

  var redFilterCookie = getCookie("redFilter");
  if (redFilterCookie === "active") {
    body.classList.add("red-filter-active");
  }
});
