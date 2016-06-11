class Cues(object):

	def __init__(self):

		techcrunchPhrases = ["sources", "we're hearing", 'TechCrunch has learned']

		bloombergPhrases = ['people familiar with the matter', 'person familiar with the matter', 
								'said the person', 'said the people', 'not authorized to speak', 
								'people familiar', 'source', 'sources']

		recodePhrases = ['multiple sources', 'one source', 'sources said', 'sources']

		wsjPhrases = ['briefed on the matter', 'people familiar', 'person familiar']

		thevergePhrases = ["According to sources,", "sources", "various sources"]

		buzzfeedPhrases = ['person familiar', 'people familiar', 'sources', 'source',
								'source familiar', 'sources familiar']

		generalPhrases = ['person familiar', 'people familiar', 'source familiar', 
								'sources familiar']

		self.phrases = {'TechCrunch': techcrunchPhrases,
						'Bloomberg': bloombergPhrases,
						'Recode': recodePhrases,
						'WSJ': wsjPhrases,
						'The Verge': thevergePhrases,
						'BuzzFeed': buzzfeedPhrases,
						'General': generalPhrases
						}