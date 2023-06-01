function displayDateTime() {
  var date = new Date();
  var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
  var formattedDate = date.toLocaleDateString('pt-BR', options);

  document.getElementById('clock').textContent = formattedDate;
}

setInterval(displayDateTime, 1000); // Atualiza a cada segund