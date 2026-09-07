import App from "./app.js";

const root = document.querySelector("#app");

function render() {
    root.innerHTML = App();
}

window.addEventListener("popstate", render);

document.addEventListener("click", (event) => {
    const link = event.target.closest("a[data-link]");
    if (!link) return;

    event.preventDefault();
    history.pushState(null, null, link.href);
    render();
});

render();
