document.addEventListener("DOMContentLoaded", () => {
    console.log("EKPP Initialized: Ready to process published outputs.");

    const outputCards = document.querySelectorAll(".output-card");
    
    outputCards.forEach(card => {
        card.addEventListener("click", (e) => {
            const targetLink = card.querySelector(".output-link");
            if (targetLink && e.target !== targetLink) {
                window.location.href = targetLink.href;
            }
        });
    });
});