import Header from "./components/header.js";
import hero from "./components/hero.js";

const App = () => {

    const path = window.location.pathname;

    console.log("Current path:", path);

    if (path.includes("about.html")) {
        return `
            ${Header()}

            <main>
                <h1>ABOUT PAGE</h1>
                <p>about page</p>
            </main>
        `;
    }

    return `
        ${Header()}

        <main>
            ${hero()}
        </main>
    `;
};

export default App;