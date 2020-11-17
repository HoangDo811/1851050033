from flask_admin.contrib.sqla import ModelView

from webapp import  admin,models,db

class _view(ModelView):
    form_create_rules = [
       'so_luong_lop',"name"
    ]

admin.add_view(ModelView(models.HocSinh,db.session))
admin.add_view(ModelView(models.User,db.session))
admin.add_view(ModelView(models.Lop,db.session))
admin.add_view(ModelView(models.MonHoc,db.session))
admin.add_view(ModelView(models.DiemMonHoc,db.session))
admin.add_view(_view(models.Khoi,db.session))