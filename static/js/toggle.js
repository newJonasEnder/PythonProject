document.addEventListener("DOMContentLoaded", function () {
    const headers = document.querySelectorAll(".inline-group h2");

    headers.forEach((header) => {
        header.style.cursor = "pointer";
        const content = header.nextElementSibling;

        if (!content) return;

        // CSS-Klasse "hidden" definieren und standardmäßig setzen
        content.classList.add("hidden");

        header.addEventListener("click", () => {
            content.classList.toggle("hidden");
        });
    });
});
