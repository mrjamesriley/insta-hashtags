var app = new Vue({
  el: '#categories-app',
  data: {
    hashtags: '',
    errorMessage: null,
    categories: [],
    checkedCategories: []
  },
  created: function() {
    let categoriesEndpoint = 'http://localhost:8000/categories'

    this.$http.get(categoriesEndpoint).then(response => {
      this.categories = response.body
    }, response => {
      this.errorMessage = "Could not connect to server, please try again later."
    });

  },
  methods: {
    generate: function() {
      var hashtags = _.flatten(_.map(this.checkedCategories, function(category) {
        return _.map(category.hashtags, function(hashtag) {
          return "#" + hashtag.name
        })
      }))

      this.hashtags = _.sampleSize(hashtags, 15).join(' ')
    }
  }
})
