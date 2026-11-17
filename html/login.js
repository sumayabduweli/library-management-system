var loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", function(event) {
  event.preventDefault();

  var username = document.getElementById("username").value.trim();
  var password = document.getElementById("password").value;

  if (username === "" || password === "") {
    alert("Please enter both your username and password.");
  } else {
    window.location.href = "index.html";
  }
}  );
