const API_URL = `https://falconia.fr:4242`

let app = new Vue({
  el: '#app',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    async register(){
      resp = await fetch(`${API_URL}/add_user`, {
        method: 'POST',
        headers: {'Content-type': 'charset=UTF-8'},
        body: new URLSearchParams({
            username: this.username,
            password: this.password
        })
      }).then(reponse => reponse.json())
    }
  }
})
