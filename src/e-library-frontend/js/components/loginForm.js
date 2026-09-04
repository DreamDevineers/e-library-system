const LoginForm = () => {
    const handleLogin = async (event) => {
        event.preventDefault();
        
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        
        console.log("email:", email);
        console.log("password:", password);
        
        try {
            const response = await fetch('http://127.0.0.1:8000/member/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 
                    email: email, 
                    password: password 
                })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                localStorage.setItem('token', data.token);
                localStorage.setItem('user', JSON.stringify(data.user));
                alert("Login successful!");
                window.location.href = "home.html";
            } else {
                alert("Error: " + (data.detail || "Invalid credentials"));
            }
        } catch (error) {
            console.error("Error:", error);
            alert("Network error! Please try again.");
        }
    };
    
    window.handleLogin = handleLogin;
    
    return `
        <section class="form login-form">
            <form class="input-container" onsubmit="window.handleLogin(event)">
                <p>Login your account to get started</p>
                
                <input
                    type="email"
                    id="login-email"
                    placeholder="Enter email..."
                    required
                >
                
                <input
                    type="password"
                    id="login-password"
                    placeholder="Enter password..."
                    required
                >
                
                <button type="submit">Login</button>
                
                <p class="register-link">
                    Don't have an account? <a href="register.html">Register here</a>
                </p>
            </form>
        </section>
    `;
};

export default LoginForm;