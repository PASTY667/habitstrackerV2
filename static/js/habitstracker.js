document.getElementById('createHabitForm').addEventListener('submit', function(event) {
  event.preventDefault();

  var habitName = document.getElementById('habitName').value;

  fetch('/create_habit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'habit_name=' + encodeURIComponent(habitName)
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    if (data.success) {
      var habitList = document.getElementById('habitList');
      var newHabitItem = document.createElement('li');
      newHabitItem.textContent = habitName;
      habitList.appendChild(newHabitItem);
      document.getElementById('habitName').value = '';
    } else {
      console.log('Erreur lors de la création de l\'habitude :', data.error);
    }
  })
  .catch(function(error) {
    console.log('Erreur :', error);
  });
});
