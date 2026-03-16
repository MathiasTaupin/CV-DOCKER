function toggleCategory(id) {

    const content = document.getElementById(id);

    // fermer les autres catégories
    document.querySelectorAll(".category-content").forEach(el => {
        if (el.id !== id) {
            el.classList.remove("active");
        }
    });

    // ouvrir / fermer celle cliquée
    content.classList.toggle("active");
}