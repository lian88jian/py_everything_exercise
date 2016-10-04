'''


@author: lianjian
'''
import MySQLdb

if __name__ == '__main__':
    
    conn = MySQLdb.connect(host="192.168.1.6",user="root",passwd="ZhaoX88A99",db="zentao",charset="utf8",port=10087)
    cursor = conn.cursor();
    cursor.execute("select t.name,t.finishedDate from zt_task t " +
        "where t.finishedBy = 'zhanyd' " +
        "and t.finishedDate like '2016-09%' " +
        "and t.`status` in ('closed', 'done')" +
        "order by t.openedDate desc")
    
    results = cursor.fetchall()
    for row in results:
        print('%s' % row[0])
    
    conn.close()