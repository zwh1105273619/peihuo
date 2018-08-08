

from app import db


class HistoryData(db.Model):
    """录入数据模型类"""

    __tablename__='T_Hisstory_Data'


    id=db.Column(db.Integer,primary_key=True)
    goodsid=db.Column(db.String(50))
    username=db.Column(db.String(50))
    stockCode=db.Column(db.String(50))
    factoryName=db.Column(db.String(50))
    weight=db.Column(db.String(50))
    material=db.Column(db.String(50))
    standard_thickness=db.Column(db.String(50))
    standard_width=db.Column(db.String(50))
    format=db.Column(db.String(50))
    width=db.Column(db.String(50))
    edge=db.Column(db.String(50))
    level=db.Column(db.String(50))
    thickness=db.Column(db.String(50))
    warehouse=db.Column(db.String(50))
    remark=db.Column(db.String(100))
    status=db.Column(db.Integer)  ##0为录入成功，1为录入失败

    def __init__(self,username,goodsid,stockCode,factoryName,weight,remark,material,standard_thickness,
                 standard_width,format,width,edge,level,thickness,warehouse,status):

        self.username=username
        self.goodsid=goodsid
        self.stockCode=stockCode
        self.factoryName=factoryName
        self.weight=weight
        self.remark=remark
        self.material=material
        self.standard_thickness=standard_thickness
        self.standard_width=standard_width
        self.format=format
        self.width=width
        self.edge=edge
        self.level=level
        self.thickness=thickness
        self.warehouse=warehouse
        self.status=status


class Fabu(db.Model):
    """发布模型"""
    __tablename__ = 'T_Fabu_Data'

    id = db.Column(db.Integer, primary_key=True)
    goodsid = db.Column(db.String(50))

    premium=db.Column(db.String(50))
    invalidTime=db.Column(db.String(50))
    issueTime=db.Column(db.String(50))
    cancelTime=db.Column(db.String(50))



    username = db.Column(db.String(50))
    stockCode = db.Column(db.String(50))
    factoryname = db.Column(db.String(50))
    weight = db.Column(db.String(50))
    material = db.Column(db.String(50))
    standard_thickness = db.Column(db.String(50))
    standard_width = db.Column(db.String(50))
    format = db.Column(db.String(50))
    width = db.Column(db.String(50))
    edge = db.Column(db.String(50))
    level = db.Column(db.String(50))
    thickness = db.Column(db.String(50))
    warehouse = db.Column(db.String(50))
    applyid=db.Column(db.String(50))
    stockid=db.column(db.String(50))
    contract=db.Column(db.String(50))
    status=db.Column(db.Integer)


    def __init__(self, username, goodsid, stockCode, factoryname, weight, material, standard_thickness,
                 standard_width, format, width, edge, level, thickness, warehouse, applyid,stockid,status,premium,invalidtime,contract):
        self.username = username
        self.goodsid = goodsid
        self.stockCode = stockCode
        self.factoryname = factoryname
        self.weight = weight
        self.material = material
        self.standard_thickness = standard_thickness
        self.standard_width = standard_width
        self.format = format
        self.width = width
        self.edge = edge
        self.level = level
        self.thickness = thickness
        self.warehouse = warehouse
        self.applyid=applyid
        self.stockid=stockid
        self.status=status

        self.premium=premium
        self.invalidTime=invalidtime
        self.contract=contract





