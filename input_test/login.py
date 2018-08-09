from model.process_front import Process_Front
from model.untils import *



def login():
    datas=read_data(r'./file/input_file/user.xlsx')

    process_front=Process_Front()
    process_front.process_login()