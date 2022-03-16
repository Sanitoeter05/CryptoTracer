import RawCrypto as rc
import pyinputplus


fileETH = "logs/logETH.txt"
fileLog = "logs/log.txt"
fileBTC = "logs/logBTC.txt"


if __name__ == '__main__':
    CT = rc.CryptoChecker(fileETH, fileLog, fileBTC)
    currentWallet = {}

    if CT.check_api_key() == False:
        key = input("paste your API key here")
        file = open(CT.api_file(), "w")
        file.write(key)
        file.close()
        print(f"start your program again\n")

    while True:
        print("what do you want to do?")
        Menu = pyinputplus.inputMenu(["add/remove Coins", "Read the walled", "Exit"], numbered=True)

        if Menu == "add/remove Coins":
            wallet_coin = ""
            aor_menu = pyinputplus.inputMenu(['add', 'remove'], numbered=True)
            if aor_menu == "add":

                print("what do you want to add?")
                coin_to_add = pyinputplus.inputMenu(['bitcoin', 'ethereum'], numbered=True)

                if coin_to_add == 'bitcoin':
                    wallet_coin = "BTC"

                elif coin_to_add == "ethereum":
                    wallet_coin = "ETH"

                path_to_walled = f"logs/log{wallet_coin}.txt"

                amount_to_add = input("how much do you want to add?")

                CT.aor_coins(path_to_walled, amount_to_add, "add")
                print("added coins")

            elif aor_menu == "remove":
                print("what do you want to remove?")
                coin_to_add = pyinputplus.inputMenu(['bitcoin', 'ethereum'], numbered=True)

                if coin_to_add == 'bitcoin':
                    wallet_coin = "BTC"

                elif coin_to_add == "ethereum":
                    wallet_coin = "ETH"

                path_to_walled = f"logs/log{wallet_coin}.txt"

                amount_to_add = input("how much do you want to remove?")

                CT.aor_coins(path_to_walled, amount_to_add, "remove")

        elif Menu == "Read the walled":
            while True:
                ETH = CT.coin_info_eth()
                BTC = CT.coin_info_btc()
                if ETH != "":
                    currentWallet.update({"ETH": {"amount": f"{ETH}"}})

                if BTC != "":
                    currentWallet.update({"BTC": {"amount": f"{BTC}"}})

                Coin = ""
                amount = ""

                wallet_menu = pyinputplus.inputMenu(['bitcoin', 'ethereum', "exit"], numbered=True)
                if wallet_menu == "bitcoin":
                    Coin = "BTC"

                elif wallet_menu == "ethereum":
                    Coin = "ETH"

                elif wallet_menu == "exit":
                    break

                try:
                    amount = currentWallet[f"{Coin}"]["amount"]
                    call = CT.API(Coin, amount)
                    coin_price = round(call["quote"]["EUR"]["price"], 2)
                    currentWallet[f"{Coin}"]["price"] = f"{coin_price}"
                    print(currentWallet[f"{Coin}"]["price"])

                except KeyError:
                    print("No Coins in your walled")

        else:
            break
