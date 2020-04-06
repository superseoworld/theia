from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    keywords=[
        "phone",
        "watch"
    ],
    location_name="United States",
    language_name="English",
    filters=[
        ["relevant_serp_items", ">", 0],
        "or",
        ["median_position", "in", [ 1, 10 ]]
    ]
)
# POST /v3/dataforseo_labs/serp_competitors/live
response = client.post("/v3/dataforseo_labs/serp_competitors/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
