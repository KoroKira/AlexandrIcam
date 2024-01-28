// cookie.js

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }
  
  // Vérifier si l'utilisateur a le cookie
  var userLoggedIn = readCookie("userLoggedIn");
  
  // Si le cookie n'est pas présent, rediriger vers la page de connexion
  if (!userLoggedIn) {
    window.location.href = '/AlexandrIcam/connexion.html';
  }
  