import pandas as pd
from client import RestClient
from dictor import dictor

# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("thomas.wawra@haufe-akademie.de", "Rys26Jr8AAF3Jit4")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    target="whitebox.eu",
    location_name="Germany",
    language_name="German",
    filters=[
        ["metrics.organic.count", ">=", 100],
        "and",
        [
            ["metrics.organic.pos_1", ">", 0],
            "or",
            ["metrics.paid.count", "in", [1, 2]]
        ]
    ]
)
# POST /v3/dataforseo_labs/categories_for_domain/live
response = client.post(
    "/v3/dataforseo_labs/categories_for_domain/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    for key, value in response.items():
        if key == 'tasks':
            results = value[0]
            for key, value in results.items():
                if key == 'result':
                    results = value[0]
                    for key, value in results.items():
                        if key == 'items':
                            results = value[0]
                            


else:
    print("error. Code: %d Message: %s" %
          (response["status_code"], response["status_message"]))

output_table = pd.DataFrame(response)
# print(pd.DataFrame(dictor(response, 'tasks.0.result.0.items')))
