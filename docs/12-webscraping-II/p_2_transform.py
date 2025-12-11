import datetime
import json
from pathlib import Path


def get_toyota_data() -> list[dict]:
    filepath = Path(__file__).parent.parent.parent / "data.json"
    with open(filepath, "r") as f:
        raw = json.load(f)

    data = []

    for item in raw["results"]:
        data.append(
            {
                "url": f"https://www.toyota.es/coches-segunda-mano/ficha.{item['id']}",
                "vehicle_status": item['vehicleStatus']['description'],
                "price": item["price"]["sellingPriceInclVAT"],
                "warranty":item['warranty']['code'],
                "km": item["mileage"]["value"],
                "unit":item['mileage']['unit']['description'],
                "is_hub_car":item['isHubCar'],
                "pricing_source":item['price']['pricingSource']['code'],
                "previous_owner": item["history"]["previousUsage"]["description"],
                "license_plate": item["licensePlate"],
                "vin": item["vin"],
                "production_date": datetime.datetime.strptime(
                    item["productionDate"], "%Y-%m-%d"
                ).strftime("%Y-%m-%d")
                if item["productionDate"]
                else None,
                "year": datetime.datetime.strptime(
                    item["productionDate"], "%Y-%m-%d"
                ).strftime("%Y")
                if item["productionDate"]
                else None,
                "model": item["product"]["model"],
                "version": item["product"]["versionName"],
                "province": item["dealer"]["address"]["region"],
                "city": item["dealer"]["address"]["city"],
                "transmission": item["product"]["transmission"]["name"],
                "eco": item["product"]["eco"]["label"]["description"],
                "euro_class": item["product"]["eco"]["euroClass"],
                "co2_emissions": item["product"]["eco"]["co2Emission"][0]["value"]
                if item["product"]["eco"]["co2Emission"]
                else None,
                "boot": item["product"]["bootCapacity"]["value"],
                "hp": item["product"]["engine"]["powerOutputHorsepower"]["value"],
            }
        )
    return data


if __name__ == "__main__":
    get_toyota_data()
