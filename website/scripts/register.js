const API_URL = `https://falconia.fr:4242`

new VUE({
  el: '#app',
  data() {
    return {
      username: null,
      password: null
    }
  },
  methods: {
    async register(){
      resp = await fetch(`${API_URL}/add_user`, {
        method: 'POST',
        headers: {'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8'},
        body new URLSearchParams({
            username: this.username,
            password: this.password
        })
      })
    }
  }
})
