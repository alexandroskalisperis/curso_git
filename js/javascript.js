addEventListener("DOMContentLoaded", inicio, false);
function inicio() {
    document.getElementById("titulo").addEventListener("mouseover", mover, false);
}

function mover() {
    tit_1 = document.getElementById("titulo");
    tit_1.style.color = "green";
}