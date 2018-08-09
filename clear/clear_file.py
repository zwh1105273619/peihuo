"""定时清理report报告和result_file"""
from config import root_dir,report_path
import datetime

import os,shutil




def clear(name):

    ##声明可以清理的文件
    path={
        'everyreport':root_dir+r'\file\everyreport',
        'report':root_dir+r'\file\report',
        'result_file':root_dir+r'\file\result_file'
    }
    file_path=path.get(name,'')
    print(file_path)

    if file_path:

        ##如果清理的是查看全部报告的文件，就将文件复制到对应文档下
        if name=='everyreport':
            for file in os.listdir(file_path):
                ##将文件名称和后缀分割
                text=os.path.splitext(file)
                now=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                ##引入当前时间戳命名新的文件名
                fp_name=text[0]+now+text[1]

                ##移动文件
                fp=os.path.join(file_path,file)
                new_fp=os.path.join(report_path.get(text[0]),fp_name)
                shutil.move(fp,new_fp)
        else:
            for dir in os.listdir(file_path):
                for file in os.listdir(file_path+'\\'+dir):
                    os.remove(file_path+'\\'+dir+'\\'+file)






if __name__ == '__main__':
    clear('everyreport')
    # clear('report')
    # clear('result_file')


