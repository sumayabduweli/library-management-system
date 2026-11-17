const loginForm = document.querySelector("form");

if (loginForm) {
  loginForm.addEventListener("submit", function (event) {
    const username = loginForm.querySelector("[name='username']");
    const password = loginForm.querySelector("[name='password']");

    if (!username?.value.trim() || !password?.value) {
      event.preventDefault();
      alert("Please enter both your username and password.");
    }
  });
}
