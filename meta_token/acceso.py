from fastapi import FastAPI
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adsinsights import AdsInsights

app = FastAPI()


app_id = ""
app_secret = ""
access_token = ''
ad_account_id = ''

@app.get("/campaign_metrics/{campaign_id}")
async def get_campaign_metrics(campaign_id: str):
    
    FacebookAdsApi.init(app_id, app_secret, access_token)


    fields = [
        AdsInsights.Field.campaign_name,
        AdsInsights.Field.impressions,
        AdsInsights.Field.cost_per_thruplay,
        AdsInsights.Field.cost_per_impression,
        AdsInsights.Field.cost_per_inline_link_click,
    ]

   
    params = {
        'time_range': {'since': 'last_week', 'until': 'today'},
        'level': 'campaign',
    }

    
    insights = AdsInsights(ad_account_id).get(fields=fields, params=params)

    
    campaign_insights = [insight for insight in insights if insight.get('campaign_name') == campaign_id]

    return campaign_insights
