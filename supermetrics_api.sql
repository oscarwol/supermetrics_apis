
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de datos: `supermetrics_api`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fb_anuncio`
--

CREATE TABLE `fb_anuncio` (
  `id` int(11) NOT NULL,
  `campaign_name` varchar(200) NOT NULL,
  `ad_set_name` varchar(200) NOT NULL,
  `ad_set_status` varchar(200) NOT NULL,
  `ad_name` varchar(200) NOT NULL,
  `ad_status` varchar(200) NOT NULL,
  `ad_set_start_time` varchar(200) NOT NULL,
  `ad_set_end_time` varchar(200) NOT NULL,
  `attribution_setting` varchar(200) NOT NULL,
  `ad_preview_url_desktop_feed` varchar(200) NOT NULL,
  `ad_preview_url_mobile_feed` varchar(200) NOT NULL,
  `ad_preview_url_facebook_story` varchar(200) NOT NULL,
  `ad_preview_url_instagram_story` varchar(200) NOT NULL,
  `ad_preview_url_instagram` varchar(200) NOT NULL,
  `destination_url` varchar(200) NOT NULL,
  `ad_creative_thumbnail_url` varchar(200) NOT NULL,
  `ad_creative_image_url` varchar(200) NOT NULL,
  `link_to_promoted_post` varchar(200) NOT NULL,
  `link_to_promoted_instagram_post` varchar(200) NOT NULL,
  `quality_ranking_text` varchar(200) NOT NULL,
  `relevance_score_status` varchar(200) NOT NULL,
  `reach_estimate_monthly_active_users` int(11) NOT NULL,
  `date` date NOT NULL,
  `reach` int(11) NOT NULL,
  `frequency` float NOT NULL,
  `impressions` int(11) NOT NULL,
  `social_reach` int(11) NOT NULL,
  `total_action_value` float NOT NULL,
  `return_on_ad_spend` float NOT NULL,
  `cost_per_lead_form` float NOT NULL,
  `cost_per_store_visit` float NOT NULL,
  `cost` float NOT NULL,
  `cost_usd` float NOT NULL,
  `cost_per_1000_people_reached` float NOT NULL,
  `cpm` float NOT NULL,
  `cpa` float NOT NULL,
  `outbound_clicks` int(11) NOT NULL,
  `link_clicks` int(11) NOT NULL,
  `outbound_ctr` float NOT NULL,
  `cost_per_outbound_click` float NOT NULL,
  `page_likes` int(11) NOT NULL,
  `new_messaging_conversations` int(11) NOT NULL,
  `cost_per_new_messaging_conversation` float NOT NULL,
  `_15_second_video_views` int(11) NOT NULL,
  `video_watches_at_75` int(11) NOT NULL,
  `cost_per_thruplay` float NOT NULL,
  `estimated_ad_recall_lift_rate` float NOT NULL,
  `desktop_app_installs` int(11) NOT NULL,
  `desktop_app_uses` int(11) NOT NULL,
  `cost_per_app_install` float NOT NULL,
  `omni_adds_to_cart_shared_item` int(11) NOT NULL,
  `omni_purchase_shared_item` int(11) NOT NULL,
  `post_engagements` int(11) NOT NULL,
  `actions` int(11) NOT NULL,
  `three_second_video_views` int(11) NOT NULL,
  `website_leads` int(11) NOT NULL,
  `website_purchases` int(11) NOT NULL,
  `website_adds_to_cart` int(11) NOT NULL,
  `mobile_app_installs` int(11) NOT NULL,
  `on_facebook_leads` int(11) NOT NULL,
  `video_watches_at_100` int(11) NOT NULL,
  `fecha_registro` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fb_campana`
--

CREATE TABLE `fb_campana` (
  `id` int(11) NOT NULL,
  `account` varchar(200) NOT NULL,
  `campaign_name` varchar(200) NOT NULL,
  `campaign_start_date` date NOT NULL,
  `campaign_end_date` date NOT NULL,
  `campaign_status` varchar(200) NOT NULL,
  `campaign_objective` varchar(200) NOT NULL,
  `campaign_buying_type` varchar(200) NOT NULL,
  `campaign_daily_budget` float NOT NULL,
  `campaign_lifetime_budget` float NOT NULL,
  `campaign_budget_remaining` float NOT NULL,
  `campaign_start_time` varchar(200) NOT NULL,
  `campaign_end_time` varchar(200) NOT NULL,
  `ad_set_name` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `reach` int(11) NOT NULL,
  `frequency` float NOT NULL,
  `impressions` int(11) NOT NULL,
  `social_reach` int(11) NOT NULL,
  `total_action_value` float NOT NULL,
  `return_on_ad_spend` float NOT NULL,
  `cost_per_lead_form` float NOT NULL,
  `cost_per_store_visit` float NOT NULL,
  `cost` float NOT NULL,
  `cost_usd` float NOT NULL,
  `cpp` float DEFAULT NULL,
  `cpm` float NOT NULL,
  `cpa` float NOT NULL,
  `outbound_clicks` int(11) NOT NULL,
  `link_clicks` int(11) NOT NULL,
  `outbound_ctr` float NOT NULL,
  `cost_per_outbound_click` float NOT NULL,
  `page_likes` int(11) NOT NULL,
  `new_messaging_conversations` int(11) NOT NULL,
  `cost_per_new_messaging_conversation` float NOT NULL,
  `15_second_video_views` int(11) DEFAULT NULL,
  `video_watches_at_75` int(11) NOT NULL,
  `cost_per_thruplay` float NOT NULL,
  `estimated_ad_recall_lift_rate` float NOT NULL,
  `desktop_app_installs` int(11) NOT NULL,
  `desktop_app_uses` int(11) NOT NULL,
  `cost_per_app_install` float NOT NULL,
  `omni_adds_to_cart_shared_item` int(11) NOT NULL,
  `omni_purchase_shared_item` int(11) NOT NULL,
  `post_engagements` int(11) NOT NULL,
  `actions` int(11) NOT NULL,
  `three_second_video_views` int(11) NOT NULL,
  `website_leads` int(11) NOT NULL,
  `website_purchases` int(11) NOT NULL,
  `website_adds_to_cart` int(11) NOT NULL,
  `mobile_app_installs` int(11) NOT NULL,
  `on_facebook_leads` int(11) NOT NULL,
  `video_watches_at_100` int(11) NOT NULL,
  `fecha_registro` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fb_edad_gen`
--

CREATE TABLE `fb_edad_gen` (
  `id` int(11) NOT NULL,
  `campaign_name` varchar(200) NOT NULL,
  `ad_set_name` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `age` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `reach` int(11) NOT NULL,
  `frequency` float NOT NULL,
  `impressions` int(11) NOT NULL,
  `return_on_ad_spend` float NOT NULL,
  `cost_per_lead_form` float NOT NULL,
  `cost_per_store_visit` float NOT NULL,
  `cost` float NOT NULL,
  `cost_usd` float NOT NULL,
  `cpm` float NOT NULL,
  `outbound_clicks` int(11) NOT NULL,
  `link_clicks` int(11) NOT NULL,
  `outbound_ctr` float NOT NULL,
  `page_likes` int(11) NOT NULL,
  `new_messaging_conversations` int(11) NOT NULL,
  `cost_per_new_messaging_conversation` float NOT NULL,
  `estimated_ad_recall_lift_rate` float NOT NULL,
  `desktop_app_installs` int(11) NOT NULL,
  `desktop_app_uses` int(11) NOT NULL,
  `cost_per_app_install` float NOT NULL,
  `post_engagements` int(11) NOT NULL,
  `website_leads` int(11) NOT NULL,
  `website_purchases` int(11) NOT NULL,
  `website_adds_to_cart` int(11) NOT NULL,
  `mobile_app_installs` int(11) NOT NULL,
  `on_facebook_leads` int(11) NOT NULL,
  `video_watches_at_100` int(11) NOT NULL,
  `fecha_registro` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fb_plataforma`
--

CREATE TABLE `fb_plataforma` (
  `id` int(11) NOT NULL,
  `campaign_name` varchar(200) NOT NULL,
  `ad_set_name` varchar(200) NOT NULL,
  `placement` varchar(200) NOT NULL,
  `publisher_platform` varchar(200) NOT NULL,
  `platform_position` varchar(200) NOT NULL,
  `device_platform` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `reach` int(11) NOT NULL,
  `frequency` float NOT NULL,
  `impressions` int(11) NOT NULL,
  `social_reach` int(11) DEFAULT NULL,
  `total_action_value` float DEFAULT NULL,
  `return_on_ad_spend` float NOT NULL,
  `cost_per_lead_form` float NOT NULL,
  `cost_per_store_visit` float NOT NULL,
  `cost` float NOT NULL,
  `cost_usd` float NOT NULL,
  `cpm` float NOT NULL,
  `outbound_clicks` int(11) NOT NULL,
  `link_clicks` int(11) NOT NULL,
  `outbound_ctr` float NOT NULL,
  `page_likes` int(11) NOT NULL,
  `new_messaging_conversations` int(11) NOT NULL,
  `cost_per_new_messaging_conversation` float NOT NULL,
  `video_watches_at_75` int(11) NOT NULL,
  `estimated_ad_recall_lift_rate` float NOT NULL,
  `desktop_app_installs` int(11) NOT NULL,
  `desktop_app_uses` int(11) NOT NULL,
  `cost_per_app_install` float NOT NULL,
  `omni_adds_to_cart_shared_item` int(11) DEFAULT NULL,
  `omni_purchase_shared_item` int(11) DEFAULT NULL,
  `post_engagements` int(11) NOT NULL,
  `actions` int(11) DEFAULT NULL,
  `three_second_video_views` int(11) DEFAULT NULL,
  `website_leads` int(11) NOT NULL,
  `website_purchases` int(11) NOT NULL,
  `website_adds_to_cart` int(11) NOT NULL,
  `mobile_app_installs` int(11) NOT NULL,
  `on_facebook_leads` int(11) NOT NULL,
  `video_watches_at_100` int(11) NOT NULL,
  `fecha_registro` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fb_region`
--

CREATE TABLE `fb_region` (
  `id` int(11) NOT NULL,
  `campaign_name` varchar(200) NOT NULL,
  `ad_set_name` varchar(200) NOT NULL,
  `country` varchar(200) NOT NULL,
  `region` varchar(200) NOT NULL,
  `date` date DEFAULT NULL,
  `reach` int(11) NOT NULL,
  `frequency` float NOT NULL,
  `impressions` int(11) NOT NULL,
  `return_on_ad_spend` float NOT NULL,
  `cost_per_lead_form` float NOT NULL,
  `cost_per_store_visit` float NOT NULL,
  `cost` float NOT NULL,
  `cost_usd` float NOT NULL,
  `cpm` float NOT NULL,
  `outbound_clicks` int(11) NOT NULL,
  `link_clicks` int(11) NOT NULL,
  `outbound_ctr` float NOT NULL,
  `page_likes` int(11) NOT NULL,
  `new_messaging_conversations` int(11) NOT NULL,
  `cost_per_new_messaging_conversation` float NOT NULL,
  `video_watches_at_75` int(11) NOT NULL,
  `estimated_ad_recall_lift_rate` float NOT NULL,
  `desktop_app_installs` int(11) NOT NULL,
  `desktop_app_uses` int(11) NOT NULL,
  `cost_per_app_install` float NOT NULL,
  `post_engagements` int(11) NOT NULL,
  `website_leads` int(11) NOT NULL,
  `website_purchases` int(11) NOT NULL,
  `website_adds_to_cart` int(11) NOT NULL,
  `mobile_app_installs` int(11) NOT NULL,
  `on_facebook_leads` int(11) NOT NULL,
  `video_watches_at_100` int(11) NOT NULL,
  `fecha_registro` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gg_campana`
--

CREATE TABLE `gg_campana` (
  `id` int(11) NOT NULL,
  `account_id` varchar(200) NOT NULL,
  `account` varchar(200) NOT NULL,
  `campaign_name` varchar(200) NOT NULL,
  `campaign_status` varchar(200) NOT NULL,
  `bidding_strategy_type` varchar(200) NOT NULL,
  `year_and_month` varchar(200) DEFAULT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `date` date NOT NULL,
  `impressions` int(11) NOT NULL,
  `clicks` int(11) NOT NULL,
  `cost` float NOT NULL,
  `cost_usd` float NOT NULL,
  `ctr` float NOT NULL,
  `cpc` float NOT NULL,
  `cpm` float NOT NULL,
  `budget` float NOT NULL,
  `daily_budget` float NOT NULL,
  `return_on_ad_spend` float NOT NULL,
  `cost_per_video_view` float NOT NULL,
  `video_views` int(11) NOT NULL,
  `watch_75_rate` float NOT NULL,
  `conversions` float NOT NULL,
  `conversion_rate` float NOT NULL,
  `cost_per_conversion` float NOT NULL,
  `impression_share` float NOT NULL,
  `search_impression_share` double NOT NULL,
  `fecha_registro` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `link_campana`
--

CREATE TABLE `link_campana` (
  `id` int(11) NOT NULL,
  `account_name` varchar(200) NOT NULL,
  `account_id` varchar(200) NOT NULL,
  `campaign_name` varchar(200) NOT NULL,
  `campaign_status` varchar(200) NOT NULL,
  `campaign_start_date` date NOT NULL,
  `campaign_end_date` date NOT NULL,
  `campaign_total_budget` float NOT NULL,
  `campaign_objective_type` varchar(200) NOT NULL,
  `campaign_cost_type` varchar(200) NOT NULL,
  `campaign_group_name` varchar(200) NOT NULL,
  `campaign_group_status` varchar(200) NOT NULL,
  `campaign_group_start_date` date NOT NULL,
  `campaign_group_end_date` date NOT NULL,
  `campaign_group_total_budget` float NOT NULL,
  `year_and_month` varchar(200) DEFAULT NULL,
  `date` date NOT NULL,
  `impressions` int(11) NOT NULL,
  `clicks` int(11) NOT NULL,
  `cost` float DEFAULT NULL,
  `cost_usd` float DEFAULT NULL,
  `ctr` float NOT NULL,
  `cpc` float NOT NULL,
  `cpm` float NOT NULL,
  `total_spent_usd` float NOT NULL,
  `opens` int(11) NOT NULL,
  `sends` int(11) NOT NULL,
  `action_clicks` int(11) NOT NULL,
  `conversions` int(11) NOT NULL,
  `cost_per_conversion` float NOT NULL,
  `video_views_at_75` int(11) NOT NULL,
  `video_views` int(11) NOT NULL,
  `fecha_registro` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `fb_anuncio`
--
ALTER TABLE `fb_anuncio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `fb_campana`
--
ALTER TABLE `fb_campana`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `fb_edad_gen`
--
ALTER TABLE `fb_edad_gen`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `fb_plataforma`
--
ALTER TABLE `fb_plataforma`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `fb_region`
--
ALTER TABLE `fb_region`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `gg_campana`
--
ALTER TABLE `gg_campana`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `link_campana`
--
ALTER TABLE `link_campana`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `fb_anuncio`
--
ALTER TABLE `fb_anuncio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=441;

--
-- AUTO_INCREMENT de la tabla `fb_campana`
--
ALTER TABLE `fb_campana`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fb_edad_gen`
--
ALTER TABLE `fb_edad_gen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fb_plataforma`
--
ALTER TABLE `fb_plataforma`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fb_region`
--
ALTER TABLE `fb_region`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `gg_campana`
--
ALTER TABLE `gg_campana`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `link_campana`
--
ALTER TABLE `link_campana`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;
