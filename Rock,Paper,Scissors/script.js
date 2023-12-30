let userScore = 0;
let compScore = 0;

const userScorePara = document.querySelector("#user-score");
const compScorePara = document.querySelector("#comp-score");

const choices = document.querySelectorAll(".image");

choices.forEach((image) => {
    image.addEventListener("click", () => {
        const userChoice = image.getAttribute("id");
        playGame(userChoice)
    })
})

const genCompChoice = () => {
    const options = ["rock", "paper", "scissors"];
    const randIdx = Math.floor(Math.random() * 3);
    return options[randIdx];
}

const msg = document.querySelector("#msg");


const msgbox = document.querySelector(".msgbox")



const showWinner = (userWin, userChoice, compChoice) => {
    if (userWin) {
        msg.innerText = `You win! Your ${userChoice} beats ${compChoice}`
        msgbox.style.boxShadow = "0 0 30px green";
        userScore++;
        userScorePara.innerText = userScore;
    }

    else {
        msg.innerText = `You Lose. Comp ${compChoice} beats ${userChoice}`;
        msgbox.style.boxShadow = "0 0 30px red";
        compScore++;
        compScorePara.innerText = 
        compScore;
    }
}

const playGame = (userChoice) => {
    //generate comp choice
    const compChoice = genCompChoice();
    console.log("Comp Choice: ", compChoice);

    if (userChoice === compChoice) {
        console.log("Game Draw");
        msg.innerText= "Game Draw";
        msgbox.style.boxShadow = "0 0 30px whitesmoke";
    }

    else {
        let userWin = true;
        if (userChoice === "rock") {
            userWin = compChoice === "scissors" ? true : false;
        }

        else if (userChoice === "paper") {
            userWin = compChoice === "scissors" ? false : true;
        }

        else {
            userWin = compChoice === "paper" ? true : false;
        }
        showWinner(userWin, userChoice, compChoice);
    }

};

function getRandomColor(){
    let val1 = Math.ceil(Math.random()*255);
    let val2 = Math.ceil(Math.random()*255);
    let val3 = Math.ceil(Math.random()*255);

    return `rgb(${val1}, ${val2}, ${val3})`;
}

let title = document.getElementById("ttl");
setInterval(() => {
    title.style.color = getRandomColor();
}, 1000);
