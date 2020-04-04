from client import RestClient
import pprint
pp = pprint.PrettyPrinter(indent=4)
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("thomas.wawra@haufe-akademie.de", "Rys26Jr8AAF3Jit4")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    location_name="Germany",
    language_code="de",
    date_from="2019-01-01",
    date_to="2020-01-01",
    keywords=[
        "robo advisor"
    ]
)
# POST /v3/keywords_data/google_trends/explore/live
# the full list of possible parameters is available in documentation
response = client.post(
    "/v3/keywords_data/google_trends/explore/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    pp.pprint(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" %
          (response["status_code"], response["status_message"]))
