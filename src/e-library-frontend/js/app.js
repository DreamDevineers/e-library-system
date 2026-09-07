import Header from "./components/header.js";
import Hero from "./components/hero.js";
import About from "./components/about.js";
import SubHeader from "./components/subheader.js";
import LoginForm from "./components/loginForm.js";
import SignupForm from "./components/signupForm.js";

const routes = {
    "/":           () => `${Header()}<main>${Hero()}</main>`,
    "/login":      () => `${SubHeader()}<main>${LoginForm()}</main>`,
    "/register":   () => `${SubHeader()}<main>${SignupForm()}</main>`,
    "/about":      () => `${SubHeader()}<main>${About()}</main>`,
};

const App = () => {
    const path = window.location.pathname;
    const view = routes[path] ?? routes["/"];
    return view();
};

export default App;
