import wx
import os
import time
from threading import Thread
import youtube_dl
import wx.lib.agw.genericmessagedialog as GMD

class OptQualidy():
    
    def __init__(self, path, id_url, id_qualidy):
        self.path = path
        self.id_url = id_url
        self.id_qualidy = id_qualidy
        
        
    def Qualidade_360p(self):
        
        opcao = {
            'format' : '18',
            '-c': '', 
            '--no-mtime': '',
            'outtmpl' :  f"{self.path}/%(title)s.%(ext)s"
            }
        try:
            youtube_dl.YoutubeDL(opcao).download([self.id_url])
        except:
            er_opcao ={
                '-c': '', 
                '--no-mtime': '',
                'outtmpl': f"{self.path}/%(title)s.%(ext)s"
            }
            youtube_dl.YoutubeDL(er_opcao).download([self.id_url])
        

    def Qualidade_760p(self):
        opcao = {
            'format' : '22',
            'outtmpl' : f"{self.path}/%(title)s.%(ext)s"
            }
        try:
            youtube_dl.YoutubeDL(opcao).download([self.id_url])
        except:
            er_opcao ={
                '-c': '', 
                '--no-mtime': '',
                'outtmpl' : f"{self.path}/%(title)s.%(ext)s"
                }
            youtube_dl.YoutubeDL(er_opcao).download([self.id_url])
            
            

    def Qualidade_1080p(self):
        opcao = {
            'format' : '137',
            '-c': '', 
            '--no-mtime': '',
            'outtmpl' : f"{self.path}/%(title)s.%(ext)s"
            }
        try:
            youtube_dl.YoutubeDL(opcao).download([self.id_url])
        except:
            er_opcao ={
                '-c': '', 
                '--no-mtime': '',
                'outtmpl': str(f"{self.path}/%(title)s.%(ext)s")
            }
            youtube_dl.YoutubeDL(er_opcao).download([self.id_url])
        

    def Audio_mp3(self):
        video_info = youtube_dl.YoutubeDL().extract_info(self.id_url, download=False)
        
        filename = self.path+f"/{video_info['title']}.mp3"
        
        opcao = {
            'format' : 'bestaudio/best',
            'keepvideo' : False,
            'outtmpl' : filename, 
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192',
                }]
            }
        
        with youtube_dl.YoutubeDL(opcao) as ydl:
            ydl.download([video_info['webpage_url']])
    def Executa(self):
        if self.id_qualidy == '0':
            self.Qualidade_360p()
            
        elif self.id_qualidy == '1':
            self.Qualidade_760p()
            
        elif self.id_qualidy == '2':
            self.Qualidade_1080p()
            
        elif self.id_qualidy == '3':
            self.Audio_mp3()

class direction(object):
    
    def __init__(self, url):
        self.url = url
        self.num_ = 0

    def valid_url(self):
        id_url = "https://www.youtube.com/watch?v="
        num  = str(self.url[:32])
        num_list = str(self.url[43:-34])
        
        if str(num) == id_url:
            if str(num_list) == str(r"&list"):
                titulo = "Não baixar Player_list"
                mensagem_error = "Desculpe esse Programa não baixar Player_list do YouTube !" 
                MessagemWind(titulo, mensagem_error).DialodBoxId()
                
            else:
                self.num_ += 1
    
    def run_direction(self):
        
        RunList = []
        
        self.valid_url()
        
        if self.num_ == 1:
            RunList.append(self.url)
        else:
            RunList.append("exurl")
            
        return RunList

class MessagemWind(object):
    def __init__(self, title_, mensagem_):
        self.title_ = title_
        self.mensagem_ = mensagem_
    
    def DialodBoxId(self):
        dlg = GMD.GenericMessageDialog(None, self.mensagem_, self.title_, agwStyle=wx.ICON_INFORMATION | wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def Ok_Messagem(self):
         wx.MessageBox(self.mensagem_, self.title_, wx.OK | wx.ICON_INFORMATION)
        
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        self.num = 0
        kwds["style"] = kwds.get("style", 0) | wx.MINIMIZE_BOX | wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((420, 550))
        self.SetTitle("DownTubeV2.0")

        # criando menu 
        self.menubar = wx.MenuBar()
        self.finame = wx.Menu()

        # meu opcao sair do prorgrama
        self.finame.Append(wx.ID_ABOUT, '&Sair', 'Sair do progrma')
        self.menubar.Append(self.finame, '&File')

        self.menubar.Bind(wx.EVT_MENU, self.Menu_Sair)

        self.SetMenuBar(self.menubar)


        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        self.text1 = wx.StaticText(self.panel_1, label='URL :', pos=(5,10))
        
        
        self.text2 = wx.StaticText(self.panel_1, label='Selecione Qualidade', pos=(3,50))
        self.text3 = wx.StaticText(self.panel_1, label='Salve Vídeo', pos=(3, 159))
        self.text4 = wx.StaticText(self.panel_1, label='Executa: ', pos=(3,305))
        self.text5 = wx.StaticText(self.panel_1, label="Processo ", pos=(3,450))
        # Adiconar URL
        self.adurl = wx.TextCtrl(self.panel_1, wx.ID_ANY, '', pos=(38,5), size=(353,30))

        # listas de opcao 
        self.ListOp = wx.CheckListBox(self.panel_1, id=wx.ID_ANY, pos=(3,79), size=(389,96), choices=['360p', '720p', '1080p', 'Audio MP3'], style=0)


        # Criando Botoes de execucao
        sizer_1 = wx.BoxSizer(wx.VERTICAL)


        # botoes listas de opcao
        sizer_1.Add(self.ListOp, 0, wx.ALL | wx.EXPAND, 5)
        
        # botoes adionar URL
        sizer_1.Add(self.adurl, 0, wx.ALL | wx.EXPAND, 5)

        # pasta atual
        self.pasta_ = wx.TextCtrl(self.panel_1, pos=(3,189), size=(390,25))
        self.pasta_.AppendText(os.getcwd()) # diretorio onde programa ser encontra

        # botoes escolher pasta para salvar 
        self.btn_pasta = wx.Button(self.panel_1, label='Pasta', pos=(150,229))
        self.btn_pasta.Bind(wx.EVT_BUTTON, self.Pasta_ES)

        sizer_1.Add(self.pasta_, 0, wx.ALL | wx.EXPAND, 5)
        sizer_1.Add(self.btn_pasta, 0, wx.ALL | wx.EXPAND | wx.RIGHT , 5)

        # botoes para download

        self.btn_down = wx.Button(self.panel_1, label='Download', pos=(60, 300))

        sizer_1.Add(self.btn_down, 0, wx.ALL | wx.EXPAND, 5)

        # criando barra de processo
        self.gauge_1 = wx.Gauge(self.panel_1,  pos=(3,460),size=(390,20))

        sizer_1.Add(self.gauge_1, 0, wx.EXPAND | wx.TOP, 8)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 8)

        sizer_2.Add(self.btn_down, 0, wx.RIGHT, 8)

        self.Layout()
    
        self.Bind(wx.EVT_TIMER, self.TimerHandler) # incindo barra de processo
        self.Bind(wx.EVT_BUTTON, self.Upload, self.btn_down) # funcao do  butao 
        self.timer = wx.Timer(self) # tempo e incior ou para da barra de processo
    
    # fechar programa
    def Menu_Sair(self, event):
        # mensagem de confimação
        exit_ = wx.MessageDialog(None, 'Você desejar sair ?', 'Pergunta', wx.YES_NO)
        
        if exit_.ShowModal() == wx.ID_YES:
            self.Close(True)
        
        exit_.Destroy()

    def Pasta_ES(self, event):
        # caminho da onde o arquivo vai ser baixando
        self.dlg_ = wx.DirDialog(self,message='Local Pasta')
        if self.dlg_.ShowModal() == wx.ID_OK:
            self.dirname = self.dlg_.GetPath()
            
            # limando valiavel
            self.pasta_.Clear()
            
            # adicionar novo caminho
            self.pasta_.AppendText(self.dirname)

        self.dlg_.Destroy()
    def Upload(self, event):
        self.btn_down.Enable(False)
        if not self.timer.IsRunning():
            # validado url do youtube
            listsf = str(self.ListOp.GetCheckedItems())
            strformat = listsf.replace(',', '').replace('(','')
            
            # format listas de opcoes
            lItems = strformat.replace(')', '').split()
            value_opts = direction(self.adurl.Value).run_direction()
            link = value_opts[0]
        
            if link == "exurl":
                MessagemWind("Erro url", "url em valida !").DialodBoxId()
                
            else:
                if len(lItems) == 1:
                    
                    self.text5.SetLabel("Fazendo Download, Aguarde...")
                    self.timer.Start(100)
                    
                    i = Thread(target=self.rundown, args=(link, str(lItems[0])))
                    i.start()

                elif len(lItems) > 1:
                    tlt = "Error Qualidade"
                    msg = "Selecione apernas uma qualidade !"
                    
                    MessagemWind(tlt, msg).DialodBoxId()
                
                elif len(lItems) == 0:
                    tlt = "Sem escolha"
                    msg = "Selecioner umas das qualidades !"
                    MessagemWind(tlt, msg).DialodBoxId()
                    
    def rundown(self, lk, qt):
        # fazendo download do video ou audio
        OptQualidy(self.pasta_.Value, lk, qt).Executa()
        
        # finalizando download da barra de processo
        self.Stop()
        
        tlt = "Sem escolha"
        msg = "Selecioner umas das qualidades !"
        MessagemWind(tlt, msg).DialodBoxId()
        
    def Stop(self):
        # stop na barra de processo
        if self.timer.IsRunning():
            self.text5.SetLabel(f"Download feito com sucesso em {self.pasta_.Value}")
            self.timer.Stop()
            self.gauge_1.SetValue(0)
        
    def TimerHandler(self, event):
        self.gauge_1.Pulse()

# exucutado todo programa 
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# chamando class de execucao 
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
