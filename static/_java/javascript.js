window.onscroll = function(){

    if (window.scrollY >= "200") {
        document.getElementById("conteudo_article").style.opacity = 1;
        document.getElementById("conteudo_article").style.left = 0;
    }
    else{
        document.getElementById("conteudo_article").style.opacity = 0;
        document.getElementById("conteudo_article").style.left = "5%";
    }
}

window.onload = function() {
    var link = document.getElementById('link').innerHTML;
    if (link != 'Fazer login'){
        document.getElementById("link").href="";
        document.getElementById("titulo_site").innerHTML="<div id='slogan'><span id='slogan_site'>Uma simples<br/>dieta para sua<br/>saúde.</span><hr id='hr_slogan'/></div>";
        document.getElementById("dropdown-content").innerHTML='<a id="link-dropdown" href="/login">Trocar conta</a>';
        document.getElementById("dropdown-content").style.padding = "16px";
    } else {
        document.getElementById("link").href="/login";
        document.getElementById("titulo_site").innerHTML='<div class="container"><span class="text1">welcome in</span><span class="text2">yournutrition</span></div>';
    }
}

function cadastro(){

    confirmar = document.getElementById('confirmar').value;
    senha = document.getElementById('senha').value;

    if (senha != confirmar){
        alert('Senha diferentes. Tente usar senhas iguais');
    }

}