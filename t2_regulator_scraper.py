import json
import csv
import beyondclient

def regulator_scraper():
    unit_token_list = ['8BA53NMG5KP1T','FH4ET5KAYGPS2','080K24ZY28XCP',
    '311HZ58QHKXHQ','70D3A26DSQHS4','7D333HF5JXTFY','AN0Q2E4WVCPDG','DENG3QFP1VHYR','LYQKK6VKTR4S8','PW79S6GDET97C',
    'VFT8WKTS1D118','BR2G215SWRGG4','LX4XWZZNR13V7','PK6J4385M4WAE','TA8P15KZ2KS1B','07C27N9FBEW5A','0958GV0E3GEZY',
    '0R91248QRJNTV','15HD98896DG0H','17BR30CM6QHNT','18V8BJWBP8V93','1F096X43XWG0Y','1J7PWED8XK0CJ','1MTWD7NN5BBE5',
    '1TWCAVEQMD5YV','1WASFTV6VA4Z7','1WGTDX9BQGS53','P9592A67J16QQ','29T7XC0PF07C9','2XF38BPFPVY3H','460SYN5QA5H53',
    '4BKTC0V6WZ70B','4W0KZW6GRFY03','5T2D0M6HRJKS9','5VM7NNJHBFKW4','6XFDK5XTE6M8Y','7950BHHPJXSBN','7BBEN1M6GA9VN',
    '7HKFY5AW3NTWP','8C6YRVPF8YHJ2','8PRMWXYDTZX5G','8RECCMXNK6D3Z','9J295RN6ENF4E','9SWM8W93GTTRT','9YWCT5X5XH5GG',
    'AAJ9WGAAD0AEB','AJVA9C69D1HMJ','ANSERC8G50D99','AV5SADETYZKW0','BA8HDG2XP4325','BHCW071VAWRXZ','BM17TEEJB9H7W',
    'L9BF48HW5Q9NS','C01BSBG42FEME','CCWG7F30ZH7MF','CF3NZDFWZSV6H','CPT75K0F56ASP','CYB6EHZYYQEWT','DZDA1Y0HV89N4',
    'ERN76FA00NT07','FETEKVPVZFQDT','HAMAPZ640T3YP','HYZHAPTQX1XZ4','LFNW86TF9HRWB','LYS35BYWRVMEX','MQ3FTAN49B5PD',
    'NQQGR2F1Z4GTK','P67SE7MY33AGG','QPKK28VNMZFD4','SE7K6QVN4SC6F','XM64DS9C60042','Z6FS9Y44WRR9M','Z86SPA4XVVP38']

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
                    # To do: add CSV support here
                    # t2b_values = str(values["hardware"],values["udid"],values["squid"],values["user_token"])
                    # device_data.append(t2b_values)
                    # device_data.append(values["udid"])
                    # device_data.append(values["squid"])
                    # device_data.append(values["user_token"])
                elif values["hardware"] == "T2b":
                    # To do: add CSV support here
                    # t2b_values = str(values["hardware"],values["udid"],values["squid"],values["user_token"])
                    # device_data.append(t2b_values)
                    # device_data.append(values["hardware"])
                    # device_data.append(values["udid"])
                    # device_data.append(values["squid"])
                    # device_data.append(values["user_token"])

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