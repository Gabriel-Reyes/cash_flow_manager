import pandas as pd
import numpy as np

from classes import payables, receivables

ap = payables('Cash Flow/sample_payables.csv').monthly()
ar = receivables('Cash Flow/sample_receivables.csv').monthly()

ap['Type'] = 'Accounts Payable'
ar['Type'] = 'Accounts Receivable'

cash_flow = pd.concat([ap,ar])
print(cash_flow.head())