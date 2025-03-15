async function enviarFormulario(evento){
    evento.preventDefault()
    
    const nome = document.getElementById("nome").value
    const senha = document.getElementById("senha").value
    const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value

   const resposta = await apiFetch("/api/user", "POST", {nome: nome, senha: senha}, {"X-CSRFToken": csrf} )

   console.log(resposta)

   if (resposta){
    window.location.href = "/home"
    
   }

}

var alunoForm = document.getElementById('alunoForm').addEventListener("submit", enviarFormulario)