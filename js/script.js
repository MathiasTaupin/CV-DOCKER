function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
        document.querySelector('.nav-links').classList.remove('active');
    }
}

// Fermer le menu quand on clique en dehors
document.addEventListener('click', function(event) {
    const nav = document.querySelector('nav');
    const navLinks = document.querySelector('.nav-links');
    if (!nav.contains(event.target) && navLinks.classList.contains('active')) {
        navLinks.classList.remove('active');
    }
});
