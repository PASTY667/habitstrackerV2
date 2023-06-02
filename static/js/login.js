document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Empêche le comportement par défaut du formulaire
  
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  
  fetch('/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password)
  })
  .then(function(response) {
    if (response.ok) {
      window.location.href = '/habitudes';
    } else {
      document.getElementById('errorMessage').textContent = 'Nom d\'utilisateur ou mot de passe incorrect';
    }
  })
  .catch(function(error) {
    console.log('Erreur :', error);
  });
});
 
