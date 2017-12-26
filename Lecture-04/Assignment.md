**Python for web** assignment
=============================

1. Write a python script to fetch news from the web API given below and show news headlines to user.

	API details:
	- API Endpoint(URL) : https://gnewsapi.herokuapp.com
	- Parameters : 
		- **news**: Category of news. Available categories are: 
    
                ['business', 'politics', 'top stories', 'technology', 'world', 'sports', 'entertainment', 'national']
		
		- **geo-country**: Country of news. Available countries are: 
    
                ['Germany', 'Poland', 'Morocco', 'Colombia', 'India (Telugu)', 'Australia', 'Hungary', 'India (Malayalam)', 
                'United Arab Emirates', 'Lebanon', 'Serbia', 'Canada (English)', 'China', 'United States (English)', 
                'Nigeria', 'Austria', 'Kenya', 'Peru', 'Italy', 'Ghana', 'Ukraine (Russian)', 'Belgium (French)', 'Vietnam', 
                'South Africa', 'Ethiopia', 'Lithuania', 'Philippines', 'Brazil', 'Saudi Arabia', 'India (Hindi)', 'India (Tamil)',
                'United States (Spanish)', 'Latvia', 'Singapore', 'Norway', 'Sweden', 'Canada (French)', 'Egypt', 'Japan', 
                'Arab world', 'Ukraine (Ukranian)', 'Netherlands', 'Hong Kong', 'Romania', 'United Kingdom', 'Slovakia', 
                'Czech Republic', 'Chile', 'Indonesia', 'France', 'Bangladesh', 'Taiwan', 'Tanzania', 'Argentina', 'Greece', 
                'Mexico', 'Pakistan', 'Bulgaria', 'Senegal', 'Zimbabwe', 'Belgium (Dutch)', 'Uganda', 'Turkey', 'Portugal', 
                'Slovenia', 'Namibia', 'Cuba', 'New Zealand', 'Russia', 'India (English)', 'Botswana', 'Venezuela', 'Israel (Hebrew)',
                'Thailand', 'Switzerland', 'Israel (English)', 'Ireland', 'Malaysia']

		- **language**: Language of news. Available languages are: 
    
                ['tamil', 'kannada', 'norwegian', 'swedish', 'bulgarian', 'arabic', 'hindi', 'catalan', 'georgian', 'latvian',
                'albanian', 'japanese', 'english', 'german', 'lithuanian', 'chinese simplified', 'polish', 'czech', 'macedonian',
                'yiddish', 'turkish', 'dutch', 'urdu', 'serbian', 'basque', 'thai', 'hungarian', 'danish', 'galician', 'latin', 
                'chinese traditional', 'vietnamese', 'portuguese', 'welsh', 'croatian', 'bengali', 'finnish', 'icelandic', 
                'azerbaijani', 'swahili', 'malay', 'korean', 'slovak', 'russian', 'irish', 'spanish', 'belarusian', 'french',
                'estonian', 'indonesian', 'slovenian', 'italian', 'maltese', 'haitian creole', 'esperanto', 'ukrainian', 
                'afrikaans', 'filipino', 'gujarati', 'hebrew', 'telugu', 'greek', 'persian', 'romanian']

	- Output format : JSON



2. Write python script to use **HackerRank Code Checker API**.
	- Input: code, language, testcases
	- Output: Output of code.

	API docs: https://www.hackerrank.com/api/docs



3. Write a python script to fetch the present, future and past contest details from **Codechef** using **web scraping**.
	- URL: https://www.codechef.com/contests

	- Show data to user in tabular form. Check out [tabulate](https://pypi.python.org/pypi/tabulate) package.
      Install using the pip command:

      ```
      pip install tabulate
      ```


4. Write a python script to fetch latest ICC rankings and show them to user in tabular form.
	- URL: http://www.espncricinfo.com/rankings/content/page/211271.html



5. Modify **codechef.py** such that:
	- The code to be submitted is **read from a file**. The user must input the name of file to be submitted as well as the problem code.

	- Scrape the submission result page by fetching its HTML data. Use:
		```
		browser.page_source
		```
	  to fetch HTML data.
	  And then, show the final submission result to the user using python script itself!

	- Explore [pyvirtualdisplay](http://www.vionblog.com/selenium-headless-firefox-webdriver-using-pyvirtualdisplay/) to run the browser in background.
