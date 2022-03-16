import coinmarketcapapi
import ast
import datetime as DT


key = open("Secure/Api_key.txt")
cmc = coinmarketcapapi.CoinMarketCapAPI(key.read())


class CryptoChecker:

    def api_file(self):
        return "Secure/Api_key.txt"

    def __init__(self, fileETH, fileLog, fileBTC):
        self.fileETH = fileETH
        self.log = fileLog
        self.fileBTC = fileBTC

    def write(self, crypto):
        self.log.write(crypto)

    def API(self, currency, amount):
        call = cmc.tools_priceconversion(amount=amount, symbol=currency, convert='EUR')
        call = repr(call.data)
        call = ast.literal_eval(call)
        return call

    def coin_info_eth(self):
        file = open(self.fileETH, 'r')
        return file.read()

    def coin_info_btc(self):
        file = open(self.fileBTC, "r")
        return file.read()

    def aor_coins(self, coin, amount, aor):
        file = open(coin, "r")
        save = file.read()
        file.close()
        if save == "":
            save = 0
        amount_to_add = amount
        if aor == "add":
            amount = float(amount) + float(save)
            self.__log_it(f"adding {amount_to_add} to {coin}")
        elif aor == "remove":
            amount = float(save) - float(amount)
            if 0.0 <= float(amount):
                self.__log_it(f"removing {amount_to_add} form {coin}")
                print("removed coins")
            elif 0.0 > amount:
                amount = save
                print(f"you cant remove {amount_to_add} coins from {amount} coins")

        file_to_change = open(coin, "w")
        file_to_change.write(str(amount))
        file_to_change.close()

    def __log_it(self, to_log):
        file = open(self.log, "a")
        log_time = DT.datetime.now()
        file.write(str(f"{log_time}: logged {to_log} to walled " + f"\n"))
        file.close()

    def check_api_key(self):
        file = "Secure/Api_key.txt"
        file = open(file, "r")
        file = file.read()
        if file == "":
            return False
        else:
            return True
