#!/usr/bin/env python3

##    MIT License
##
##    Copyright (c) 2025 and later AJ_Lethal
##
##    Permission is hereby granted, free of charge, to any person obtaining a copy
##    of this software and associated documentation files (the "Software"), to deal
##    in the Software without restriction, including without limitation the rights
##    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##    copies of the Software, and to permit persons to whom the Software is
##    furnished to do so, subject to the following conditions:
##
##    The above copyright notice and this permission notice shall be included in all
##    copies or substantial portions of the Software.
##
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##    SOFTWARE.

import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import IntVar
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from idlelib.tooltip import Hovertip
import colorsys
import io
import struct
import copy
import csv
import random
import ast

sIconData = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACN0lEQVQ4y33SsW9bZRQF8N/3vef3Ejt+thNHsUtNmgqoEKFIFFUIpAJDEWKFlalLdwYGxJ/QoQMSYmQqf0E3BkDMZUEMKCRSghUEIS6J4zhxHoNNCEN7pbsc3XvuuUeHJ1fAm/gB2xf6Cyz/O5Q8hWBF4mu33PCBwjsK1xT+9oo9Y3yLMj7l+mXPWXUTBTI8g9dVzHkDC/Akgpt5Pf+4c7kT5f+nDa0gW8wSfIUX0wsXV/A+3sV7tz+6XV+/tR4e/PTAps3pVEnnoKPX6729Ndkqd3d355OZD28J7lv0mhesOdW989mdpHulG5qjpsFfA4PjgfZe29WNq6ppNdRqtbCzs1NP8argU5e0dF2RGhuazC/MJ0mSuH7jupXlFQ8/fyg9SiVh6nueT3+L+ETTksKa3/X96GdHTvobfWdnZ2KMmu2mRtE4X4bRaAS1BF9a9KxSrrSkZSJV29/ez4pWEUII+ht9j757pDwqxRgNh0ObW5uG7eEkYF9HQ4aJicSRTMWxxKFSLkoFFaU/lCqiVHQJz0/d39dQiEpBqaY0J5gYiw41NOSCkaHMQFVTVV19an+KPUMncjWZYCxBKUpEcw6dOkEqQ9V4ZkLE8VTBXXwoaMzyNkWnfSA4FoRzLJVatq6natvBFCLHqmgNPaX6LMANZmJTibqaZdcsaNnzqy2DFKcz7lNntkVLEi9LrEotqairyGSiirFDj/3mFwfGSvfChaRX0MVLWEMbi+cK/qvH+B7f4M9/AHnXl1q0TF/QAAAAAElFTkSuQmCC'
lIconData = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAFl0lEQVRYw+3XXYhc5RkH8N97zpkzH7sz2dnd7M5uom5MFsHaiNVQFS0S0hQUoQilVBHaUgq56oWlpRfFll70piC9KaUFoRci7V1LoGCv+iFtLBQNRGOMERqzyWY1X7s72dn5OL3YN8mabIwxXvYZ3jNzeN95vv/P87zBrVGKL+FZ7Izvl+gtvIxX0Lkeg3ALwkv4nqofecioHahHjst4D69Zcsav8Tza17Pg09JXNbzgSSPuxSaUkWMYU5iSO+kBy+bx742YJJ9SeA37PKJuFtl1TLsDj8rxXWz+LBVoafm82Rv4MGAGs2ax7bNUoGJKxdAnOFlFSxa99pkocB92yIVP9O+AXMAovoLG+u3sphOPF57Y90QeyiHZ39t/Yw59JjoThrYNvTw/Pz9ot9t/wQ8jTG8KBXfjxWd+/Mydj33tsfrYxFh+6M1DloeWP94B54LZ47Npa7yVNpvNrNfr3bW8vPy5WB+W0hsUmRl8Gd/BT3Y/u3vHnm/sUavXVIYqwsng0PKhtYqwEXXYcmiL1qAlTVN5nhseHra0tHT7ysrKSfwzvU6BeRjPS/zUZt8244sqRp/65lNhevv0mnZpaqI1IX8vd3TpqKJcXClrxVoxar3ZMnN2Rp7nV5iXSpIkCQsLCzl+d3UEZ/ADia+bNmJKsElQxmHGt45/5HC9Wbf3yb1m3phx8PBBBz44IAmJ2vma8YVxY2FMXsmvsbDRaMDWq5PwQfxSwy63C5rRF11cMLAgZFl2TemuDlftfHinO2bv0PtFT3GukGWZtHz96GZZdg0K7sNvjdlhi6AW28eCwrzCOccU6u3F9mRzsnltooWgMlRRbVSL/sX+DfvLYDD4SB1o4ucabjMpl+AM3lY47G1nfV9hD/567OAxg/5gQ6Z5JTe5fTL0+/0bwqndbsPZSwo8IbXbqIaBxGmrjmo77zf4IyaxD+VX//Rqf+7Y3IZMkzQx+8CsTtH5WOHdbtepU6dgCbUUP9Nwt2FBF32phpIRD2h60Lh7jLvHZtNnTp0pXThxoTQ2PWZ4ZFiarcW5KAoXFy969+C7DrxyQKVUkee5EMI1wufm5hxfPV5ItXQcCZgzYUo1Ij9Z900h6Ej1pAoDwXm1sXQs2bV7l9vuuk25Vrb44aJ3Xn/HawdeG/QavVCdq4atE1uNjIzIskxRFNrttvn5efO1eXbhlL6/+fPa+LBZTb5OeBEdFHTVrcj0BZukcb+r5wNBVXZZ8Ty2mxLO6zohKEuUFIKgJDGKVmzMF/AHp7NL9Vo3MurHzVUX1aVWVCQSFVQFPYUPHTVi1kTEUbrOa4s47bBJNZvUpILEqAm5SjzTj12S8poCq5fwEQenAcZUldYxT7GCeYWK3JDEyrq9DD0cUdhmVFNTEgUmUoN1RhZxxdfHFW6/bH2hY0gmvc7EmOsrqejp6erG5yCGr1B3UaJiNQrsoidRkl5u30X01BGdFMMKexEEIWqYKKIniqvWmrWpVHb5U5JcVrYkk8uU4splcolCoheNKvA+5vwjw0sKj+h4yGpkEzaYm8MGv29mJSq2aNoqsahwVB+/v8SyHtfauHWFVm7x3jCD5+Qet11qWmagcNSK4/6Op6+OcgMzgkcVOusUOIYjOBdT7eNmiDFrSH9aYq/NSqYMa0itGjjuvBPew7dwcKOBqh2zYGec9JsKiwqrMStORIVORcCWMY4duF/wBSXTNsk0ldRlEsGCnvf1LfoPnsPBjW5GSZzm74+on5LYIzEpSATLCkGhpjCCuhCzO5co66qibDi2tYEVq87pOGtJ4UX8CvM3upolcY5/NLbqikRdalxqRmpUakgql0XkhJjnQUdPSUfPsr5V72M/XsKh6MWbuhtWYzLdGz1zZ+yQrdjK108eSziJ/+J1/AtvYOFK6fk/fZT+B472o2FerjL4AAAAAElFTkSuQmCC'

## button icon data, icons based on Tango Desktop set
openBtnIconData = b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAA3WAAAN1gGQb3mcAAAD0ElEQVRIx6WVS2tdVRTHf3vvcx9NbrANgkI7SgLFWsWUDgwU4geooyY4FIuIH8CB4sB+BRUc9AOI0IHFgQOhLQFrrXYifVCtVGNI2t60zc19nHPu2Xuv5eA+cpNg29g/LNicc9b67b0e+xieosV3Tp2x1nwCxqqKMcb03/QW5VLprkp8t9uVa+fOnSt2+huAxcVFNzU1Vcvz3Oz84EH93qcnTpz46PR772OM2WYA589/y4VLF9aajcbpiYn9F8+ePetH/ROAmZmZX40x07VabdcJsvyFSqeTsrKygvc9X1UlxoiqcvLk2xRF8fKVq1e+3Gg0Pp6fn/9uaWkpbAPEGI8uLCyUBs6jdvmnHxER2p02169fH4JVlWOzszjnOHVqwY6NjU1d/eXnD4zENvDDToB1zrG+vo73HhFBVRER0jRlfHycyQOTzM3NgW4ByuUym5ubqCrT0zPu9p3bb67dWzuyCxBCUBGhKIohYGAhBIw15HnOjZs3EInDU8y+cYxut4sxhqSUYI2txBjLu2oQY9QQPDFGfIjD4DEKURRjHGPjNQ4ffmWYOoBypQrGIgrWJoBFjbPzn11Kls68FTFGEwDvPSFE1luBa8uBol8iUUOzdZCqr7D+/Z9b6RkseNhbqRJC5O8HB0r1ytxCtnZv+viHX9+4hn4xBMQYqbeEDhMcPDhJpZwMooEBw2gH665uqwBHjr7uDoseW623Xrt5t34RzOcjKQo0M+HQS/s5/uohXOKIolvD8gQN3ltjsBbz2x/33a2/6sm2GsQYyT1MVkpkRaTd8nR9ZC9KnKVWdYQowRqb7wJkQalWSr2dGIOzlr3JEKIiirfWpEOA915D8GTeMF4t94MbEvfsgLyIOAsSFRUtjKGzo00jWQH7qgnWGpwBfYb4UZS8EHwQKlUHqsQoObA5CmBQA1WDD4qMNIoqiPae9Sa8F9hHQUS39VTuA7kPmahsjE6yhBDIvVBEJXYjaREovOCjEkTQHZ2pW0MxUmRDlhVspkUWoj4arQEhBIpoaKaBNARyH1Ht7V7/o/d3yhpotrvSTouOEWkMAYBmhZC4hFY3UgiEqOxVRVTSLMQ096lamtsAaSFMTlQZqzhqzm6rwTPPgTU8eiyS5SHTaFoDgANY3fB0vbC89hjrHP9HivLgYdNkaZ6Lzx8PAKUQwu93VluzDdmXdJbrbP139yZRJE87jazTWmms3KoDJgFMu93+ZnP1/j++ouWn3zxPnOQYi+x+0X50eXnpq+bgnkqAF4ED/XQ9D0GBbn/INgBv+gFdH/Q8wQcABWLf9F8A0n+tNyUc0gAAAABJRU5ErkJggg=='
saveBtnIconData = b'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'
saveAsBtnIconData = b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADdYAAA3WAZBveZwAAAVxSURBVEhLrVVbbBRVGP7OzOzs7GX2fmt32922W6DYCGK8hYQIBiXEF6PFpkZ8FAQbX0RfTCVRTHwSU/WVByUkCFF8EQgkUgGhrZSKtAqLbemWQkvptrvdnd2dGc85u0t8AMWELzkz5+w58/237z9L8A/s/GjX59dzkZdmM3qdrkOs/gyBmGWHrN/x2bOXgraRD3p7Dp+ubv0n7hr4Yl/3o4eGmk9Gm5JKQyhMykSWXYos6ibI7aUS5jOzhcXx/qlCriA3+UbfnxkpHzh48KBe/fy+4F4y8uOj0W+ibWvrp6fS8tjEhHx9fEycvHmTZCmFYrNDdTgl2Rv3LGimKz1j29iYmB1es/yZvwYHBw3OdB9wA8H2DV/5PQ5zaW5Si1pTn1qM3PaoK31kcckM5/JaQ0k3REOUSUnXiWyzkbJBLNNz1g2Gt/j1yKlfcrt3c657ghtIPLHxQ6/dmPLa8u/KpnEsZMi3nMbYpOKQ89mCGMsXpbhosQCmAUEQ4fQEiJRNTalSLnb8/JqzAycGCpztHuA16Hxv19G4WrqUv13cAJPy8C3AYoU6oflC80qT6q9rBCGkOgTYFy4WFuZu5QPlhUkRxt1aCMAZHWR/72e9XAgSewTs2b7yAnnj9a6tzbJspWcqoDz4/lwKP13NcGIG0zTp0GF4VyqzNzRle+eLXp/TxvcYLg5faBgY7M/QKTfAySwa+d2mqPGGhriQTLYiHk+gsTGOhlgcLtXNjlBSA6VSkc85FB80Q0Z9fYyfDYZCdB6F1+v3O51qc3d3d5gd4wZKOSL5fAEYhoEiJWHeHhv4E/t+7MfF1BQ7wj039DKfc1QjOtR3CfuO9mN8+jZ1oASrVYbqpF5ZSjG2zw0IxFhFvSAVL0uc7NTwNfwwOIZ0jsDp9kGyyLw2Ou1ABp2eU71+9F2Zw7d9l3Enq0EURXg8XoQjEZWYQpSdq+TbJOuTzUlB16mkKQszUuezIxIOIRhNwBOshyjQclHDLE0GramWzyJA91y+IBIRN1wOG1WYgFAwhLq6+rBpmO3cQE9Pj0S19LTfHxCYBzVsWdeKZncJ+cwMCktZLC7McQMsTUWtgPxSDmVqbPHWGLrWJRAPqzy1NP+wSJYkIeImxi3Mz8+0K4oNFtlCw/NwLxi8riC6nl2Odr+GOzfTcLp8MKgBDvpW3R5MjA6je3MLVre2QpFtkGUZFtovVIlwud0Oxi0YBMvCoQhTNzKZDBRFgcPhgCRJCPnq0fXcamxud2AqNQKvP0LrValJargfH299DKuSbXC7PPwbTdNQKBQgUyOqQ7UxboF60962YiXK5bIpigKy2Szm5+d5JHa7HbFIIzrWP4ltzyeQ+u08PNTI+OgQ9m5bi8cfWQM3jSSXy/FvGHmhkKdRyGYsGlOpzp6StGKxPRwOo/fLvYQXudrHtcZiYKoqG2W0Wcq4PKRjlfIHDu6/xq+Nyj5/8jlDU6KZJFtapbxWdEmiIG5qaWkhLLzOV1+DleaR3SC0X/mbfVgzxX4pmhJkYT0IXbB1xysd2PPJHiyjdWC9MTjYz+UapBAJ6RRoUWwsLQwBf4A+Cde6QaMxqm8WGRtsLhlUpuXKui5Sh3w+j2AggFisATQtUFUXl3lBK4i06E4uGZp/HqaLbrJuZusHGS6Xi9fK4XDyORtWq5WrrdaQFU1WYVWs9F5pRFNT0wMNRsZqxRRXGzWZ18Bv0xpOnDxOD9F7/3+gbeVy/HphAOmpSb6+mrpC1efgcwbS/c4Oc/ubO3H6zM80tH/993tgRMIROGnavjtyGGTH29sub3ph8wqf18d67aFAK2hIp9PZc+fPXiUdHS9vidSHD9BcPiT6CqjihqZvzLz1N/NFVvSVJ826AAAAAElFTkSuQmCC9fVl90nWikfKHo1Gse3bOfStikajY54T1ZUrV7L97EwjRLm5uQQCgQklys3NHfOcqEbmglE+MPoSca+llMr2x1RgxDKbm5v/p2R3kuM4SCnHVCALoJSivLyctra2uzqGdyPbtpk8efJIfp0FMMZ0X7hwoaKpqSlruVrrMf07tRG7HXmOfz86X09PD1rrM0DIHi7ND3fs2PGSlLLsnvz1cVJKXerv738BCI7cikPAZKAAyAOCwMSOwsTlcvNDKA0kgKvA1dHXcgFEh1uI23w1fU75wy0NJIeB+DdAoXGCgbptnwAAAABJRU5ErkJggg=='
aboutBtnIconData = b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAGF0lEQVRIx42WXWwcVxXHf/djZvbD3rW99tpefyW14zgfTRORh0KLEKSQIqpWRe0DSDwhhQcewhMSQmrUh1IQb6hS1UrwgiJVCEpRURXRGqiaxkqatM2HY5J6N3GStb2Ovfba3o/ZOzOXh7UTELTKlf6auXc053fOuWfOHcGDjBMn5PD5WFoos0M39Eb+bz/Lg7AP8qr4vAcjT700QSieRfAEMCGg04IRILBIENcsnEZFr3bnuvMXXv+ReSDAl4695iwXV38souiHA33psYfH+t39o71i13C32DnQBcDVwhLT+QV77sod/2phqdo04csIdXLunZ8ufiFg8Fu/GNOKV11P7X/uyIHMk4/tdoIgYrpQ4ubCGsWlClJIxkd6GB/OcHjvAFMX5+zv3vpo9U6pcj7C/vrG4o33ufC6+R/A3udPuLWq987OgcyjP/n+Y3EQ8r1zeS7NLhJEIJUEBAKLALSWZDuSPPO1PQz1tts3Tl2qTV269e5Sef2VW6d+PrltV23fJEaOHvc859kXjh1J54tl+ed/zlBc3gChcF2F4zjsGUiz2bQ4jkIIyWa9yWe3V4gs4quHdjiVzXrv7btrlfaRI7OV/OTaPcDIUy9NCCte/t6TBwcHsmn91j9mKG/4uJ5LzHPxXIffHH+CHzx9mH3DHZyeXkBJiVQKYyIWy5uMDWZEtivpNfygr3h31e8e3Xe+PHsulACEfHco1zF69CvjzuS5PKvVJvG4S8xziHkOibiHVK1glVIk4x6JuEfM0ziuxg8izk4XyXal5KHdA4OD2c7DociNA+jWRohvPjKec30TMl24S8xz8La8dxyF4yh++cZ5hjJJiuU6ibhHFEaYQNGQBhNI5krrVKo+2Uy7MzqUGby9sL4PuKx5/g+KzdmJA2N9YjpfwgqBo3UrNZ7egmiOfXsv2a42CvNl/vjBDYwJkEqy/bUFQcRiuUYuk1CD2XSvkHYcQObKsx0I0TE+0iPmFtdwHN2SVriOxtWamKvp624nl03R29VOPO6RSMTwPOeeA1IJ1qs+nqvpSicyCLsLQHoxOWqxzZ0DXSwsb6J0KyVKSRyt8WIaL+YiRKuipZLEYq3UubrliOMopBBsNAK01qSTsSSWXgAdBFSVQgghEFIghURKiZQCKQVKShxH3wMIIYm5GoElDCNMIFFSorXC1apVXVKEQogmgLz9aH0Gi565scT4UDdgQYBSEqVaMCUlbEewVZ7WCoTYmktJzHPpzbQRRRGVaqMshZgFkLz4YmTh+rUbJTs2lEGJFsNaCMOIMGqJre20NiKKIoRorYRRRBhGJOIu2c4ETWPs8lptIQjspRYAQMjTZ6fvmMN7B0gnPYIgILK2pcgSmABrW4AoijAmoGkMxgREUUTM03Smk4z0pqjXmsH07OIC2s7cB8jwlY+m71SvzC7ao18eI+Yomr6haQKMCWj4zfuAMKJa9/F9gzERSkpS7QkOjWXxfWOvFBaXr99c+cQJkh/fA3TnuvPNhvnVa2+eXds11Gkf2dWHkmBMgO8bGr7BRvcjqNV8Gr5BSUGqPc6OvjSj/SmmPimYqYtzb1dN/eTsqeP+vV60cOGvUWr064XNmv+4taL38UM79GA2Jap1w3qtiZKCDy4VeXsqz8fXl9BaEfdcOjuSHBzt4cDODGc+LZgzn85NForLv4/FGhfuXn0//K9uWsn/fbN99BultfV6z9pmLZvrSXl7dvaIwWyKZKzVl7RWtCU9hrJpHhro4MBDGTSRfXfqmjlzcW6yWNr4bdPUP5x584XNbbv6Pw+c7lJmsticlyvLK3PrG/XvHJwYzPV1p3Quk5Ceq9Fao5QgDCx137eFucXo8vX5tdPnZ96bn1/8S1AtnS2eO7n2RUemC7SnR4883Na/77nhof6Du3b09Q73ZTq7M+lkqj3uCmtZWV2vz5dWKlc/u1W+np/71/Kti3+ql65cNdW1FaAC1IDo/wHagBSQ1rHOTLJ//4ST6t/tJDqGldfWL6SXgtCGfqXsbyzPmfXSzer8hcths75teB1YBTaB4PP+KjTgAXEguQXdvsa3Kq++ZWRbtS01tg1vj38DwkCcCvji0AkAAAAASUVORK5CYII=Y29tL3hhcC8xLjAvIgogICB4bXBNTTpEb2N1bWVudElEPSJnaW1wOmRvY2lkOmdpbXA6OTlkYTRjMGItN2UwNS00MGZkLWFhNjItZThhMzk4YjNlYmM0IgogICB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOmY2ZmIzY2FjLWRmODEtNDk0YS1iN2RjLWJmZjBlNDIwOGI2OSIKICAgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjUwYmM3MTFlLTFlMDItNDg4My05NmU3LWI3NjQ2NTc3YjRkNyIKICAgZGM6Rm9ybWF0PSJpbWFnZS9wbmciCiAgIEdJTVA6QVBJPSIyLjAiCiAgIEdJTVA6UGxhdGZvcm09IldpbmRvd3MiCiAgIEdJTVA6VGltZVN0YW1wPSIxNzQyNTg4MjI3MDQ2ODk0IgogICBHSU1QOlZlcnNpb249IjIuMTAuMzgiCiAgIHRpZmY6T3JpZW50YXRpb249IjEiCiAgIHhtcDpDcmVhdG9yVG9vbD0iR0lNUCAyLjEwIgogICB4bXA6TWV0YWRhdGFEYXRlPSIyMDI1OjAzOjIxVDE0OjE2OjU4LTA2OjAwIgogICB4bXA6TW9kaWZ5RGF0ZT0iMjAyNTowMzoyMVQxNDoxNjo1OC0wNjowMCI+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmZmM2FkOGExLTdlODctNGRiYS1hNjQ4LWViOThmMmY2MmRmNyIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iR2ltcCAyLjEwIChXaW5kb3dzKSIKICAgICAgc3RFdnQ6d2hlbj0iMjAyNS0wMy0yMVQxNDoxNzowNyIvPgogICAgPC9yZGY6U2VxPgogICA8L3htcE1NOkhpc3Rvcnk+CiAgPC9yZGY6RGVzY3JpcHRpb24+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz5aOuJXAAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6QMVFBEHC2qAiAAACEBJREFUWMPNl3twVNUdxz/ncXc3m2TzDkgC5gEUQtRECKKUIT5QBNuirfSPjuNox3HqjHZ0pnY61U6q1alO/aftOBW1aGu1yGh1FMpTUEYBxSCPyCMJBCSQB5uEPPaVvef0j3t3JZYZqdOZ9s6cvXf37jm/7/l+f68D/+NLXOwfm5tb9PFcZ5FA3C4QiyyUAgX+63MCzgrsDhe7tnpsfMf27S3p/wqAqhUthSIZfATBPdOnlXFdU21+U/1UMbk0n5JIDgADw3F6oiPsaTtlt37SOdLe1QeW520w+Zuut1qGvjGAqqVPPiCVeHzpwlk59/5ggTNzWulFcdbxRZRVb+weX/fB53Fj5aNd63/++/8IQFVzS8iGQ3+bUzvppsfvuzG3rrochLfwh/tOsvfIGaLDMQbOJRACSgtzKCnIpXHmJVxz+VRqKosBONLVz6PPbh470NGzkbH4j7q2tyS+FsCc21sCY2PBj1dcWz/7V/deH8gJOLR/EeWFt/fw6aHTaEehpEQIb2rmDmCsxRrDvNkV3Lm8gdrKYhKpNE88/17qja0HDoXDiflta1tS59tTE81bkVe9680V19UvePL+m4KOVry1/XMee3EbfYNxAgGN42iUUmilkEr6z9J7lhJHK85ER9m0u5P8cJC66jKua6pVvYNjRfuOnr1y6OiWNfDrCwOoXhb62dUNVXc/8+DyHKUkf1izk1c27MdxNFprtFYoKdBKobVi+bxKll9dQ3kkwPG+MaSUCAlSChCCPYdOMxpLMXf2FBY1VuuDnb1TRyPrUoNHt3z0bwAqbn2yJEc5a5575LZIcSTM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'
addSlotIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH1gcaCwcs9PsrvAAAAQ9JREFUOMvtlTFLA0EUhL87T1BstBCsLKzs70oRgv6MNBYhhSD+AkkKsfEPBNv8BVstLGxyjb2FtY2FiuLtGwtzITEHu8ELWGRgYRdm5z12hrewwLwRhZCyVn8ApMNjPrhqZr47cWADabfdoNNuMFagFuGZ8T+ENQM38Rg1KaoR53eNKUOTKqMuTw75Mo0iE8cxbx8FElwcH1CYkED6idVZ7yb1dgzw+ul4en5HAjNhAmfCGRQGzonChBnsbK2GPQWQd3q3Ux2cNvfJH1+4u3+o0sm9wlXhz1p9RZOcqLZUrK8tY5pH3IZm1SW8VG62N1fY290InjWJR9iV5hydX6cVRukv0y0aW6WYLT6GYHwD8BReNGzpZScAAAAASUVORK5CYII='
removeSlotIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH1gcaCwc7dyiuewAAAIlJREFUOMvtkrEJAmEMRt8PNm5g7Qp3IziGra0jiAO4wGHrHLrA3RDWtiLIXfJZ2IjG4u/zIM1HeAkhkCTJX8p30G5OPdBUeob+uG4/g1nQ1By2K0YXBRhNoUl6VwF23flnkUjM/Wlcbw8kcBcuMBfmMDmYicmFOywX83BwJB723aX6FPlVSVLBC1diMdtPBZMcAAAAAElFTkSuQmCC'
duplicateSlotIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAABmJLR0QAiACKAIUJpanVAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH1QoaFAYzCZZFWgAAAmJJREFUOMuVlU1PE1EUht9z70y/FnTXX9B2pv4PY4grVyYuXbMoUTAQ1yaABZVEiSFx7catKxNDoA2RICRAa13jAlhYIqbT297j4jLTmdpO29m06Tnz3Oe+96NUebX2kLV2MeVDQjSelBc+jqpbqtNxni0sT8vF6zfrTlzdEoIAAK3W74mhMzNZEFFsjxVXZGbqdDpy4DckEkkwM08MbjZ/RqCHRwePbm7+5AGEIAQiM8DL9ZVhGRIRfY6Ai8VC8N3zPPl150t+8ekSMTNNvKhEqGyszo40Vl2FW1O6vm5NlT8AHmncbrexV92ZaqeEYx9ibIpKdSKN9Xp9LNR1S8PBhUIehsXGuLYb1FzXjbVk5uHGzIxmsxmAlVKRxkajMRTab2GUSnf6YL/AzMjnQ8aeh9r+XtBYKpVGWJp+IoozNhkzM5Tq/mccBppPf1AXzEAymYyCtdaBsQEDntfG/rdq0Og4TmA3aEwkYFkSSilorfvgXq8XmRZzdOswM87O6kGW4b5MJoNsNgsAyOVyASsE9mG+BUXAjlOMAAGGEBJSSmitIYSAP/vbxTM7IJ1OB5EQEWzbHlgsAlF/F9i2DSJh7CwrWLxqbRdaa1h2IvHj7damO+rc+4OFbYUQIBLQWuP99rthrx5Zcf8CK2svlgbz96fPzCYGMGbv3gcAXF5d4PD7AZiwZY07/+H8bduClOYVY02Q0lzX57/OcXJ6jFQms1mem98eC1ZKIZVKRY6slH3rXk/j8uoCJ6fHgKDH5bn5D+bWjnkqG6ufut3ug8Gbq3+IGQxoAapq8L3lxed//do/xpSdCpp9RFcAAAAASUVORK5CYII='
moveSlotUpIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAABHNCSVQICAgIfAhkiAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAL/SURBVDiNtZRNaFxVFMd/5368eZkxRmQsbTEGxbZC0IWMpU5SbCmxILapFCO2LgSlWbhLbFJBcKErP0BcCIqCdeEiUAviQoJIwIgW3biwCoYGjTImTIXWTjsz7+O4yLzwUkuSgjlwuPdd7vmd/z33vCuqymaY2RTqZoLdRjfunXTvg2zfNh8PT01p8r+AByf9S9vv6DuGQWr627vA6Hox65ZiYMIdva1Ufvlg9WhpaM+RYs+t5eN7J4IX1ouTtbpicCyoFEulmacOniidr8+SpBG7ynv4dPrjxpVW48i3b0Rf3rTiR8al13o3/cSBZ0uLV+f46/IFapfmWLh8nsf2PVnyzp0ZnAx33RR4cFK6U2dnDu97pie1LS5c/BFnHNZ4fl36nkZSZ6h6qBuNv6qOye0bAo+MiFXc54/uHundUt5qfln6Dmt8xx2I8MPCF5RuKcrAg0NbjHfTlVHx64Jrd9v3qv1Du/t3VPxPta+xYvHOUwgCfGBQ28Z45dzCWfruvMfdf+9D/V099vSa4IEX/fh9d1WO7a8Mhz/XZjFOCMMCYVggCD2RaeAKQlAw4CPO/XmGygMPh33bdg5XJ/ypPGulK6rj7vG+rTumnjt0qss5j5KikjAzf5pYWtSvzXMt+Wc5SuHwzpNoqmgKzXaLs9OfXK1f/OPp2bfizyD3gxgr478vznW98sHzAFgvzVdPfBj6wNFoLxLZBt4bBFAF44R3PnqtGbc17CCKOBkDVoNnX4/2X1cWNdbiA8+V1hK+YDAGEEFVsVaI2xp+82Yk19d3FfhGZozQiP9GbYwLBOMEEUFTRewNeRsEi6WZXkIMGCs4bzBOiNspsjZ3dVfIsjkRKWRrzbgBCppCmihJpGgC6EpMUUQKIrJKpMuAgO98u84cVTjQO4pKirEgIizfHqTpyhvTDcRAJCJxNne5BDYHdUD95NvHy2sfmHomImcKJKKqmeI8NBuzZKbjHb2kHY+BJFMJtIG2qqb/eTY7SWzOM6jtbElz8CQHV83B/gXtSQriGSyg6AAAAABJRU5ErkJggg=='
moveSlotDownIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAABHNCSVQICAgIfAhkiAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAL8SURBVDiNtZRPbBRVHMc/781Md1bTGMCkhYNtOIiAnkw0bSFpNCGeOEAwMRyMMaReNCY0JXpFozQWT3JWExsEIzaxJkSREGiJIglRNCqVDSEIxlKqsN3ZeX9+HnZ2O112Wznwkl/e78283+f33nd+v1Eiwv0Y+r5QgbDdi4GR6AaermWjNX9NjZruewLj6Xp76COsNzhvsT7FeYvzBusNqUs4dPittonbgwFQnP7jCFW7QNUukLqk4T+3cc8Kl7nHoVD/a98KYEFYrBqR2lrEs1I1LQtehHgEX3signHVFU/c0HjLSHRSPIONjKFKRHws4vF4vNQsdRUSW27sGRiOFo+uOTU1agaXgL2TsZ7uR5/es/3NYhhEOLGx8xYvFrRHh4L3CQm3iAoaHcAru96IRcCYKhMnxhdmb/15sM5Tea0GhqO9m9Y/uX/H4MvFC9e+oWLnsVSp+jvMVa+R2H9BAQIiEOtOtvbs5uTUVwuXr8/snx4177bUeOo9M/brlR/Gvz13LNm8rp8gVBhV5u/qDFbfIYo1HbEmijXFYszW9bs4f/FscuXGpYk89C4wwNqSG5r+5evvf7z0ndm4tp/ZtITq8EQZMIoDOuKAvp4dlK5etj/9fu7nyrx7sZmjWpXNln2qU6nowvZnX+gNH6roi/PHCUKNDhVKweOrtlGZ0zIxefS6M/aJ6YMy18xoWW5nDshtbczg5Imj/xTcKjas6SfsUEQFzYaH+yi61Xx5/IvbQvBMK2hbMMCpMblqU7vt2OSn5e5oE+sefKxmhc0c/ny8XE3NzjMHkt/axbeUIj8GRsKdqzvXfLz7+ZceCCLFJ599WL45e3Pf6dH0g+XiloCVUgoIcqYB3fdasPeR3t7hoKBUaaZ05Oz77nXA58wBTkTsEnAGjKg1TJjzg2zWT70avBMEuuv8ITOUppgMaDOoBUw2W8DUwVEO2Ow3r00OYtqs03pL16/Q/E+sX1NnlvVdQ4LmE6dAKiL+ro/XTufMryerw10OLpKD/QceAIZcIO5IFQAAAABJRU5ErkJggg=='
exportCsvIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAD5klEQVQ4y6WVf0zUZRzHX5/vnXDYHabp0XEKAkqena7mmEAgF2NK/YO6VltrWf7lbHNtzrmmlcVMxmJrTnSutVrZijaNtnKJ1UjqTkI3MU4NMS30C4nOkx/fu/tyd09/XCAgMJqf7dk+z+d59vo8z/v57PMIQE3t3neBN3kAU0pVv7Fz91vjgjW1e9WDWk3tXjWWaR07uXr1KhaLBaWSewQBTQCV9CUZGxMBUbjdC++7wTiwiCAiKAVXrnT9B4cbPT24MzMB0HUdtzsThdCj6/jKfJNKMylYRKHrOiIyCh+Zi2joes+9vZr8H7Dgdrux2+0AXL58GZ/Ph4gQDAbxer0ABINBNJkhWNM0VEIRjUaTMU24Y9zi4Nfvc+b6CQaGO7E2PYwjJYuSrKrRJNOC287+RtHqYkQEm82G3e7g9KUWGi7tIjs7h7IKD4sWl9MfGuCGfoOTgQMEP2xl/7Yj04NXFxTicrnQdR0zanK0/TMC+sc8U+UjP9fDbfMaHUONxFOGcSzNYJN3I41fnWDfp7t4hPGVoU2Uore3F4BwzOBU90HmzJ3Dye8CHDpwhPZf/2J5+lpA6B/u5Q+jiaoNlbT+/SUh89b04JHRcOYwoGDoUZ7N2sGOyo+4eF7nrP8CLtvyZPLhQfq5Tlauk3MDP04NHgv/J3yRVIubt9cfYuHcxeS58tnqq6PjfBcOMokaccxwHD3URV72EsLxvqnBp1sDo/78tDzWLdlMJBJBREhPT6fkyTIiZghrJB3TSBA14oT672C3pRNXgyMlj1LKNQ5cVFiM0+kEYNmCVRQ89hR2hwMRYXBwEMMIJxtOwoIZToLDYZPUWbNRmHxesEp1d3cjIj3WkSwjMvT19SEilOavJdVi4/eudg62bYa2MddUFqJDMRIJhVImqQvSUMSpX9Ou6j/IoXi79X6NRyzNlobD4WDl0idYl7UTTWZTWuxj0/NbGDYVUSNG1IgTHRpGxTVe3rCVytKNiIgC9lineryIGUUGk77HtZK8nP0cbnmd1OKH6LzrJ2be65LNXV/w+LynafrlG6WUOuSvi71jnbRpo1ixwosmGpoInmUeAAaMuzQE9lCxpoJzN5swY2FSrGl45/s4eeo4CRU/9lK99TU/MazJYk1aRkbGtL/Elhe2EYkZHA/UU1pUzvmbP7HSWc7PgQBOSyH5n3Q8Z+bOgwsXkg/3Xk11taZpu2f6Dflvf0t01p9UlFbyQ8v3DIRvB1/ZL95ITg7bOjtHW+2ovIAFiE0FfNXjwRsKcfTFPg24pom2KKES3cDisrMliX3NzeNgTICrmZy6eLt1NtAIrPfXxYyJ6/8CQo7FjfAVQsgAAAAASUVORK5CYII='
importCsvIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAD2UlEQVQ4y6WV/0+VVRjAP89533vvC/LeLjIxuNqyoq0N2ioVuKyBpWu2Vqt+MFu/VPYXULrULHUSYebaWmv90FZkzkqxVkSrqY0EISwlr2wCQSD3kohr+l7gXl/e0w/XS5eFX5pnO9t5nj3n8zznOc95jgDUN+zYBrzGTQyt9fZXN2zeMktZ37BD3+yob9ihs5lmtjAwMIBhGGidthEElAA6vZa0LksDogmHF/3nBLPAIoKIoDX09/ddgcNIPE64uBiAWCxGOFyMRojHYtRU18yZmjnBIppYLIaIzMAzsogiFov/a6vk/4CFcDhMXl4eAL29vdTU1CAiRKNRSktLAYhGoyi5QbBSCu1pkslkWqfSjhJOAtdz+e7kfhYtXoRpmOkTXQWssoVfjnfOOLAsC9sOYucFERFs22b3wTfoHP2Idw6+jh20r6RCXR9cvqyCoqIiRAmpZIqJRIJEwkFEePOzTZydaOeJVWs5m2in7tON6SqZO+DZYBFhdHQUgIAVIC9oY9s2P5xpoudCC5XlS+kYOUhl+VJ6xlv4qmsvhqgbA2dmKpUi4Tg0Hd1Ln9NMdaSK7nOHSLmTdJ87RHWkihPn9rHvx8brX1423LIsfhvs4KehD1n14GpOnT9Myp0EIOVOcur8EaojK9jbtpVw4W3XjvhYR/vMuqv3GF90b2Vl1SMsmH8rNXetRRQoUzD9wkP3PEu4eDGRiqW83byOoURfpuTRWhfNAldWRCgsLATgy9Mb8fQULa0H+KTpfcTwCMzzEcg1COSa+PzCx59/QGvbEab1JU44jURqzeeGh4epetk3Zma8ZNIwNjaGiLBtdQuWZSGiWH/gYZLuJDnz/HhcxjAMPJkG4NtNY4TyQ7y1s4479jQ2rmHJMmWw3rxaG7QCFradrlUlOSQvT5CT48cVD6UUotJgz/Nm9hy/7wGgbx1Qqa52eVOpJI7j4DgOPnULztRFQsF8ArkG/lyFa13E8oc43tM5s7e1YF8u8LznsWDOiDWasrJSlCiUCCUFFfQP/sryO0sYmBhHGcIlYpTdW0Ld1y8xP38/Y1NxlJIRz9M+YMAEZhr0woUL50zLK89s44X3lrOSFeT4oiS9BPGp09wfeZSU67Jhz5O40w6h/FDwwvjfoPXTAlBXv327Umrztb6e1vEmzNAIT615nMFkO5cu/4UhPpbMK6fAfztn/ujh+28O6WntNh/d6T6W/dIFMAB3LnCk1rwb4We/GSiIRCpVuDhMMGQzPBjn9+hJb2joT9Ho3W273FqySy0Lrq8VeaTWfBfhRSAHjQKmgC5gS9su93DG7h8255+CV8L7SwAAAABJRU5ErkJggg=='
addRndColorIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAEiklEQVQ4y62Va2xUVRDH/3Mfe+/u7Xa3dFvbUheKVBB5tlVAIhiklIAQMYIhFDUCicRY+8nIBwRDSBQ0GqIi8tFGBAyPKpYoKUSUgLRpCMEGtKVsN4Xu0u727u692/s4xw9IY2kRo05ykpMzM79MZv6TA/wHKy6+t0/4t9C6J1FXW7sS4fDc/w/8wiwcHxugD659f+Tw6tU1CIfnjIgR/w5Q/fJ4Me+pYtw4d2vobfVMHF8101Oz+CFVytecyT+dPT1j3ooNB6LRLAYGokNxNBpw2ZuTHrUN/riSIy8gLhhGyryqBKRvtRNXdq+toMUzSlQxdsvCg0Hg527O9190j5XVbFt58OAJRCLnRgcv3zzlQ5E8y2VRHhccqwoeBVxPGjBuuoMTjYR3U26cuvsdDFoMXhkYV+DB+YjJv2zjjfb4Nc82Nn4FgA9vxbLNjzRwRusAVuhyh0RBJO5yKirTBDXglTP5Cv3YLaI6YEKBC9cmMJLxcEggSDQ51XOxsiWKrwGwIfAzb02eDwivSpLUJ8nygKJ4bCOd1TJpk6ysS4GACm9QhBOU0XxdxGyWhBYg9Jhgje12Is0U0k0nNDuMaRe6cVS6A1Y5zij+wic8IWOSKAkTjaTzPM/y+QCi8WjaIyhUXpSbg0DIB3cK4ZsrDEusfn74kpm4HHU3yKKpE/FkaQAl62dDHdHjqo0NrQAqAECkbE9hcNe8St+arjOxL46UTQstLwhromNyJDpSmHvjJjt5Lrb74C/WPpfBAmAA1Ltq1RvuaDqu2L5pIbZvWgiXqyXT7eouW+9DnkKv9V82u7JJDtkHeII+XDBz0J1wYi6D8qcQMkRghw59BOl+y5Bu/QSMc7FIlUtTE0r9g9kcqPAgOA6I6D4iozQfVyIcQApAhnPOR2zei1Xw3Q12bF5ODNMyGXlnhann9/0+ADvL4QwCeQW50PJ85bklkg4gCcC5kydVbWxoAVAJAL+OUvH5qQ1Xh4IpiQL6GGAERgwejUNSacGMRWNLfHkeXR7j4ci6xYyoh6o2NvD36xbBZhwEwHb5MDDntw8BeHtvM6b7doAmjkFOiEGSJPTfsO2+WOoqEeVYpp0WRDrtCNgqAUB60MX1uAHOAcY4GAcMi8N1ORzGwRgwocgLAJCn5kELKpAlB5bjIL9IlUNhdUr0smFZWf0sON8hMCEhAWjdtvdU5V+rfG7JYwCAYz+0DKs+N1fHA2VepBMWMroFLhJCJQJudhos2WucJA3r4VK86b12JrXsq626kxgOl6OwZiufVeZH27UUAKC8pfadeApCluESe3pCfby7cE5R2C/cshyEiv3o7dLdrja9SfazVxio7/jOdgZguNwikd9QeNfw9rfhcwAqAAGdnUsFmQ6QxKuLw/lCtLPP7WxNNnl9eElwhcTRXe1DA7qnjmeV+XH49tW9vVFIATCbP+1Ywhm+S8SyNb0d6SZvQF4nujRwZGc7v98P0rplTzO27GkGwNsAJIgoXldXlwHAAODUZx1LU7HBd+WAvJaROAL6j0zTNNTX14/qW/H6JLpX3h8LhfRGTvQ9nwAAAABJRU5ErkJggg=='
rndAllColorsIconData = b'iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAE6UlEQVQ4y52UW2xUVRSG/332uU3P3JnSMoMt0GIHi1AoYKPS+iA2REAUKUZCFeRFYsqTl/pmjCZgDJAg8UVflARDBCOhjWi0EVpuQjW0Umpv1BnoZTqdmc6cmXPmnL19EGukJYrrbe+91peVP/v/Kf5HNa1FU+22Zy9GIj4kk5FZe4T7hW5bgdMhD/lw8MzJEw0N9SgpqZm1j94PtKEKp7dWyfVPlaniHM0Kn+toW/7Ypt1fRCK5GZvT+4FurxbqV86X6VjcxNJCgXhUEj7b/kPV48/MhN8TvO7lBdT3xDzcvhBD4yqc3rJMql8VkunwhA3d5EibwNKQQvwFVsXZ9rYVc8Nrj9240T09T+4GPv1GRWVe52sUp1RHuKA7b47X+fVs+eZSIiqEI+QyhKkpC9kcgdOpwF9goaXfxk9D+VMfn8cWAPkZ4I3NDx2gRN4oUanUG1IFWQFPJXSij7EUksmJYM+Ee325NWe+rAuiJiKapuz8YD5BJLUgEtOTFPzbI+1orKys5OL0ps1LPmcMz4HkHYxbPJsSYCsCCS5yEz0Ab86QXQNAPqjeFmAK0E0HP3EtN9kdsXdLNJsihCfmexB85RGo7kefzIoAsOGtcC3nZLUoigOUUlkSqXsqoRcybhPTMlAU9MDhVqm4OkAPdwI7rQh0TlnCwGftQ+i1GTMB6AD5ZevWvfYnBw5CBACV46zimlshB3RQDuhpGzzHAQDjkXSvoJDFxW4nPIECxMOFaO3l8A+PW8Oj5ojNoNzRNUMI2PHjB//+Fb+2x3Dt+yGsCdgwRSCZtmAbeQgEKLvUe+R3rtZKqlKq+RQiKxJGTIq+CWvgx86pw5YJE0AcQBIA+0vaaY0bVwG+kRHMVXMYvplD1mCQsiaIgIeL+uOyJGkwPAVQfYDDV4C45hYd/lFk0/kEgAQAa4ZBXq2D4tUc9spFgN82QBmgZ/IQKEGW0c6aYmtJoVcmt/waFBeFw8eRY8zlcIrRoZ+T3/2p711Z8c5+EMpQb1nG5av9tOPSkNg9nqbDnFAuKk6+vEgqXurjKDVTGO9LIp/jsAzAF3ALTr+2cNPrYX02g4lcl3iuovlrre/d53OGtRmEu0xbZuUBGT4VCGkWJvMSorrFLc1mYIQywiBrnEDkGzKTZlX93sXDkl+eQs6exwi51fL+dZO2tTHEYhEsW7frJG5fyAiUconaCwodYFMW552Cj1xJyanfbDGW0VwZUZY1UbYFQSBEIJJogdVKqvialbF2EkKCNkFH/7lYdtp5JSWL0dDwAnJd+2k0YtQVefBgUkdxYm35i8QhlgUX+jilhGheVZBEC6ZlgXIZRAaPdOtmIpHqEAjfzogw2rrvOpsOoWQyjkhkHNXrdvAvv7kyeK7f7ukaQVffxfixBSu91f6go6R4oSaYuTxyaRM2A7xFMiaiWTY6kDlDVNZIOBlr2d/DZqRbMhlDPm+jb/CmCEC5824NXIp/6gk5qh0uaVGgWCNZPY9A0I2xobQ9eDXVKjrtXZyQWMu+HnbP2IxGowDA7xyzhJB0U1OTceyj1qPukFLj8NKy4gf85NbQpN1/JdGqFvCXKBfip/Zd5/816C1N0+w9e/bwQ4cOAQAGL08edRapNVnDKBvuSrSqHrpD4kLiqw/+Cf3XqqqqmvV+w5vh9+qbw+71b1eSe83+AYXFOeQGt6WNAAAAAElFTkSuQmCC'

## check for unsaved changes upon being called on opening
def unsavedChanges():
    if dirtyFlag == 1:
        confirmChanges = messagebox.askyesnocancel("Confirm exit", "You have unsaved changes, do you want to save before exiting?")
        if confirmChanges is None:
            return
        elif confirmChanges:
            saveFce()
            root.destroy()
        else:
            root.destroy()
    else:
        root.destroy() 

## defining main window
root = tk.Tk()
root.title("NFS FCE Paint Booth")
root.protocol('WM_DELETE_WINDOW', unsavedChanges)
root.resizable(False, False)
smallIcon = tk.PhotoImage(data=sIconData)
largeIcon = tk.PhotoImage(data=lIconData)
root.iconphoto(False, largeIcon, smallIcon)

## "About" dialog
def aboutDlg():
    aboutMsg = messagebox.showinfo("About NFS FCE Paint Booth",
                                   "NFS FCE Paint Booth v1.5 \n"
                                   "A NFS3/HS FCE color editor that doesn't suck!\n"
                                    "(c) 2025 and later AJ_Lethal\n\n"
                                    "Licensed under the MIT License")
    
## initializing general variables
colors = [[0,0,0,0],[]]
for i in range(16):
    colors[1].append(list())
    colors[1][i].append(list())
    colors[1][i].append(list())
    colors[1][i].append(list())
    colors[1][i].append(list())

colorList=[]
colorAmount = 0
colorListVar = tk.StringVar()
selectedColor = 0

fceType = tk.StringVar()
fceTypeStr = tk.StringVar()
fcePath = ''
fcePathPrev = ''
fcePathStr = tk.StringVar()

hueFieldsVars = [0,0,0,0]
hueFieldsVars[0] = tk.IntVar()
hueFieldsVars[1] = tk.IntVar()
hueFieldsVars[2] = tk.IntVar()
hueFieldsVars[3] = tk.IntVar()

satFieldsVars = [0,0,0,0]
satFieldsVars[0] = tk.IntVar()
satFieldsVars[1] = tk.IntVar()
satFieldsVars[2] = tk.IntVar()
satFieldsVars[3] = tk.IntVar()

briFieldsVars = [0,0,0,0]
briFieldsVars[0] = tk.IntVar()
briFieldsVars[1] = tk.IntVar()
briFieldsVars[2] = tk.IntVar()
briFieldsVars[3] = tk.IntVar()

tolFieldsVars = [0,0,0,0]
tolFieldsVars[0] = tk.IntVar()
tolFieldsVars[1] = tk.IntVar()
tolFieldsVars[2] = tk.IntVar()
tolFieldsVars[3] = tk.IntVar()

htmlFieldsVars = ['','','','']
htmlFieldsVars[0] = tk.StringVar()
htmlFieldsVars[1] = tk.StringVar()
htmlFieldsVars[2] = tk.StringVar()
htmlFieldsVars[3] = tk.StringVar()

buttonColors = ['','','','']
buttonColors[0] = ''
buttonColors[1] = ''
buttonColors[2] = ''
buttonColors[3] = ''

buttonColorsDisp = ['','','','']
buttonColorsDisp[0] = ''
buttonColorsDisp[1] = ''
buttonColorsDisp[2] = ''
buttonColorsDisp[3] = ''

randHue = 0
randSat = 0
randBri = 0

rndAllColAmount = tk.IntVar()
rndAllColAmount.set(10)

dirtyFlag = 0

rndColorMode3Vals =["Only primary color","All colors"]
rndColorMode4Vals =["Only primary color","Only primary & secondary color","All colors except hair color","All colors"]
rndColorModeIdx = None
           

## functions to validate characters inputted in text boxes
def inputCallback(input):
    if len(input) > 3:
        return False
    if input.isdigit() and input != "" and int(input) <= 255 and int(input) >= 0:
        return True
    elif input == "":
        return True
    else:
        return False
      
def inputCallbackHue(input):
    if len(input) > 3:
        return False
    if input.isdigit() and input != "" and int(input) <= 360 and int(input) >= 0:
        return True
    elif input == "":
        return True
    else:
        return False
 
def inputCallbackHtml(string, newString):
    acceptedChars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F','#','']
    for i in str(newString):
        if len(newString) > 7:
            return False
        
    for i in str(string):
        if len(string) > 7:
            return False
        if not i in acceptedChars:
            return False
        else:
            return True
    
## function to open FCE file and load color data, also enables disabled UI elements and selects first color
def openFce(*args):
    global dirtyFlag
    if dirtyFlag == 1:
        confirmChanges = messagebox.askyesnocancel("Confirm changes", "You have unsaved changes, do you want to save?")
        if confirmChanges is None:
            return
        elif confirmChanges:
            saveFce()
    global fcePath
    global fcePathPrev
    global fceType
    global colorAmount
    global colorsPrev
    if fcePath != "":
        fcePathPrev = fcePath
    fcePath = filedialog.askopenfilename(title="Open NFS3/HS .fce file", filetypes=[("NFS3/HS car mesh", "*.fce *.FCE")])
    if fcePath == "":
        fcePath = fcePathPrev
        return
    with open (fcePath, 'rb') as file:
        hueFieldSbox1.state(['!disabled'])
        satFieldSbox1.state(['!disabled'])
        briFieldSbox1.state(['!disabled'])
        tolFieldSbox1.state(['!disabled'])
        htmlField1.state(['!disabled'])
        
        hueFieldSbox2.state(['!disabled'])
        satFieldSbox2.state(['!disabled'])
        briFieldSbox2.state(['!disabled'])
        tolFieldSbox2.state(['!disabled'])
        htmlField2.state(['!disabled'])

        hueFieldSbox3.state(['!disabled'])
        satFieldSbox3.state(['!disabled'])
        briFieldSbox3.state(['!disabled'])
        tolFieldSbox3.state(['!disabled'])
        htmlField3.state(['!disabled'])

        hueFieldSbox4.state(['!disabled'])
        satFieldSbox4.state(['!disabled'])
        briFieldSbox4.state(['!disabled'])
        tolFieldSbox4.state(['!disabled'])
        htmlField4.state(['!disabled'])
        
        file.seek(0)
        if file.read(4) == b'\x14\x10\x10\x00':
            fceType = 'NFSHS'
            colorPos = file.seek(2080)
            colors[0] = list(struct.unpack('I', file.read(4)))
            for i in range(3):
                colors[0].append(0)
            colorAmount = colors[0][0]
            colorPos = file.seek(2084)
            for i in range(colorAmount):
                colorPos = file.tell()
                for x in range(4):
                    colors[1][i][x] = list(struct.unpack('>4B', file.read(4)))
                    colors[1][i][x][0] = round(colors[1][i][x][0] * 1.411764705882353)
                    if x < 3:
                        colorPos = colorPos + 64
                    file.seek(colorPos)
                colorPos = colorPos-188
                file.seek(colorPos)
            rndColorModeCbox['values'] = rndColorMode4Vals
            rndColorModeCbox['state'] = 'readonly'
            rndColorModeCbox.current(0)
        else:
            fceType = 'NFS3'
            colorPos = file.seek(2044)
            colors[0] = list(struct.unpack('I', file.read(4)))
            for i in range(3):
                colors[0].append(i)
            colorAmount = colors[0][0]
            colorPos = file.seek(2048)
            for i in range(colorAmount):
                colorPos = file.tell()
                for x in range(4):
                    colors[1][i][x] = list(struct.unpack('4I', file.read(16)))
                    colors[1][i][x][0] = round(colors[1][i][x][0] * 1.411764705882353)
                    if x == 1:
                        colorPos = colorPos + 260
                    file.seek(colorPos)
                    if x == 1 or x == 3:
                        colors[1][i][x] = [0,0,0,0]
                colorPos = colorPos - 244
                file.seek(colorPos)
            rndColorModeCbox['values'] = rndColorMode3Vals
            rndColorModeCbox['state'] = 'readonly'
            rndColorModeCbox.current(0)

    for i in range(16-colorAmount):
        colors[1][i+colorAmount][0:4] = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    colorsPrev = []
    if colorsPrev:
        colorsPrev.clear()
    colorsPrev = copy.deepcopy(colors)
    
    if fcePath != "":
        saveFCEBtn.state(['!disabled'])
        saveAsFCEBtn.state(['!disabled'])

    openFileLabel()    
    typeLabel['textvariable'] = fceTypeStr
    fceTypeStr.set(f'Type: {fceType}')
    
    colorListUI['state']=tk.NORMAL
    if colorAmount < 16:
        addColorBtn.state(['!disabled'])
        addRndColorBtn.state(['!disabled'])
        dupColorBtn.state(['!disabled'])
    if colorAmount > 0:
        remColorBtn.state(['!disabled'])
    rndAllColorsBtn.state(['!disabled'])
    rndColorsLbl.state(['!disabled'])
    rndColorsSbox.state(['!disabled'])
    importColorsBtn.state(['!disabled'])
    exportColorsBtn.state(['!disabled'])
    colorListBoxPopulate()
    colorListUI.selection_clear(0, tk.END)
    colorListUI.selection_set(0)
    loadColorUI()
    
    if fceType == 'NFSHS':
        hueLabel.state(['!disabled'])
        satLabel.state(['!disabled'])
        briLabel.state(['!disabled'])
        tolLabel.state(['!disabled'])
        
        colorLabel1.state(['!disabled'])
        colorLabel2.state(['!disabled'])
        colorLabel3.state(['!disabled'])
        colorLabel4.state(['!disabled'])
        htmlLabel1.state(['!disabled'])
        htmlLabel2.state(['!disabled'])
        htmlLabel3.state(['!disabled'])
        htmlLabel4.state(['!disabled'])
        colorButton1['state']=tk.NORMAL
        colorButton2['state']=tk.NORMAL
        colorButton3['state']=tk.NORMAL
        colorButton4['state']=tk.NORMAL
    else:
        hueLabel.state(['!disabled'])
        satLabel.state(['!disabled'])
        briLabel.state(['!disabled'])
        tolLabel.state(['!disabled'])
        
        hueFieldSbox1.state(['!disabled'])
        satFieldSbox1.state(['!disabled'])
        briFieldSbox1.state(['!disabled'])
        tolFieldSbox1.state(['!disabled'])
        
        colorLabel1.state(['!disabled'])
        colorLabel2.state(['disabled'])
        colorLabel3.state(['!disabled'])
        colorLabel4.state(['disabled'])
        htmlLabel1.state(['!disabled'])
        htmlLabel2.state(['disabled'])
        htmlLabel3.state(['!disabled'])
        htmlLabel4.state(['disabled'])
        colorButton1['state']=tk.NORMAL
        colorButton2['state']=tk.DISABLED
        colorButton3['state']=tk.NORMAL
        colorButton4['state']=tk.DISABLED

        hueFieldSbox1.state(['!disabled'])
        satFieldSbox1.state(['!disabled'])
        briFieldSbox1.state(['!disabled'])
        tolFieldSbox1.state(['!disabled'])
        htmlField1.state(['!disabled'])

        hueFieldSbox2.state(['disabled'])
        satFieldSbox2.state(['disabled'])
        briFieldSbox2.state(['disabled'])
        tolFieldSbox2.state(['disabled'])
        htmlField2.state(['disabled'])

        hueFieldSbox3.state(['!disabled'])
        satFieldSbox3.state(['!disabled'])
        briFieldSbox3.state(['!disabled'])
        tolFieldSbox3.state(['!disabled'])
        htmlField3.state(['!disabled'])

        hueFieldSbox4.state(['disabled'])
        satFieldSbox4.state(['disabled'])
        briFieldSbox4.state(['disabled'])
        tolFieldSbox4.state(['disabled'])
        htmlField4.state(['disabled'])
    file.close()
    dirtyFlag = 0

## sets fileLabel to active file
def openFileLabel():
    fileLabel['textvariable'] = fcePathStr
    fcePathStr.set(f'File: {fcePath}')

## copies colors list and adjusts hue for saving
def colorsListForSave():
    global colorsWrite
    colorsWrite = copy.deepcopy(colors)
    for i in range(colorAmount):
        for x in range(4):
            colorsWrite[1][i][x][0] = round(colorsWrite[1][i][x][0] / 1.411764705882353)

## saves file
def saveFce(*args):
    global dirtyFlag
    global fcePath
    if fcePath:
        fceSavePath = fcePath
        colorsListForSave()
        if fceType == 'NFSHS':
            with open (fceSavePath, 'r+b') as fileSave:
                colorPos = fileSave.seek(2080)
                fileSave.write(struct.pack('B',colorsWrite[0][0]))
                colorPos = fileSave.seek(2084)
                for i in range(colorAmount):
                    colorPos = fileSave.tell()
                    for x in range(4):
                        fileSave.write(struct.pack('>4B',
                                                    colorsWrite[1][i][x][0],
                                                    colorsWrite[1][i][x][1],
                                                    colorsWrite[1][i][x][2],
                                                    colorsWrite[1][i][x][3])
                                        )
                        if x < 3:
                            colorPos = colorPos + 64
                        fileSave.seek(colorPos)
                    colorPos = colorPos - 188
                    fileSave.seek(colorPos)
            fileSave.close()
            
        else:
            with open (fceSavePath, 'r+b') as fileSave:
                colorPos = fileSave.seek(2044)
                fileSave.write(struct.pack('B',colorsWrite[0][0]))
                colorPos = fileSave.seek(2304)
                fileSave.write(struct.pack('B',colorsWrite[0][0]))
                colorPos = fileSave.seek(2048)
                for i in range(colorAmount):
                    colorPos = fileSave.tell()
                    fileSave.write(struct.pack('4I',
                                                colorsWrite[1][i][0][0],
                                                colorsWrite[1][i][0][1],
                                                colorsWrite[1][i][0][2],
                                                colorsWrite[1][i][0][3])
                                    )
                    colorPos = colorPos + 260
                    fileSave.seek(colorPos)
                    fileSave.write(struct.pack('4I',
                                                colorsWrite[1][i][2][0],
                                                colorsWrite[1][i][2][1],
                                                colorsWrite[1][i][2][2],
                                                colorsWrite[1][i][2][3])
                                    )
                    colorPos = colorPos - 244
                    fileSave.seek(colorPos)
            fileSave.close()
            
        fileLabel['textvariable'] = fcePathStr
        fcePathStr.set(f'File saved to: {fcePath}')
        loadColorUI()
        fileLabel.after(5000, openFileLabel)
        dirtyFlag = 0

## saves file as another file
def saveFceAs(*args):
    global dirtyFlag
    global fcePath
    global fcePathPrev
    if fcePath:
        colorsListForSave()
        fcePathPrev = fcePath
        with open (fcePath, 'rb') as file:
            fceFile = file.read()
            file.seek(0)       
            if fceType == 'NFSHS':
                fceSavePath = filedialog.asksaveasfilename(title="Save NFSHS FCE file as...", filetypes=[("NFSHS FCE mesh file", "*.fce")], defaultextension=[".fce"])
                if fceSavePath == "":
                    fcePath = fcePathPrev
                    return
                with open (fceSavePath, 'wb') as fileSave:
                    fileSave.write(fceFile)
                    colorPos = fileSave.seek(2080)
                    fileSave.write(struct.pack('B',colorsWrite[0][0]))
                    colorPos = fileSave.seek(2084)
                    for i in range(colorAmount):
                        colorPos = fileSave.tell()
                        for x in range(4):
                            fileSave.write(struct.pack('>4B',
                                                        colorsWrite[1][i][x][0],
                                                        colorsWrite[1][i][x][1],
                                                        colorsWrite[1][i][x][2],
                                                        colorsWrite[1][i][x][3])
                                            )
                            if x < 3:
                                colorPos = colorPos + 64
                            fileSave.seek(colorPos)
                        colorPos = colorPos - 188
                        fileSave.seek(colorPos)
                fileSave.close()
                
            else:
                fceSavePath = filedialog.asksaveasfilename(title="Save NFS3 FCE file as...", filetypes=[("NFS3 FCE mesh file", "*.fce *.FCE")], defaultextension=[".fce"])
                if fceSavePath == "":
                    fcePath = fcePathPrev
                    return
                with open (fceSavePath, 'wb') as fileSave:
                    fileSave.write(fceFile)
                    colorPos = fileSave.seek(2044)
                    fileSave.write(struct.pack('B',colorsWrite[0][0]))
                    colorPos = fileSave.seek(2304)
                    fileSave.write(struct.pack('B',colorsWrite[0][0]))
                    colorPos = fileSave.seek(2048)
                    for i in range(colorAmount):
                        colorPos = fileSave.tell()
                        fileSave.write(struct.pack('4I',
                                                    colorsWrite[1][i][0][0],
                                                    colorsWrite[1][i][0][1],
                                                    colorsWrite[1][i][0][2],
                                                    colorsWrite[1][i][0][3])
                                        )
                        colorPos = colorPos + 260
                        fileSave.seek(colorPos)
                        fileSave.write(struct.pack('4I',
                                                    colorsWrite[1][i][2][0],
                                                    colorsWrite[1][i][2][1],
                                                    colorsWrite[1][i][2][2],
                                                    colorsWrite[1][i][2][3])
                                        )
                        colorPos = colorPos - 244
                        fileSave.seek(colorPos)
                fileSave.close()
                
            fcePath = fceSavePath
            fileLabel['textvariable'] = fcePathStr
            fcePathStr.set(f'File saved to: {fceSavePath}')
            loadColorUI()
            fileLabel.after(5000, openFileLabel)
        dirtyFlag = 0

## function to load color into color fields upon selecting it in the listbox
def loadColorUI(*args):
    global selectedColor
    selectedColorInput = colorListUI.curselection()
    if len(selectedColorInput)==1:
        selectedColor = int(selectedColorInput[0])

        if fceType == 'NFSHS':
            for i in range(4):
                hueFieldsVars[i].set(colors[1][selectedColor][i][0])
                satFieldsVars[i].set(colors[1][selectedColor][i][1])
                briFieldsVars[i].set(colors[1][selectedColor][i][2])
                tolFieldsVars[i].set(colors[1][selectedColor][i][3])

        else:
            for i in range(4):
                if i == 1 or i == 3:
                    hueFieldsVars[i].set(0)
                    satFieldsVars[i].set(0)
                    briFieldsVars[i].set(0)
                    tolFieldsVars[i].set(0)
                else:
                    hueFieldsVars[i].set(colors[1][selectedColor][i][0])
                    satFieldsVars[i].set(colors[1][selectedColor][i][1])
                    briFieldsVars[i].set(colors[1][selectedColor][i][2])
                    tolFieldsVars[i].set(colors[1][selectedColor][i][3])
        updateColorButtons()
        
    if selectedColor == 0 and colorAmount-1 <=1 :
        moveSlotUpBtn.state(['disabled'])
        moveSlotDownBtn.state(['disabled'])
    if selectedColor == 0:
        moveSlotUpBtn.state(['disabled'])
        moveSlotDownBtn.state(['!disabled'])
    elif selectedColor == colorAmount-1:
        moveSlotUpBtn.state(['!disabled'])
        moveSlotDownBtn.state(['disabled'])
    else:
        moveSlotUpBtn.state(['!disabled'])
        moveSlotDownBtn.state(['!disabled'])
                
## convert rgb values to html codes    
def rgb2hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)

## convert hex codes to rgb values
def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    
## updates colors when called and updates colors list
def updateColor(*args):
    global dirtyFlag
    global colorsPrev
    global fceType
    if fceType == 'NFSHS':
        for i in range(4):
            colors[1][selectedColor][i][0] = hueFieldsVars[i].get()
            colors[1][selectedColor][i][1] = satFieldsVars[i].get()
            colors[1][selectedColor][i][2] = briFieldsVars[i].get()
            colors[1][selectedColor][i][3] = tolFieldsVars[i].get()
            
    else:
        for i in range(4):
            if i == 1:
                colors[1][selectedColor][i] = [0,0,0,0]
            elif i == 3:
                colors[1][selectedColor][i] = [0,0,0,0]
            else:
                colors[1][selectedColor][i][0] = hueFieldsVars[i].get()
                colors[1][selectedColor][i][1] = satFieldsVars[i].get()
                colors[1][selectedColor][i][2] = briFieldsVars[i].get()
                colors[1][selectedColor][i][3] = tolFieldsVars[i].get()

    if colorsPrev == colors:
        dirtyFlag = 0
    elif colorsPrev != colors:
        dirtyFlag = 1
        
    updateColorButtons()

## updates HSV color fields based on the html fields input
def updateColorHtml(*args):
    global dirtyFlag
    global colorsPrev
    for i in range(4):
        htmlColorRaw = htmlFieldsVars[i].get()
        htmlColorRaw = htmlColorRaw.strip('#')
        rgbColor = hex_to_rgb(htmlColorRaw)
        hsvColorTemp = colorsys.rgb_to_hsv(rgbColor[0]/255,
                                         rgbColor[1]/255,
                                         rgbColor[2]/255)
        hueFieldsVars[i].set(round((hsvColorTemp[0]*255)*1.411764705882353))
        satFieldsVars[i].set(round((hsvColorTemp[1]*255)))
        briFieldsVars[i].set(round((hsvColorTemp[2]*255)))

    if htmlFieldsVars[3].get() == '#463612':
        satFieldsVars[3].set(190)

    updateColor()

## updates color buttons
def updateColorButtons(*args):
    global hue, sat, bri, tol
    for i in range(4):
        hue = hueFieldsVars[i].get()
        sat = satFieldsVars[i].get()
        bri = briFieldsVars[i].get()
        tol = tolFieldsVars[i].get()
        
        hueNFS = (hue/1.411764705882353)/255
        satNFS = sat/255
        briNFS = bri/255
        tolNFS = tol/255
        briTol = briNFS
        if tolNFS == 0:
            tolNFS = 0.001
        else:
            briTol = (briNFS+(briNFS/(0.94/tolNFS)))
        if briTol > 1:
            briTol = 1
        else:
            briTol

        rgbRaw = list(colorsys.hsv_to_rgb(hueNFS, satNFS, briNFS))
        rgbRawDisp = list(colorsys.hsv_to_rgb(hueNFS, satNFS, briTol))

        hexRaw=rgb2hex(round(rgbRaw[0]*255)
                      ,round(rgbRaw[1]*255)
                      ,round(rgbRaw[2]*255))
        
        hexRawDisp=rgb2hex(round(rgbRawDisp[0]*255)
                          ,round(rgbRawDisp[1]*255)
                          ,round(rgbRawDisp[2]*255))
        
        buttonColors[i] = f'#{hexRaw}'
        buttonColorsDisp[i] = f'#{hexRawDisp}'
        htmlFieldsVars[i].set(f'#{hexRaw}')
        
    colorButton1.config(background=buttonColorsDisp[0])
    colorButton2.config(background=buttonColorsDisp[1])
    colorButton3.config(background=buttonColorsDisp[2])
    colorButton4.config(background=buttonColorsDisp[3])

## function to populate color listbox
def colorListBoxPopulate():
    colorList.clear()
    for i in range(colorAmount):
        i=i+1
        colorList.append(f"Color {i}")
    colorListVar.set(colorList)

## color chooser function
def chooseColor(i):
    chosenColor = colorchooser.askcolor(buttonColors[i], title="Select color")
    if chosenColor != (None, None):
        chosenColorHsvRaw = (colorsys.rgb_to_hsv(chosenColor[0][0]/255.0,
                                              chosenColor[0][1]/255.0,
                                              chosenColor[0][2]/255.0))
        chosenColorHsvNfsHue = hueFieldsVars[i].set(round((chosenColorHsvRaw[0]*255) * 1.411764705882353))
        chosenColorHsvNfsSat = satFieldsVars[i].set(round(chosenColorHsvRaw[1]*255))
        chosenColorHsvNfsBri = briFieldsVars[i].set(round(chosenColorHsvRaw[2]*255))
    else:
        return
    updateColor()
        
## adds a color entry when called
def addColor(*args):
    global dirtyFlag
    global colorAmount
    if fcePath:
        colorAmount = colorAmount + 1
        colorAmountIndex = colorAmount - 1
        colors[0][0] = colorAmount
        if fceType == 'NFSHS':
            colors[1][colorAmountIndex][0] = [180,192,127,127]
            colors[1][colorAmountIndex][1] = [0,0,64,127]
            colors[1][colorAmountIndex][2] = [0,0,127,127]
            colors[1][colorAmountIndex][3] = [42,190,70,127]
        else:
            colors[1][colorAmountIndex][0] = [180,192,127,127]
            colors[1][colorAmountIndex][2] = [0,0,128,127]
        colorListBoxPopulate()
        if colorAmount == 16:
            dupColorBtn.state(['disabled'])
            addColorBtn.state(['disabled'])
            addRndColorBtn.state(['disabled'])
        else:
            remColorBtn.state(['!disabled'])
        dirtyFlag = 1

## removes selected color entry when called        
def remColor(*args):
    global dirtyFlag
    global colorAmount
    global selectedColor
    if fcePath:
        colorAmount = colorAmount - 1
        colors[0][0] = colorAmount
        colors[1].pop(selectedColor)
        colors[1].append(list())
        colors[1][15].append([0,0,0,0])
        colors[1][15].append([0,0,0,0])
        colors[1][15].append([0,0,0,0])
        colors[1][15].append([0,0,0,0])
        colorListBoxPopulate()   
        if colorAmount == 0:
            remColorBtn.state(['disabled'])
        else:
            dupColorBtn.state(['!disabled'])
            addColorBtn.state(['!disabled'])
            addRndColorBtn.state(['!disabled'])
        dirtyFlag = 1
        colorListUI.selection_clear(0, tk.END)
        if selectedColor == colorAmount:
            selectedColor = selectedColor - 1
        colorListUI.selection_set(selectedColor)
        loadColorUI()

## duplicates selected color when called
def dupColor(*args):
    global dirtyFlag
    global colorAmount
    if fcePath:
        colorAmount = colorAmount + 1
        colorAmountIndex = colorAmount - 1
        colors[0][0] = colorAmount
        if fceType == 'NFSHS':
            for i in range(4):
                colors[1][colorAmountIndex][i] = list(colors[1][selectedColor][i])
        else:
            colors[1][colorAmountIndex][0] = list(colors[1][selectedColor][0])
            colors[1][colorAmountIndex][2] = list(colors[1][selectedColor][2])
        colorListBoxPopulate()
        if colorAmount == 16:
            dupColorBtn.state(['disabled'])
            addColorBtn.state(['disabled'])
            addRndColorBtn.state(['disabled'])
        else:
            remColorBtn.state(['!disabled'])
        dirtyFlag = 1

## moves color up
def moveSlotUp(*args):
    global dirtyFlag
    if fcePath:
        if selectedColor <= 0:
            return
        slotMove = colors[1].pop(selectedColor)
        slotNewPos = selectedColor - 1
        colors[1].insert(slotNewPos, slotMove)
        colorListBoxPopulate()
        colorListUI.selection_clear(0, tk.END)
        colorListUI.selection_set(slotNewPos)
        loadColorUI()
        dirtyFlag = 1

## moves color down
def moveSlotDown(*args):
    global dirtyFlag
    if fcePath:
        if selectedColor == colorAmount - 1:
            return
        slotMove = colors[1].pop(selectedColor)
        slotNewPos = selectedColor + 1
        colors[1].insert(slotNewPos, slotMove)
        colorListBoxPopulate()
        colorListUI.selection_clear(0, tk.END)
        colorListUI.selection_set(slotNewPos)
        loadColorUI()
        dirtyFlag = 1

## random color function
def randNfsColor():
    global randHue, randSat, randBri
    randHue = random.randrange(0, 360)
    randSat = random.randrange(0, 255)
    if randSat <= 64:
        randBri = random.randrange(8, 180)
    else:
        randBri = random.randrange(8, 160)

## adds a color entry with randomized colors when called, also determined by random color mode
def addRndColor(*args):
    global dirtyFlag
    global colorAmount
    if fcePath:
        colorAmount = colorAmount + 1
        colorAmountIndex = colorAmount - 1
        colors[0][0] = colorAmount
        if fceType == 'NFSHS':
            if rndColorModeCbox.current() == 0:
                randNfsColor()
                colors[1][colorAmountIndex][0] = [randHue,randSat,randBri,127]
                colors[1][colorAmountIndex][1] = [0,0,64,127]
                colors[1][colorAmountIndex][2] = [0,0,16,127]
                colors[1][colorAmountIndex][3] = [30,190,70,127]
            elif rndColorModeCbox.current() == 1:
                for i in range(2):
                    if i == 1:
                        i = 2
                    randNfsColor()
                    colors[1][colorAmountIndex][i] = [randHue,randSat,randBri,127]
                colors[1][colorAmountIndex][1] = [0,0,64,127]
                colors[1][colorAmountIndex][3] = [30,190,70,127]
            elif rndColorModeCbox.current() == 2:
                for i in range(3):
                    randNfsColor()
                    colors[1][colorAmountIndex][i] = [randHue,randSat,randBri,127]
                colors[1][colorAmountIndex][3] = [42,190,70,127]
            else:
                for i in range(4):
                    randNfsColor()
                    colors[1][colorAmountIndex][i] = [randHue,randSat,randBri,127]
        else:
            if rndColorModeCbox.current() == 0:
                randNfsColor()
                colors[1][colorAmountIndex][0] = [randHue,randSat,randBri,127]
                colors[1][colorAmountIndex][2] = [0,0,16,127]
            else:
                for i in range(3):
                    randNfsColor()
                    colors[1][colorAmountIndex][i] = [randHue,randSat,randBri,127]
        colorListBoxPopulate()
        if colorAmount == 16:
            dupColorBtn.state(['disabled'])
            addColorBtn.state(['disabled'])
            addRndColorBtn.state(['disabled'])
        else:
            remColorBtn.state(['!disabled'])
        dirtyFlag = 1

## makes a whole new color table, amount of colors specfied in associated spinbox, also determined by random color mode
def rndAllColors(*args):
    global dirtyFlag
    global colorAmount
    if fcePath:
        colorAmount = rndAllColAmount.get()
        colors[0][0] = colorAmount
        colorAmountIndex = colorAmount - 1           
        if fceType == 'NFSHS':
            if rndColorModeCbox.current() == 0:
                for i in range(colorAmount):
                    randNfsColor()
                    colors[1][i][0] = [randHue,randSat,randBri,127]
                    colors[1][i][1] = [0,0,64,127]
                    colors[1][i][2] = [0,0,16,127]
                    colors[1][i][3] = [30,190,70,127]
            elif rndColorModeCbox.current() == 1:
                for i in range(colorAmount):
                    for x in range(2):
                        if x == 1:
                            x = 2
                        randNfsColor()
                        colors[1][i][x] = [randHue,randSat,randBri,127]
                    colors[1][i][1] = [0,0,64,127]
                    colors[1][i][3] = [42,190,70,127]
            elif rndColorModeCbox.current() == 2:
                for i in range(colorAmount):
                    for x in range(3):
                        randNfsColor()
                        colors[1][i][x] = [randHue,randSat,randBri,127]
                    colors[1][i][3] = [42,190,70,127]
            else:
                for i in range(colorAmount):
                    for x in range(4):
                        randNfsColor()
                        colors[1][i][x] = [randHue,randSat,randBri,127]
        else:
            if rndColorModeCbox.current() == 0:
                for i in range(colorAmount):
                    randNfsColor()
                    colors[1][i][0] = [randHue,randSat,randBri,127]
                    colors[1][i][2] = [0,0,16,127]
            else:
                for i in range(colorAmount):
                    for x in range(2):
                        if x == 1:
                            x = 2
                        randNfsColor()
                        colors[1][i][x] = [randHue,randSat,randBri,127]             
        colorListBoxPopulate()
        colorListUI.selection_clear(0, tk.END)
        colorListUI.selection_set(0)
        loadColorUI()
        if colorAmount == 16:
            dupColorBtn.state(['disabled'])
            addColorBtn.state(['disabled'])
            addRndColorBtn.state(['disabled'])
        else:
            remColorBtn.state(['!disabled'])
        dirtyFlag = 1

## imports color table from a CSV file
def csvImport(*args):
    global dirtyFlag
    global colorAmount
    if fcePath:
        csvFilePath = filedialog.askopenfilename(title="Import .csv file", filetypes=[("Comma-separated values", "*.csv")])
        if csvFilePath:
            with open(csvFilePath, 'r', newline='') as csvFile:
                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                colors[0].clear()
                colors[1].clear()
                colors[0] = next(reader) 
                for row in reader:
                    colors[1].append(row)
            csvFile.close() 
            for i in range(4):
                colors[0][i]=ast.literal_eval(colors[0][i])

            for i in range(16):
                for x in range(4):
                    colors[1][i][x]=ast.literal_eval(colors[1][i][x])
            colorAmount = colors[0][0]
            colorListBoxPopulate()
            colorListUI.selection_clear(0, tk.END)
            colorListUI.selection_set(0)
            loadColorUI()
            dirtyFlag = 1
    

## exports current color table to a CSV file
def csvExport(*args):
    if fcePath:
        csvFileSavePath = filedialog.asksaveasfilename(title="Export colors to .csv file", filetypes=[("Comma-separated values", ".csv")], defaultextension=".csv")
        if csvFileSavePath:
            with open(csvFileSavePath, 'w', newline='') as csvSaveFile:
                if fceType == 'NFS3':
                    for i in range(colorAmount):
                        colors[1][i][1] = [0,0,64,127]
                        colors[1][i][3] = [30,190,70,127]
                writer = csv.writer(csvSaveFile)
                writer.writerow(colors[0])
                writer.writerows(colors[1])
            csvSaveFile.close()

## defining window frames
mainFrame = ttk.Frame(root, padding=(5,5,5,5))
mainFrame.grid(row = 0, column = 0)
topFrame = ttk.Frame(mainFrame)
topFrame.grid(row = 0, column = 0, padx=2, pady=2, columnspan=6, sticky='NSEW')
leftFrame = ttk.Frame(mainFrame)
leftFrame.grid(row = 1, column = 0, padx=2, pady=2, sticky='NSEW')
rightFrame = ttk.Frame(mainFrame)
rightFrame.grid(row = 1, column = 1, padx=2, pady=2)
bottomFrame = ttk.Frame(mainFrame)
bottomFrame.grid(row = 2, column = 0, padx=2, pady=2, columnspan=6, sticky='NSEW')

mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)
topFrame.columnconfigure(0, weight=0)
topFrame.columnconfigure(1, weight=0)
topFrame.columnconfigure(2, weight=0)
topFrame.columnconfigure(3, weight=1)
leftFrame.columnconfigure(0, weight=1)
leftFrame.columnconfigure(1, weight=1)
leftFrame.columnconfigure(2, weight=1)
leftFrame.columnconfigure(3, weight=1)
leftFrame.columnconfigure(4, weight=1)
leftFrame.columnconfigure(5, weight=1)
rightFrame.columnconfigure(0, weight=3)
rightFrame.columnconfigure(1, weight=3)
rightFrame.columnconfigure(2, weight=3)
rightFrame.columnconfigure(3, weight=3)
rightFrame.columnconfigure(4, weight=3)
rightFrame.columnconfigure(5, weight=3)
rightFrame.columnconfigure(6, weight=3)
bottomFrame.columnconfigure(0, weight=3)
bottomFrame.columnconfigure(1, weight=0)
bottomFrame.columnconfigure(2, weight=1)

## loads button icon data for use
openBtnIcon = tk.PhotoImage(data=openBtnIconData)
saveBtnIcon = tk.PhotoImage(data=saveBtnIconData)
saveAsBtnIcon = tk.PhotoImage(data=saveAsBtnIconData)
aboutBtnIcon = tk.PhotoImage(data=aboutBtnIconData)
addSlotIcon = tk.PhotoImage(data=addSlotIconData)
removeSlotIcon = tk.PhotoImage(data=removeSlotIconData)
duplicateSlotIcon = tk.PhotoImage(data=duplicateSlotIconData)
moveSlotUpIcon = tk.PhotoImage(data=moveSlotUpIconData)
moveSlotDownIcon = tk.PhotoImage(data=moveSlotDownIconData)
exportCsvIcon = tk.PhotoImage(data=exportCsvIconData)
importCsvIcon = tk.PhotoImage(data=importCsvIconData)
addRndColorIcon = tk.PhotoImage(data=addRndColorIconData)
rndAllColorsIcon = tk.PhotoImage(data=rndAllColorsIconData)

## defining UI elements
openFCEBtn = ttk.Button(topFrame, image=openBtnIcon, text='Open FCE File', command=openFce)
openFCEBtn.grid(row = 0, column=0, sticky="W")
saveFCEBtn = ttk.Button(topFrame, image=saveBtnIcon, text='Save FCE File', command=saveFce, state='disabled')
saveFCEBtn.grid(row = 0, column=1, sticky="W")
saveAsFCEBtn = ttk.Button(topFrame, image=saveAsBtnIcon, text='Save FCE File As...', command=saveFceAs, state='disabled')
saveAsFCEBtn.grid(row = 0, column=2, sticky="W")
aboutBtn = ttk.Button(topFrame, image=aboutBtnIcon, text='About', command=aboutDlg)
aboutBtn.grid(row = 0, column=3, sticky="E")

colorListUI = tk.Listbox(leftFrame, listvariable=colorListVar, exportselection = 'False', state='disabled')
colorListUI.grid(row=0, column=0, rowspan=8, columnspan=6, sticky="NSEW")
colorListUI.bind('<<ListboxSelect>>', loadColorUI)
colorListUI.selection_set(0)
colorListUISBar = ttk.Scrollbar(leftFrame, orient=tk.VERTICAL, command = colorListUI.yview)
colorListUISBar.grid(row=0, column=5, rowspan=8, sticky="NSEW")
colorListUI.configure(yscrollcommand = colorListUISBar.set)
leftSeparator = ttk.Separator(leftFrame, orient="vertical")
leftSeparator.grid(row = 0, column = 6, rowspan=15, padx=2, sticky="NS")

addColorBtn = ttk.Button(leftFrame, image=addSlotIcon, text="Add Color", state='disabled', command = addColor)
addColorBtn.grid(row = 8, column=0,sticky="NSEW")
remColorBtn = ttk.Button(leftFrame, image=removeSlotIcon, text="Remove Color", state='disabled', command = remColor)
remColorBtn.grid(row = 8, column=1,sticky="NSEW")
dupColorBtn = ttk.Button(leftFrame, image=duplicateSlotIcon, text="Duplicate Color", state='disabled', command = dupColor)
dupColorBtn.grid(row = 8, column=2,sticky="NSEW")
moveSlotUpBtn = ttk.Button(leftFrame, image=moveSlotUpIcon, text="Move Color Up", state='disabled', command = moveSlotUp)
moveSlotUpBtn.grid(row = 8, column=3,sticky="NSEW")
moveSlotDownBtn = ttk.Button(leftFrame, image=moveSlotDownIcon, text="Move Color Down", state='disabled', command = moveSlotDown)
moveSlotDownBtn.grid(row = 8, column=4,sticky="NSEW")
rndSeparator1 = ttk.Separator(leftFrame, orient="horizontal")
rndSeparator1.grid(row = 9, column = 0, columnspan=5, pady=2, sticky="EW")
addRndColorBtn = ttk.Button(leftFrame, image=addRndColorIcon, text="Add Random Color", state='disabled', command = addRndColor)
addRndColorBtn.grid(row = 10, column=0,sticky="NSEW")
rndAllColorsBtn = ttk.Button(leftFrame, image=rndAllColorsIcon, text="Randomize All Colors", state='disabled', command = rndAllColors)
rndAllColorsBtn.grid(row = 10, column=1, sticky="NSEW")
rndColorsLbl = ttk.Label(leftFrame, text="No. of colors: ", state='disabled')
rndColorsLbl.grid(row = 10, column=2, columnspan=2,sticky="W")
rndColorsSbox = ttk.Spinbox(leftFrame, from_=1, to=16, width=3, state='disabled', textvariable = rndAllColAmount, justify='right')
rndColorsSbox.grid(row = 10, column=4, sticky="WE")
rndColorModeCbox = ttk.Combobox(leftFrame, values='', state='disabled')
rndColorModeCbox.grid(row = 11, column=0, columnspan= 5,sticky="WE", pady=2)
rndSeparator2 = ttk.Separator(leftFrame, orient="horizontal")
rndSeparator2.grid(row = 12, column = 0, columnspan=5, pady=2, sticky="EW")
leftSubFrame = ttk.Frame(leftFrame)
leftSubFrame.grid(row = 13, column = 0, columnspan = 6, sticky='NSEW')
leftSubFrame.columnconfigure(0, weight=1)
leftSubFrame.columnconfigure(1, weight=1)
importColorsBtn = ttk.Button(leftSubFrame, image=importCsvIcon, compound='left', text="Import Colors", state='disabled', command = csvImport)
importColorsBtn.grid(row = 13, column=0, sticky="NSEW")
exportColorsBtn = ttk.Button(leftSubFrame, image=exportCsvIcon, compound='left', text="Export Colors", state='disabled', command = csvExport)
exportColorsBtn.grid(row = 13, column=1, sticky="NSEW")

hueLabel = ttk.Label(rightFrame, text="Hue", anchor="center", state='disabled')
hueLabel.grid(row = 0, column = 2, padx=2, pady=2, sticky='NSEW')
satLabel = ttk.Label(rightFrame, text="Sat", anchor="center", state='disabled')
satLabel.grid(row = 0, column = 3, padx=2, pady=2, sticky='NSEW')
briLabel = ttk.Label(rightFrame, text="Bri", anchor="center", state='disabled')
briLabel.grid(row = 0, column = 4, padx=2, pady=2, sticky='NSEW')
tolLabel = ttk.Label(rightFrame, text="Tol", anchor="center", state='disabled')
tolLabel.grid(row = 0, column = 5, padx=2, pady=2, sticky='NSEW')

colorLabel1 = ttk.Label(rightFrame, text="Primary color", state='disabled')
colorLabel1.grid(row = 1, column = 0, padx=2, pady=2, sticky='E')
colorButton1 = tk.Button(rightFrame, background='#000', relief='groove', width='2', command=lambda:chooseColor(0), state='disabled')
colorButton1.grid(row = 1, column = 1)
hueFieldSbox1 = ttk.Spinbox(rightFrame, from_=0, to=360, width=4, textvariable=hueFieldsVars[0], command=updateColor, state='disabled', justify='right')
hueFieldSbox1.grid(row = 1, column = 2, padx=2, pady=2)
hueFieldSbox1.bind('<Tab>', updateColor)
satFieldSbox1 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=satFieldsVars[0], command=updateColor, state='disabled', justify='right')
satFieldSbox1.grid(row = 1, column = 3, padx=2, pady=2)
satFieldSbox1.bind('<Tab>', updateColor)
briFieldSbox1 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=briFieldsVars[0], command=updateColor, state='disabled', justify='right')
briFieldSbox1.grid(row = 1, column = 4, padx=2, pady=2)
briFieldSbox1.bind('<Tab>', updateColor)
tolFieldSbox1 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=tolFieldsVars[0], command=updateColor, state='disabled', justify='right')
tolFieldSbox1.grid(row = 1, column = 5, padx=2, pady=2)
tolFieldSbox1.bind('<Tab>', updateColor)
htmlLabel1 = ttk.Label(rightFrame, text="Hex code:", state='disabled')
htmlLabel1.grid(row = 2, column = 2, sticky='E')
htmlField1 = ttk.Entry(rightFrame, textvariable=htmlFieldsVars[0], justify='right', width='15', state='disabled')
htmlField1.grid(row = 2, column = 3, columnspan=3, sticky="W")
htmlField1.bind('<Return>', updateColorHtml)

colorLabel2 = ttk.Label(rightFrame, text="Interior color", state='disabled')
colorLabel2.grid(row = 3, column = 0, padx=2, pady=2, sticky='E')
colorButton2 = tk.Button(rightFrame, background='#000', relief='groove', width='2', command=lambda:chooseColor(1), state='disabled')
colorButton2.grid(row = 3, column = 1)
hueFieldSbox2 = ttk.Spinbox(rightFrame, from_=0, to=360, width=4, textvariable=hueFieldsVars[1], command=updateColor, state='disabled', justify='right')
hueFieldSbox2.grid(row = 3, column = 2, padx=2, pady=2)
hueFieldSbox2.bind('<Tab>', updateColor)
satFieldSbox2 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=satFieldsVars[1], command=updateColor, state='disabled', justify='right')
satFieldSbox2.grid(row = 3, column = 3, padx=2, pady=2)
satFieldSbox2.bind('<Tab>', updateColor)
briFieldSbox2 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=briFieldsVars[1], command=updateColor, state='disabled', justify='right')
briFieldSbox2.grid(row = 3, column = 4, padx=2, pady=2)
briFieldSbox2.bind('<Tab>', updateColor)
tolFieldSbox2 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=tolFieldsVars[1], command=updateColor, state='disabled', justify='right')
tolFieldSbox2.grid(row = 3, column = 5, padx=2, pady=2)
tolFieldSbox2.bind('<Tab>', updateColor)
htmlLabel2 = ttk.Label(rightFrame, text="Hex code: ", state='disabled')
htmlLabel2.grid(row = 4, column = 2, sticky='E')
htmlField2 = ttk.Entry(rightFrame, textvariable=htmlFieldsVars[1], justify='right', width='15', state='disabled')
htmlField2.grid(row = 4, column = 3, columnspan=3, sticky="W")
htmlField2.bind('<Return>', updateColorHtml)

colorLabel3 = ttk.Label(rightFrame, text="Secondary color", state='disabled')
colorLabel3.grid(row = 5, column = 0, padx=2, pady=2, sticky='E')
colorButton3 = tk.Button(rightFrame, background='#000', relief='groove', width='2', command=lambda:chooseColor(2), state='disabled')
colorButton3.grid(row = 5, column = 1)
hueFieldSbox3 = ttk.Spinbox(rightFrame, from_=0, to=360, width=4, textvariable=hueFieldsVars[2], command=updateColor, state='disabled', justify='right',)
hueFieldSbox3.grid(row = 5, column = 2, padx=2, pady=2)
hueFieldSbox3.bind('<Tab>', updateColor)
satFieldSbox3 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=satFieldsVars[2], command=updateColor, state='disabled', justify='right')
satFieldSbox3.grid(row = 5, column = 3, padx=2, pady=2)
satFieldSbox3.bind('<Tab>', updateColor)
briFieldSbox3 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=briFieldsVars[2], command=updateColor, state='disabled', justify='right')
briFieldSbox3.grid(row = 5, column = 4, padx=2, pady=2)
briFieldSbox3.bind('<Tab>', updateColor)
tolFieldSbox3 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=tolFieldsVars[2], command=updateColor, state='disabled', justify='right')
tolFieldSbox3.grid(row = 5, column = 5, padx=2, pady=2)
tolFieldSbox3.bind('<Tab>', updateColor)
htmlLabel3 = ttk.Label(rightFrame, text="Hex code: ", state='disabled')
htmlLabel3.grid(row = 6, column = 2, sticky='E')
htmlField3 = ttk.Entry(rightFrame, textvariable=htmlFieldsVars[2], justify='right', width='15', state='disabled')
htmlField3.grid(row = 6, column = 3, columnspan=3, sticky="W")
htmlField3.bind('<Return>', updateColorHtml)

colorLabel4 = ttk.Label(rightFrame, text="Driver hair color", state='disabled')
colorLabel4.grid(row = 7, column = 0, padx=2, pady=2, sticky='E')
colorButton4 = tk.Button(rightFrame, background='#000', relief='groove', width='2', command=lambda:chooseColor(3), state='disabled')
colorButton4.grid(row = 7, column = 1)
hueFieldSbox4 = ttk.Spinbox(rightFrame, from_=0, to=360, width=4, textvariable=hueFieldsVars[3], command=updateColor, state='disabled', justify='right')
hueFieldSbox4.grid(row = 7, column = 2, padx=2, pady=2)
hueFieldSbox4.bind('<Tab>', updateColor)
satFieldSbox4 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=satFieldsVars[3], command=updateColor, state='disabled', justify='right')
satFieldSbox4.grid(row = 7, column = 3, padx=2, pady=2)
satFieldSbox4.bind('<Tab>', updateColor)
briFieldSbox4 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=briFieldsVars[3], command=updateColor, state='disabled', justify='right')
briFieldSbox4.grid(row = 7, column = 4, padx=2, pady=2)
briFieldSbox4.bind('<Tab>', updateColor)
tolFieldSbox4 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=tolFieldsVars[3], command=updateColor, state='disabled', justify='right')
tolFieldSbox4.grid(row = 7, column = 5, padx=2, pady=2)
tolFieldSbox4.bind('<Tab>', updateColor)
htmlLabel4 = ttk.Label(rightFrame, text="Hex code: ", state='disabled')
htmlLabel4.grid(row = 8, column = 2, sticky='E')
htmlField4 = ttk.Entry(rightFrame, textvariable=htmlFieldsVars[3], justify='right', width='15', state='disabled')
htmlField4.grid(row = 8, column = 3, columnspan=3, sticky="W")
htmlField4.bind('<Return>', updateColorHtml)

bottomSeparator = ttk.Separator(bottomFrame, orient="horizontal")
bottomSeparator.grid(row = 0, column = 0, columnspan=6, pady=2, sticky="EW")
fileLabel = ttk.Label(bottomFrame, textvariable=fcePathStr)
fileLabel.grid(row = 1, column = 0, sticky='NSEW')
bottomSeparator2 = ttk.Separator(bottomFrame, orient="vertical")
bottomSeparator2.grid(row = 1, column = 1, padx=2, sticky="NS")
typeLabel = ttk.Label(bottomFrame, textvariable=fceTypeStr, anchor='e')
typeLabel.grid(row = 1, column = 2, sticky='NSEW')

## color field validation
reg = rightFrame.register(inputCallback)
regHue = rightFrame.register(inputCallbackHue)
regHtml = rightFrame.register(inputCallbackHtml)
hueFieldSbox1.config(validate="key", validatecommand=(regHue, '%P'))
satFieldSbox1.config(validate="key", validatecommand=(reg, '%P'))
briFieldSbox1.config(validate="key", validatecommand=(reg, '%P'))
tolFieldSbox1.config(validate="key", validatecommand=(reg, '%P'))
htmlField1.config(validate="key", validatecommand=(regHtml, '%S', '%P'))

hueFieldSbox2.config(validate="key", validatecommand=(regHue, '%P'))
satFieldSbox2.config(validate="key", validatecommand=(reg, '%P'))
briFieldSbox2.config(validate="key", validatecommand=(reg, '%P'))
tolFieldSbox2.config(validate="key", validatecommand=(reg, '%P'))
htmlField2.config(validate="key", validatecommand=(regHtml, '%S', '%P'))

hueFieldSbox3.config(validate="key", validatecommand=(regHue, '%P'))
satFieldSbox3.config(validate="key", validatecommand=(reg, '%P'))
briFieldSbox3.config(validate="key", validatecommand=(reg, '%P'))
tolFieldSbox3.config(validate="key", validatecommand=(reg, '%P'))
htmlField3.config(validate="key", validatecommand=(regHtml, '%S', '%P'))

hueFieldSbox4.config(validate="key", validatecommand=(regHue, '%P'))
satFieldSbox4.config(validate="key", validatecommand=(reg, '%P'))
briFieldSbox4.config(validate="key", validatecommand=(reg, '%P'))
tolFieldSbox4.config(validate="key", validatecommand=(reg, '%P'))
htmlField4.config(validate="key", validatecommand=(regHtml, '%S', '%P'))

## tooltips
openTip = Hovertip(openFCEBtn, 'Open FCE file (Ctrl+O)')
saveTip = Hovertip(saveFCEBtn, 'Save FCE file (Ctrl+S)')
saveAsTip = Hovertip(saveAsFCEBtn, 'Save FCE file as... (Ctrl+Shift+S)')
aboutTip = Hovertip(aboutBtn, 'About...')
addColorTip = Hovertip(addColorBtn, 'Add color (Ctrl+A)')
remColorTip = Hovertip(remColorBtn, 'Remove color (Ctrl+Del)')
dupColorTip = Hovertip(dupColorBtn, 'Duplicate color (Ctrl+D)')
addRndColorTip = Hovertip(addRndColorBtn, 'Add random color (Ctrl+R)')
rndAllColorsTip = Hovertip(rndAllColorsBtn, 'Randomize all colors (Ctrl+Shift+R)')
rndColorModeTip = Hovertip(rndColorModeCbox, 'Set random color mode')
moveSlotUpTip = Hovertip(moveSlotUpBtn, 'Move color up (Ctrl+Page Up)')
moveSlotDownTip = Hovertip(moveSlotDownBtn, 'Move color down (Ctrl+Page Down)')
exportCsvTip = Hovertip(exportColorsBtn, 'Export colors (Ctrl+E)')
importCsvTip = Hovertip(importColorsBtn, 'Import colors (Ctrl+I)')

## sets key bindings
root.bind('<Control-o>', openFce)
root.bind('<Control-O>', openFce)
root.bind('<Control-s>', saveFce)
root.bind('<Control-S>', saveFce)
root.bind('<Control-Shift-s>', saveFceAs)
root.bind('<Control-Shift-S>', saveFceAs)
root.bind('<Control-a>', addColor)
root.bind('<Control-A>', addColor)
root.bind('<Control-d>', dupColor)
root.bind('<Control-D>', dupColor)
root.bind('<Control-Delete>', remColor)
root.bind('<Control-r>', addRndColor)
root.bind('<Control-R>', addRndColor)
root.bind('<Control-Shift-r>', rndAllColors)
root.bind('<Control-Shift-R>', rndAllColors)
root.bind('<Control-Prior>', moveSlotUp)
root.bind('<Control-Next>', moveSlotDown)
root.bind('<Control-e>', csvExport)
root.bind('<Control-E>', csvExport)
root.bind('<Control-i>', csvImport)
root.bind('<Control-I>', csvImport)

root.mainloop()
