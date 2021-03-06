import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


keywords_apple = ["Apple", "Apple Inc"]

data = pd.read_csv('data/news.csv')
data = data.dropna()
data = (data[data.keywords.str.contains('|'.join(keywords_apple))])
data["timestamp"] = data["timestamp"].apply(lambda date: date[:10])
dateList = list(set(data['timestamp'].tolist()))
dateList.sort()


sia = SIA()
results = []
headlines = data["headline"].tolist()

for hl in headlines:
    pol_score = sia.polarity_scores(hl)
    if pol_score['compound'] >= 0.0:
        continue
    pol_score['headline'] = hl
    results.append(pol_score)

print(results[:20])

