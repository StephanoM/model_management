headers = {
    # "Authority": "www.modelmanagement.com",
    # "Path": "/backend/api/models/search",
    # "Scheme": "https",
    # "Accept": "application/json, text/plain, */*",
    # "Accept-encoding": "gzip, deflate, br, zstd",
    # "Accept-language": "en",
    # "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOWVjOTEyNjBhZmM4ZGNkNDJmZjJiYTA1NDE4OWIyZDc4YTExMmJmYjE3NDc0ODc2OWM1YjFmNTQzYTk4Yzc4YjNiZjgzM2YyNWRhMmQwNDciLCJpYXQiOjE3Mjk3MjM1NTkuMDczODA2LCJuYmYiOjE3Mjk3MjM1NTkuMDczODEsImV4cCI6MTczMjMxOTE1OS4wNjQ1NTQsInN1YiI6IjM5NTc0MzAiLCJzY29wZXMiOltdfQ.5TJm_dOUAaCOImpu_GK8M-jbWjg0tPzDnfw6WY7YXIFJN09D6IekJyHEni7vJ6XZZtTGGJPBiJwysoQdF2Z-5n7LR6i2RjmAH7o843N5Uin1pxbsLXw671sDpIrfFfABWnUkBiSBrfsGyYHG9OyPsq0-3kTBJmG5MxtTx4hpSU6HCaZ-Ooz9fS1T5Cb52t_s-RgArvLWPOx2xat0DkofcXIWqSWsd-JVLL4bqItwQM5368rKKkkdnsksxTy1Pvb3LGEfwg_FsO0s7To1u-1zx_Z7aFAvpdnkV_grRy_K4qTXbSKuQKyjZhnroJdLacGpgOVODiIg2CT03TZ3jKfCzIAM9D-XCQUCQRPDjZdMs8LwUE_7DvD8deV7SZwDXqq5vsVXyZdDgjCTCMyeuq5q2hv9mFDCm4cp7pBO3lJSrmsK8Ral6ub_U5-6FmdW4KaP4Ayp06QZLD37yU8K9F3iJgrwKfBGEKzeBd0XLyzkd6bco5EeqLC8h0aobHbXBJsagUwsxzfftj6oxBUzZATVm8sRMqIg-s2MdhMeMe9mGi2tKiQorT3WfHtVZO6zHy8_uxSB4vaNbHO0cxiUrkXq88RayMbCrXn9yLj1RIm5tM1GyjZZayCrnwcKzfZGB72stlx5q4auTD6dsh0kNqhFcv8Dyru8S11TseSj-2qQ1RA",
    # "Content-length": "172",
    # "Content-type": "application/json",
    # "Origin": "https://www.modelmanagement.com",
    # "Priority": "u=1, i",
    # "Referer": "https://www.modelmanagement.com/models/?country=US",
    # "Sec-Ch-Ua": '"Chromium";v="130", "Opera";v="116", "Not?A_Brand";v="99"',
    # "Sec-Ch-Ua-Mobile": "?0",
    # "Sec-Ch-Ua-Platform": '"Windows"',
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-origin",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/116.0.0.0 (Edition developer)",
    # "Cookie": '''
    #     i18n_redirected=en; auth.strategy=customLocal; __zlcmid=1ONn7H2ncYWtkp6; freshman=industry_professional; auth._refresh_token.customLocal=false; auth._token.customLocal=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOWVjOTEyNjBhZmM4ZGNkNDJmZjJiYTA1NDE4OWIyZDc4YTExMmJmYjE3NDc0ODc2OWM1YjFmNTQzYTk4Yzc4YjNiZjgzM2YyNWRhMmQwNDciLCJpYXQiOjE3Mjk3MjM1NTkuMDczODA2LCJuYmYiOjE3Mjk3MjM1NTkuMDczODEsImV4cCI6MTczMjMxOTE1OS4wNjQ1NTQsInN1YiI6IjM5NTc0MzAiLCJzY29wZXMiOltdfQ.5TJm_dOUAaCOImpu_GK8M-jbWjg0tPzDnfw6WY7YXIFJN09D6IekJyHEni7vJ6XZZtTGGJPBiJwysoQdF2Z-5n7LR6i2RjmAH7o843N5Uin1pxbsLXw671sDpIrfFfABWnUkBiSBrfsGyYHG9OyPsq0-3kTBJmG5MxtTx4hpSU6HCaZ-Ooz9fS1T5Cb52t_s-RgArvLWPOx2xat0DkofcXIWqSWsd-JVLL4bqItwQM5368rKKkkdnsksxTy1Pvb3LGEfwg_FsO0s7To1u-1zx_Z7aFAvpdnkV_grRy_K4qTXbSKuQKyjZhnroJdLacGpgOVODiIg2CT03TZ3jKfCzIAM9D-XCQUCQRPDjZdMs8LwUE_7DvD8deV7SZwDXqq5vsVXyZdDgjCTCMyeuq5q2hv9mFDCm4cp7pBO3lJSrmsK8Ral6ub_U5-6FmdW4KaP4Ayp06QZLD37yU8K9F3iJgrwKfBGEKzeBd0XLyzkd6bco5EeqLC8h0aobHbXBJsagUwsxzfftj6oxBUzZATVm8sRMqIg-s2MdhMeMe9mGi2tKiQorT3WfHtVZO6zHy8_uxSB4vaNbHO0cxiUrkXq88RayMbCrXn9yLj1RIm5tM1GyjZZayCrnwcKzfZGB72stlx5q4auTD6dsh0kNqhFcv8Dyru8S11TseSj-2qQ1RA; _gcl_au=1.1.2116165893.1729723330.23606382.1729723559.1729723559; AK_b3cd91=osv7tmg5ddjvj0v7p2r8vfjj05; mmt=%7B%22public%22%3Atrue%2C%22internal%22%3Afalse%2C%22private%22%3Atrue%2C%22uid%22%3A%223957430%22%7D; mmts=1; mm_alerts={"flash_offer_apr_19":true}; mm=__current_user_id%3D3957430%26__CurrentUserType%3DUser%26UserTarget%3Dmember%26hash%3D0c97220dbc103564924896458528d09b%26date%3D1730144045; _gid=GA1.2.157905768.1730613984; _ga_TFZYV5TM0W=GS1.2.1730684035.9.0.1730684035.0.0.0; _ga=GA1.2.890789214.1729723331; _ga_0X5XTW2N46=GS1.1.1730730975.15.1.1730731361.57.0.285158891; _dc_gtm_UA-6571879-1=1
    #     '''
}

cookies = {
    "i18n_redirected": "en",
    "auth.strategy": "customLocal",
    "__zlcmid": "1ONn7H2ncYWtkp6",
    "freshman": "industry_professional",
    "auth._refresh_token.customLocal": "false",
    "auth._token.customLocal": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOWVjOTEyNjBhZmM4ZGNkNDJmZjJiYTA1NDE4OWIyZDc4YTExMmJmYjE3NDc0ODc2OWM1YjFmNTQzYTk4Yzc4YjNiZjgzM2YyNWRhMmQwNDciLCJpYXQiOjE3Mjk3MjM1NTkuMDczODA2LCJuYmYiOjE3Mjk3MjM1NTkuMDczODEsImV4cCI6MTczMjMxOTE1OS4wNjQ1NTQsInN1YiI6IjM5NTc0MzAiLCJzY29wZXMiOltdfQ.5TJm_dOUAaCOImpu_GK8M-jbWjg0tPzDnfw6WY7YXIFJN09D6IekJyHEni7vJ6XZZtTGGJPBiJwysoQdF2Z-5n7LR6i2RjmAH7o843N5Uin1pxbsLXw671sDpIrfFfABWnUkBiSBrfsGyYHG9OyPsq0-3kTBJmG5MxtTx4hpSU6HCaZ-Ooz9fS1T5Cb52t_s-RgArvLWPOx2xat0DkofcXIWqSWsd-JVLL4bqItwQM5368rKKkkdnsksxTy1Pvb3LGEfwg_FsO0s7To1u-1zx_Z7aFAvpdnkV_grRy_K4qTXbSKuQKyjZhnroJdLacGpgOVODiIg2CT03TZ3jKfCzIAM9D-XCQUCQRPDjZdMs8LwUE_7DvD8deV7SZwDXqq5vsVXyZdDgjCTCMyeuq5q2hv9mFDCm4cp7pBO3lJSrmsK8Ral6ub_U5-6FmdW4KaP4Ayp06QZLD37yU8K9F3iJgrwKfBGEKzeBd0XLyzkd6bco5EeqLC8h0aobHbXBJsagUwsxzfftj6oxBUzZATVm8sRMqIg-s2MdhMeMe9mGi2tKiQorT3WfHtVZO6zHy8_uxSB4vaNbHO0cxiUrkXq88RayMbCrXn9yLj1RIm5tM1GyjZZayCrnwcKzfZGB72stlx5q4auTD6dsh0kNqhFcv8Dyru8S11TseSj-2qQ1RA",
    "_gcl_au": "1.1.2116165893.1729723330",
    "AK_b3cd91": "osv7tmg5ddjvj0v7p2r8vfjj05",
    "geoip_country": "us",
    "geoip_country_name": "united+states",
    "mmt": '{"public":true,"internal":false,"private":true,"uid":"3957430"}',
    "mmts": "1",
    "mm_alerts": '{"flash_offer_apr_19":true}',
    "mm": "__current_user_id=3957430&__CurrentUserType=User&UserTarget=member&hash=0c97220dbc103564924896458528d09b&date=1730144045",
    "_gid": "GA1.2.157905768.1730613984",
    "_ga_TFZYV5TM0W": "GS1.2.1730684035.9.0.1730684035.0.0.0",
    "_ga": "GA1.2.890789214.1729723331",
    "mm_session": "iMeMg1Yq5WExCVHKigI7vSCIkCyUNGXOOjmmF9oa",
    "_dc_gtm_UA-6571879-1": "1",
    "_ga_0X5XTW2N46": "GS1.1.1730730975.15.1.1730731358.60.0.285158891"
}