from src.db_manager import DatabaseManager
from src.visualization import visualization
if __name__ == "__main__":
    db_path = './data/movies.db'  
    
    db_manager = DatabaseManager(db_path)
    
    
    query = "SELECT * FROM movies" 

    

    df = db_manager.read_data(query)


    vis = visualization()
    years_graphic = vis.plot_data(df,'YEAR','BOX_OFFICE','BOX OFFICE OVER THE YEARS', 'YEAR' , 'BOX_OFFICE' )
        
    budget_graphic = vis.plot_data(df,'YEAR','BUDGET','BUDGET OVER THE YEARS', 'YEAR' , 'BOX_OFFICE' )
   
    query2 =  '''
        SELECT NAME, (BOX_OFFICE - BUDGET) AS "REVENUE" 
        FROM MOVIES 
        ORDER BY REVENUE DESC 
        LIMIT 5;
'''

    df2 = db_manager.read_data(query2)

    vis.top_list('barh',df2['NAME'], df2['REVENUE'], '5 MOST REVENUE MOVIES')


   


    query3 = ''' 
        SELECT NAME, (BOX_OFFICE - BUDGET) AS "REVENUE" 
        FROM MOVIES 
        ORDER BY REVENUE ASC 
        LIMIT 5;
    
    '''
    df3 = db_manager.read_data(query3)

    vis.top_list('barh',df3['NAME'], df3['REVENUE'], '5 LEAST REVENUE MOVIES')




    query4= ''' 
    SELECT NAME,IMDB_RATING 
    FROM MOVIES
    ORDER BY IMDB_RATING 
    DESC 
    '''
    df4 = db_manager.read_data(query4)

    vis.top_list('barh',df4['NAME'], df4['IMDB_RATING'], 'WORST TO BEST IMDB RATING')

    query5= ''' 
    SELECT IMDB_RATING FROM MOVIES
    '''
    df5 = db_manager.read_data(query5)
    vis.gauss_function(df5,'IMDB RATING','rating','movie')

    db_manager.close_conn()