const Header = () => `
    <header class="header">
        <nav>
            <div class="logo-box">
                <a class="logo-text" href="/" data-link>
                    bookit<span class="logo-dot">.</span>
                </a>
            </div>

            <ul class="nav-items">
                <li class="nav-item"><a href="/" data-link>Home</a></li>
                <li class="nav-item"><a href="/about" data-link>About Us</a></li>
            </ul>

            <div class="nav-buttons">
                <a href="/login" data-link class="btn">login account</a>
            </div>
        </nav>
    </header>
`;

export default Header;
