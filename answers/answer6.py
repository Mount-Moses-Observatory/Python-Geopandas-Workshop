dfsjoin2 = gpd.sjoin(boroughs,stop_search[stop_search['Outcome'] == 'Arrest']) 
dfpivot2 = pd.pivot_table(dfsjoin2,index='id',columns='Object of search',aggfunc={'Object of search':'count'})
dfpivot2.columns = dfpivot2.columns.droplevel()
dfpivot2 = dfpivot2.reset_index()
boroughs4 = boroughs.merge(dfpivot2, how='left',on='id')
boroughs4.head()
