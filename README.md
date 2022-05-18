# Readable News: Readability of News Over Time

Has the news become more readable over time? We use the [NYT Corpus](https://github.com/notnews/nytimes-corpus-extractor) as our main data source to assess how the complexity of news articles has evolved over time. We supplement this data using (i) [CNN transcripts](https://github.com/notnews/cnn_transcripts), (ii) [NPR transcripts](https://github.com/zcgzcgzcg1/MediaSum/tree/main/data), and (iii) [MSNBC transcripts](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FUPJDE1).

We use the [Python package py-readability-metrics](https://pypi.org/project/py-readability-metrics/) to estimate where each article lies on the Flesch Reading Ease scale, Flesch-Kincaid Grade Level Scale, The Fog Scale, and the SMOG scale, along with the number of words, and such. We also use the [Python package LexicalRichness](https://pypi.org/project/lexicalrichness/) to estimate lexical richness.

### NYT is least readable

Overall, we find NYT the most ~~highbrow~~ rarefied in taste out of the four news outlets. 
NTY has the lowest readability score, with articles requiring higher language competency. On the other hand, NYT also has a higher usage of unique terms (possibly more jargon). 
Even so, the readability of NYT articles has increased while the other three news outlets (CNN, NPR, MSNBC) have either remained mostly the same or decreased over time. Hence, the trend in NYT's readability suggests they feel the competition from alternative news sources, both traditional and untraditional. Our findings suggest NYT is threading the line to increase accessibility while maintaining its key demographic of college-educated Americans.

### Data and coverage

NYT article data is available for 1987&ndash;2007 (21 years):

<p align="center"><img width="60%" src="figs/data_coverage/nyt_monthyear.png"></p>

At a finer resolution, we can see that the Sunday newspaper has more articles than the weekday editions, and increasingly so. Below is a plot for two full years of NYT data coverage:

<p align="center"><img width="60%" src="figs/data_coverage/nyt_dowmonth_1987.png"></p>

<p align="center"><img width="60%" src="figs/data_coverage/nyt_dowmonth_2006.png"></p>

Before computing the text statistics (readability & lexical richness), we do some basic text pre-processing. For the plots of readability and lexical richness, we also drop: (i) the 99th percentile in text length and (ii) the 1st percentile in text length or articles with fewer than 100 words, whichever is lower.


### What we find
1. We use simple methods in computational linguistics to characterize NYT articles.
While the average NYT article length has increased over time, so has readability and lexical richness. Uinsg alternative measures of readability and lexical richness lead to similar findings.

    * Average NYT article length has increased over the years to ~675 words in 2007 (an average reading time of 2–3 minutes):
      <details>
        <summary><em>Figure notes</em></summary>
        <em>Each marker is an average of NYT articles for each month-year. Red line is a LOWESS (locally weighted scatterplot smoothing) with a generous smoothing bandwidth.</em>
      </details>

    <p align="center"><img width="55%" src="figs/nyt_wordcount.png"></p>

    * Unique number of words per NYT article has also increased over time:
      <details>
        <summary><em>Figure notes</em></summary>
        <em>Each marker is an average of NYT articles for each month-year. Red line is a LOWESS (locally weighted scatterplot smoothing) with a generous smoothing bandwidth.</em>
      </details>

    <p align="center"><img width="55%" src="figs/nyt_uniquewords.png"></p>
    
    * Wordcount and unique words per NYT article moves together over time. Does this mean the lexical richness of NYT articles are steady over time as article length has increased? Our results on lexical richness below suggest a steady increase in lexical richness.
      <details>
        <summary><em>Figure notes</em></summary>
        <em>Each marker is an annual average of NYT articles. Both lines are indexed to 1987—the first year of our sample—so that each subsequent marker indicates annual percentage change since the base year of 1987.</em>
      </details>    
    <p align="center"><img width="55%" src="figs/nyt_words_uniquewords.png"></p>

2. Our main measure of readability is the [Flesch Reading-Ease measure](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests). This measure is inversely related to the average number of syllables per word and the average number of words per sentence. A higher measure indicates higher ease of reading. A higher Flesch measure indicates higher ease of reading.

    * Our figure below shows an increase in readability from 1987 till the turn of the millennium by about 4 points. 
For a sense of scale, a 10-point gap in Flesch reading ease can separate US grades.
At the end of our sample, the average NYT article has a level of readability that is considered fairly difficult: a level understandable for 10th&ndash;12th grade students.
      <details>
        <summary><em>Figure notes</em></summary>
        <em>Each marker is an average of NYT articles for each month-year. NYT articles with word count in the top and bottom one percentile are dropped. Red line is a LOWESS (locally weighted scatterplot smoothing) with a generous smoothing bandwidth.</em>
      </details>
      
    <p align="center"><img width="55%" src="figs/nyt_readability_flesch_ease.png"></p>
    
    * We get similar findings using the [SMOG](https://en.wikipedia.org/wiki/SMOG) (Simple Measure of Gobbledygook) readability index. This measure depends on the number of sentences and polysyllabic words. The higher the numbers, the less readable. 
      <details>
        <summary><em>Figure notes</em></summary>
        <em>Each marker is an annual average of NYT articles. NYT articles with word count in the top and bottom one percentile are dropped. Both lines are indexed to 1987—the first year of our sample—so that each subsequent marker indicates annual percentage change since the base year of 1987.</em>
      </details>    
      
    <p align="center"><img width="55%" src="figs/nyt_readability_index.png"></p>


3. Our main measure for the lexical richness (also called [lexical diversity](https://en.wikipedia.org/wiki/Lexical_diversity)) of the average NYT article is the MTLD ([Measure of Lexical Diversity (McCarthy 2005, McCarthy and Jarvis 2010)](https://github.com/lsys/lexicalrichness)). 
MTLD measures lexical richness using the mean length of sequential words in a text that can maintain a minimal level of type-token ratio (TTR, also known as text-type ratio). This ratio is simply the number of unique words divided by total words. A higher value indicates higher lexical richness.

    * We find an increase in lexical richness for the average NYT article, with the uptrend persisting towards the end of our sample in 2007. We deem the 40% increase over 21 years as non-trivial.
      <details>
        <summary>Figure notes</summary>
        <em>Each marker is an average of NYT articles for each month-year. NYT articles with word count in the top and bottom one percentile are dropped. Red line is a LOWESS (locally weighted scatterplot smoothing) with a generous smoothing bandwidth.</em>
      </details>    
      
    <p align="center"><img width="55%" src="figs/nyt_lexicalrichness_mtld.png"></p>

    * An alternative measure is simply the TTR (type-token ratio). The benefit of this measure is that it's intuitive where the MTLD is less so but more robust to varying text lengths. Both suggest an increase in lexical richness.
      <details>
        <summary><em>Figure notes</em></summary>
        <em>Each marker is an annual average of NYT articles. NYT articles with word count in the top and bottom one percentile are dropped. Both lines are indexed to 1987—the first year of our sample—so that each subsequent marker indicates annual percentage change since the base year of 1987.</em>
      </details>    
      
    <p align="center"><img width="55%" src="figs/nyt_lexicalrichness_index.png"></p>

4. Using data for three other outlets (CNN 2001&ndash;2022, NPR 2005&ndash;2019, and MSNBC 2003&ndash;2021), we see that NYT is the least readable while being the most lexically rich. 
For instance, NYT has an average of ~50 while CNN has an average of ~70 for the Flesch reading ease score. This 20-point difference is stark. A score of 50 is at the more readable tail of the US college level ((50&ndash;30)), which is the key NYT demographic. A score of ~70, on the other hand, is at the more readable tail of the 8th&ndash;9th grade in US school level reading level (70&ndash;60). In other words, the difference in readability between NYT and CNN is years of education.

<p align="center">
  <img alt="Light" src="figs/readability_nyt_cnn_npr_msnbc.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Dark" src="figs/lexicalrichness_nyt_cnn_npr_msnbc.png" width="45%">
</p>
