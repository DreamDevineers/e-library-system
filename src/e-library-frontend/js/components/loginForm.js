const LoginForm = () => `
    <section class="form login-form">
        <form class="input-container">
            <p>Login your account to get started</p>

            <input
                type="email"
                id="email"
                placeholder="enter email..."
            >

            <input
                type="password"
                id="password"
                placeholder="enter password..."
            >

            <button type="submit">Login</button>
        </form>
    </section>
`;

export default LoginForm;
