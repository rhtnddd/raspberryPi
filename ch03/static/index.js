let click = document.getElementById("click");
let ggugim = document.getElementById("ggugim");
let imageElement = document.getElementById("myImage");
click.addEventListener('click', () => {
    imageElement.src="../static/jungukugim.png";
    imageElement.alt = "두 번째 이미지";
    fetch("/on");
});
ggugim.addEventListener('click', () => {
    imageElement.src="../static/junguggugim.png";
    imageElement.alt = "첫 번째 이미지";
    fetch("/off");
});
