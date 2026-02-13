const footerPlaceholder = document.getElementById("footer-placeholder");

if (footerPlaceholder) {
  footerPlaceholder.innerHTML = `
    <footer class="footer">
      <div>
        <h4>About</h4>
        <p>WorkWay Careers helps you find your dream job.</p>
      </div>

      <div>
        <h4>Contact</h4>
        <p>Email: contact@workway.com</p>
        <p>Phone: +94 123 456 789</p>
      </div>

      <div>
        <h4>Terms</h4>
        <p><a href="#">Privacy Policy</a> | <a href="#">Terms & Conditions</a></p>
      </div>

      <div>
        <h4>Follow Us</h4>
        <p>
          <a href="#">Facebook</a> | <a href="#">LinkedIn</a> | <a href="#">Twitter</a>
        </p>
      </div>
    </footer>
  `;
}