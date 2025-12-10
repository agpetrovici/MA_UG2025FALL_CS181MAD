import json

import requests

params = {"brand": "toyota"}
payload = {
    "uscEnv": "production",
    "filters": [
        {"filterId": "cash", "min": None, "max": None},
        {"filterId": "usedCarBrand", "valueIds": ["38"]},
        {"filterId": "usedCarModel", "valueIds": ["CO", "CR"]},
    ],
    "filterContext": "used",
    "offset": 0,
    "resultCount": 10,
    "sortOrder": "cashAsc",
    "distributorCode": "94244",
    "includeActiveFilterAggregations": False,
    "enableBiasedSort": False,
    "disabledFiltersIds": [],
    "enableExperimentalTotalCountQuery": False,
    "enableVehicleAggregations": False,
    "vehicleAggregationsVersionCode": "",
    "hasContentBlock": True,
}
r = requests.post(
    "https://usc-webcomponents.toyota-europe.com/v1/api/usedcars/results/es/es",
    params=params,
    json=payload,
)
data = r.json()
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
