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

- Developments in Financial Market section is removed due to the fact that it does not contain any opinions of policymakers. 
- Committee Policy Action section is removed from the process because it is the duplicate of FOMC statement.
- Display 20 most frequently addressed bigrams and trigrams of full texts
- Display 8 most frequently addresed bigrams and trigrams of sections.
- Sample charts of the July 2021 FOMC minutes

<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/bigram_fulltext_latest_minutes.png" width=50% height=50%>

-----
<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/bigram_staff_opinions_minutes.png" width=50% height=50%>

-----
<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/trigram_fulltext_latest_minutes.png" width=50% height=50%>

-----
<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/trigram_staff_opinions_minutes.png" width=50% height=50%>

4. Conduct bigram and trigram extraction from 2016 to 2021.

- Display the top 5 most frequently addressed bigrams and triagrms in yearly basis.

- Sample charts of the year 2020. 

-----
<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/2020_bigram.png" width=80% height=80%>

-----
<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/2020_trigram.png" width=80% height=80%>

5. Bigram and Trigram extractions from 2016 to 2021 by sections.

- Display the top 5 most frequently addressed bigrams and trigrams of four different section of the text.

- Smaple charts of the year 2020.

<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/2020_staff_review_finance_bigram.png" width=80% height=80%>
-----
<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/2020_staff_review_econ_bigram.png" width=80% height=80%>
-----
<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/2020_staff_outlook_bigram.png" width=80% height=80%>
-----
<img src="https://github.com/treksis/Fed_minutes_analysis/blob/main/img/2020_participatns_views_bigram.png" width=80% height=80%>
