import requests

from website.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import VKProvider

import vk_api

USER_FIELDS = [
    "first_name",
    "last_name",
    "nickname",
    "screen_name",
    "sex",
    "bdate",
    "city",
    "country",
    "timezone",
    "photo",
    "photo_medium",
    "photo_big",
    "photo_max_orig",
    "has_mobile",
    "contacts",
    "education",
    "online",
    "counters",
    "relation",
    "last_seen",
    "activity",
    "universities",
]


class VKOAuth2Adapter(OAuth2Adapter):
    provider_id = VKProvider.id
    access_token_url = "https://oauth.vk.com/access_token"
    authorize_url = "https://oauth.vk.com/authorize"
    profile_url = "https://api.vk.com/method/users.get"
    wall_url = "https://api.vk.com/method/wall.get"

    # PAY ATTENTION, THIS VALUES CAN BE CHANGED IN APP SETTINGS
    service_key = "23fc074823fc074823fc074835238049bf223fc23fc0748419829b938c193a0d50635ac"
    app_id = 8146679

    def complete_login(self, request, app, token, **kwargs):
        uid = kwargs["response"].get("user_id")
        params = {
            "v": "5.95",
            "access_token": token.token,
            "fields": ",".join(USER_FIELDS),
        }
        if uid:
            params["user_ids"] = uid

        def merge_two_dicts(x, y):
            z = x.copy()
            z.update(y)
            return z

        vk_session = vk_api.VkApi(app_id = self.app_id, client_secret=self.service_key)
        vk_session.token = {'access_token': token.token, 'expires_in': 0}
        vk = vk_session.get_api()
        group_list = vk.groups.get(user_id = uid, offset = 0)
 
        resp = requests.get(self.profile_url, params=params)
        resp.raise_for_status()
        extra_data = resp.json()["response"][0]
        email = kwargs["response"].get("email")
        if email:
            extra_data["email"] = email
        user_data = merge_two_dicts(extra_data, group_list)
        return self.get_provider().sociallogin_from_response(request, user_data)


oauth2_login = OAuth2LoginView.adapter_view(VKOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(VKOAuth2Adapter)
