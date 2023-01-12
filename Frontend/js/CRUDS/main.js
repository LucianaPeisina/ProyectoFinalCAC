if (document.getElementById("app")) {
    const { createApp } = Vue
 
    createApp({
        data() {

            return {
                noticias: [],
                page: 1,
                page: 1,
                errored: false,
                loading: true, 
                url: "http://lucianahpeisina.pythonanywhere.com/noticias"
               
            }
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.noticias = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },

            eliminar(noticia) {
                const url = 'http://lucianahpeisina.pythonanywhere.com/noticias/' + noticia;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        },

        
        created() {
            this.fetchData(this.url)
        }
        
        
    }).mount('#app')
}


