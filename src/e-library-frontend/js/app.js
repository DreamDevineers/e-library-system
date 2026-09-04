import Header from "./components/header.js";
import Hero from "./components/hero.js";
import About from "./components/about.js";
import SubHeader from "./components/subheader.js";
import LoginForm from "./components/loginForm.js"
import SignupForm from "./components/signupForm.js"

const App = () => {

    const path = window.location.pathname;

    console.log("Current path:", path);

    if (path.endsWith("about.html")) {
        return `
            ${SubHeader()}

            <main>
                ${About()}
            </main>
        `;
    }

    if (path.endsWith("login.html")) {
        return `
            ${SubHeader()}

            <main>
                ${LoginForm()}
            </main>
        `;
    }

    if (path.endsWith("register.html")) {
        return `
            ${SubHeader()}

            <main>
                ${SignupForm()}
            </main>
        `;
    }

    return `
        ${Header()}

        <main>
            ${Hero()}
        </main>
    `;
};

export default App;