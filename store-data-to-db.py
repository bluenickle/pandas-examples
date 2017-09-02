# -*- coding:utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Date

test_data = [
    {'name': 'Alice', 'number': 120, 'score': 95.5, 'issue_date': '2017-08-01' },
    {'name': 'Bob', 'number': 121, 'score': 97.5, 'issue_date': '2017-08-01' }
]

df = pd.DataFrame(test_data)

engine = create_engine('mysql://user:pass@host:port/pandas_test?charset=utf8')


df.to_sql(name='score', #表名
        con=engine, #数据库连接
        if_exists='replace', #遇见重复数据的处理方法: replace, append或fail
        schema='pandas_test', #数据库名
        index=True, #是否将pandas的Index作为数据库的Index
        index_label='id', #Index的数据库字段名
        dtype={'issue_date': Date}) #指定字段的类型




