from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

host = ""
app = Flask(__name__)
CORS(app)
url = "mysql+pymysql://root@localhost:3306/supermetrics_api"

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "SUPERMETRICSWOL"

db = SQLAlchemy(app)
ma = Marshmallow(app)
base = db.Model.metadata.reflect(db.engine)

session = Session(db.engine, future=True)

datos_insertados = 0


class google_metrics(db.Model):
    __table__ = db.Model.metadata.tables["gg_campana"]

    def __init__(self, account_id,
                 account,
                 campaign_name,
                 campaign_status,
                 bidding_strategy_type,
                 year_and_month,
                 start_date,
                 end_date,
                 date,
                 impressions,
                 clicks,
                 cost,
                 cost_usd,
                 ctr,
                 cpc,
                 cpm,
                 budget,
                 daily_budget,
                 return_on_ad_spend,
                 cost_per_video_view,
                 video_views,
                 watch_75_rate,
                 conversions,
                 conversion_rate,
                 cost_per_conversion,
                 impression_share,
                 search_impression_share,
                 ):
        self.account_id = account_id
        self.account = account
        self.campaign_name = campaign_name
        self.campaign_status = campaign_status
        self.bidding_strategy_type = bidding_strategy_type
        self.year_and_month = year_and_month
        self.start_date = start_date
        self.end_date = end_date
        self.date = date
        self.impressions = impressions
        self.clicks = clicks
        self.cost = cost
        self.cost_usd = cost_usd
        self.ctr = ctr
        self.cpc = cpc
        self.cpm = cpm
        self.budget = budget
        self.daily_budget = daily_budget
        self.return_on_ad_spend = return_on_ad_spend
        self.cost_per_video_view = cost_per_video_view
        self.video_views = video_views
        self.watch_75_rate = watch_75_rate
        self.conversions = conversions
        self.conversion_rate = conversion_rate
        self.cost_per_conversion = cost_per_conversion
        self.impression_share = impression_share
        self.search_impression_share = search_impression_share


class linkedin_metrics(db.Model):
    __table__ = db.Model.metadata.tables["link_campana"]

    def __init__(self,
                 account_name,
                 account_id,
                 campaign_name,
                 campaign_status,
                 campaign_start_date,
                 campaign_end_date,
                 campaign_total_budget,
                 campaign_objective_type,
                 campaign_cost_type,
                 campaign_group_name,
                 campaign_group_status,
                 campaign_group_start_date,
                 campaign_group_end_date,
                 campaign_group_total_budget,
                 year_and_month,
                 date,
                 impressions,
                 clicks,
                 ctr,
                 cpc,
                 cpm,
                 total_spent_usd,
                 opens,
                 sends,
                 action_clicks,
                 conversions,
                 cost_per_conversion,
                 video_views_at_75,
                 video_views
                 ):

        self.account_name = account_name
        self.account_id = account_id
        self.campaign_name = campaign_name
        self.campaign_status = campaign_status
        self.campaign_start_date = campaign_start_date
        self.campaign_end_date = campaign_end_date
        self.campaign_total_budget = campaign_total_budget
        self.campaign_objective_type = campaign_objective_type
        self.campaign_cost_type = campaign_cost_type
        self.campaign_group_name = campaign_group_name
        self.campaign_group_status = campaign_group_status
        self.campaign_group_start_date = campaign_group_start_date
        self.campaign_group_end_date = campaign_group_end_date
        self.campaign_group_total_budget = campaign_group_total_budget
        self.year_and_month = year_and_month
        self.date = date
        self.impressions = impressions
        self.clicks = clicks
        self.ctr = ctr
        self.cpc = cpc
        self.cpm = cpm
        self.total_spent_usd = total_spent_usd
        self.opens = opens
        self.sends = sends
        self.action_clicks = action_clicks
        self.conversions = conversions
        self.cost_per_conversion = cost_per_conversion
        self.video_views_at_75 = video_views_at_75
        self.video_views = video_views


class fb_region(db.Model):
    __table__ = db.Model.metadata.tables["fb_region"]

    def __init__(self, campaign_name,
                 ad_set_name,
                 country,
                 region,
                 date,
                 reach,
                 frequency,
                 impressions,
                 return_on_ad_spend,
                 cost_per_lead_form,
                 cost_per_store_visit,
                 cost,
                 cost_usd,
                 cpm,
                 outbound_clicks,
                 link_clicks,
                 outbound_ctr,
                 page_likes,
                 new_messaging_conversations,
                 cost_per_new_messaging_conversation,
                 video_watches_at_75,
                 estimated_ad_recall_lift_rate,
                 desktop_app_installs,
                 desktop_app_uses,
                 cost_per_app_install,
                 post_engagements,
                 website_leads,
                 website_purchases,
                 website_adds_to_cart,
                 mobile_app_installs,
                 on_facebook_leads,
                 video_watches_at_100
                 ):
        self.campaign_name = campaign_name
        self.ad_set_name = ad_set_name
        self.country = country
        self.region = region
        self.date = date
        self.reach = reach
        self.frequency = frequency
        self.impressions = impressions
        self.return_on_ad_spend = return_on_ad_spend
        self.cost_per_lead_form = cost_per_lead_form
        self.cost_per_store_visit = cost_per_store_visit
        self.cost = cost
        self.cost_usd = cost_usd
        self.cpm = cpm
        self.outbound_clicks = outbound_clicks
        self.link_clicks = link_clicks
        self.outbound_ctr = outbound_ctr
        self.page_likes = page_likes
        self.new_messaging_conversations = new_messaging_conversations
        self.cost_per_new_messaging_conversation = cost_per_new_messaging_conversation
        self.video_watches_at_75 = video_watches_at_75
        self.estimated_ad_recall_lift_rate = estimated_ad_recall_lift_rate
        self.desktop_app_installs = desktop_app_installs
        self.desktop_app_uses = desktop_app_uses
        self.cost_per_app_install = cost_per_app_install
        self.post_engagements = post_engagements
        self.website_leads = website_leads
        self.website_purchases = website_purchases
        self.website_adds_to_cart = website_adds_to_cart
        self.mobile_app_installs = mobile_app_installs
        self.on_facebook_leads = on_facebook_leads
        self.video_watches_at_100 = video_watches_at_100


class fb_edad_gen(db.Model):
    __table__ = db.Model.metadata.tables["fb_edad_gen"]

    def __init__(self, campaign_name,
                 ad_set_name,
                 gender,
                 age,
                 date,
                 reach,
                 frequency,
                 impressions,
                 return_on_ad_spend,
                 cost_per_lead_form,
                 cost_per_store_visit,
                 cost,
                 cost_usd,
                 cpm,
                 outbound_clicks,
                 link_clicks,
                 outbound_ctr,
                 page_likes,
                 new_messaging_conversations,
                 cost_per_new_messaging_conversation,
                 estimated_ad_recall_lift_rate,
                 desktop_app_installs,
                 desktop_app_uses,
                 cost_per_app_install,
                 post_engagements,
                 website_leads,
                 website_purchases,
                 website_adds_to_cart,
                 mobile_app_installs,
                 on_facebook_leads,
                 video_watches_at_100
                 ):
        self.campaign_name = campaign_name
        self.ad_set_name = ad_set_name
        self.gender = gender
        self.age = age
        self.date = date
        self.reach = reach
        self.frequency = frequency
        self.impressions = impressions
        self.return_on_ad_spend = return_on_ad_spend
        self.cost_per_lead_form = cost_per_lead_form
        self.cost_per_store_visit = cost_per_store_visit
        self.cost = cost
        self.cost_usd = cost_usd
        self.cpm = cpm
        self.outbound_clicks = outbound_clicks
        self.link_clicks = link_clicks
        self.outbound_ctr = outbound_ctr
        self.page_likes = page_likes
        self.new_messaging_conversations = new_messaging_conversations
        self.cost_per_new_messaging_conversation = cost_per_new_messaging_conversation
        self.estimated_ad_recall_lift_rate = estimated_ad_recall_lift_rate
        self.desktop_app_installs = desktop_app_installs
        self.desktop_app_uses = desktop_app_uses
        self.cost_per_app_install = cost_per_app_install
        self.post_engagements = post_engagements
        self.website_leads = website_leads
        self.website_purchases = website_purchases
        self.website_adds_to_cart = website_adds_to_cart
        self.mobile_app_installs = mobile_app_installs
        self.on_facebook_leads = on_facebook_leads
        self.video_watches_at_100 = video_watches_at_100


class fb_campana(db.Model):
    __table__ = db.Model.metadata.tables["fb_campana"]

    def __init__(self, account,
                 campaign_name,
                 campaign_start_date,
                 campaign_end_date,
                 campaign_status,
                 campaign_objective,
                 campaign_buying_type,
                 campaign_daily_budget,
                 campaign_lifetime_budget,
                 campaign_budget_remaining,
                 campaign_start_time,
                 campaign_end_time,
                 ad_set_name,
                 date,
                 reach,
                 frequency,
                 impressions,
                 social_reach,
                 total_action_value,
                 return_on_ad_spend,
                 cost_per_lead_form,
                 cost_per_store_visit,
                 cost,
                 cost_usd,
                 cost_per_1000_people_reached,
                 cpm,
                 cpa,
                 outbound_clicks,
                 link_clicks,
                 outbound_ctr,
                 cost_per_outbound_click,
                 page_likes,
                 new_messaging_conversations,
                 cost_per_new_messaging_conversation,
                 _15_second_video_views,
                 video_watches_at_75,
                 cost_per_thruplay,
                 estimated_ad_recall_lift_rate,
                 desktop_app_installs,
                 desktop_app_uses,
                 cost_per_app_install,
                 omni_adds_to_cart_shared_item,
                 omni_purchase_shared_item,
                 post_engagements,
                 actions,
                 three_second_video_views,
                 website_leads,
                 website_purchases,
                 website_adds_to_cart,
                 mobile_app_installs,
                 on_facebook_leads,
                 video_watches_at_100,
                 ):
        self.account = account
        self.campaign_name = campaign_name
        self.campaign_start_date = campaign_start_date
        self.campaign_end_date = campaign_end_date
        self.campaign_status = campaign_status
        self.campaign_objective = campaign_objective
        self.campaign_buying_type = campaign_buying_type
        self.campaign_daily_budget = campaign_daily_budget
        self.campaign_lifetime_budget = campaign_lifetime_budget
        self.campaign_budget_remaining = campaign_budget_remaining
        self.campaign_start_time = campaign_start_time
        self.campaign_end_time = campaign_end_time
        self.ad_set_name = ad_set_name
        self.date = date
        self.reach = reach
        self.frequency = frequency
        self.impressions = impressions
        self.social_reach = social_reach
        self.total_action_value = total_action_value
        self.return_on_ad_spend = return_on_ad_spend
        self.cost_per_lead_form = cost_per_lead_form
        self.cost_per_store_visit = cost_per_store_visit
        self.cost = cost
        self.cost_usd = cost_usd
        self.cost_per_1000_people_reached = cost_per_1000_people_reached
        self.cpm = cpm
        self.cpa = cpa
        self.outbound_clicks = outbound_clicks
        self.link_clicks = link_clicks
        self.outbound_ctr = outbound_ctr
        self.cost_per_outbound_click = cost_per_outbound_click
        self.page_likes = page_likes
        self.new_messaging_conversations = new_messaging_conversations
        self.cost_per_new_messaging_conversation = cost_per_new_messaging_conversation
        self._15_second_video_views = _15_second_video_views
        self.video_watches_at_75 = video_watches_at_75
        self.cost_per_thruplay = cost_per_thruplay
        self.estimated_ad_recall_lift_rate = estimated_ad_recall_lift_rate
        self.desktop_app_installs = desktop_app_installs
        self.desktop_app_uses = desktop_app_uses
        self.cost_per_app_install = cost_per_app_install
        self.omni_adds_to_cart_shared_item = omni_adds_to_cart_shared_item
        self.omni_purchase_shared_item = omni_purchase_shared_item
        self.post_engagements = post_engagements
        self.actions = actions
        self.three_second_video_views = three_second_video_views
        self.website_leads = website_leads
        self.website_purchases = website_purchases
        self.website_adds_to_cart = website_adds_to_cart
        self.mobile_app_installs = mobile_app_installs
        self.on_facebook_leads = on_facebook_leads
        self.video_watches_at_100 = video_watches_at_100


class fb_plataforma(db.Model):
    __table__ = db.Model.metadata.tables["fb_plataforma"]

    def __init__(self,
                 campaign_name,
                 ad_set_name,
                 placement,
                 publisher_platform,
                 platform_position,
                 device_platform,
                 date,
                 reach,
                 frequency,
                 impressions,
                 return_on_ad_spend,
                 cost_per_lead_form,
                 cost_per_store_visit,
                 cost,
                 cost_usd,
                 cpm,
                 outbound_clicks,
                 link_clicks,
                 outbound_ctr,
                 page_likes,
                 new_messaging_conversations,
                 cost_per_new_messaging_conversation,
                 video_watches_at_75,
                 estimated_ad_recall_lift_rate,
                 desktop_app_installs,
                 desktop_app_uses,
                 cost_per_app_install,
                 post_engagements,
                 website_leads,
                 website_purchases,
                 website_adds_to_cart,
                 mobile_app_installs,
                 on_facebook_leads,
                 video_watches_at_100):

        self.campaign_name = campaign_name
        self.ad_set_name = ad_set_name
        self.placement = placement
        self.publisher_platform = publisher_platform
        self.platform_position = platform_position
        self.device_platform = device_platform
        self.date = date
        self.reach = reach
        self.frequency = frequency
        self.impressions = impressions
        self.return_on_ad_spend = return_on_ad_spend
        self.cost_per_lead_form = cost_per_lead_form
        self.cost_per_store_visit = cost_per_store_visit
        self.cost = cost
        self.cost_usd = cost_usd
        self.cpm = cpm
        self.outbound_clicks = outbound_clicks
        self.link_clicks = link_clicks
        self.outbound_ctr = outbound_ctr
        self.page_likes = page_likes
        self.new_messaging_conversations = new_messaging_conversations
        self.cost_per_new_messaging_conversation = cost_per_new_messaging_conversation
        self.video_watches_at_75 = video_watches_at_75
        self.estimated_ad_recall_lift_rate = estimated_ad_recall_lift_rate
        self.desktop_app_installs = desktop_app_installs
        self.desktop_app_uses = desktop_app_uses
        self.cost_per_app_install = cost_per_app_install
        self.post_engagements = post_engagements
        self.website_leads = website_leads
        self.website_purchases = website_purchases
        self.website_adds_to_cart = website_adds_to_cart
        self.mobile_app_installs = mobile_app_installs
        self.on_facebook_leads = on_facebook_leads
        self.video_watches_at_100 = video_watches_at_100


class fb_anuncio(db.Model):
    __table__ = db.Model.metadata.tables["fb_anuncio"]

    def __init__(self, campaign_name,
                 ad_set_name,
                 ad_set_status,
                 ad_name,
                 ad_status,
                 ad_set_start_time,
                 ad_set_end_time,
                 attribution_setting,
                 ad_preview_url_desktop_feed,
                 ad_preview_url_mobile_feed,
                 ad_preview_url_facebook_story,
                 ad_preview_url_instagram_story,
                 ad_preview_url_instagram,
                 destination_url,
                 ad_creative_thumbnail_url,
                 ad_creative_image_url,
                 link_to_promoted_post,
                 link_to_promoted_instagram_post,
                 quality_ranking_text,
                 relevance_score_status,
                 reach_estimate_monthly_active_users,
                 date,
                 reach,
                 frequency,
                 impressions,
                 social_reach,
                 total_action_value,
                 return_on_ad_spend,
                 cost_per_lead_form,
                 cost_per_store_visit,
                 cost,
                 cost_usd,
                 cost_per_1000_people_reached,
                 cpm,
                 cpa,
                 outbound_clicks,
                 link_clicks,
                 outbound_ctr,
                 cost_per_outbound_click,
                 page_likes,
                 new_messaging_conversations,
                 cost_per_new_messaging_conversation,
                 _15_second_video_views,
                 video_watches_at_75,
                 cost_per_thruplay,
                 estimated_ad_recall_lift_rate,
                 desktop_app_installs,
                 desktop_app_uses,
                 cost_per_app_install,
                 omni_adds_to_cart_shared_item,
                 omni_purchase_shared_item,
                 post_engagements,
                 actions,
                 three_second_video_views,
                 website_leads,
                 website_purchases,
                 website_adds_to_cart,
                 mobile_app_installs,
                 on_facebook_leads,
                 video_watches_at_100):

        self.campaign_name = campaign_name
        self.ad_set_name = ad_set_name
        self.ad_set_status = ad_set_status
        self.ad_name = ad_name
        self.ad_status = ad_status
        self.ad_set_start_time = ad_set_start_time
        self.ad_set_end_time = ad_set_end_time
        self.attribution_setting = attribution_setting
        self.ad_preview_url_desktop_feed = ad_preview_url_desktop_feed
        self.ad_preview_url_mobile_feed = ad_preview_url_mobile_feed
        self.ad_preview_url_facebook_story = ad_preview_url_facebook_story
        self.ad_preview_url_instagram_story = ad_preview_url_instagram_story
        self.ad_preview_url_instagram = ad_preview_url_instagram
        self.destination_url = destination_url
        self.ad_creative_thumbnail_url = ad_creative_thumbnail_url
        self.ad_creative_image_url = ad_creative_image_url
        self.link_to_promoted_post = link_to_promoted_post
        self.link_to_promoted_instagram_post = link_to_promoted_instagram_post
        self.quality_ranking_text = quality_ranking_text
        self.relevance_score_status = relevance_score_status
        self.reach_estimate_monthly_active_users = reach_estimate_monthly_active_users
        self.date = date
        self.reach = reach
        self.frequency = frequency
        self.impressions = impressions
        self.social_reach = social_reach
        self.total_action_value = total_action_value
        self.return_on_ad_spend = return_on_ad_spend
        self.cost_per_lead_form = cost_per_lead_form
        self.cost_per_store_visit = cost_per_store_visit
        self.cost = cost
        self.cost_usd = cost_usd
        self.cost_per_1000_people_reached = cost_per_1000_people_reached
        self.cpm = cpm
        self.cpa = cpa
        self.outbound_clicks = outbound_clicks
        self.link_clicks = link_clicks
        self.outbound_ctr = outbound_ctr
        self.cost_per_outbound_click = cost_per_outbound_click
        self.page_likes = page_likes
        self.new_messaging_conversations = new_messaging_conversations
        self.cost_per_new_messaging_conversation = cost_per_new_messaging_conversation
        self._15_second_video_views = _15_second_video_views
        self.video_watches_at_75 = video_watches_at_75
        self.cost_per_thruplay = cost_per_thruplay
        self.estimated_ad_recall_lift_rate = estimated_ad_recall_lift_rate
        self.desktop_app_installs = desktop_app_installs
        self.desktop_app_uses = desktop_app_uses
        self.cost_per_app_install = cost_per_app_install
        self.omni_adds_to_cart_shared_item = omni_adds_to_cart_shared_item
        self.omni_purchase_shared_item = omni_purchase_shared_item
        self.post_engagements = post_engagements
        self.actions = actions
        self.three_second_video_views = three_second_video_views
        self.website_leads = website_leads
        self.website_purchases = website_purchases
        self.website_adds_to_cart = website_adds_to_cart
        self.mobile_app_installs = mobile_app_installs
        self.on_facebook_leads = on_facebook_leads
        self.video_watches_at_100 = video_watches_at_100


@app.route(host+'/google', methods=['GET'])
def index():
    try:
        datos_insertados = 0

        # Gestion de Fechas
        hoy = datetime.strftime(datetime.now(), '%Y-%m-%d')
        ayer = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        #########################################################

        url = f"https://aws1-api-dwh.supermetrics.com/enterprise/v2/query/data/json?json=%7B%22ds_id%22%3A%22AW%22%2C%22ds_accounts%22%3A%222407232949%2C2285540917%2C1361834813%2C8334020145%2C5340596231%2C6100337025%22%2C%22ds_user%22%3A%22reporting.omd%40gmail.com%22%2C%22start_date%22%3A%22{ayer}%22%2C%22end_date%22%3A%22{ayer}%22%2C%22fields%22%3A%22profileID%2Cprofile%2CCampaignname%2CCampaignstatus%2CBiddingstrategyType%2CYearmonth%2CstartDate%2CendDate%2CDate%2CImpressions%2CClicks%2CCost%2CCost_usd%2CCtr%2CCPC%2CCPM%2CBudget%2Cdailybudget%2CROAS%2CCostPerVideoView%2Cvideoviews%2CVideoQuartile75Rate%2CConversions%2CConversionRate%2CCostPerConversion%2CImpressionShare%2CSearchImpressionShare%22%2C%22settings%22%3A%7B%22blanks_to_zero%22%3Atrue%2C%22exclude_invalid_accounts%22%3Atrue%2C%22asset_level%22%3A%22ASSET_LEVEL_DEFAULT%22%2C%22allow_sum_unique%22%3Atrue%7D%2C%22max_rows%22%3A1000000%2C%22api_key%22%3A%22api_6Zu872pqQTdMha8EG9t1_q3OLImELChXyMwTpl5HYyl_IOQEtVnWv8GFmRML4vTGjlDe_dBkRh0P9A9R2hYlYqwxCCVHoyj04K%22%7D"
        data = requests.get(url).json()["data"]
        if validar_datos_existentes("google"):
            return f"Los datos del día {ayer} ya fueron ingresados al sistema"
        for numero, dato in enumerate(data):
            if numero == 0:
                continue
            account_id = dato[0]
            account = dato[1]
            campaign_name = dato[2]
            campaign_status = dato[3]
            bidding_strategy_type = dato[4]
            year_and_month = dato[5]
            start_date = dato[6]
            end_date = dato[7]
            date = dato[8]
            impressions = dato[9]
            clicks = dato[10]
            cost = dato[11]
            cost_usd = dato[12]
            ctr = dato[13]
            cpc = dato[14]
            cpm = dato[15]
            budget = dato[16]
            daily_budget = dato[17]
            return_on_ad_spend = dato[18]
            cost_per_video_view = dato[19]
            video_views = dato[20]
            watch_75_rate = dato[21]
            conversions = dato[22]
            conversion_rate = dato[23]
            cost_per_conversion = dato[24]
            impression_share = dato[25]
            search_impression_share = dato[26]
            insert_data("google",
                        account_id,
                        account,
                        campaign_name,
                        campaign_status,
                        bidding_strategy_type,
                        year_and_month,
                        start_date,
                        end_date,
                        date,
                        impressions,
                        clicks,
                        cost,
                        cost_usd,
                        ctr,
                        cpc,
                        cpm,
                        budget,
                        daily_budget,
                        return_on_ad_spend,
                        cost_per_video_view,
                        video_views,
                        watch_75_rate,
                        conversions,
                        conversion_rate,
                        cost_per_conversion,
                        impression_share,
                        search_impression_share)
            datos_insertados += 1
        return f"{datos_insertados} Datos de Google ingresados correctamente, fecha: {ayer}"
    except:
        return f"Ocurrio un error intentando subir los datos de {ayer}, intente nuevamente"


@app.route(host+'/linkedin', methods=['GET'])
def linkedin_data():
    try:
        datos_insertados = 0
        # Gestion de Fechas
        hoy = datetime.strftime(datetime.now(), '%Y-%m-%d')
        ayer = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        #########################################################

        url = f"https://aws1-api-dwh.supermetrics.com/enterprise/v2/query/data/json?json=%7B%22ds_id%22%3A%22LIA%22%2C%22ds_accounts%22%3A%22504960320%2C506892177%2C507144536%2C509521037%2C509540472%22%2C%22ds_user%22%3A%22xtHWhYnlIX%22%2C%22start_date%22%3A%22{ayer}%22%2C%22end_date%22%3A%22{ayer}%22%2C%22fields%22%3A%22accountName%2CaccountId%2CcampaignName%2CcampaignStatus%2CcampaignStartDate%2CcampaignEndDate%2CcampaignTotalBudget%2CcampaignObjectiveType%2CcampaignCostType%2CcampaignGroupName%2CcampaignGroupStatus%2CcampaignGroupStartDate%2CcampaignGroupEndDate%2CcampaignGroupTotalBudget%2CyearMonth%2Cdate%2Cimpressions%2Cclicks%2Cctr%2Ccpc%2Ccpm%2Cspend_usd%2Copens%2Csends%2CactionClicks%2Cconversions%2CconversionCost%2CvideoThirdQuartileCompletions%2CvideoViews%22%2C%22settings%22%3A%7B%22blanks_to_zero%22%3Atrue%2C%22allow_sum_unique%22%3Atrue%7D%2C%22max_rows%22%3A1000%2C%22api_key%22%3A%22api_6Zu872pqQTdMha8EG9t1_q3OLImELChXyMwTpl5HYyl_IOQEtVnWv8GFmRML4vTGjlDe_dBkRh0P9A9R2hYlYqwxCCVHoyj04K%22%7D"
        data = requests.get(url).json()["data"]
        if validar_datos_existentes("linkedin"):
            return f"Los datos del día {ayer} ya fueron ingresados al sistema"
        for numero, dato in enumerate(data):
            if numero == 0:
                continue
            account_name = dato[0]
            account_id = dato[1]
            campaign_name = dato[2]
            campaign_status = dato[3]
            campaign_start_date = dato[4]
            campaign_end_date = dato[5]
            campaign_total_budget = dato[6]
            campaign_objective_type = dato[7]
            campaign_cost_type = dato[8]
            campaign_group_name = dato[9]
            campaign_group_status = dato[10]
            campaign_group_start_date = dato[11]
            campaign_group_end_date = dato[12]
            campaign_group_total_budget = dato[13]
            year_and_month = dato[14]
            date = dato[15]
            impressions = dato[16]
            clicks = dato[17]
            ctr = dato[18]
            cpc = dato[19]
            cpm = dato[20]
            total_spent_usd = dato[21]
            opens = dato[22]
            sends = dato[23]
            action_clicks = dato[24]
            conversions = dato[25]
            cost_per_conversion = dato[26]
            video_views_at_75 = dato[27]
            video_views = dato[28]

            insert_data("linkedin",
                        account_name,
                        account_id,
                        campaign_name,
                        campaign_status,
                        campaign_start_date,
                        campaign_end_date,
                        campaign_total_budget,
                        campaign_objective_type,
                        campaign_cost_type,
                        campaign_group_name,
                        campaign_group_status,
                        campaign_group_start_date,
                        campaign_group_end_date,
                        campaign_group_total_budget,
                        year_and_month,
                        date,
                        impressions,
                        clicks,
                        ctr,
                        cpc,
                        cpm,
                        total_spent_usd,
                        opens,
                        sends,
                        action_clicks,
                        conversions,
                        cost_per_conversion,
                        video_views_at_75,
                        video_views)
            datos_insertados += 1
        return f"{datos_insertados} Datos de LinkedIn ingresados correctamente, fecha: {ayer}"
    except:
        return f"Ocurrio un error intentando subir los datos de {ayer}, intente nuevamente"


@app.route(host+'/fb-edad-gen', methods=['GET'])
def fb_edad_gen_data():
    try:
        datos_insertados = 0

        # Gestion de Fechas
        hoy = datetime.strftime(datetime.now(), '%Y-%m-%d')
        ayer = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        #########################################################

        url = f"https://aws1-api-dwh.supermetrics.com/enterprise/v2/query/data/json?json=%7B%22ds_id%22%3A%22FA%22%2C%22ds_accounts%22%3A%22act_2430504383699464%2Cact_527509224467939%2Cact_3063703993883466%2Cact_246027520912733%2Cact_458134259014638%2Cact_4554234937959768%22%2C%22ds_user%22%3A%22135849212472962%22%2C%22start_date%22%3A%22{ayer}%22%2C%22end_date%22%3A%22{ayer}%22%2C%22fields%22%3A%22adcampaign_name%2Cadset_name%2CGender%2CAge%2CDate%2Creach%2CFrequency%2Cimpressions%2CROAS%2Ccost_per_lead_form%2Ccost_per_store_visit%2Ccost%2Ccost_usd%2CCPM%2Coutbound_clicks%2Caction_link_click%2Coutbound_CTR%2Caction_like%2Cnew_messaging_conversations%2Ccost_per_new_messaging_conversation%2Cestimated_ad_recall_rate%2Caction_app_install%2Caction_app_use%2Ccost_per_app_install%2Caction_post_engagement%2Coffsite_conversions_fb_pixel_lead%2Coffsite_conversions_fb_pixel_purchase%2Coffsite_conversions_fb_pixel_add_to_cart%2Caction_mobile_app_install%2Consite_conversion.lead_grouped%2Cvideo_p100_watched_actions%22%2C%22settings%22%3A%7B%22blanks_to_zero%22%3Atrue%2C%22action_report_time%22%3A%22conversion%22%2C%22allow_sum_unique%22%3Atrue%7D%2C%22max_rows%22%3A1000000%2C%22api_key%22%3A%22api_6Zu872pqQTdMha8EG9t1_q3OLImELChXyMwTpl5HYyl_IOQEtVnWv8GFmRML4vTGjlDe_dBkRh0P9A9R2hYlYqwxCCVHoyj04K%22%7D"
        data = requests.get(url).json()["data"]
        if validar_datos_existentes("fb-edad-gen"):
            return f"Los datos del día {ayer} ya fueron ingresados al sistema"
        for numero, dato in enumerate(data):
            if numero == 0:
                continue
            campaign_name = dato[0]
            ad_set_name = dato[1]
            gender = dato[2]
            age = dato[3]
            date = dato[4]
            reach = dato[5]
            frequency = dato[6]
            impressions = dato[7]
            return_on_ad_spend = dato[8]
            cost_per_lead_form = dato[9]
            cost_per_store_visit = dato[10]
            cost = dato[11]
            cost_usd = dato[12]
            cpm = dato[13]
            outbound_clicks = dato[14]
            link_clicks = dato[15]
            outbound_ctr = dato[16]
            page_likes = dato[17]
            new_messaging_conversations = dato[18]
            cost_per_new_messaging_conversation = dato[19]
            estimated_ad_recall_lift_rate = dato[20]
            desktop_app_installs = dato[21]
            desktop_app_uses = dato[22]
            cost_per_app_install = dato[23]
            post_engagements = dato[24]
            website_leads = dato[25]
            website_purchases = dato[26]
            website_adds_to_cart = dato[27]
            mobile_app_installs = dato[28]
            on_facebook_leads = dato[29]
            video_watches_at_100 = dato[30]
            insert_data("fb-edad-gen",
                        campaign_name,
                        ad_set_name,
                        gender,
                        age,
                        date,
                        reach,
                        frequency,
                        impressions,
                        return_on_ad_spend,
                        cost_per_lead_form,
                        cost_per_store_visit,
                        cost,
                        cost_usd,
                        cpm,
                        outbound_clicks,
                        link_clicks,
                        outbound_ctr,
                        page_likes,
                        new_messaging_conversations,
                        cost_per_new_messaging_conversation,
                        estimated_ad_recall_lift_rate,
                        desktop_app_installs,
                        desktop_app_uses,
                        cost_per_app_install,
                        post_engagements,
                        website_leads,
                        website_purchases,
                        website_adds_to_cart,
                        mobile_app_installs,
                        on_facebook_leads,
                        video_watches_at_100)
            datos_insertados += 1
        return f"{datos_insertados} Datos de FB-EDAD-GEN ingresados correctamente, fecha: {ayer}"
    except:
        return f"Ocurrio un error intentando subir los datos de {ayer}, intente nuevamente"


@app.route(host+'/fb-region', methods=['GET'])
def fb_region_data():
    try:
        datos_insertados = 0

        # Gestion de Fechas
        hoy = datetime.strftime(datetime.now(), '%Y-%m-%d')
        ayer = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        #########################################################

        url = f"https://aws1-api-dwh.supermetrics.com/enterprise/v2/query/data/json?json=%7B%22ds_id%22%3A%22FA%22%2C%22ds_accounts%22%3A%22act_527509224467939%2Cact_3063703993883466%2Cact_246027520912733%2Cact_458134259014638%2Cact_4554234937959768%2Cact_2430504383699464%22%2C%22ds_user%22%3A%22135849212472962%22%2C%22start_date%22%3A%22{ayer}%22%2C%22end_date%22%3A%22{ayer}%22%2C%22fields%22%3A%22adcampaign_name%2Cadset_name%2CCountryname%2CRegion%2CDate%2Creach%2CFrequency%2Cimpressions%2CROAS%2Ccost_per_lead_form%2Ccost_per_store_visit%2Ccost%2Ccost_usd%2CCPM%2Coutbound_clicks%2Caction_link_click%2Coutbound_CTR%2Caction_like%2Cnew_messaging_conversations%2Ccost_per_new_messaging_conversation%2Cvideo_p75_watched_actions%2Cestimated_ad_recall_rate%2Caction_app_install%2Caction_app_use%2Ccost_per_app_install%2Caction_post_engagement%2Coffsite_conversions_fb_pixel_lead%2Coffsite_conversions_fb_pixel_purchase%2Coffsite_conversions_fb_pixel_add_to_cart%2Caction_mobile_app_install%2Consite_conversion.lead_grouped%2Cvideo_p100_watched_actions%22%2C%22settings%22%3A%7B%22blanks_to_zero%22%3Atrue%2C%22action_report_time%22%3A%22conversion%22%2C%22allow_sum_unique%22%3Atrue%7D%2C%22max_rows%22%3A1000000%2C%22api_key%22%3A%22api_6Zu872pqQTdMha8EG9t1_q3OLImELChXyMwTpl5HYyl_IOQEtVnWv8GFmRML4vTGjlDe_dBkRh0P9A9R2hYlYqwxCCVHoyj04K%22%7D"
        data = requests.get(url).json()["data"]
        if validar_datos_existentes("fb-region"):
            return f"Los datos del día {ayer} ya fueron ingresados al sistema"
        for numero, dato in enumerate(data):
            if numero == 0:
                continue
            campaign_name = dato[0]
            ad_set_name = dato[1]
            country = dato[2]
            region = dato[3]
            date = dato[4]
            reach = dato[5]
            frequency = dato[6]
            impressions = dato[7]
            return_on_ad_spend = dato[8]
            cost_per_lead_form = dato[9]
            cost_per_store_visit = dato[10]
            cost = dato[11]
            cost_usd = dato[12]
            cpm = dato[13]
            outbound_clicks = dato[14]
            link_clicks = dato[15]
            outbound_ctr = dato[16]
            page_likes = dato[17]
            new_messaging_conversations = dato[18]
            cost_per_new_messaging_conversation = dato[19]
            video_watches_at_75 = dato[20]
            estimated_ad_recall_lift_rate = dato[21]
            desktop_app_installs = dato[22]
            desktop_app_uses = dato[23]
            cost_per_app_install = dato[24]
            post_engagements = dato[25]
            website_leads = dato[26]
            website_purchases = dato[27]
            website_adds_to_cart = dato[28]
            mobile_app_installs = dato[29]
            on_facebook_leads = dato[30]
            video_watches_at_100 = dato[31]
            insert_data("fb-region",
                        campaign_name,
                        ad_set_name,
                        country,
                        region,
                        date,
                        reach,
                        frequency,
                        impressions,
                        return_on_ad_spend,
                        cost_per_lead_form,
                        cost_per_store_visit,
                        cost,
                        cost_usd,
                        cpm,
                        outbound_clicks,
                        link_clicks,
                        outbound_ctr,
                        page_likes,
                        new_messaging_conversations,
                        cost_per_new_messaging_conversation,
                        video_watches_at_75,
                        estimated_ad_recall_lift_rate,
                        desktop_app_installs,
                        desktop_app_uses,
                        cost_per_app_install,
                        post_engagements,
                        website_leads,
                        website_purchases,
                        website_adds_to_cart,
                        mobile_app_installs,
                        on_facebook_leads,
                        video_watches_at_100)
            datos_insertados += 1
        return f"{datos_insertados} Datos de FB-EDAD-GEN ingresados correctamente, fecha: {ayer}"
    except:
        return f"Ocurrio un error intentando subir los datos de {ayer}, intente nuevamente"


@app.route(host+'/fb-campana', methods=['GET'])
def fb_campana_data():
    try:
        datos_insertados = 0

        # Gestion de Fechas
        hoy = datetime.strftime(datetime.now(), '%Y-%m-%d')
        ayer = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        #########################################################

        url = f"https://aws1-api-dwh.supermetrics.com/enterprise/v2/query/data/json?json=%7B%22ds_id%22%3A%22FA%22%2C%22ds_accounts%22%3A%22act_2430504383699464%2Cact_527509224467939%2Cact_3063703993883466%2Cact_246027520912733%2Cact_458134259014638%2Cact_4554234937959768%22%2C%22ds_user%22%3A%22135849212472962%22%2C%22start_date%22%3A%22{ayer}%22%2C%22end_date%22%3A%22{ayer}%22%2C%22fields%22%3A%22profile%2Cadcampaign_name%2Ccampaign_start_date%2Ccampaign_end_date%2Ccampaignstatus%2Ccampaignobjective%2Ccampaignbuyingtype%2Ccampaign_daily_budget%2Ccampaign_lifetime_budget%2Ccampaign_budget_remaining%2Ccampaign_start_time%2Ccampaign_end_time%2Cadset_name%2CDate%2Creach%2CFrequency%2Cimpressions%2CSocialReach%2Cactionvalue%2CROAS%2Ccost_per_lead_form%2Ccost_per_store_visit%2Ccost%2Ccost_usd%2CCPP%2CCPM%2CCPA%2Coutbound_clicks%2Caction_link_click%2Coutbound_CTR%2CCPOC%2Caction_like%2Cnew_messaging_conversations%2Ccost_per_new_messaging_conversation%2Cvideo_15_sec_watched_actions%2Cvideo_p75_watched_actions%2Ccost_per_thruplay%2Cestimated_ad_recall_rate%2Caction_app_install%2Caction_app_use%2Ccost_per_app_install%2Comni_add_to_cart_shared_item%2Comni_purchase_shared_item%2Caction_post_engagement%2CActions%2Caction_video_view%2Coffsite_conversions_fb_pixel_lead%2Coffsite_conversions_fb_pixel_purchase%2Coffsite_conversions_fb_pixel_add_to_cart%2Caction_mobile_app_install%2Consite_conversion.lead_grouped%2Cvideo_p100_watched_actions%22%2C%22settings%22%3A%7B%22blanks_to_zero%22%3Atrue%2C%22action_report_time%22%3A%22conversion%22%2C%22allow_sum_unique%22%3Atrue%7D%2C%22max_rows%22%3A1000000%2C%22api_key%22%3A%22api_6Zu872pqQTdMha8EG9t1_q3OLImELChXyMwTpl5HYyl_IOQEtVnWv8GFmRML4vTGjlDe_dBkRh0P9A9R2hYlYqwxCCVHoyj04K%22%7D"
        data = requests.get(url).json()["data"]
        if validar_datos_existentes("fb-campana"):
            return f"Los datos del día {ayer} ya fueron ingresados al sistema"
        for numero, dato in enumerate(data):
            if numero == 0:
                continue
            account = dato[0]
            campaign_name = dato[1]
            campaign_start_date = dato[2]
            campaign_end_date = dato[3]
            campaign_status = dato[4]
            campaign_objective = dato[5]
            campaign_buying_type = dato[6]
            campaign_daily_budget = dato[7]
            campaign_lifetime_budget = dato[8]
            campaign_budget_remaining = dato[9]
            campaign_start_time = dato[10]
            campaign_end_time = dato[11]
            ad_set_name = dato[12]
            date = dato[13]
            reach = dato[14]
            frequency = dato[15]
            impressions = dato[16]
            social_reach = dato[17]
            total_action_value = dato[18]
            return_on_ad_spend = dato[19]
            cost_per_lead_form = dato[20]
            cost_per_store_visit = dato[21]
            cost = dato[22]
            cost_usd = dato[23]
            cost_per_1000_people_reached = dato[24]
            cpm = dato[25]
            cpa = dato[26]
            outbound_clicks = dato[27]
            link_clicks = dato[28]
            outbound_ctr = dato[29]
            cost_per_outbound_click = dato[30]
            page_likes = dato[31]
            new_messaging_conversations = dato[32]
            cost_per_new_messaging_conversation = dato[33]
            _15_second_video_views = dato[34]
            video_watches_at_75 = dato[35]
            cost_per_thruplay = dato[36]
            estimated_ad_recall_lift_rate = dato[37]
            desktop_app_installs = dato[38]
            desktop_app_uses = dato[39]
            cost_per_app_install = dato[40]
            omni_adds_to_cart_shared_item = dato[41]
            omni_purchase_shared_item = dato[42]
            post_engagements = dato[43]
            actions = dato[44]
            three_second_video_views = dato[45]
            website_leads = dato[46]
            website_purchases = dato[47]
            website_adds_to_cart = dato[48]
            mobile_app_installs = dato[49]
            on_facebook_leads = dato[50]
            video_watches_at_100 = dato[51]
            insert_data("fb-campana", account,
                        campaign_name,
                        campaign_start_date,
                        campaign_end_date,
                        campaign_status,
                        campaign_objective,
                        campaign_buying_type,
                        campaign_daily_budget,
                        campaign_lifetime_budget,
                        campaign_budget_remaining,
                        campaign_start_time,
                        campaign_end_time,
                        ad_set_name,
                        date,
                        reach,
                        frequency,
                        impressions,
                        social_reach,
                        total_action_value,
                        return_on_ad_spend,
                        cost_per_lead_form,
                        cost_per_store_visit,
                        cost,
                        cost_usd,
                        cost_per_1000_people_reached,
                        cpm,
                        cpa,
                        outbound_clicks,
                        link_clicks,
                        outbound_ctr,
                        cost_per_outbound_click,
                        page_likes,
                        new_messaging_conversations,
                        cost_per_new_messaging_conversation,
                        _15_second_video_views,
                        video_watches_at_75,
                        cost_per_thruplay,
                        estimated_ad_recall_lift_rate,
                        desktop_app_installs,
                        desktop_app_uses,
                        cost_per_app_install,
                        omni_adds_to_cart_shared_item,
                        omni_purchase_shared_item,
                        post_engagements,
                        actions,
                        three_second_video_views,
                        website_leads,
                        website_purchases,
                        website_adds_to_cart,
                        mobile_app_installs,
                        on_facebook_leads,
                        video_watches_at_100)
            datos_insertados += 1
        return f"{datos_insertados} Datos de FB-CAMPANA ingresados correctamente, fecha: {ayer}"
    except:
        return f"Ocurrio un error intentando subir los datos de {ayer}, intente nuevamente"


@app.route(host+'/fb-plataforma', methods=['GET'])
def fb_plataforma_data():
    try:
        datos_insertados = 0

        # Gestion de Fechas
        hoy = datetime.strftime(datetime.now(), '%Y-%m-%d')
        ayer = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        #########################################################

        url = f"https://aws1-api-dwh.supermetrics.com/enterprise/v2/query/data/json?json=%7B%22ds_id%22%3A%22FA%22%2C%22ds_accounts%22%3A%22act_2430504383699464%2Cact_527509224467939%2Cact_3063703993883466%2Cact_246027520912733%2Cact_458134259014638%2Cact_4554234937959768%22%2C%22ds_user%22%3A%22135849212472962%22%2C%22start_date%22%3A%22{ayer}%22%2C%22end_date%22%3A%22{ayer}%22%2C%22fields%22%3A%22adcampaign_name%2Cadset_name%2Cplacement%2Cpublisher_platform%2Cplatform_position%2Cdevice_platform%2CDate%2Creach%2CFrequency%2Cimpressions%2CROAS%2Ccost_per_lead_form%2Ccost_per_store_visit%2Ccost%2Ccost_usd%2CCPM%2Coutbound_clicks%2Caction_link_click%2Coutbound_CTR%2Caction_like%2Cnew_messaging_conversations%2Ccost_per_new_messaging_conversation%2Cvideo_p75_watched_actions%2Cestimated_ad_recall_rate%2Caction_app_install%2Caction_app_use%2Ccost_per_app_install%2Caction_post_engagement%2Coffsite_conversions_fb_pixel_lead%2Coffsite_conversions_fb_pixel_purchase%2Coffsite_conversions_fb_pixel_add_to_cart%2Caction_mobile_app_install%2Consite_conversion.lead_grouped%2Cvideo_p100_watched_actions%22%2C%22settings%22%3A%7B%22blanks_to_zero%22%3Atrue%2C%22action_report_time%22%3A%22conversion%22%2C%22allow_sum_unique%22%3Atrue%7D%2C%22max_rows%22%3A1000000%2C%22api_key%22%3A%22api_6Zu872pqQTdMha8EG9t1_q3OLImELChXyMwTpl5HYyl_IOQEtVnWv8GFmRML4vTGjlDe_dBkRh0P9A9R2hYlYqwxCCVHoyj04K%22%7D"
        data = requests.get(url).json()["data"]
        if validar_datos_existentes("fb-plataforma"):
            return f"Los datos del día {ayer} ya fueron ingresados al sistema"
        for numero, dato in enumerate(data):
            if numero == 0:
                continue
            campaign_name = dato[0]
            ad_set_name = dato[1]
            placement = dato[2]
            publisher_platform = dato[3]
            platform_position = dato[4]
            device_platform = dato[5]
            date = dato[6]
            reach = dato[7]
            frequency = dato[8]
            impressions = dato[9]
            return_on_ad_spend = dato[10]
            cost_per_lead_form = dato[11]
            cost_per_store_visit = dato[12]
            cost = dato[13]
            cost_usd = dato[14]
            cpm = dato[15]
            outbound_clicks = dato[16]
            link_clicks = dato[17]
            outbound_ctr = dato[18]
            page_likes = dato[19]
            new_messaging_conversations = dato[20]
            cost_per_new_messaging_conversation = dato[21]
            video_watches_at_75 = dato[22]
            estimated_ad_recall_lift_rate = dato[23]
            desktop_app_installs = dato[24]
            desktop_app_uses = dato[25]
            cost_per_app_install = dato[26]
            post_engagements = dato[27]
            website_leads = dato[28]
            website_purchases = dato[29]
            website_adds_to_cart = dato[30]
            mobile_app_installs = dato[31]
            on_facebook_leads = dato[32]
            video_watches_at_100 = dato[33]

            insert_data("fb-plataforma",
                        campaign_name,
                        ad_set_name,
                        placement,
                        publisher_platform,
                        platform_position,
                        device_platform,
                        date,
                        reach,
                        frequency,
                        impressions,
                        return_on_ad_spend,
                        cost_per_lead_form,
                        cost_per_store_visit,
                        cost,
                        cost_usd,
                        cpm,
                        outbound_clicks,
                        link_clicks,
                        outbound_ctr,
                        page_likes,
                        new_messaging_conversations,
                        cost_per_new_messaging_conversation,
                        video_watches_at_75,
                        estimated_ad_recall_lift_rate,
                        desktop_app_installs,
                        desktop_app_uses,
                        cost_per_app_install,
                        post_engagements,
                        website_leads,
                        website_purchases,
                        website_adds_to_cart,
                        mobile_app_installs,
                        on_facebook_leads,
                        video_watches_at_100)
            datos_insertados += 1
        return f"{datos_insertados} Datos de FB-plataforma ingresados correctamente, fecha: {ayer}"
    except:
        return f"Ocurrio un error intentando subir los datos de {ayer}, intente nuevamente"


@app.route(host+'/fb-anuncio', methods=['GET'])
def fb_anuncio_data():
    try:
        datos_insertados = 0

        # Gestion de Fechas
        hoy = datetime.strftime(datetime.now(), '%Y-%m-%d')
        ayer = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        #########################################################

        url = f"https://aws1-api-dwh.supermetrics.com/enterprise/v2/query/data/json?json=%7B%22ds_id%22%3A%22FA%22%2C%22ds_accounts%22%3A%22act_2430504383699464%2Cact_527509224467939%2Cact_3063703993883466%2Cact_246027520912733%2Cact_458134259014638%2Cact_4554234937959768%22%2C%22ds_user%22%3A%22135849212472962%22%2C%22start_date%22%3A%22{ayer}%22%2C%22end_date%22%3A%22{ayer}%22%2C%22fields%22%3A%22adcampaign_name%2Cadset_name%2Cadsetstatus%2Cad_name%2Cadstatus%2Cadsetstart_time_exact%2Cadsetend_time_exact%2Cattribution_setting%2Cdesktop_feed_preview_url%2Cmobile_feed_preview_url%2Cfacebook_story_preview_url%2Cinstagram_story_preview_url%2Cinstagram_preview_url%2CdestinationURL%2Ccreative_thumbnail_url%2Ccreative_image_url%2Cpromoted_post_permalink_url%2Cpromoted_post_permalink_url_ig%2Cquality_score_organic_text%2Crelevance_status%2Creach_estimate_users%2CDate%2Creach%2CFrequency%2Cimpressions%2CSocialReach%2Cactionvalue%2CROAS%2Ccost_per_lead_form%2Ccost_per_store_visit%2Ccost%2Ccost_usd%2CCPP%2CCPM%2CCPA%2Coutbound_clicks%2Caction_link_click%2Coutbound_CTR%2CCPOC%2Caction_like%2Cnew_messaging_conversations%2Ccost_per_new_messaging_conversation%2Cvideo_15_sec_watched_actions%2Cvideo_p75_watched_actions%2Ccost_per_thruplay%2Cestimated_ad_recall_rate%2Caction_app_install%2Caction_app_use%2Ccost_per_app_install%2Comni_add_to_cart_shared_item%2Comni_purchase_shared_item%2Caction_post_engagement%2CActions%2Caction_video_view%2Coffsite_conversions_fb_pixel_lead%2Coffsite_conversions_fb_pixel_purchase%2Coffsite_conversions_fb_pixel_add_to_cart%2Caction_mobile_app_install%2Consite_conversion.lead_grouped%2Cvideo_p100_watched_actions%22%2C%22settings%22%3A%7B%22blanks_to_zero%22%3Atrue%2C%22action_report_time%22%3A%22conversion%22%2C%22allow_sum_unique%22%3Atrue%7D%2C%22max_rows%22%3A1000000%2C%22api_key%22%3A%22api_6Zu872pqQTdMha8EG9t1_q3OLImELChXyMwTpl5HYyl_IOQEtVnWv8GFmRML4vTGjlDe_dBkRh0P9A9R2hYlYqwxCCVHoyj04K%22%7D"
        data = requests.get(url).json()["data"]
        if validar_datos_existentes("fb-anuncio"):
            return f"Los datos del día {ayer} ya fueron ingresados al sistema"
        for numero, dato in enumerate(data):
            if numero == 0:
                continue
            campaign_name = dato[0]
            ad_set_name = dato[1]
            ad_set_status = dato[2]
            ad_name = dato[3]
            ad_status = dato[4]
            ad_set_start_time = dato[5]
            ad_set_end_time = dato[6]
            attribution_setting = dato[7]
            ad_preview_url_desktop_feed = dato[8]
            ad_preview_url_mobile_feed = dato[9]
            ad_preview_url_facebook_story = dato[10]
            ad_preview_url_instagram_story = dato[11]
            ad_preview_url_instagram = dato[12]
            destination_url = dato[13]
            ad_creative_thumbnail_url = dato[14]
            ad_creative_image_url = dato[15]
            link_to_promoted_post = dato[16]
            link_to_promoted_instagram_post = dato[17]
            quality_ranking_text = dato[18]
            relevance_score_status = dato[19]
            reach_estimate_monthly_active_users = dato[20]
            date = dato[21]
            reach = dato[22]
            frequency = dato[23]
            impressions = dato[24]
            social_reach = dato[25]
            total_action_value = dato[26]
            return_on_ad_spend = dato[27]
            cost_per_lead_form = dato[28]
            cost_per_store_visit = dato[29]
            cost = dato[30]
            cost_usd = dato[31]
            cost_per_1000_people_reached = dato[32]
            cpm = dato[33]
            cpa = dato[34]
            outbound_clicks = dato[35]
            link_clicks = dato[36]
            outbound_ctr = dato[37]
            cost_per_outbound_click = dato[38]
            page_likes = dato[39]
            new_messaging_conversations = dato[40]
            cost_per_new_messaging_conversation = dato[41]
            _15_second_video_views = dato[42]
            video_watches_at_75 = dato[43]
            cost_per_thruplay = dato[44]
            estimated_ad_recall_lift_rate = dato[45]
            desktop_app_installs = dato[46]
            desktop_app_uses = dato[47]
            cost_per_app_install = dato[48]
            omni_adds_to_cart_shared_item = dato[49]
            omni_purchase_shared_item = dato[50]
            post_engagements = dato[51]
            actions = dato[52]
            three_second_video_views = dato[53]
            website_leads = dato[54]
            website_purchases = dato[55]
            website_adds_to_cart = dato[56]
            mobile_app_installs = dato[57]
            on_facebook_leads = dato[58]
            video_watches_at_100 = dato[59]

            insert_data("fb-anuncio",
                        campaign_name,
                        ad_set_name,
                        ad_set_status,
                        ad_name,
                        ad_status,
                        ad_set_start_time,
                        ad_set_end_time,
                        attribution_setting,
                        ad_preview_url_desktop_feed,
                        ad_preview_url_mobile_feed,
                        ad_preview_url_facebook_story,
                        ad_preview_url_instagram_story,
                        ad_preview_url_instagram,
                        destination_url,
                        ad_creative_thumbnail_url,
                        ad_creative_image_url,
                        link_to_promoted_post,
                        link_to_promoted_instagram_post,
                        quality_ranking_text,
                        relevance_score_status,
                        reach_estimate_monthly_active_users,
                        date,
                        reach,
                        frequency,
                        impressions,
                        social_reach,
                        total_action_value,
                        return_on_ad_spend,
                        cost_per_lead_form,
                        cost_per_store_visit,
                        cost,
                        cost_usd,
                        cost_per_1000_people_reached,
                        cpm,
                        cpa,
                        outbound_clicks,
                        link_clicks,
                        outbound_ctr,
                        cost_per_outbound_click,
                        page_likes,
                        new_messaging_conversations,
                        cost_per_new_messaging_conversation,
                        _15_second_video_views,
                        video_watches_at_75,
                        cost_per_thruplay,
                        estimated_ad_recall_lift_rate,
                        desktop_app_installs,
                        desktop_app_uses,
                        cost_per_app_install,
                        omni_adds_to_cart_shared_item,
                        omni_purchase_shared_item,
                        post_engagements,
                        actions,
                        three_second_video_views,
                        website_leads,
                        website_purchases,
                        website_adds_to_cart,
                        mobile_app_installs,
                        on_facebook_leads,
                        video_watches_at_100
                        )
            datos_insertados += 1
        return f"{datos_insertados} Datos de FB-ANUNCIO ingresados correctamente, fecha: {ayer}"
    except:
        return f"Ocurrio un error intentando subir los datos de {ayer}, intente nuevamente"


@app.route(host+'/bulk', methods=['GET'])
def bulk_apis():
    try:
        google = requests.get("http://localhost:5000/google")
        linkedin = requests.get("http://localhost:5000/linkedin")
        fb_1 = requests.get("http://localhost:5000/fb-edad-gen")
        fb_2 = requests.get("http://localhost:5000/fb-region")
        fb_3 = requests.get("http://localhost:5000/fb-campana")
        fb_4 = requests.get("http://localhost:5000/fb-plataforma")
        fb_5 = requests.get("http://localhost:5000/fb-anuncio")
        datasx = {
            "Google": str(google.text),
            "Linkedin": str(linkedin.text),
            "FB_EDAD_GEN": str(fb_1.text),
            "FB_REGION": str(fb_2.text),
            "FB_CAMPANA": str(fb_3.text),
            "FB_PLATAFORMA": str(fb_4.text),
            "FB_ANUNCIO": str(fb_5.text)
        }
        return datasx
    except:
        return "Ocurrio un error, intenta ingresando individualmente cada API."


@app.route(host+'/reverse', methods=['GET'])
def reverse_all_data():
    datasx = {}
    fecha_registro = datetime.strftime(datetime.now(), '%Y-%m-%d')
    counter = 0
    counter_total = 0
    if google_metrics.query.filter(google_metrics.fecha_registro == fecha_registro).first():
        for google_obj in google_metrics.query.filter(google_metrics.fecha_registro == fecha_registro).all():
            db.session.delete(google_obj)
            counter+=1
            counter_total+=1
        datasx["Google"] = str(counter) + " Datos removidos"
        db.session.commit()
        counter = 0

    if linkedin_metrics.query.filter(linkedin_metrics.fecha_registro == fecha_registro).first():
        for linkedin_obj in linkedin_metrics.query.filter(linkedin_metrics.fecha_registro == fecha_registro).all():
            db.session.delete(linkedin_obj)
            counter+=1
            counter_total+=1
        datasx["Linkedin"] = str(counter) + " Datos removidos"
        db.session.commit()
        counter = 0
        

    if fb_anuncio.query.filter(fb_anuncio.fecha_registro == fecha_registro).first():
        for fb_anuncio_obj in fb_anuncio.query.filter(fb_anuncio.fecha_registro == fecha_registro).all():
            db.session.delete(fb_anuncio_obj)
            counter+=1
            counter_total+=1
        datasx["FB_ANUNCIO"] = str(counter) + " Datos removidos"
        db.session.commit()
        counter = 0    
            
    if fb_campana.query.filter(fb_campana.fecha_registro == fecha_registro).first():
        for fb_campana_obj in fb_campana.query.filter(fb_campana.fecha_registro == fecha_registro).all():
            db.session.delete(fb_campana_obj)
            counter+=1
            counter_total+=1
        datasx["FB_CAMPANA"] = str(counter) + " Datos removidos"
        db.session.commit()
        counter = 0
        
    if fb_plataforma.query.filter(fb_plataforma.fecha_registro == fecha_registro).first():
        for fb_plataforma_obj in fb_plataforma.query.filter(fb_plataforma.fecha_registro == fecha_registro).all():
            db.session.delete(fb_plataforma_obj)
            counter+=1
            counter_total+=1
        datasx["FB_PLATAFORMA"] = str(counter) + " Datos removidos"
        db.session.commit()
        counter = 0    
            
    if fb_edad_gen.query.filter(fb_edad_gen.fecha_registro == fecha_registro).first():
        for fb_edad_gen_obj in fb_edad_gen.query.filter(fb_edad_gen.fecha_registro == fecha_registro).all():
            db.session.delete(fb_edad_gen_obj)  
            counter+=1
            counter_total+=1
        datasx["FB_EDAD_GEN"] = str(counter) + " Datos removidos"
        db.session.commit()
        counter = 0
          
    if fb_region.query.filter(fb_region.fecha_registro == fecha_registro).first():
        for fb_region_obj in fb_region.query.filter(fb_region.fecha_registro == fecha_registro).all():
            db.session.delete(fb_region_obj)    
            counter+=1
            counter_total+=1
        datasx["FB_REGION"] = str(counter) + " Datos removidos"
        db.session.commit()
        counter = 0

    if counter_total > 0:
        datasx["status"] = f"Datos del día {fecha_registro} borrados exitosamente, {counter_total} datos afectados"
        return datasx
    return "Ningun dato fue afectado"


# Funcion que valida si la carga ya fue realizada
def validar_datos_existentes(medio):
    fecha_registro = datetime.strftime(datetime.now(), '%Y-%m-%d')

    if medio == "google":
        total_registros_por_fecha = google_metrics.query.filter(
            google_metrics.fecha_registro == fecha_registro).count()
        if google_metrics.query.filter(google_metrics.fecha_registro == fecha_registro).first():
            return True
    elif medio == "linkedin":
        total_registros_por_fecha = linkedin_metrics.query.filter(
            linkedin_metrics.fecha_registro == fecha_registro).count()
        if linkedin_metrics.query.filter(linkedin_metrics.fecha_registro == fecha_registro).first():
            return True
    elif medio == "fb-edad-gen":
        total_registros_por_fecha = fb_edad_gen.query.filter(
            fb_edad_gen.fecha_registro == fecha_registro).count()
        if fb_edad_gen.query.filter(fb_edad_gen.fecha_registro == fecha_registro).first():
            return True
    elif medio == "fb-region":
        total_registros_por_fecha = fb_region.query.filter(
            fb_region.fecha_registro == fecha_registro).count()
        if fb_region.query.filter(fb_region.fecha_registro == fecha_registro).first():
            return True
    elif medio == "fb-campana":
        total_registros_por_fecha = fb_campana.query.filter(
            fb_campana.fecha_registro == fecha_registro).count()
        if fb_campana.query.filter(fb_campana.fecha_registro == fecha_registro).first():
            return True
    elif medio == "fb-plataforma":
        total_registros_por_fecha = fb_plataforma.query.filter(
            fb_plataforma.fecha_registro == fecha_registro).count()
        if fb_plataforma.query.filter(fb_plataforma.fecha_registro == fecha_registro).first():
            return True
    elif medio == "fb-anuncio":
        total_registros_por_fecha = fb_anuncio.query.filter(
            fb_anuncio.fecha_registro == fecha_registro).count()
        if fb_anuncio.query.filter(fb_anuncio.fecha_registro == fecha_registro).first():
            return True
    return False


def insert_data(medio, *args):
    if medio == "google":
        nuevo_registro = google_metrics(*args)
        db.session.add(nuevo_registro)
        db.session.commit()
    elif medio == "linkedin":
        nuevo_registro = linkedin_metrics(*args)
        db.session.add(nuevo_registro)
        db.session.commit()
    elif medio == "fb-edad-gen":
        nuevo_registro = fb_edad_gen(*args)
        db.session.add(nuevo_registro)
        db.session.commit()
    elif medio == "fb-region":
        nuevo_registro = fb_region(*args)
        db.session.add(nuevo_registro)
        db.session.commit()
    elif medio == "fb-campana":
        nuevo_registro = fb_campana(*args)
        db.session.add(nuevo_registro)
        db.session.commit()
    elif medio == "fb-plataforma":
        nuevo_registro = fb_plataforma(*args)
        db.session.add(nuevo_registro)
        db.session.commit()
    elif medio == "fb-anuncio":
        nuevo_registro = fb_anuncio(*args)
        db.session.add(nuevo_registro)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
