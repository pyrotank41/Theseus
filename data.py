import alpaca_trade_api as tradeapi
import keys


class data:
    def __init__(self):
        self.api = tradeapi.REST(keys.paper_alpaca['key'], keys.paper_alpaca['secret'],
                                 base_url=keys.paper_alpaca['url'])
        pass

    def get_bars(self, symbol, multiplier, timespan, _from, _to, limit=100):
        return self.api.polygon.historic_agg_v2(symbol, multiplier, timespan, _from=_from, to=_to).df



if __name__ == "__main__":
    d = data()
    print(d.get_bars('TSLA', 4, 'hour', '2020-11-01', '2020-12-01'))
