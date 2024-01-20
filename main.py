import requests
import json

print("   _____         _                     _                _____                                ")
print("  / ____|       (_)                   (_)              / ____|                               ")
print(" | (_____      ___ _ __ ___  _ __ ___  _ _ __   __ _  | (___   ___ _ __ __ _ _ __   ___ _ __ ")
print("  \___ \ \ /\ / / | '_ ` _ \| '_ ` _ \| | '_ \ / _` |  \___ \ / __| '__/ _` | '_ \ / _ \ '__|")
print("  ____) \ V  V /| | | | | | | | | | | | | | | | (_| |  ____) | (__| | | (_| | |_) |  __/ |   ")
print(" |_____/ \_/\_/ |_|_| |_| |_|_| |_| |_|_|_| |_|\__, | |_____/ \___|_|  \__,_| .__/ \___|_|   ")
print("                                                __/ |                       | |              ")
print("                                               |___/                        |_|              ")
print("Made by: ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++.>---.++++++++++++.--------.++++++++++++++.")

def main():
    print("\n")
    participantId = input("Participant Id: ")
    print("Sort By: age, distance, stroke, course, time, date, meet")
    sortBy = input(": ")
    
    url = "https://sal-sc-results-prod-app.azurewebsites.net/api/public/results/results"
    params = {
        "pageNumber": 1,
        "pageSize": 10000,
        "sortTime": True,
        "participantId": participantId
    }

    headers = {
        "Sec-Ch-Ua": "",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Authorization": "Bearer null",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36",
        "Sec-Ch-Ua-Platform": "",
        "Origin": "https://results.swimming.org.au",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://results.swimming.org.au/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, params=params, headers=headers)

    # Extract only the required fields from the response
    filtered_data = []
    for result in response.json()["data"]["data"]:
        filtered_result = {
            "age": result["age"],
            "distance": result["distance"],
            "stroke": result["stroke"],
            "course": result["course"],
            "time": result["time"],
            "date": result["date"],
            "meet": result["meet"]
        }
        filtered_data.append(filtered_result)

    # Sort the filtered data by age
    sorted_data = sorted(filtered_data, key=lambda x: x[sortBy])

    # Save the filtered data to a new JSON file
    with open("data.json", "w") as f:
        json.dump(sorted_data, f, indent=2)
        
    print("Done! your data is in the file data.json")
        
while True:
    main()
