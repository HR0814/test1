const rocket = document.getElementById("rocket");
const earth = document.getElementById("earth");
const moon = document.getElementById("moon");
const saturn = document.getElementById("saturn");
const jupyter = document.getElementById("jupyter");
const earthText = document.querySelector(".earth-text");
const moonText = document.querySelector(".moon-text");
const saturnText = document.querySelector(".saturn-text");
const jupyterText = document.querySelector(".jupyter-text");
const github = document.querySelector(".github-icon");


const class_name = ["earth", "moon", "saturn", "jupyter"];

let left = 40.7;
let cnt = 1;

const earth_css = document.styleSheets[1].rules[13].style;
const moon_css = document.styleSheets[1].rules[14].style;
const saturn_css = document.styleSheets[1].rules[15].style;
const jupyter_css = document.styleSheets[1].rules[16].style;

// Input Keyboard Function
const handleMove = (e) => {
    const key = e.key;
    c_name = rocket.className;
    if (key == "ArrowRight" && cnt <= 3) {
        rocket.style.marginLeft = `${left}%`;
        rocket.classList.replace(c_name, class_name[cnt]);
        imageAnimation(class_name[cnt]);
        cnt += 1;
        left += 14.2;
    } else if (key == "ArrowLeft" && cnt >= 1) {
        imageAnimation(class_name[cnt - 1]);
        rocket.classList.replace(c_name, class_name[cnt - 1]);
        left -= 14.2;
        cnt -= 1;
        rocket.style.marginLeft = `${left}%`;
    }
    if (key === "Enter") {
        console.log("다음 페이지로 이동!");
    }
};

// Insert Animation Function
const imageAnimation = (name) => {
    if (name == earth.className) {
        earth_css.animation = "1.5s ease-in-out 0s infinite normal none running imageMove";
        moon_css.animation = "";
        saturn_css.animation = "";
        jupyter_css.animation = "";
        earthText.innerText = "Press Enter";
        moonText.innerText = "";
        saturnText.innerText = "";
        jupyterText.innerText = "";
    } else if (name == moon.className) {
        moon_css.animation = "1.5s ease-in-out 0s infinite normal none running imageMove";
        earth_css.animation = "";
        saturn_css.animation = "";
        jupyter_css.animation = "";
        moonText.innerText = "Press Enter";
        earthText.innerText = "";
        saturnText.innerText = "";
        jupyterText.innerText = "";
    } else if (name == saturn.className) {
        saturn_css.animation = "1.5s ease-in-out 0s infinite normal none running imageMove";
        earth_css.animation = "";
        moon_css.animation = "";
        jupyter_css.animation = "";
        saturnText.innerText = "Press Enter";
        earthText.innerText = "";
        moonText.innerText = "";
        jupyterText.innerText = "";
    } else {
        jupyter_css.animation = "1.5s ease-in-out 0s infinite normal none running imageMove";
        earth_css.animation = "";
        moon_css.animation = "";
        saturn_css.animation = "";
        jupyterText.innerText = "Press Enter";
        earthText.innerText = "";
        moonText.innerText = "";
        saturnText.innerText = "";
    }
};

const earthMouseEnter = (e) => {
    cnt = 0;
    left = 26.5;
    rocket.style.marginLeft = "26.5%";
    rocket.classList.replace(rocket.className, "earth");
    earth_css.animation = "1.5s ease-in-out 0s infinite normal none running imageMove";
    moon_css.animation = "";
    saturn_css.animation = "";
    jupyter_css.animation = "";
    earthText.innerText = "Press Enter";
    moonText.innerText = "";
    saturnText.innerText = "";
    jupyterText.innerText = "";
};

const moonMouseEnter = (e) => {
    cnt = 1;
    left = 40.7;
    rocket.style.marginLeft = "40.7%";
    rocket.classList.replace(rocket.className, "moon");
    moon_css.animation = "1.5s ease-in-out 0s infinite normal none running imageMove";
    earth_css.animation = "";
    saturn_css.animation = "";
    jupyter_css.animation = "";
    moonText.innerText = "Press Enter";
    earthText.innerText = "";
    saturnText.innerText = "";
    jupyterText.innerText = "";
};

const saturnMouseEnter = (e) => {
    cnt = 2;
    left = 54.9;
    rocket.style.marginLeft = "54.9%";
    rocket.classList.replace(rocket.className, "saturn");
    saturn_css.animation = "1.5s ease-in-out 0s infinite normal none running imageMove";
    earth_css.animation = "";
    moon_css.animation = "";
    jupyter_css.animation = "";
    saturnText.innerText = "Press Enter";
    earthText.innerText = "";
    moonText.innerText = "";
    jupyterText.innerText = "";
};
const jupyterMouseEnter = (e) => {
    cnt = 3;
    left = 69.1;
    rocket.style.marginLeft = "69.1%";
    rocket.classList.replace(rocket.className, "jupyter");
    jupyter_css.animation = "1.5s ease-in-out 0s infinite normal none running imageMove";
    earth_css.animation = "";
    moon_css.animation = "";
    saturn_css.animation = "";
    jupyterText.innerText = "Press Enter";
    earthText.innerText = "";
    moonText.innerText = "";
    saturnText.innerText = "";
};

imageAnimation(rocket.className);

earth.addEventListener("mouseenter", earthMouseEnter);
moon.addEventListener("mouseenter", moonMouseEnter);
saturn.addEventListener("mouseenter", saturnMouseEnter);
jupyter.addEventListener("mouseenter", jupyterMouseEnter);
window.addEventListener("keydown", handleMove);
github.addEventListener("click", () => {
    document.location.href = "https://github.com/hungeun/1class";
})
