window.onscroll = function(){

    if (window.scrollY >= "250") {
        document.getElementById('conteudo_dieta').style.opacity = 1;
        document.getElementById('conteudo_dieta').style.left = 0;
    }
    else{
        document.getElementById('conteudo_dieta').style.opacity = 0;
        document.getElementById('conteudo_dieta').style.left = "5%";
    }

}

function cadastro(){

    confirmar = document.getElementById('confirmar').value;
    senha = document.getElementById('senha').value;

    if (senha != confirmar){
        alert('Senha diferentes. Tente usar senhas iguais');
    }

}