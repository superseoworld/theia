from client import RestClient
from pandas import DataFrame

client = RestClient("twawra@gmail.com", "hCX2X1V3UoV9cSsM")

domains = ["reservix.de"]

LOCATION_NAME = "Germany"
LANGUAGE_NAME = "German"


def getKeywordsForSite(sites=list(), location_name=LOCATION_NAME, language_name=LANGUAGE_NAME)

    post_data = dict()

    for site in sites:
        post_data[len(post_data)] = dict(
            location_name=LOCATION_NAME,
            language_name=LANGUAGE_NAME,
            target=domain)

    # POST /v3/keywords_data/google/keywords_for_site/live
    # the full list of possible parameters is available in documentation
    response = client.post(
        "/v3/keywords_data/google/keywords_for_site/live", post_data)
    # you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
    if response["status_code"] == 20000:
        return response["tasks"][0]["result"])
    else:
        print("error. Code: %d Message: %s" %
            (response["status_code"], response["status_message"]))
