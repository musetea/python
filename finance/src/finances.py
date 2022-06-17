import pandas as pd
import FinanceDataReader as fdr

def krx():
    krx = fdr.StockListing("KRX")
    print(krx.shape)
    print(krx.head())
    print(krx.info())
    print(krx.describe())
    krx.to_csv('krx.csv', index=False)

def fn_ex(d):
    print(d.shape)
    print(d.info())
    print(d.describe())
    print(d.nunique())
    print(d.index)
    print(d.columns)
    print(d.values)
    print(d['Name'])
    print(d.loc[0])
    print(d[['Symbol', 'Name']])
    print(d.loc[[0,1]])
    print(d.loc[4, 'Name'])
    print(d.loc[[0,1,2,3], ['Name', 'Symbol']])
    print(d[d['Name'] == '카카오'])

def fn_region_market(d):
    print(d[ d['Region'] == "서울특별시" & d['Market'] == "KOSPI" ] )
    

def main():
    d = pd.read_csv('krx.csv')
    fn_region_market(d)
    

if __name__ == "__main__":
    main()