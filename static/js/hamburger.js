document.addEventListener("DOMContentLoaded", () => {
    const menuIcon = document.getElementById("nav-icon1");
    const fullscreenMenu = document.getElementById("fullscreenMenu");
    const closeBtn = document.getElementById("closeBtn");

    if (menuIcon && fullscreenMenu) {
        // Ouvrir le menu lorsque l'icône hamburger est cliquée
        menuIcon.addEventListener("click", () => {
            menuIcon.classList.toggle("open"); // Ajoute l'animation au bouton
            fullscreenMenu.classList.toggle("show"); // Affiche le menu plein écran
        });
    }

    if (closeBtn && fullscreenMenu && menuIcon) {
        // Fermer le menu lorsque le bouton de fermeture est cliqué
        closeBtn.addEventListener("click", () => {
            menuIcon.classList.remove("open");
            fullscreenMenu.classList.remove("show");
        });
    }
});
