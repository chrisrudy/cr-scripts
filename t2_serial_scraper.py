import json
import beyondclient

def regulator_scraper():
    unit_token_list = ['7RY0DYQDK28V7','DKZQ3Z77H8SG7','L01JC18RPK2EP','L179E11194H3R','L21M7Q55JAJQE','L3ACTQMYTG6JQ',
                        'L45E13536RAT1','L606H3YKJ0WMJ','L7GDZEF2HJQXB','L7JZ7GBGCX37G','L8G659J55FE8T','L9AEWKDAYY0N0',
                        'L9HQ08JH0AS6C','LA5H87M0ZVS6X','LAEEZ08Y347S2','LBGGV2W4PCCZW','LC09R4PYZVG36','LES8FGS7EY549',
                        'LFTTMK3CSHAWM','LGHXFTS8TG7WX','LJXE009NYW5AW','LJZH23C4CFV9Z','LNV96N205KH8V','LPR336E46ADZZ',
                        'LQP34BQV261YB','LRSVC0RV4B2FY','LT56QA83X2M2Q','LTVPTP89YDZ4G','LV1YYR6SJRS9S','LWC52T0TAQHF2',
                        'LYNPXN2NNESKT','LZFEC0A1AZ6V1','7GXT0A8TF5HPZ','8JX7YTS9VRBVX','CY9SW77Y6VQ38','CZ04SN4ZVME2V',
                        'D8TWAZHDSQH8W','DWPQJ86TE2B1B','L8XKYC21KTJVE','LA1347PHF46FR','LFVFWDVS3JD97','LSNC3GB16AEKF',
                        'NBD1NS0JZ3FMQ','NG3N25FBX6160','PT2S121ZRYDM9','RJJTT8C9V4CA3','WT259TNNMP4M9']
    device_data = []

    for user_token in unit_token_list:
        loop_killer = True
        page_number = 0

        while loop_killer == True:
            reg_url = f"https://regulator.sqprod.co/api/js/v2/devices?user_token={user_token}&pagination_token={page_number}"
            print(reg_url)
            # Handles duo authentication
            beyond = beyondclient.session()
            reg_response = beyond.get(reg_url)

            if reg_response.status_code == 200:
                reg_json = json.loads(reg_response.content)
            else:
                print("Check whether you're authorized to access Regulator")

            for values in reg_json["entities"]:
                if values["hardware"] == "T2":
                    device_data.append(values["udid"])
                elif values["hardware"] == "T2b":
                    device_data.append(values["hardware"])
                    device_data.append(values["udid"])

            print(reg_json["meta"]["pagination_token"])

            if reg_json["meta"]["pagination_token"] == None:
                break
            else:
                page_number += 1

            print(device_data)

        else:
            if reg_json["meta"]["pagination_token"] == "null":
                for values in reg_json["entities"]:
                    if values["hardware"] == "T2":
                        device_data.append(values["udid"])
                    elif values["hardware"] == "T2b":
                        device_data.append(values["hardware"])
                        device_data.append(values["udid"])

        with open("t2_serials.txt", "w") as serial_numbers:
            for devices in device_data:
                serial_numbers.write(f"\'{devices}\',\n")


regulator_scraper()