function formatar(mascara, documento) {

    var i = documento.value.length;
    var saida = mascara.substring(0,1);
    var texto = mascara.substring(i);

    if (texto.substring(0,1) != saida) {
        documento.value += texto.substring(0,1);
    }

}

window.onscroll = function(){

    if (window.scrollY >= "350") {
        document.getElementById('conteudo_dieta').style.opacity = 1;
        document.getElementById('conteudo_dieta').style.left = 0;
    }
    else{
        document.getElementById('conteudo_dieta').style.opacity = 0;
        document.getElementById('conteudo_dieta').style.left = "5%";
    }

}

function tabela(){

    var peso = document.getElementById("peso").value;
    var idade = document.getElementById("idade").value;
    var altura = document.getElementById("altura").value;
    var doenca = document.getElementById("doenca").value;
    var objetivo = document.getElementById("objetivo").value;

    var msg = peso + idade + altura + doenca + objetivo;
    
    alert(msg);

}