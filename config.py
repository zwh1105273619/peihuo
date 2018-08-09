"""
配置
"""


user_add = 'zwh_e835'

user_shenqingruku_one = 'zwh_e838'


user_fabu = 'zwh_e836'

user_buy_sell = 'zwh_e839'
user_buy_sold = 'zwh_e836'


number = 2

root_dir = r'F:\autotest\peihuo'

excel_login_input=''
excel_add_input=root_dir+r'\file\input_file\rukumingxi.xlsx'
excel_fabu_input=root_dir+r'\file\input_file\fabu.xlsx'


report_every=root_dir+r'\file\everyreport\{}.html'
excel_every=root_dir+r'\file\everyreport\{}.xlsx'


##读取用例路径配置
cases_path={
    'shenqingtihuo':root_dir+r'\test_cases\front\shenqingtihuo',
    'add':root_dir+r'\test_cases\front\add',
    'apply':root_dir+r'\test_cases\front\apply',
    'apply_data':root_dir+r'\test_cases\front\apply_data',
    'fabu':root_dir+r'\test_cases\front\fabu',
    'buy_count':root_dir+r'\test_cases\front\buy_count',
    'buy_data':root_dir+r'\test_cases\front\buy_data',
    'tihuoshenqing_data':root_dir+r'\test_cases\front\tihuoshenqing',
    'tihuoshenqingchaxun_data':root_dir+r'\test_cases\front\tihuoshenqingchaxun',
}



##报告名称配置
report_name={
    'add':'录入明细',
    'add_data':'录入明细数据验证',
    'apply':'申请入库',
    'apply_data':'申请入库数据验证',
    'fabu':'发布上架',
    'fabu_data':'发布数据验证',
    'buy_count':'应邀统计',
    'buy_data':'应邀数据统计',
    'tihuoshenqing_data':'提货申请数据验证',
    'shenqingtihuo':'申请提货',
    'tihuoshenqingchaxun_data':'提货申请查询数据验证',
}


##报告路径配置
report_path={
    report_name.get('add_data'):root_dir+r'\file\report\add',
    report_name.get('add'):root_dir+r'\file\result_file\add',
    report_name.get('apply'):root_dir+r'\file\report\apply',
    report_name.get('apply_data'):root_dir+r'\file\report\apply_data',
    report_name.get('fabu_data'):root_dir+r'\file\report\fabu',
    report_name.get('fabu'):root_dir+r'\file\result_file\fabu',
    report_name.get('buy_count'):root_dir+r'\file\report\buy_count',
    report_name.get('buy_data'):root_dir+r'\file\report\buy_data',
    report_name.get('tihuoshenqing_data'):root_dir+r'\file\report\tihuoshenqing_data',
    report_name.get('shenqingtihuo'):root_dir+r'\file\report\shenqingtihuo',
    report_name.get('tihuoshenqingchaxun_data'):root_dir+r'\file\report\tihuoshenqingchaxun_data',
}



