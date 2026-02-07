const navPlaceholder = document.getElementById("nav-placeholder");
if (navPlaceholder) {
  const user = JSON.parse(localStorage.getItem("user")); // check if logged in

  navPlaceholder.innerHTML = `
    <nav class="navbar">
      <div class="logo">WorkWay Careers</div>
      <ul class="nav-links">
        <li><a href="/index.html">Home</a></li>
        <li><a href="/user/jobs.html">Jobs</a></li>
        <li><a href="/user/apply.html">Apply</a></li>
        <li><a href="#">About Us</a></li>
        ${user ? `<li><a href="#" id="logoutBtn">Logout</a></li>` : `<li><a href="/user/login.html">Login</a></li>`}
      </ul>
    </nav>
  `;

  if (user) {
    document.getElementById("logoutBtn").addEventListener("click", () => {
      localStorage.removeItem("user");
      window.location.reload();
    });
  }
}
