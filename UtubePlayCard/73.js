console.log("Dynamic Website Builder");

let cont = document.querySelector(".container");

function sortView(v){
    if (v>=1000 && v<1000000) {
        return `${v/1000}K`;
    }

    else if (v>=1000000) {
        return `${v/1000000}M`;
    }

    else{
        return v;
    }
}

function createCard(title, cName, views, monthsOld, duration, thumbnail) {

    var cardDiv = document.createElement('div');
    cardDiv.className = 'card';
    cont.appendChild(cardDiv);

    cardDiv.innerHTML = `<div class="thumb"> 
<img src="${thumbnail}"
    alt="">

<div class="time">
    ${duration} </div>
</div>

<div class="side">
<div class="title">${title}</div>

<span id="cName" class="low">${cName}</span>
<span id="views" class="low"> &#8226; ${sortView(views)} views &#8226;</span>
<span id="monthsOld" class="low">${monthsOld} months ago</span>
</div>`;
}

createCard("Installing VS Code & How Websites Work | Sigma Web Development Course - Tutorial #1" , "CodeWithHarry", 807000, 2, "31:20", "https://i.ytimg.com/vi/tVzUXW6siu0/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCLbeHLcVNUxbHKUuMxpLbTQSNcPQ");

createCard("Your First HTML Website | Sigma Web Development Course - Tutorial #2", "CodeWithHarry", 410000, 2, "28:31", "https://i.ytimg.com/vi/kJEsTjH5mVg/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBCA3_MiIeOkWOlW_VvWSqOu4QXog")

createCard("Your First HTML Website | Sigma Web Development Course - Tutorial #2", "CodeWithHarry", 410000, 2, "28:31", "https://i.ytimg.com/vi/kJEsTjH5mVg/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBCA3_MiIeOkWOlW_VvWSqOu4QXog")

createCard("Your First HTML Website | Sigma Web Development Course - Tutorial #2", "CodeWithHarry", 410000, 2, "28:31", "https://i.ytimg.com/vi/kJEsTjH5mVg/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBCA3_MiIeOkWOlW_VvWSqOu4QXog")

createCard("Your First HTML Website | Sigma Web Development Course - Tutorial #2", "CodeWithHarry", 410000, 2, "28:31", "https://i.ytimg.com/vi/kJEsTjH5mVg/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBCA3_MiIeOkWOlW_VvWSqOu4QXog")

createCard("Your First HTML Website | Sigma Web Development Course - Tutorial #2", "CodeWithHarry", 410000, 2, "28:31", "https://i.ytimg.com/vi/kJEsTjH5mVg/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBCA3_MiIeOkWOlW_VvWSqOu4QXog")

createCard("Your First HTML Website | Sigma Web Development Course - Tutorial #2", "CodeWithHarry", 410000, 2, "28:31", "https://i.ytimg.com/vi/kJEsTjH5mVg/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBCA3_MiIeOkWOlW_VvWSqOu4QXog")