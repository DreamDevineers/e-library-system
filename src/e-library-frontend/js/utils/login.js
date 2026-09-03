import LoginForm from "./components/login_form.js";

const loginPage = document.querySelector("#login-page");

loginPage.innerHTML = LoginForm();

const loginForm = document.querySelector(".input-container");

loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://localhost:8000/member/login", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            console.error("Login failed:", data);
            return;
        }

        console.log("Login successful:", data);

        window.location.href = "../../index.html";

    } catch (error) {
        console.error("Unable to connect to the server:", error);
    }
});
