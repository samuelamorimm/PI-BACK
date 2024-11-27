// Função para exibir o alerta
function showAlert(title, content) {
  document.getElementById('customAlert').style.display = 'block'; // Mostrar o modal
}

// Função para fechar o alerta
function closeAlert() {
  document.getElementById('customAlert').style.display = 'none'; // Esconder o modal
}

// Adicionando o evento para o envio do formulário
document.getElementById('formAgendamento').addEventListener('submit', function(event) {
  event.preventDefault(); // Evita que o formulário seja enviado normalmente
  
  const nome = document.getElementById("nome").value;
  const cpf = document.getElementById("cpf").value;
  const data = document.getElementById("data").value;
  const servico = document.getElementById("servico").value;

  if (nome && cpf && data && servico) {
      // Exibir alerta de sucesso
      showAlert();
  } else {
      // Exibir alerta de erro
      showAlert('Erro', 'Por favor, preencha todos os campos.');
  }
});

