document.getElementById('id_data').addEventListener('change', function() {
    var dataSelecionada = this.value

    if (dataSelecionada) {
        fetch(`/buscar-servicos/${dataSelecionada}/`)
        .then(response => response.json())
        .then(data => {
            var servicoSelect = document.getElementById('id_servico');
            servicoSelect.innerHTML = '<option value="">Sem serviço para esta data!</option>'

            data.servicos.forEach(function(servico){
                var option = document.createElement('option');
                option.value = servico.id;
                option.textContent = servico.servico;
                servicoSelect.appendChild(option);
            })
        })
    }       
})