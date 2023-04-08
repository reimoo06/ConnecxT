import time
import kivy



from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
import http.client as httplib
from kivy.lang import Builder
from kivy.uix.label import Label
import socket
from datetime import datetime

now = datetime.now()


hostname=socket.gethostname() #<----- local bisa aja bikin rusak
IPAddr=socket.gethostbyname(hostname)


Builder.load_string("""
<MySec>:
    orientation: 'vertical'
    Label:
        id: kv_sec
        text: root.seconds_string
        text_size: self.size
        halign: 'center'
        valign: 'middle'
        font_name: 'DejaVuSans'
""")
amountFT = "Loading"
amounttry = 0 

# function to check internet connectivity

def checkInternetHttplib(url="www.google.com",

                         timeout=3):

    connection = httplib.HTTPConnection(url,timeout=timeout)
    
    try:

        # only header requested for fast operation

        connection.request("HEAD", "/")

        connection.close()  # connection closed



        return True

    except Exception as exep:

        print(exep)

        return False






class MySec(BoxLayout):
    
    seconds_string = StringProperty('')


class Test(App):
    def build(self):

      
        Clock.schedule_interval(lambda dt: self.update_time(), 0.001)
        return MySec()
        


    def update_time(self):
        global amounttry
        global amounttryerr
        is_online = checkInternetHttplib("www.google.com", 3)
        is_onlast = "Offline"
        
        if is_online == True:
            is_onlast="Online"
        elif is_online == False:
            is_onlast="Offline"
        else:
            is_onlast="Error ocurred, try again later."
            
        if is_online == False:
            amountFT = "Offline 0"
            
        elif is_online == True:
            amounttry += 1
            amountFT = amounttry
        
        self.root.seconds_string = str("Connection Test by reimoo06 \n\n Your internet is currently: ")+ str(is_onlast) + "\nYour current ip address: " + str(IPAddr) + " ("+(hostname) +")" + "\n\n Targeted test page: www.google.com / 8.8.8.8 \n Alternative targeted test page: 1dot1dot1dot1.cloudflare-dns.com / 1.1.1.1" + "\n\n Time page visited/reloaded: " +str(amountFT) + " time(s)" + "\n Time alt page visited/reloaded: " + str(amountFT) + " time(s)"
Test().run()
