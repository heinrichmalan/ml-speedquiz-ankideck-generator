import genanki

SpeedQuizNote = genanki.Model(
  1582166554,
  'Quiz Item',
  fields=[
    {'name': 'ImagePrompt'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<style>div { text-align: center; } img { width: 200px }</style> <div>{{ImagePrompt}}</div>',
      'afmt': '<style>div { text-align: center; } img { width: 200px }</style> {{FrontSide}}<hr id="answer"><div><h1>{{Answer}}</h1></div>',
    },
  ])