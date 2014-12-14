$(document).on('ready',inicio);

function inicio()
{
    $("#Consulta").on("click",ocultar);
}

function ocultar()
{
    $("#Benchmark").slideUp();
}