document.getElementById("sentimentAnalyseSubmit").addEventListener("submit", function(event) {
        event.preventDefault(); // Formun varsayılan davranışını engelle

        var formData = new FormData(this);

        // Ajax isteği yap
        fetch(window.location.href, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("analyseResult").innerHTML = data.result;
                // Sonuç gösterme işlemleri burada yapılacak
            })
            .catch(error => {
                console.error('Hata:', error);
            });
    });