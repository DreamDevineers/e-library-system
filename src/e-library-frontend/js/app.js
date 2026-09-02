import Header from "./components/header.js";
import hero from "./components/hero.js";

const App = () => `
    ${Header()}
    

    <main>
        ${hero()}
    </main>
`;

export default App;
