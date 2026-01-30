const API_BASE = "http://localhost:5001";

// get job ID from URL (job.html?id=3)
const params = new URLSearchParams(window.location.search);
const jobId = params.get("id");

async function loadJobDetails(jobId) {
  const detailsContainer = document.getElementById("viewDetailsContainer");

  if (!jobId) {
    detailsContainer.innerHTML = `<p class="empty">Invalid job ID.</p>`;
    return;
  }

  try {
    const res = await fetch(`${API_BASE}/user/jobs/${jobId}`);
    if (!res.ok) throw new Error("Failed to load job details");

    const data = await res.json();
    const job = data.job;
    renderJobDetails(job);

  } catch (err) {
    console.error(err);
    detailsContainer.innerHTML = `
      <p class="empty">Error loading job details.</p>
    `;
  }
}

function renderJobDetails(job) {
  const detailsContainer = document.getElementById("viewDetailsContainer");
  detailsContainer.innerHTML = "";

  if (!job) {
    detailsContainer.innerHTML = `<p class="empty">Job not found.</p>`;
    return;
  }

  const card = document.createElement("div");
  card.classList.add("job-details-card");

  const id = job.job_id;
  const title = job.title;
  const company_name = job.company_name;
  const location = job.location;
  const type = job.job_type;
  const description = job.description;
  const closingDate = job.closing_date;
  

  card.innerHTML = `
    <h3>${title}</h3>
    <p><strong>Location:</strong> ${location}</p>
    <p><strong>Company:</strong> ${company_name}</p>
    <p><strong>Type:</strong> ${type}</p>
    <p><strong>Description:</strong> ${description}</p>
    <p><strong>Closing Date:</strong> ${closingDate}</p>
    <button class="btn apply-btn" data-job-id="${id}">Apply</button>
  `;

  detailsContainer.appendChild(card);
  
  const applyBtn = card.querySelector(".apply-btn");
  applyBtn.addEventListener("click", () => {
    window.location.href = `/user/apply.html?job_id=${id}`;
});
}



function applyJob(id) {
  window.location.href = `/user/apply.html?job_id=${id}`;
}

// load job details on page load
loadJobDetails(jobId);

