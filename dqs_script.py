DQS_USERS = [
    {
        "first_name": "Elijah",
        "last_name": "Wood",
        "country": "US",
        "email": "convertobonchev+amg@gmail.com",
        "visible_vpd": 29,
        "role": "CRA",
    },
    {
        "first_name": "Sean",
        "last_name": "Bean",
        "country": "GB",
        "email": "convertobonchev+bi@gmail.com",
        "visible_vpd": 19,
        "role": "CRA",
    },
]


def create_dqs_account(user_data, vpd_admin=False):
    vpd_id = 0
    if vpd_admin:
        vpd_id = 2
    subprocess.call(
        [
            "python",
            "manage.py",
            "dqs",
            "create-user",
            "--email",
            user_data["email"],
            "--password",
            '"Qwer$321"',
            "--vpd_id",
            f"{vpd_id}",
            "--first_name",
            user_data["first_name"],
            "--last_name",
            user_data["last_name"],
            "--country_iso",
            user_data["country"],
        ]
    )


def get_access_token(username):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    body = {
        "client_id": "ldn-umt",
        "username": username,
        "password": "Qwer$321",
        "grant_type": "password",
    }

    token_response = requests.post(
        url="https://sso-staging.drugdev.com/auth/realms/drugdev/protocol/openid-connect/token",
        data=body,
        headers=headers,
    )

    return "Bearer {}".format(token_response.json()["access_token"])


def update_user(user_data):
    url = "https://dqs-api-qa1.drugdev.com/user/account/"
    response = requests.request(
        "PUT",
        url,
        data=urlencode(user_data),
        headers={
            "Authorization": get_access_token(user_data["email"]),
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    return response.json()
