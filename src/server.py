from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Gersat(BaseModel):
    nGertec: str
    nSefaz: str
    vLinux: str
    super_hash: bool
    led_on: bool
    led_off: bool
    token: bool
    nvram: bool
    usb: bool
    msp: bool

g1 = Gersat(
    nGertec=str(random.randrange(start=1000000000000000, stop=9999999999999999)),
    nSefaz=str(random.randrange(start=100000000000, stop=999999999999)),
    vLinux="5.4.0",
    super_hash=True,
    led_on=True,
    led_off=True,
    token=True,
    nvram=True,
    usb=True,
    msp=True
    )

g2 = Gersat(
    nGertec=str(random.randrange(start=1000000000000000, stop=9999999999999999)),
    nSefaz=str(random.randrange(start=100000000000, stop=999999999999)),
    vLinux="5.4.0",
    super_hash=True,
    led_on=False,
    led_off=True,
    token=True,
    nvram=True,
    usb=False,
    msp=True
    )

g3 = Gersat(
    nGertec=str(random.randrange(start=1000000000000000, stop=9999999999999999)),
    nSefaz=str(random.randrange(start=100000000000, stop=999999999999)),
    vLinux="5.4.0",
    super_hash=True,
    led_on=False,
    led_off=True,
    token=False,
    nvram=True,
    usb=True,
    msp=True
    )

# g4 = Gersat(
#     nGertec=str(random.randrange(start=1000000000000000, stop=9999999999999999)),
#     nSefaz=str(random.randrange(start=100000000000, stop=999999999999)),
#     vLinux="5.4.0",
#     super_hash=True,
#     led_on=False,
#     led_off=True,
#     token=False,
#     nvram=True,
#     usb=True,
#     msp=True
#     )

devices: List[Gersat] = [g1, g2, g3]
@app.get('/teste')
def testes():
    return devices