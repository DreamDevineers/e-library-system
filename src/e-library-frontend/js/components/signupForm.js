const SignupForm = () => {
    const handleSignup = async (event) => {
        event.preventDefault();
        
        const name = document.getElementById('signup-name').value;
        const email = document.getElementById('signup-email').value;
        const phone = document.getElementById('signup-phone').value;
        const password = document.getElementById('signup-password').value;
        
        console.log("name:", name);
        console.log("email:", email);
        console.log("phone:", phone);
        console.log("password:", password);
        
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
                    name: name,
                    email: email,
                    phone: phone,
                    password: password
                })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                alert("Account created successfully! Please login.");
                window.location.href = "login.html";
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
                    id="signup-name"
                    placeholder="Enter full name..."
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
                    type="password"
                    id="signup-password"
                    placeholder="Enter password..."
                    required
                >
                
                <button type="submit">Sign Up</button>
                
                <p class="login-link">
                    Already have an account? <a href="login.html">Login here</a>
                </p>
            </form>
        </section>
    `;
};

export default SignupForm;