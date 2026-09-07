const SignupForm = () => {
    const handleSignup = async (event) => {
        event.preventDefault();

        const firstName = document.getElementById('signup-first-name').value;
        const lastName = document.getElementById('signup-last-name').value;
        const email = document.getElementById('signup-email').value;
        const phone = document.getElementById('signup-phone').value;
        const password = document.getElementById('signup-password').value;
        const address = document.getElementById('signup-address').value;

        // console.log("first name:", firstName);
        // console.log("last name:", lastName);
        // console.log("email:", email);
        // console.log("phone:", phone);
        // console.log("password:", password);
        // console.log("address:", address);

        if (password.length < 6) {
            alert("Password must be at least 6 characters long!");
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/member/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    first_name: firstName,
                    last_name: lastName,
                    email: email,
                    phone: phone,
                    password: password,
                    address: address
                })
            });

            const data = await response.json();

            if (response.ok) {
                alert("Account created successfully! Please login.");
                history.pushState(null, null, '/login');
                window.dispatchEvent(new PopStateEvent('popstate'));
            } else {
                alert("Error: " + (data.detail || "Registration failed"));
            }

        } catch (error) {
            console.error("Error:", error);
            alert("Network error! Please try again.");
        }
    };

    window.handleSignup = handleSignup;

    return `
        <section class="form">
            <form class="input-container" onsubmit="window.handleSignup(event)">

                <p>Sign up for an account to get started</p>

                <input
                    type="text"
                    id="signup-first-name"
                    placeholder="Enter first name..."
                    required
                >

                <input
                    type="text"
                    id="signup-last-name"
                    placeholder="Enter last name..."
                    required
                >

                <input
                    type="email"
                    id="signup-email"
                    placeholder="Enter email..."
                    required
                >

                <input
                    type="text"
                    id="signup-phone"
                    placeholder="Enter phone number..."
                    required
                >

                <input
                    type="text"
                    id="signup-address"
                    placeholder="Enter address..."
                    required
                >

                <input
                    type="password"
                    id="signup-password"
                    placeholder="Enter password..."
                    required
                >

                <button type="submit">Sign Up</button>

                <p class="login-link">
                    Already have an account?
                    <a href="/login" data-link>Login here</a>
                </p>

            </form>
        </section>
    `;
};

export default SignupForm;
