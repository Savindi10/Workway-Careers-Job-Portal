const API_BASE = "http://localhost:5001";

// get job_id from URL
const params = new URLSearchParams(window.location.search);
const jobId = params.get("job_id");

document.getElementById("job_id").value = jobId;

document.getElementById("applicationForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const resumeUrl = document.getElementById("resume_url").value;
  const message = document.getElementById("message");

  try {
    const res = await fetch(`${API_BASE}/user/jobs/${jobId}/apply`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: 1, // later from login/session
        resume_url: resumeUrl
      })
    });

    if (!res.ok) throw new Error("Apply failed");

    message.style.color = "green";
    message.innerText = "Application submitted successfully!";

  } catch (err) {
    message.style.color = "red";
    message.innerText = "Error submitting application.";
    console.error(err);
  }
});

