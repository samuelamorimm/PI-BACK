// Selecionando o modal e os links de "Deletar"
const modal = document.getElementById('myModal');
const modalContent = modal.querySelector('.modal-content');
const closeModalBtns = modal.querySelector('.cancel-btn');
const deleteLinks = document.querySelectorAll('.btn-post[data-action="delete"]');
const deleteForm = document.getElementById('delete-form');
const modalTitle = document.getElementById('modal-title');

// Função para mostrar o modal
function showModal(postTitle, actionUrl) {
    // Atualiza o título do modal
    modalTitle.textContent = `Tem certeza que deseja excluir o post "${postTitle}"?`;

    // Atualiza a ação do formulário de exclusão
    deleteForm.action = actionUrl;

    // Exibe o modal
    modal.style.display = 'block';
}

// Eventos de click nos links de deletar
deleteLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault(); // Evita que o link redirecione para outra página

        const postTitle = link.getAttribute('data-post-title');
        const actionUrl = link.getAttribute('data-post-url');

        showModal(postTitle, actionUrl);
    });
});

// Fecha o modal ao clicar no botão de cancelar ou fora do modal
closeModalBtns.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Fecha o modal se clicar fora do conteúdo do modal
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};
