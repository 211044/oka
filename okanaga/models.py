from django.db import models


class Employee(models.Model):
    empid = models.CharField(max_length=8, unique=True, primary_key=True)
    empfname = models.CharField(max_length=64)
    emplname = models.CharField(max_length=64)
    emppasswd = models.CharField(max_length=256)
    emprole = models.IntegerField()  # 受付: 0, 医師: 1


class Tabyouin(models.Model):
    tabyouinid = models.CharField(primary_key=True, max_length=8, verbose_name="他病院ID")
    tabyouinmei = models.CharField(max_length=64, verbose_name="他病院名")
    tabyouinaddress = models.CharField(max_length=64, verbose_name="他病院住所")
    tabyouintel = models.CharField(max_length=20, verbose_name="他病院電話番号")
    tabyouinshihonkin = models.IntegerField(verbose_name="資本金")
    kyukyu = models.IntegerField(verbose_name="救急フラグ", help_text="救急対応の時は1、そうでない時は1以外")


class Patient(models.Model):
    patid = models.CharField(max_length=8, primary_key=True, verbose_name='患者 ID')
    patfname = models.CharField(max_length=64, verbose_name='患者名')
    patlname = models.CharField(max_length=64, verbose_name='患者姓')
    hokenmei = models.CharField(max_length=64, verbose_name='保険証名記号番号')
    hokenexp = models.DateField(verbose_name='有効期限')


class Medicine(models.Model):
    medicineid = models.CharField(max_length=8, primary_key=True, verbose_name='薬剤 ID')
    medicinename = models.CharField(max_length=64, verbose_name='薬剤名')
    unit = models.CharField(max_length=8, verbose_name='単位')

    def __str__(self):
        return self.medicinename


class MedicineAdministration(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='患者')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='薬剤')
    quantity = models.IntegerField(verbose_name='数量')
    medicine_name = models.CharField(max_length=100, verbose_name='薬剤名', default='unknown')


class Supplier(models.Model):
    shiireid = models.CharField(primary_key=True, max_length=8, verbose_name="仕入れ先 ID")
    shiiremei = models.CharField(max_length=64, verbose_name="仕入れ先名")
    shiireaddress = models.CharField(max_length=64, verbose_name="仕入れ先住所")
    shiiretel = models.CharField(max_length=15, verbose_name="仕入れ先電話番号")
    shihonkin = models.IntegerField(verbose_name="資本金")
    nouki = models.IntegerField(verbose_name="納期", help_text="発注して届く日数")

    def __str__(self):
        return self.shiiremei
