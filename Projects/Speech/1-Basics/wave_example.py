import  wave



obj=wave.open('myname.wav', 'rb')

print("Numbe of channels,",obj.getnchannels())
print("Sample width,",obj.getsampwidth())
print("frame rate,",obj.getframerate())
print("Number of frames,",obj.getnframes())
print("parameters",obj.getparams())

t_audio = obj.getnframes()/obj.getframerate();
print(t_audio)

obj_new = wave.open('myname_new.wav', 'wb')
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)
