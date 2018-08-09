from model.process_front import Process_Front
from model.untils import read_data,write_data
import datetime
from db_model.peihuo_model import HistoryData
from app import db
from config import excel_add_input,excel_every,report_name



def input_detail_304(username):
    ##读取excel
    # datas=read_data(r'F:\autotest\peihuo\file\input_file\rukumingxi.xlsx')
    datas = read_data(excel_add_input)

    ##实例化，登录并进入相应界面
    process_front = Process_Front()
    process_front.process_login(username)
    process_front.into_shiwuruku()
    result=[]
    for index,data in enumerate(datas):
        ##获得初始数据
        start_data=process_front.get_shiwuruku_count()


        ##录入
        remind_text=process_front.ruku_add_detail(*data)
        process_front.fresh()
        process_front.into_shiwuruku()

        ##获得录入后的数据
        end_data=process_front.get_shiwuruku_count()

        ##如果数字+1，录入成功，否则失败
        if start_data.get('num')+1==end_data.get('num'):
            print(index+1,data[0],'录入成功',remind_text)
            historydata=HistoryData(username,'冷轧304卷',*data,0)
            db.session.add(historydata)
            db.session.commit()
            one_result=(index+1,data[0],'录入成功',remind_text)
        else:
            print(index+1,data[0], '录入失败', remind_text)
            historydata = HistoryData(username,'冷轧304卷', *data, 1)
            db.session.add(historydata)
            db.session.commit()
            one_result = (index+1,data[0], '录入失败', remind_text)
        result.append(one_result)

    ##以当前时间戳生成文件名，写入excel
    process_front.close()
    write_data(excel_every.format(report_name.get('add')),result,('编号','钢卷号','结果','提示信息'))

if __name__ == '__main__':
    input_detail_304('zwh_e835')