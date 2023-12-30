let cir = document.querySelector(".circle");

function changeColor() {
    let val1 = Math.ceil(Math.random()*256);
    let val2 = Math.ceil(Math.random()*256);
    let val3 = Math.ceil(Math.random()*256);

    return `rgb(${val1}, ${val2}, ${val3})`;
}

function pos() {
    return Math.random()*90;
}

setInterval(() => {
    cir.style.background = changeColor();
    cir.style.top = `${pos()}%`;
    cir.style.left = `${pos()}%`;
}, 550);

function stopGame() {
    alert("Gotcha! You win");
    clearInterval();
}

cir.addEventListener("click", stopGame);