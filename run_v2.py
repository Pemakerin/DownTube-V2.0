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
        video_info = youtube_dl.YoutubeDL().extract_info(url = self.id_url, download=False)
        
        filename = self.path+"/"+f"{video_info['title']}.mp3"
        
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
        
        with youtube_dl.YoutubeDL(opcoes) as ydl:
            ydl.download([video_info['webpage_url']])

        subprocess.call('open', filename)
    
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
        self.SetTitle("DownTube V2.0")
        """self.ico = wx.Icon("iconyou.png", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.ico)"""
        # criando menu 
        self.menubar = wx.MenuBar()
        self.finame = wx.Menu()

        # meu opcao sair do prorgrama
        self.finame.Append(wx.ID_ABOUT, '&Sair', 'Sair do progrma')
        self.menubar.Append(self.finame, '&Opção')

        self.menubar.Bind(wx.EVT_MENU, self.Menu_Sair)

        self.SetMenuBar(self.menubar)


        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        self.text1 = wx.StaticText(self.panel_1, label='URL :', pos=(5,10))
        
        
        self.text2 = wx.StaticText(self.panel_1, label='Selecione Qualidade', pos=(3,50))
        self.text3 = wx.StaticText(self.panel_1, label='Salve Vídeo', pos=(3, 159))
        self.text4 = wx.StaticText(self.panel_1, label='Executa: ', pos=(3,305))
        self.text5 = wx.StaticText(self.panel_1, label="Processo ", pos=(3,450))
        # Adiconar URL
        self.adurl = wx.TextCtrl(self.panel_1, wx.ID_ANY, "Adicioner a URL", pos=(38,5), size=(353,30))

        # listas de opcao 
        self.ListOp = wx.CheckListBox(self.panel_1, id=wx.ID_ANY, pos=(3,79), size=(389,96), choices=['360p', '720p', '1080p', 'MP3 Player'], style=0)


        # Criando Botoes de execucao
        sizer_1 = wx.BoxSizer(wx.VERTICAL)


        # botoes listas de opcao
        sizer_1.Add(self.ListOp, 0, wx.ALL | wx.EXPAND, 5)
        
        # botoes adionar URL
        sizer_1.Add(self.adurl, 0, wx.ALL | wx.EXPAND, 5)

        # pasta atual
        self.pasta_ = wx.TextCtrl(self.panel_1, pos=(3,189), size=(390,25))
        self.pasta_.AppendText(os.getcwd())

        # botoes escolher pasta para salvar 
        self.btn_pasta = wx.Button(self.panel_1, label='Pasta', pos=(150,229))
        self.btn_pasta.Bind(wx.EVT_BUTTON, self.Pasta_ES)

        sizer_1.Add(self.pasta_, 0, wx.ALL | wx.EXPAND, 5)
        sizer_1.Add(self.btn_pasta, 0, wx.ALL | wx.EXPAND | wx.RIGHT , 5)

        # botoes para download

        self.btn_down = wx.Button(self.panel_1, label='Download', pos=(60, 300))

        sizer_1.Add(self.btn_down, 0, wx.ALL | wx.EXPAND, 5)

        # criando bar de processo
        self.gauge_1 = wx.Gauge(self.panel_1,  pos=(3,460),size=(390,20))

        sizer_1.Add(self.gauge_1, 0, wx.EXPAND | wx.TOP, 8)

        
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 8)

        sizer_2.Add(self.btn_down, 0, wx.RIGHT, 8)

        self.Layout()
    
        self.Bind(wx.EVT_TIMER, self.TimerHandler)
        self.Bind(wx.EVT_BUTTON, self.Upload, self.btn_down)
        self.timer = wx.Timer(self)
    
    def Menu_Sair(self, event):
        exit_ = wx.MessageDialog(None, 'Você desejar sair ?', 'Pergunta', wx.YES_NO)
        
        if exit_.ShowModal() == wx.ID_YES:
            self.Close(True)
        
        exit_.Destroy()

    def Pasta_ES(self, event):
        self.dlg_ = wx.DirDialog(self,message='Local Pasta')
        if self.dlg_.ShowModal() == wx.ID_OK:
            self.dirname = self.dlg_.GetPath()

            self.pasta_.Clear()
            self.pasta_.AppendText(self.dirname)

        self.dlg_.Destroy()
    def Upload(self, event):
        if not self.timer.IsRunning():
            
            i = Thread(target=self.ytime)
            i.daemon = True
            i.start()
            
            self.text5.SetLabel("Fazendo Download, Aguarde...")
            self.timer.Start(100)
            
            
    def ytime(self):
        listsf = str(self.ListOp.GetCheckedItems())
        strformat = listsf.replace(',', '').replace('(','')
        
        lItems = strformat.replace(')', '').split()
        value_opts = direction(self.adurl.Value).run_direction()
        link = value_opts[0]
        
        if link == "exurl":
            MessagemWind("Erro url", "url em valida !").DialodBoxId()
            pass
        else:
            if len(lItems) == 1:
                OptQualidy(self.pasta_.Value, link, str(lItems[0])).Executa()
            else:
                tlt = "Error Qualidade"
                msg = "Selecione apernas uma qualidade !"
                MessagemWind(tlt, msg).DialodBoxId()
        
        def Stop():
            if self.timer.IsRunning():
                self.text5.SetLabel("Processo")
                self.timer.Stop()
                self.gauge_1.SetValue(0)
                
                titulo_m = "Sucesso"
                mensagem_m =  "Download feito com sucesso"
                MessagemWind(titulo_m, mensagem_m).Ok_Messagem()
                
        Stop()
        
    def TimerHandler(self, event):
        self.gauge_1.Pulse()
        
# executado frame wxClass
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
    
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
