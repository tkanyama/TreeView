#!/usr/bin/env python
# -*- coding: utf-8 -*-
###coding: utf-8 の部分は、書類のコーディングに依存する
###ファイル(F)->保存オプションの詳細設定(V)...
###で書類のコーディングが変更可能
###この場合「Unicode(UTF-8シグネチャなし)-コードページ65001」
###SHIFT-JISの場合はcp932
import pypyodbc

def pypy():
    cnn = pypyodbc.connect('DRIVER={FileMaker ODBC};SERVER=192.168.0.171:2399;UID=admin;PWD=;DATABASE=tosho.fmp12')
    cur = cnn.cursor()
    #日本語フィールドの場合、かならずダブルクォーテーションで囲む必要があります。
    cur.execute("SELECT \"ID\",\"名前\" from \"テーブル名\" WHERE \"ID\" = 番号")
    rows = cur.fetchall()
    for row in rows:
        print(row[1])
    cur.close()
    cnn.close()

if __name__ == "__main__":
    pypy()
