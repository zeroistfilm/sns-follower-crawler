import requests

cookies = {
    'personalization_id': '"v1_IZ7EwhEwDaq5P9hQIlNiIQ=="',
    'guest_id_marketing': 'v1%3A165728872491540990',
    'guest_id_ads': 'v1%3A165728872491540990',
    'guest_id': 'v1%3A165728872491540990',
    'external_referer': 'padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D',
    '_gid': 'GA1.2.1932765668.1657514577',
    'gt': '1546711996691025920',
    '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCPB9pvCBAToMY3NyZl9p%250AZCIlMjEyYTA1ZjI2MmM1YmUxZWRlMWU3MDUyNmJhMjc3NDA6B2lkIiU1MGVh%250ANDNiNTQwZjdiOGRiMzdjZTBkOTRhMzg0NjJlZA%253D%253D--384643328bab1344776692d179233652dc257290',
    'g_state': '{"i_l":0}',
    'at_check': 'true',
    '_ga_BYKEBDM7DS': 'GS1.1.1657599906.1.1.1657599924.0',
    'kdt': 'tida5xi7HPAMaNsR4NBosXcr1WdvpsTVdrQIRz2y',
    'auth_token': 'd5a8f47bda91b709e3a60667f971074dab19c6c3',
    'ct0': '5208f3bc3326d7365f9e3a39892619d792887477e9e55dc1399b0cf406dd79d046876fd42a28313d5d4cc0f0dfa7fbbd6828bbe338a4dcc9fe265ce9b23a26975e39e44ad91fea90d83e7332bebd0088',
    'twid': 'u%3D1475092423638667269',
    'att': '1-bcqz0jYkVeybFKtgO2JZSkANxlBNrDbM9GdMUky5',
    'lang': 'ko',
    'mbox': 'session#b82e7b311bc04082a8a0dca834c298d2#1657603287|PC#b82e7b311bc04082a8a0dca834c298d2.32_0#1720846227',
    '_ga_34PHSZMC42': 'GS1.1.1657601424.1.1.1657601428.0',
    '_ga': 'GA1.2.1029047494.1657288728',
}

headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'personalization_id="v1_IZ7EwhEwDaq5P9hQIlNiIQ=="; guest_id_marketing=v1%3A165728872491540990; guest_id_ads=v1%3A165728872491540990; guest_id=v1%3A165728872491540990; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _gid=GA1.2.1932765668.1657514577; gt=1546711996691025920; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCPB9pvCBAToMY3NyZl9p%250AZCIlMjEyYTA1ZjI2MmM1YmUxZWRlMWU3MDUyNmJhMjc3NDA6B2lkIiU1MGVh%250ANDNiNTQwZjdiOGRiMzdjZTBkOTRhMzg0NjJlZA%253D%253D--384643328bab1344776692d179233652dc257290; g_state={"i_l":0}; at_check=true; _ga_BYKEBDM7DS=GS1.1.1657599906.1.1.1657599924.0; kdt=tida5xi7HPAMaNsR4NBosXcr1WdvpsTVdrQIRz2y; auth_token=d5a8f47bda91b709e3a60667f971074dab19c6c3; ct0=5208f3bc3326d7365f9e3a39892619d792887477e9e55dc1399b0cf406dd79d046876fd42a28313d5d4cc0f0dfa7fbbd6828bbe338a4dcc9fe265ce9b23a26975e39e44ad91fea90d83e7332bebd0088; twid=u%3D1475092423638667269; att=1-bcqz0jYkVeybFKtgO2JZSkANxlBNrDbM9GdMUky5; lang=ko; mbox=session#b82e7b311bc04082a8a0dca834c298d2#1657603287|PC#b82e7b311bc04082a8a0dca834c298d2.32_0#1720846227; _ga_34PHSZMC42=GS1.1.1657601424.1.1.1657601428.0; _ga=GA1.2.1029047494.1657288728',
    'referer': 'https://twitter.com/_ll__l__/followers',
    'sec-ch-ua': '"Whale";v="3", " Not;A Brand";v="99", "Chromium";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.141 Whale/3.15.136.29 Safari/537.36',
    'x-csrf-token': '5208f3bc3326d7365f9e3a39892619d792887477e9e55dc1399b0cf406dd79d046876fd42a28313d5d4cc0f0dfa7fbbd6828bbe338a4dcc9fe265ce9b23a26975e39e44ad91fea90d83e7332bebd0088',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'ko',
}

params = {
    'variables': '{"userId":"1169226141632098305","count":200,"includePromotedContent":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true}',
    'features': '{"dont_mention_me_view_api_enabled":true,"interactive_text_enabled":true,"responsive_web_uc_gql_enabled":false,"vibe_tweet_context_enabled":false,"responsive_web_edit_tweet_api_enabled":false,"standardized_nudges_misinfo":false,"responsive_web_enhance_cards_enabled":false}',
}

response = requests.get('https://twitter.com/i/api/graphql/fJSopkDA3UP9priyce4RgQ/Followers', params=params,
                        cookies=cookies, headers=headers)

print(response.json())
