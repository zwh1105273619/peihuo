from model.process_front import Process_Front
from model.untils import read_data,write_data
import datetime
from db_model.peihuo_model import Fabu
from app import db





def fabu_304(username):
    ##读取excel
    datas = read_data(r'F:\autotest\peihuo\file\input_file\fabu.xlsx')

    ##实例化
    process_front=Process_Front()
    process_front.process_login(username)
    process_front.into_shangpinshangjia()

    ##判断商品上架界面数据是否足够,不够就自己录入补足
    shangpinshangjia_count=int(process_front.get_table_count())
    if len(datas)>shangpinshangjia_count:
        value=len(datas)-shangpinshangjia_count
        print('差值是{}'.format(value))
        for i in range(value):
            process_front.into_shiwuruku()
            process_front.ruku_add_detail(stockCode='{}{}'.format(username,datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
            process_front.fresh()

        ##全部申请入库
        process_front.fresh()
        process_front.into_shiwuruku()
        process_front.shiwuruku_apply()

    ##进入商品上架
    process_front.fresh()
    process_front.into_shangpinshangjia()
    result=[]
    for index,data in enumerate(datas):
        ##获得初始数据,表格第一条数据以及数据总数
        start_count=int(process_front.get_table_count())
        print('第{}次，初始数据{}'.format(index,start_count))
        tr=process_front.get_table_trs()[0]
        data_detail={
            'goodsname':tr.find('td',attrs={'name':'goodsName'}).text,
            'stockcode': tr.find('td', attrs={'name': 'stockCode'}).text,
            'goodsid': tr.find('td', attrs={'name': 'goodsId'}).text,
            'factoryname': tr.find('td', attrs={'name': 'factoryName'}).text,
            'weight': tr.find('td', attrs={'name': 'weightAvlb'}).text,
            'factoryid': tr.find('td', attrs={'name': 'factoryId'}).text,
            'material': tr.find('td', attrs={'name': '1'}).text,
            'thickness': tr.find('td', attrs={'name': '2'}).text,
            'standard_width': tr.find('td', attrs={'name': '3'}).text,
            'format': tr.find('td', attrs={'name': '4'}).text,
            'width': tr.find('td', attrs={'name': '5'}).text,
            'edge': tr.find('td', attrs={'name': '6'}).text,
            'level': tr.find('td', attrs={'name': '7'}).text,
            'standard_thickness': tr.find('td', attrs={'name': '8'}).text,
            'warehouse': tr.find('td', attrs={'name': 'warehouseName'}).text,
            'stocktype': tr.find('td', attrs={'name': 'stockType'}).text,
            'issueid': tr.find('td', attrs={'name': 'issueId'}).text,
            'applyid': tr.find('td', attrs={'name': 'applyId'}).text,
            'stockid': tr.find('td', attrs={'name': 'stockId'}).text,
        }
        print(data_detail)
        text=process_front.fabu(premium=data[2],contract=data[0],date_valid=True if data[1]=='1' else False)
        process_front.fresh()
        process_front.into_shangpinshangjia()
        end_count=int(process_front.get_table_count())
        print('第{}次，结束数据{}'.format(index, end_count))


        if start_count-end_count==1:
            ##发布成功
            fabu=Fabu(
                username=username,
                goodsid=data_detail.get('goodsname'),
                stockCode=data_detail.get('stockcode'),
                factoryname=data_detail.get('factoryname'),
                weight=data_detail.get('weight'),
                material=data_detail.get('material'),
                standard_thickness=data_detail.get('standard_thickness'),
                standard_width=data_detail.get('standard_width'),
                format=data_detail.get('format'),
                width=data_detail.get('width'),
                edge=data_detail.get('edge'),
                level=data_detail.get('level'),
                thickness=data_detail.get('thickness'),
                warehouse=data_detail.get('warehouse'),
                applyid=data_detail.get('applyid'),
                stockid=data_detail.get('stockid'),
                status=0,
                contract=data[0],
                invalidtime=datetime.datetime.today().strftime('%Y-%m-%d') if data[1]=='1' else '',
                premium=str(int(float(data[2])*1000)),
            )
            ##加入数据库
            db.session.add(fabu)
            db.session.commit()
            ##excel写入内容
            result_one=[index+1,data[0],data[1],data[2],'发布成功',text]
            result.append(result_one)

        else:
            ##发布失败
            fabu = Fabu(
                username=username,
                goodsid=data_detail.get('goodsname'),
                stockCode=data_detail.get('stockcode'),
                factoryname=data_detail.get('factoryname'),
                weight=data_detail.get('weight'),
                material=data_detail.get('material'),
                standard_thickness=data_detail.get('standard_thickness'),
                standard_width=data_detail.get('standard_width'),
                format=data_detail.get('format'),
                width=data_detail.get('width'),
                edge=data_detail.get('edge'),
                level=data_detail.get('level'),
                thickness=data_detail.get('thickness'),
                warehouse=data_detail.get('warehouse'),
                applyid=data_detail.get('applyid'),
                stockid=data_detail.get('stockid'),
                status=1,
                contract=data[0],
                invalidtime=datetime.datetime.today().strftime('%Y-%m-%d') if data[1]=='1' else '',
                premium=data[2],
            )
            ##加入数据库
            db.session.add(fabu)
            db.session.commit()
            ##excel写入内容
            result_one = [index+1, data[0],data[1],data[2],'发布失败', text]
            result.append(result_one)
    ##关闭网页，将结果写入excel
    process_front.close()
    now=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    write_data(r'F:\autotest\peihuo\file\result_file\fabu\{}.xlsx'.format(now),result,('编号','合约名称','日期是否有效','升贴水','结果','提示信息'))







if __name__ == '__main__':
    fabu_304('zwh_e836')


