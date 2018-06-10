console.log('hello there')

var categories = [
  {
    name: 'general',
    tags: [
    'atkinsdiet',
    'fatadapted',
    'guthealth',
    'hflc',
    'highfat',
    'keto',
    'ketodiet',
    'ketoexperiment',
    'ketofam',
    'ketogenicdiet',
    'ketogram',
    'ketojourney',
    'ketolife',
    'ketolondon',
    'ketones',
    'ketosis',
    'ketouk',
    'lchf',
    'lowcarbdiet',
    'lowcarbliving',
    ]
  },
  {
    name: 'keto_food',
    tags: [
      'brainfoods',
      'eatfat',
      'eatfatlosefat',
      'fooddairy',
      'foodporn',
      'healthyfats',
      'ketoeats',
      'ketofoods',
      'paleo',
      'primal',
    ],
  },
  {
    name: 'biohacking',
    tags: [
      'bebetter',
      'biohacking',
      'optimisation',
      'optimisation',
      'quantifiedself',
      'wellness',
    ]
  },
  {
    name: 'workout',
    tags: [
    'fatburner',
    'fatisfuel',
    'gymtime',
    'healthyhabits',
    'instafit',
    'ketogains',
    'ketonesforfuel',
    'ketoworkout',
    'leangains',
    'musclegain',
    ],
  },
  {
    name: 'fasting',
    tags: [
    'IF',
    'fasting',
    'intermittentfasting',
    'longevity',
    ]
  }
]

var app = new Vue({
  el: '#categories-app',
  data: {
    categories: categories,
    hashtags: '',
    checkedCategories: []
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
