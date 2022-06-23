import pandas as pd
import FinanceDataReader as fdr
import numpy as np

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

# 서울소재지 코스피 종목의 종목코드 와 종목명만 수집 
def fn_region_market(d):
    print("서울소재지 코스피 종목의 종목코드 와 종목명만 수집")
    rows = (d['Region'] == "서울특별시") & (d['Market'] == "KOSPI")
    print(d.loc[rows, ["Symbol", "Name"]] )

## 결측치
def fn_listingDate(d):
    print(d["ListingDate"].head(1))
    d['ListingYear'] = d['ListingDate'].dt.year
    print(d['ListingYear'])
    # np.nan == float
    print(type(np.nan))
    

def main():
    d = pd.read_csv('krx.csv')
    # object -> datetime
    d["ListingDate"] = pd.to_datetime(d['ListingDate'])
    #fn_region_market(d)
    fn_listingDate(d)    

if __name__ == "__main__":
    main()