var toggles = document.querySelectorAll(".c-hamburger");

for (var i = toggles.length - 1; i >= 0; i--) {
  var toggle = toggles[i];
  toggleHandler(toggle);
}

function toggleHandler(toggle) {
  toggle.addEventListener("click", function(e) {
    e.preventDefault();
    if (this.classList.contains("is-active") === true) {
      this.classList.remove("is-active");
      $('.navbar').removeClass('open');
    } else {
      this.classList.add("is-active");
      $('.navbar').addClass('open');
    }
  });
}

$(".navbar ul li a").click(function(event) {
  $(".navbar").removeClass('open');
  $(".c-hamburger").removeClass('is-active');
});