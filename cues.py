class Cues(object):

	def __init__(self):

		techcrunchPhrases = ["sources", "we're hearing", 'TechCrunch has learned']

		bloombergPhrases = ['people familiar with the matter', 'person familiar with the matter', 
								'said the person', 'said the people', 'not authorized to speak', 
								'people familiar', 'source', 'sources']

		recodePhrases = ['multiple sources', 'one source', 'sources said', 'according to multiple sources',
							'according to sources', 'according to a source']

		wsjPhrases = ['briefed on the matter', 'people familiar', 'person familiar']

		thevergePhrases = ["According to sources,", "sources", "various sources"]

		buzzfeedPhrases = ['person familiar', 'people familiar', 'sources', 'source',
								'source familiar', 'sources familiar']

		reutersPhrases = ['people with knowledge of the matter', 'person with knowledge of the matter',
								'sources said', 'source said']

		generalPhrases = ['person familiar', 'people familiar', 'source familiar', 
								'sources familiar']

		self.publications = ["recode", "techcrunch", "bloomberg", "theinformation", "vanityfair", 
								"mic", "venturebeat", "arstechnica", "motherboard", "ap", "fusion",
									"anandtech", "engadget", "latimes", "buzzfeed", "wsj", "theverge", 
									"backchannel", "adage", "medium", "govinsider", "cnet", "reuters",
									"pcworld", "statnews", "slack", "nytimes"]

		self.pubcap = {'recode': 'Recode', 'techcrunch': 'TechCrunch', 'bloomberg': 'Bloomberg', 
						'theinformation': 'The Information', 'vanityfair': 'Vanity Fair',
						'mic': 'Mic', 'venturebeat': 'VentureBeat', 'arstechnica': 'Ars Technica',
						'motherboard': 'Vice Motherboard', 'ap': 'Associated Press',
						'fusion': 'Fusion', 'anandtech': 'AnandTech', 'engadget': 'Engadget',
						'latimes': 'Los Angeles Times', 'buzzfeed': 'BuzzFeed', 
						'wsj': 'The Wall Street Journal', 'theverge': 'The Verge', 'backchannel': 'Backchannel',
						'adage': 'Ad Age', 'medium': 'Medium', 'cnet': 'CNET', 'reuters': 'Reuters',
						'pcworld': "PCWorld", "statnews": "STAT", "Not found": "Couldn't find publication.",
						"slack": "Slack blog", "nytimes": "The New York Times"}

		self.phrases = {'TechCrunch': techcrunchPhrases,
						'Reuters': reutersPhrases,
						'Bloomberg': bloombergPhrases,
						'Recode': recodePhrases,
						'WSJ': wsjPhrases,
						'The Verge': thevergePhrases,
						'BuzzFeed': buzzfeedPhrases,
						'General': generalPhrases
						}