console.log("LOGIN JS LOADED");
const API_BASE = "http://localhost:5001";

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const loginError = document.getElementById("loginError");

  if (!loginForm) {
    console.error("Login form not found");
    return;
  }

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!email || !password) {
      loginError.textContent = "Please enter email and password";
      return;
    }

    try {
      const response = await fetch(`${API_BASE}/api/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      });

      const data = await response.json();

      if (!response.ok) {
        loginError.textContent = data.message || "Invalid credentials";
        return;
      }

      // ✅ Save user
      localStorage.setItem("user", JSON.stringify(data.user));

      // ✅ Redirect to existing page
      window.location.href = "/user/index.html";

    } catch (error) {
      console.error("Login error:", error);
      loginError.textContent = "Server error. Try again later.";
    }
  });
});
