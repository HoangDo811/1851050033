from webapp import db
from sqlalchemy import Column, Integer, String,DATETIME, Float, ForeignKey,BigInteger,Boolean,Unicode,UnicodeText,Enum as EnumSQL
import uuid
from sqlalchemy_utils import UUIDType, ChoiceType, IPAddressType,PasswordType,Password
from datetime import datetime
from flask_login import UserMixin
from enum import Enum
from sqlalchemy.orm import relationship
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(UUIDType(binary=False),primary_key=True,default=uuid.uuid4())
    name = Column(String,nullable=False)

    def __str__(self):
        return self.name

class Role(Enum):
    admin = 2
    giaovien = 1


class User(BaseModel, UserMixin):
    __tablename__ = "User"

    username = Column(String(50), nullable=False)
    password = Column(String, nullable=False)
    joindate = Column(DATETIME,nullable=False,default=datetime.now())
    role = Column(EnumSQL(Role),nullable=False,default=Role.giaovien)
    email = Column(String, nullable=False)
    phonenumber = Column(String(20), nullable=True)
    active = Column(Boolean,nullable=False,default=True)

class Khoi(BaseModel):
    __tablename__ = "khoi"
    so_luong_lop = Column(Integer)
    lop = relationship('Lop', backref='khois', lazy=True)


class Lop(BaseModel):
    __tablename__ = "lop"

    si_so = Column(Integer)
    id_khoi = Column(UUIDType, ForeignKey(Khoi.id), nullable=False)
    id_hs = relationship('HocSinh', backref='lops', lazy=True)


class HocSinh(BaseModel):
    __tablename__ = "hosohocsinh"

    gioi_tinh = Column(String(10), nullable=False)
    ngay_sinh = Column(DATETIME, nullable=False)
    dia_chi = Column(String(255), nullable=False)
    email = Column(String(100))
    lop = Column(UUIDType, ForeignKey(Lop.id), nullable=False)
    diem_mh = relationship('DiemMonHoc', backref='hosohocsinhs', lazy=True)


class MonHoc(BaseModel):
    __tablename__ = "monhoc"

    diem_mh = relationship('DiemMonHoc', backref='monhocs', lazy=True)


class DiemMonHoc(BaseModel):
    __tablename__ = "diemmonhoc"
    name = None
    id_hs = Column(UUIDType, ForeignKey(HocSinh.id), primary_key=True, nullable=True)
    id_mh = Column(UUIDType, ForeignKey(MonHoc.id), primary_key=True, nullable=True)
    hoc_ky = Column(String(20), primary_key=True, nullable=True)
    nam_hoc = Column(String(20), primary_key=True, nullable=True)
    loai_diem = Column(String(20), nullable=True)
    diem = Column(Float)

if __name__=='__main__':
    db.drop_all()
    db.create_all()





