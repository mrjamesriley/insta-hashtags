var app = new Vue({
  el: '#categories-app',
  data: {
    hashtags: '',
    errorMessage: null,
    categories: [],
    checkedCategories: []
  },
  created: function() {
    let categoriesEndpoint = 'http://127.0.0.1:8000/categories/'

    this.$http.get(categoriesEndpoint).then(response => {
      this.categories = response.body
    }, response => {
      this.errorMessage = "Could not connect to server, please try again later."
    });

  },
  methods: {
    generate: function() {
      var sampledTags = _.flatten(_.map(this.checkedCategories, function(category) {
        return _.values(category.tags)
      }))

      var formattedTags = sampledTags.map(function(tag) {
        return "#" + tag
      })

      this.hashtags = _.sampleSize(formattedTags, 15).join(' ')
    }
  }
})
