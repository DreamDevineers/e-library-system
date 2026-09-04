import LoginForm from "./components/login_form.js";

const loginPage = document.querySelector(LoginForm);
console.log("loginPage:", loginPage);

loginPage.innerHTML = LoginForm();

const loginForm = document.querySelector(".input-container");

loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.querySelector("#email").value;
    const password = document.querySelector("#password").value;

    console.log("Email:", email);
    console.log("Password:", password);

    try {
        const response = await fetch("http://127.0.0.1:8000/member/login", {
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
