document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");

    const sourceFilter = document.getElementById("sourceFilter");

    const resultItems = document.querySelectorAll(".result-item");

    const noResults = document.getElementById("noResults");

    function filterItems() {

        if (!searchInput || !sourceFilter) {

            return;

        }

        const searchText = searchInput.value.toLowerCase();

        const selectedSource = sourceFilter.value;

        let visibleItems = 0;

        resultItems.forEach(function (item) {

            const text = item.textContent.toLowerCase();

            const source = item.dataset.source;

            const matchesSearch = text.includes(searchText);

            const matchesSource =

                selectedSource === "all" ||

                source === selectedSource;

            const visible = matchesSearch && matchesSource;

            item.hidden = !visible;

            if (visible) {

                visibleItems++;

            }

        });

        if (noResults) {

            noResults.hidden = visibleItems !== 0;

        }

    }

    if (searchInput) {

        searchInput.addEventListener("input", filterItems);

    }

    if (sourceFilter) {

        sourceFilter.addEventListener("change", filterItems);

    }

});
