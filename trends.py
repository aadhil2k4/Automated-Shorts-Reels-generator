from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

trending_df = pytrends.trending_searches(pn='india')
most_trending = trending_df.iloc[0, 0]
print(most_trending)