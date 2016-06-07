class Cues(object):

	def __init__(self):

		techcrunchPhrases = ["sources", "we're hearing", 'TechCrunch has learned']

		bloombergPhrases = ['people familiar with the matter', 'person familiar with the matter', 
								'said the person', 'said the people', 'not authorized to speak']

		recodePhrases = ['multiple sources', 'one source']

		wsjPhrases = ['briefed on the matter', 'people familiar', 'person familiar']\

		thevergePhrases = ["According to sources,", "sources", "various sources"]

		generalPhrases = ['person familiar', 'people familiar', 'souce familiar', 
								'sources familiar']

		self.phrases = {'TechCrunch': techcrunchPhrases,
						'Bloomberg': bloombergPhrases,
						'Recode': recodePhrases,
						'WSJ': wsjPhrases,
						'The Verge': thevergePhrases,
						'General': generalPhrases
						}