class Cues(object):

	def __init__(self):

		techcrunchPhrases = ["sources", "we're hearing", 'TechCrunch has learned']

		bloombergPhrases = ['people familiar with the matter', 'person familiar with the matter', 
								'said the person', 'said the people', 'not authorized to speak']

		recodePhrases = ['multiple sources', 'one source']

		wsjPhrases = ['briefed on the matter', 'people familiar', 'person familiar']

		generalPhrases = ['hearing', 'source', 'sources', 'person familiar', 
							'people familiar', 'person', 'matter', 
							'has learned', 'not to be named', 'said the people']

		self.phrases = {'TechCrunch': techcrunchPhrases,
						'Bloomberg': bloombergPhrases,
						'Recode': recodePhrases,
						'WSJ': wsjPhrases,
						'General': generalPhrases
						}