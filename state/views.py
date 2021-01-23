from django.shortcuts import render, redirect
from django.db import connection
import pandas as pd
import sqlparse
# import csv

# from .models import Entry
# from pymongo import MongoClient
# from ast import literal_eval
# from djongo.database import MongoClient




# with client.watch() as stream:  
#        for change in stream:  
#            print(change)  
# [
#             {
#                 '$match': {
#                     'blog': 'Tolani'
#                 }
#             },
#         ]
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def index(request):
    
    # for column in columns:
    #     print('NAME: {name!s:12} DEFINITION: {definition}'.format(
    #         name=column[0], definition=' '.join(str(t) for t in column[1:])))

    if request.method == 'GET':
        try:
            # db = sqlite3.connect(':memory:')
            # dfs = pd.read_excel('state/IC4_VB_ACTIVE_TXN.xlsx', sheet_name=None)
            # for table, df in dfs.items():
            #     df.to_sql(table, db)
            sql = request.GET['q']
            # print(sql)
            
            with connection.cursor() as cursor:
                query = sql
                cursor.execute(query)
                row = dictfetchall(cursor)

                # all_count, yes_count = row
                for i in row:
                    column = i.keys()
                # print(row)
                # p = pd.read_sql_query()("select * from state_person")
                # print(p)
                
                    # for us in rows:
                    #     row2 = us
                
                # print(all_count)
                # print(yes_count)
            context = {
                'a': row,
                'c': column
                
            }
            return render(request, 'index.html', context )
        except Exception as a:
            print(a)
            context = {
                'error': a
            }
    return render(request, 'index.html', context)
    # client = MongoClient()
    # db = client.workstat
    # collect = db.state_entry.find()
    # for u in collect:
    #     a=db[u].find({"blog":"Tolani"})
    #     print(a)

    # quer = [i for i in db.aggregate(
    #     pipeline=cursor_manager.CursorManager({})
    #  )]
    # print(quer)
        # if request.method == 'POST':
        #     # val = '{"blog":"Tolani"}'
        #         try:
        #             val = request.POST['q']
        #             dic1 = eval(val.strip())
        #             client = MongoClient()
        #             db = client.workstat
        #             print(dic1)
        #             collect = db['state_entry'].aggregate(dic1)
        #             print(collect)
        #             context = {
        #         'a': collect
        #     }
        #             return render(request, 'index.html', context)
        #         except:
        #             print(Exception)
            # if val != str:
            #     print('Not String')
# {"blog":"Test", "$and":[{ "headline":"Test"}]}

            # { "$and": [ { "blog": { "$ne": "Test" } }, { "blog": { "$exists": true } } ] }
            
        # db = pymongo.MongoClient()
        # if request.method == 'POST':
        #     val = request.POST['q']
        #     print(val)
        #     index=[i for i in Entry.objects.mongo_aggregate([
        #         {
        #             val
        #         },
        #     ])]
        #     print(index)
        #     return redirect('/')
        # return render(request, 'index.html')


    
    # [i for i in Entry.objects.mongo_aggregate([
    #         {
    #             '$match': {
    #                 'blog': 'Tolani'
    #             }
    #         },
    #     ])]
    # # index =Entry.objects.mongo_aggregate(
    # [
    #         {
    #             '$match': {
    #                 'blog': {
    #                     '$in':['Tolani', 'Naijaloaded']
    #                 } 
    #             }
    #         },
    #     ]
    
    # )

    # print(index)
    # with connection.cursor() as cursor:
    #     query = """
    #     [        {
    #             '$match': {
    #                 'blog': 'Naijaloaded'
    #             }
    #         }
    # ]
     
    #     """
    #     cursor.execute(query)
    #     row = cursor.fetchone()
    #     all_count, yes_count = row
    #     print(row)
    
    # [
    #         {
    #             '$match': {
    #                 'blog': {
    #                     '$in':['Tolani', 'Naijaloaded']
    #                 } 
    #             }
    #         },
    #     ]
    

    # database_wrapper = connections['workstat']
    # eggs_collection = database_wrapper.get_collection('state_entry')
    # eggs_collection.find({"blog":"Naijaloaded"})
    # context = {
    #     'q':index
    # }
    



# def results(request):
#     with connection.cursor() as cursor:
#         query = """
#         SELECT count(*) as all_count, 
#         count(*) FILTER(WHERE vote = 'yes') as yes_count
#         FROM people_person;
#         """
#         cursor.execute(query)
#         row = cursor.fetchone()
#         all_count, yes_count = row


            
        # {"blog":"Test", "$and":[{ "headline":"Test"}]}
