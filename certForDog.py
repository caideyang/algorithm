#encoding:utf-8
import xlrd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time,os


class CertForDog:
    """
    接受excel文件，处理生成证书；
    _excel :狗狗信息excel文件全路径
    _pic_path:生成的证书路径
    font:字体
    ggrandpa :曾祖父信息
    ggrandma :曾祖母信息
    
    """

    def __init__(self,excel,pic_path):
        self._excel = excel
        self._pic_path = pic_path
        self.font = {
            "namefont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 30), #姓名
            "breedfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 28), #品种
            "colorfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 30), #颜色
            "sexfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 30), #性别
            "birthfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 28), #出生日期
            "ownerfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 30), #犬主
            "breaderfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 28), #繁殖者
            "codenumfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 28), #芯片号码
            "parentsfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 28), #父母
            "grandparentsfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 22), #祖父母
            "ggrandparentsfont":ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 18), #曾祖父母
        }
        self.ggandpa  =  []
        self.ggpandma =  []
    def getExcel(self):
        return self._excel
    #获取狗狗信息列表,index为excel中的sheet索引。
    def getDogInfo(self,index):
        dogs_info = []
        excel = xlrd.open_workbook(self._excel)
        sheet0 = excel.sheet_by_index(index)
        nrows = sheet0.nrows
        for dog in range (1,nrows):
            dog_info = sheet0.row_values(dog)
            dogs_info.append(dog_info)
        return dogs_info
    #    
    def setGrandpa(self,*args):
        self.ggandpa = args
        
    def setGrandma(self,*args):
        self.ggpandma = args
        
    def crateDir(self):
        if os.path.exists(self._pic_path):
            print("需要创建的路径 【%s】 已经存在，生成的照片将存放到该路径！" % self._pic_path)
        else:
            os.mkdir(self._pic_path)
            print("路径 【%s】 创建成功，生成的照片将存放到该路径！" % self._pic_path)
    #创建血统证书
    def createCert(self,template_path,dogs_info):
        for dog_info in dogs_info:
            image_file = template_path + '\\' + dog_info[-1] +".jpg"  #获取模板文件
            img = Image.open(image_file)
            #新建一个画板
            draw = ImageDraw.Draw(img)
            if  dog_info[-1] == "new":

                draw.text((350, 330), dog_info[2], (255, 0, 0), font=self.font["namefont"]) #狗狗名称
                draw.text((350, 415), dog_info[3], (255, 0, 0), font=self.font["breedfont"]) #品种
                draw.text((350, 577), dog_info[4], (255, 0, 0), font=self.font["colorfont"]) #毛色
                draw.text((350, 498), dog_info[5], (255, 0, 0), font=self.font["sexfont"]) #公母
                draw.text((350, 666), dog_info[6], (255, 0, 0), font=self.font["birthfont"]) #出生日期
                draw.text((350, 742), dog_info[7], (255, 0, 0), font=self.font["grandparentsfont"]) #犬主人
                draw.text((350, 819), dog_info[8], (255, 0, 0), font=self.font["breaderfont"]) #繁殖者
                draw.text((350, 985), dog_info[9], (255, 0, 0), font=self.font["codenumfont"]) #芯片号码
                draw.text((350, 909), dog_info[10], (255, 0, 0), font=self.font["codenumfont"]) #犬住址
                draw.text((900, 510), dog_info[11], (255, 0, 0), font=self.font["parentsfont"]) #父亲信息
                draw.text((900, 875), dog_info[12], (255, 0, 0), font=self.font["parentsfont"]) #母亲信息
                draw.text((1190, 430), dog_info[13], (255, 0, 0), font=self.font["grandparentsfont"]) #祖父信息
                draw.text((1190, 608), dog_info[14], (255, 0, 0), font=self.font["grandparentsfont"]) #祖母信息
                draw.text((1190, 795), dog_info[15], (255, 0, 0), font=self.font["grandparentsfont"]) #外祖父信息
                draw.text((1190, 965), dog_info[16], (255, 0, 0), font=self.font["grandparentsfont"]) #外祖母信息
                draw.text((1507, 385), dog_info[17], (255, 0, 0), font=self.font["ggrandparentsfont"]) #曾祖父
                draw.text((1507, 480), dog_info[18], (255, 0, 0), font=self.font["ggrandparentsfont"]) #曾祖母
                draw.text((1507, 560), dog_info[19], (255, 0, 0), font=self.font["ggrandparentsfont"]) #增外祖父
                draw.text((1507, 660), dog_info[20], (255, 0, 0), font=self.font["ggrandparentsfont"]) #增外祖母
                draw.text((1507, 747), dog_info[21], (255, 0, 0), font=self.font["ggrandparentsfont"]) #外曾祖父
                draw.text((1507, 845), dog_info[22], (255, 0, 0), font=self.font["ggrandparentsfont"]) #外曾祖母
                draw.text((1507, 930), dog_info[23], (255, 0, 0), font=self.font["ggrandparentsfont"]) #外曾外祖父
                draw.text((1507, 1025), dog_info[24], (255, 0, 0), font=self.font["ggrandparentsfont"]) #外曾外祖母
                draw.text((278, 136), dog_info[9][-9:], (255, 0, 0), font=self.font["ggrandparentsfont"]) #证书编号

            else:
                draw.text((350, 385), dog_info[2], (255, 255, 0), font=self.font["namefont"]) #狗狗名称
                draw.text((350, 470), dog_info[3], (255, 255, 0), font=self.font["breedfont"]) #品种
                draw.text((350, 630), dog_info[4], (255, 255, 0), font=self.font["colorfont"]) #毛色
                draw.text((350, 545), dog_info[5], (255, 255, 0), font=self.font["sexfont"]) #公母
                draw.text((350, 713), dog_info[6], (255, 255, 0), font=self.font["birthfont"]) #出生日期
                draw.text((350, 795), dog_info[7], (255, 255, 0), font=self.font["ownerfont"]) #犬主人
                draw.text((350, 884), dog_info[8], (255, 255, 0), font=self.font["breaderfont"]) #繁殖者
                draw.text((350, 980), dog_info[9], (255, 255, 0), font=self.font["codenumfont"]) #芯片号码
                draw.text((895, 525), dog_info[11], (255, 255, 0), font=self.font["parentsfont"]) #父亲信息
                draw.text((895, 890), dog_info[12], (255, 255, 0), font=self.font["parentsfont"]) #母亲信息
                draw.text((1195, 440), dog_info[13], (255, 255, 0), font=self.font["grandparentsfont"]) #祖父信息
                draw.text((1195, 615), dog_info[14], (255, 255, 0), font=self.font["grandparentsfont"]) #祖母信息
                draw.text((1195, 800), dog_info[15], (255, 255, 0), font=self.font["grandparentsfont"]) #外祖父信息
                draw.text((1195, 975), dog_info[16], (255, 255, 0), font=self.font["grandparentsfont"]) #外祖母信息
                draw.text((1488, 392), dog_info[17], (255, 255, 0), font=self.font["ggrandparentsfont"]) #曾祖父
                draw.text((1488, 488), dog_info[18], (255, 255, 0), font=self.font["ggrandparentsfont"]) #曾祖母
                draw.text((1488, 574), dog_info[19], (255, 255, 0), font=self.font["ggrandparentsfont"]) #增外祖父
                draw.text((1488, 670), dog_info[20], (255, 255, 0), font=self.font["ggrandparentsfont"]) #增外祖母
                draw.text((1488, 759), dog_info[21], (255, 255, 0), font=self.font["ggrandparentsfont"]) #外曾祖父
                draw.text((1488, 851), dog_info[22], (255, 255, 0), font=self.font["ggrandparentsfont"]) #外曾祖母
                draw.text((1488, 938), dog_info[23], (255, 255, 0), font=self.font["ggrandparentsfont"]) #外曾外祖父
                draw.text((1488, 1036), dog_info[24], (255, 255, 0), font=self.font["ggrandparentsfont"]) #外曾外祖母
            
            draw = ImageDraw.Draw(img)
            dog_name =  dog_info[3] +"-"+ dog_info[2] +"-"+ dog_info[0] +"-"+ dog_info[1] +".jpg"
            img.save(self._pic_path+"\\"+dog_name) 
            print("%s 创建完毕" % dog_name)
        

if __name__ == "__main__":
    #创建一个对象，导入狗狗信息D:\cert_dog.xlsx  ，导出位置D:\20180305
    cert = CertForDog('D:\\mydogs\\cert_dog.xlsx','D:\\mydogs\\20180306')
    #创建导出位置
    cert.crateDir()
    #获取狗狗信息，参数0 是获取第一个sheet的值
    dogs_info = cert.getDogInfo(0)
#     print(dogs_info)
    #根据模板，创建证书，模板位置：'D:\template'
    cert.createCert('D:\\mydogs\\template', dogs_info)
    
    
    
    
    
    
    
    
    
    
    
    
    
    