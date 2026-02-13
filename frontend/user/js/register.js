const API_BASE = "http://localhost:5001/api";

document.getElementById("registerForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${API_BASE}/register`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name, email, password })
    });

    const data = await res.json();

    if (!res.ok) {
      document.getElementById("message").innerText = data.error || "Register failed";
      return;
    }

    document.getElementById("message").innerText =
      "Registered successfully! Redirecting...";

    setTimeout(() => {
      window.location.href = "./login.html";
    }, 1500);

  } catch (err) {
    document.getElementById("message").innerText = "Server error";
  }
});