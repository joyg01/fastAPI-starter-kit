class TestSettings():
    OPEN_TOKEN_DUMMY: str = "DUMMY VALUE FOR COOKIE"
    OPEN_TOKEN_DECODED_USER: dict = {
        "firstname": "Geo",
        "not-on-or-after": "2021-05-22T10:39:07Z",
        "pf_attribute_list": "IAMPFIZERUSER,cn,displayname,firstname,group,lastname,INTERNETEMAILADDRESS",
        "subject": "joyg01",
        "cn": "joyg01",
        "not-before": "2021-05-22T10:03:07Z",
        "IAMPFIZERUSER": "joyg01",
        "lastname": "Joy",
        "authnContext": "urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified",
        "displayname": "'Joy, Geo'",
        "INTERNETEMAILADDRESS": "Geo.Joy@pfizer.com",
        "renew-until": "2021-05-22T22:04:06Z",
        "email": "Geo.Joy@pfizer.com",
        "group": [
            "group1",
            "group_for_admins",
            "group_for_users"
        ],
        "is.subsequent.request": "TRUE"
    }

test_settings = TestSettings()