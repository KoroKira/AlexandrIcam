<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Connexion</title>
</head>
<body>

<?php
// Fonction pour vérifier si l'e-mail est autorisé
function isEmailAuthorized($email) {
  // Utilisation d'une expression régulière pour vérifier le format
  return preg_match('/^[a-zA-Z0-9._%+-]+@[0-9]{4}\.icam\.fr$/', $email);
}

// Vérifier si le formulaire a été soumis
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Récupérer l'adresse e-mail soumise depuis le formulaire
  $userEmailAddress = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

  // Vérifier si l'adresse e-mail est autorisée
  if (isEmailAuthorized($userEmailAddress)) {
    echo '<p>Bienvenue sur le site autorisé!</p>';
    // Effectuer d'autres actions nécessaires pour l'utilisateur autorisé
  } else {
    echo '<p>Accès refusé. Votre adresse e-mail n\'est pas autorisée sur ce site.</p>';
    // Rediriger ou effectuer d'autres actions en conséquence
  }
}
?>

<!-- Formulaire de connexion -->
<form method="post" action="">
  <label for="email">Adresse e-mail :</label>
  <input type="email" id="email" name="email" required>
  <br>
  <input type="submit" value="Connexion">
</form>

</body>
</html>
