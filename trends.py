from pytrends.request import TrendReq

def getMostTrending():
    pytrends = TrendReq(hl='en-US', tz=360)

    trending_df = pytrends.realtime_trending_searches(pn='IN')
    most_trending = trending_df.iloc[0, 0]
    return most_trending

if __name__ == "__main__":
    most_trending = getMostTrending()
    print(most_trending)