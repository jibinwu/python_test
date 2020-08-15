import requests
import pymysql
import json
import ddt


class   TestPlate():
    def conmysql(self):
        db=pymysql.connect(host='114.55.43.36',user='haibao',passwd='haibao1234',
                           db='db-haibao-core',port=3306,charset='utf8')
        cursor=db.cursor()
        sql="select * from usr_vhl where partner_code='weic-h5-all' order by update_datetime desc limit 10"
        cursor.execute(sql)
        results=cursor.fetchall()
        self.plates=[]
        for i in results:
            plate=i[2]
            self.plates.append(plate)
        return self.plates

    def addplate(self,plates):
        for plate in plates:
            content={"ownerName":"杨清淑","ownerPhone":"13404918779","plate":plate,"partnerCode":"undefined","checkCode":"2908"}
            headers={'Content-Type':'application/json;charset=UTF-8',
                     'Referer':'http://wxxtest.jbx188.com/index?pcode=undefined&version=testb'}
            r=requests.post('http://wxxtest.jbx188.com/api/hbb-biz/api/v1/vehicle/addVehicleAndIsEnableQuote',
                          data=json.dumps(content),headers=headers)
            print(r.status_code)
            print(r.json())
if __name__ == '__main__':
    object=TestPlate()
    A=object.conmysql()
    object.addplate(A)