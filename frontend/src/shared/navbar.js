console.log("NAVBAR LOADED - NEW VERSION");

const navPlaceholder = document.getElementById("nav-placeholder");

function getUserFromLocalStorage() {
  try {
    const raw = localStorage.getItem("user");

    // if null, empty, or undefined
    if (!raw || raw === "undefined" || raw === "null") {
      return null;
    }

    // try parse JSON
    return JSON.parse(raw);
  } catch (error) {
    console.warn("Invalid user data in localStorage. Clearing it.");
    localStorage.removeItem("user");
    return null;
  }
}

if (navPlaceholder) {
  const user = getUserFromLocalStorage();

  navPlaceholder.innerHTML = `
    <nav class="navbar">
      <div class="logo">
        <a href="/index.html" class="logo-link">WorkWay Careers</a>
      </div>

      <ul class="nav-links">
        <li><a href="/index.html">Home</a></li>
        <li><a href="/user/jobs.html">Jobs</a></li>
        <li><a href="/about.html">About</a></li>

        ${
          user
            ? `
              <li class="nav-user">Hi, ${user.name}</li>
              <li><a href="#" id="logoutBtn">Logout</a></li>
            `
            : `
              <li><a href="/user/login.html">Login</a></li>
              <li><a href="/user/register.html">Register</a></li>
            `
        }
      </ul>
    </nav>
  `;

  // Logout
  if (user) {
    document.getElementById("logoutBtn").addEventListener("click", (e) => {
      e.preventDefault();
      localStorage.removeItem("user");
      window.location.href = "/index.html";
    });
  }
}
