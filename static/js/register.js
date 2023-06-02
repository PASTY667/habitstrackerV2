document.getElementById('registerForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Empêche le comportement par défaut du formulaire
  
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  
  // Vérifier si le nom d'utilisateur est déjà pris
  fetch('/check-username', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'username=' + encodeURIComponent(username)
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    if (data.is_taken) {
      document.getElementById('errorMessage').textContent = 'Le nom d\'utilisateur est déjà pris';
    } else {
      document.getElementById('registerForm').submit();
    }
  })
  .catch(function(error) {
    console.log('Erreur :', error);
  });
});
 
