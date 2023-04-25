
from flask import Flask,   render_template,request
import serial
from time import sleep
#from power_supply import * 


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def base():

      ser = serial.Serial("COM6", 115200)
      cmd = "MEASure:VOLTage? " + ("\r")
      ser.write(cmd.encode())
      vol = ser.readline().decode('Ascii')
      print(vol)
      sleep(2)
      #actual current

      cmd = "MEASure:CURRent? " + ("\r")
      ser.write(cmd.encode())
      cur = ser.readline().decode('Ascii')
      print(cur)
      sleep(2)

      return render_template("base.html" , c=vol , d=cur)


 
@app.route('/control', methods=['POST','GET'])
def control ():
    if request.method == 'POST':
        
        ser = serial.Serial("COM6", 115200)
        sleep(2)

        print(ser.is_open)
        #setting voltage
        voltage= request.form.get('voltage')
        cmd = "VOLTage " + str(voltage) + ("\r")
        ser.write(cmd.encode('Ascii'))
        print(voltage)
        sleep(2)
        #setting current
        current= request.form.get('current')
        cmd = "CURRent " + str(current) + ("\r")
        ser.write(cmd.encode('Ascii'))
        print(current)
        sleep(4)

        #actual voltage
        ser = serial.Serial("COM6", 115200)
        cmd = "MEASure:VOLTage? " + ("\r")
        ser.write(cmd.encode())
        vol = ser.readline().decode('Ascii')
        print(vol)
        sleep(4)
      #actual current

        cmd = "MEASure:CURRent? " + ("\r")
        ser.write(cmd.encode())
        cur = ser.readline().decode('Ascii')
        print(cur)
        sleep(4)


      
          
    return render_template("base.html"  , a=voltage , b=current , c=vol , d=cur )
          
    
@app.route('/get_toggled_status') 
def toggled_status():


 ser = serial.Serial("COM6", 115200)


 print(ser.is_open)

 current_status = request.args.get('status')
 if current_status == 'power supply mode on':

    cmd = "OUTPut 0" + ("\r")
    ser.write(cmd.encode())
    
    return 'power supply mode off' 
    
 else :
    cmd = "OUTPut 1" + ("\r")
    ser.write(cmd.encode())
    
    return ('power supply mode on') 
  
     
if __name__=='__main__': 
    app.run(debug=True, host='0.0.0.0', port=5000) 
        