const API_BASE = "http://localhost:5001"; // later change to your docker hostname or domain

const jobsContainer = document.getElementById("jobsContainer");
const searchInput = document.getElementById("jobSearch");
const searchBtn = document.getElementById("searchBtn");

let allJobs = []; // store jobs from backend 

function renderJobs(jobList) {
  jobsContainer.innerHTML = "";

  if (!jobList || jobList.length === 0) {
    jobsContainer.innerHTML = `<p class="empty">No jobs found.</p>`;
    return;
  }

  jobList.forEach(job => {
    const card = document.createElement("div");
    card.classList.add("job-card");

    // adapt field names depending on your backend JSON keys
    const id = job.job_id;
    const title = job.title;
    const location = job.location;
    const type = job.job_type || job.type; // supports either name

    card.innerHTML = `
      <h3>${title}</h3>
      <p><strong>Location:</strong> ${location}</p>
      <p><strong>Type:</strong> ${type}</p>
      <button class="btn details-btn " onclick="viewDetails(${id})">More Details</button>
      <button class="btn apply-btn" onclick="applyJob(${id})">Apply</button>
    `;

    jobsContainer.appendChild(card);
  });
}

async function loadJobsFromBackend() {
  try {
    const res = await fetch(`${API_BASE}/user/jobs`);
    if (!res.ok) throw new Error("Failed to load jobs");

    const data = await res.json();

    // if your backend returns { jobs: [...] } instead of [...]
    allJobs = Array.isArray(data) ? data : (data.jobs || []);
    renderJobs(allJobs);
  } catch (err) {
    console.error(err);
    jobsContainer.innerHTML = `<p class="empty">Error loading jobs. Check backend + CORS.</p>`;
  }
}

// Search functionality (filter the jobs we already loaded)
searchBtn.addEventListener("click", () => {
  const keyword = searchInput.value.trim().toLowerCase();

  const filtered = allJobs.filter(job =>
    (job.title || "").toLowerCase().includes(keyword) ||
    (job.location || "").toLowerCase().includes(keyword) ||
    (job.job_type || job.type || "").toLowerCase().includes(keyword)
  );

  renderJobs(filtered);
});

function viewDetails(id) {
 window.location.href = `/user/job.html?id=${id}`;  // actual path to job details page
}

function applyJob(id) {
  fetch(`${API_BASE}/user/jobs/${id}/apply`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: 1, // later from login/session
      resume_url: "Resume text or URL here"
    })
  })
    .then(res => res.json())
    .then(data => alert("Application submitted successfully!"))
    .catch(err => alert("Error submitting application."));
}

// ✅ Instead of renderJobs(sampleJobs), do this:
loadJobsFromBackend();

