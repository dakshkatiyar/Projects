const randomDelay = () => {
    return new Promise((resolve, reject) => {
        timeout = 1 + 4 * Math.random();
        setTimeout(() => {
            resolve();
        }, timeout * 1000);
    })
}

const addItem = async (item) => {
    await randomDelay();
    let div = document.createElement("div");
    div.innerHTML = item;
    document.body.append(div);
}

async function main() {

   let t = setInterval(() => {
        let last = document.body.lastElementChild;
        if (last.innerHTML.endsWith("...")) {
            last.innerHTML = last.innerHTML.slice(0, last.innerHTML.length-3)
        }

        else{
            last.innerHTML+= ".";
        }
    }, 100);

    let text = ["Initializing Hacking",
        "Reading your Files",
        "Password files detected",
        "Sending all files and passwords to server",
        "Cleaning up"
    ]

    for (const item of text) {
        await addItem(item);
    }

    await randomDelay();
    clearInterval(t);
}

main();