import json
from random import randint
from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
import serial
from .models import *
ser = serial.Serial('COM3', '9600')
class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        await self.accept()  
        for i in range(1000):
            if ser.readable():
                coor = ser.readline()
                coordinate = int(coor.decode())
                await self.send(json.dumps({'message': coordinate}))               
            await sleep(0.01)
            
        
        
        # while True:
        #     for i in range(10):
        #         coordinate = i
        #         await self.send(json.dumps({'message': coordinate}))
        #         await sleep(1)


    async def disconnect(self, close_code):
        await ser.close()
        await self.close(self)

"""
class LoadBooks(WebsocketConsumer):
    def connect(self):
        self.accept()

        booklist = [None]*5

        for i in len(booklist):
            barcode = request.GET.get('barcode')
            if barcode:
                booklist[i] = BookList.objects.filter(barcode__icontains = barcode)
                self.send(json.dumps(booklist[i]))
"""