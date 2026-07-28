document.addEventListener("DOMContentLoaded", function () {
  // 1. Create and inject the Burger Toggle Button
  const toggleBtn = document.createElement("button");
  toggleBtn.id = "menu-toggle";
  toggleBtn.className = "menu-toggle";
  toggleBtn.setAttribute("aria-label", "Toggle Navigation");
  toggleBtn.innerHTML = "☰";
  document.body.prepend(toggleBtn);

  // 2. Create and inject the Sidebar Navigation Drawer
  const sidebar = document.createElement("nav");
  sidebar.id = "docs-sidebar";
  sidebar.className = "docs-sidebar";
  sidebar.innerHTML = `
    <ul>
      <li><a href="index.html"><code>📄 Engineering Documentation System</code> (EDS)</a></li>
      <li><a href="eks.html"><code>🧠 Engineering Knowledge System</code> (EKS)</a></li>
      <li><a href="afk.html"><code>🤝 Assisted Flow of Knowledge)</code> (AFK)</a></li>
    </ul>
  `;
  document.body.insertBefore(sidebar, toggleBtn.nextSibling);

  // 3. Bind toggle behaviors
  toggleBtn.addEventListener("click", function () {
    sidebar.classList.toggle("active");
  });

  // Close sidebar automatically when clicking a navigation link
  sidebar.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", function() {
      sidebar.classList.remove("active");
    });
  });
});