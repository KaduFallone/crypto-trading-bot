import pandas as pd
import os

class MyOrdersSave:
    def __init__(self, order, filename):
        self.order = order
        self.filename = filename
        self.filtered_order = self.filter_orders()


    def filter_orders(self):
        quantity = round(float(self.order['executedQty']), 2)
        unit_price = round(float(self.order['fills'][0]['price']), 2) if self.order['fills'] else None
        value = round(float(self.order['cummulativeQuoteQty']), 2)
        time = pd.to_datetime(self.order['transactTime'], unit='ms').tz_localize('UTC').tz_convert('America/Sao_Paulo').isoformat(sep=' ', timespec='seconds')

        return{
            'order_id': self.order['orderId'],
            'symbol': self.order['symbol'],
            'side': self.order['side'],
            'price': value,
            'quantity': quantity,
            'unit_price': unit_price,
            'time': time

        }

    def save_to_xls(self):
        df_novo = pd.DataFrame([self.filtered_order])
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            df_existente = pd.read_excel(self.filename)
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
        else:
            df_final = df_novo
        df_final.to_excel(self.filename, index=False)
        print(f"Order saved to {self.filename}\n")






# Order Sell: {
#     'symbol': 'XRPBRL', 
#     'orderId': 310951645, 
#     'orderListId': -1, 
#     'clientOrderId': 'x-HNA2TXFJed90a7e04099c9d130328d', 
#     'transactTime': 1787058487613, 
#     'price': '0.00000000', 
#     'origQty': '3.00000000', 
#     'executedQty': '3.00000000', 
#     'origQuoteOrderQty': '0.00000000', 
#     'cummulativeQuoteQty': '15.61800000', 
#     'status': 'FILLED', 
#     'timeInForce': 'GTC', 
#     'type': 'MARKET', 
#     'side': 'SELL', 
#     'workingTime': 1787058487613, 
#     'fills': [{'price': '5.20600000', 
#                'qty': '3.00000000', 
#                'commission': '0.00000372', 
#                'commissionAsset': 'BNB', 
#                'tradeId': 6970026}], 
#     'selfTradePreventionMode': 'EXPIRE_MAKER'}
