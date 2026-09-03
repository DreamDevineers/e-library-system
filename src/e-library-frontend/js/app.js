import Header from "./components/header.js";
import hero from "./components/hero.js";
import About from "./components/about.js";
import SubHeader from "./components/subheader.js";

const App = () => {

    const path = window.location.pathname;

    console.log("Current path:", path);

    if (path.includes("about.html")) {
        return `
            ${Header()}

            <main>
                ${About()}
            </main>
        `;
    }

    if (path.includes("login.html")) {
        return `
            ${SubHeader()}

            <main>
                
            </main>
        `;
    }

    if (path.includes("register.html")) {
        return `
            ${SubHeader()}

            <main>
                
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