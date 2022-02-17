$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
    $("#menu-collapse-button").toggleClass("bx-align-left bx-x");
  });
});
