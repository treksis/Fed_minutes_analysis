<h1>FOMC mintues analysis</h1>

1. Scrap FOMC minutes from the year 2016 to 2021.

2. Clean up FOMC minutes text into JSON format. 

Headers of file are following:

- 'Developments in Financial Markets and Open Market Operations'
- 'Staff Review of the Economic Situation'
- 'Staff Review of the Financial Situation'
- 'Staff Economic Outlook'
- "Participants' Views on Current Economic Conditions and the Economic Outlook"
- 'Committee Policy Action'

3. Conduct bigram and trigram analysis on the text sets.

- Developments in Financial Market section is deleted due to the fact that it does not contain any opinions of policymakers. 
- Committee Policy Action section is deleted from the process because it is the duplicate of FOMC statement.
- Display 20 most frequently addressed bigrams and trigrams of full texts
- Display 8 most freqnetly addresed bigrams and trigrams of sections.

![alt text](img\bigram_fulltext_latest_minutes.png)
![alt text](img\bigram_staff_opinions_minutes.png)
![alt text](img\trigram_fulltext_latest_minutes.png)
![alt text](img\trigram_staff_opinions_minutes.png)