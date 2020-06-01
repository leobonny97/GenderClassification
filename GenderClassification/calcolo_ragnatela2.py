import os
import time
import threading
import multiprocessing
import math
from pylab import *
import PIL.Image as im
import csv
import sys
import pandas as pd
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from string import Template
import string

filegender=pd.read_csv('../train_gtruth.csv', index_col=0)
array = np.genfromtxt ("train_gtruth.csv", delimiter = ",", skip_header = 1)
array=array.astype(int)

def distanza(x1, y1, x2, y2):
    x12 = (x2 - x1) * (x2 - x1)
    y12 = (y2 - y1) * (y2 - y1)
    xy = x12 + y12
    dist = math.sqrt(xy)
    return dist

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

intero = 0

voltostr = ''

cerchi = 4
fetteQ = 4  # fette per quadrante

fette = fetteQ * 4
s1 = cerchi * fette

file = [[0 for y in range(s1+2)] for x in range(100187)]

# in range inseriamo il numero di immagine da dare in input alla ragnatela
dizionario = [[0 for y in range(s1)] for x in range(100187)]
# x = width
# y = height

dizionario=np.array(dizionario, dtype=int)

dizionario_str = ['' for xx in range(100187)]

dizionario_gen = ['' for xx in range(100187)]

volto = np.zeros(s1)


def aggiungi(xcentro, ycentro, rax, xpunto, ypunto, distNaso, coeff, immm):
    indice = 0

    settore = np.zeros(3)  # cerchio, quadrante, fetta

    a = 0  # a = raggioStart
    b8 = 1 * rax / 15  # b = raggioStop
    i = 1  # in quale cerchio cade il punto. i = [1, cerchi]

    b4 = 3 * rax / 15
    b2 = 7 * rax / 15

    # cerchi
    if (distNaso > a and distNaso <= b8):
        settore[0] = 1
    elif (distNaso > b8 and distNaso <= b4):
        settore[0] = 2
    elif (distNaso > b4 and distNaso <= b2):
        settore[0] = 3
    else:
        settore[0] = 4

    # quadrante
    if (xpunto <= xcentro and y <= ycentro):
        # il punto appartiene al quadrante in alto a sinistra
        settore[1] = 2
    elif (x <= xnose and y >= ynose):
        # il punto appartiene al quadrante in basso a sinistra
        settore[1] = 3
    elif (x >= xnose and y <= ynose):
        # il punto appartiene al quadrante in alto a destra
        settore[1] = 1
    else:
        # il punto appartiene al quadrante in basso a destra
        settore[1] = 4

    a = 0  # grado Start
    b = 90 / fetteQ  # grado Stop
    i = 1  # in quale fetta cade il punto. i = [1, fette]

    radang_a = 0  # radiante Start
    radang_b = math.radians(b)  # radiante Stop
    tng_a = math.tan(radang_a)
    tng_b = math.tan(radang_b)

    # fetta
    while (settore[2] == 0 and b < 90):
        if (coeff > tng_a and coeff <= tng_b):
            settore[2] = i
        b = b + (90 / fetteQ)
        radang_b = math.radians(b)  # radiante Stop
        tng_a = tng_b
        tng_b = math.tan(radang_b)
        i = i + 1

    if (xpunto == xnose):
        settore[2] = 1

    if (settore[2] == 0):
        settore[2] = fetteQ

    if (settore[1] == 1 or settore[1] == 3):
        indice = int(fette * (settore[0] - 1) + fetteQ * (settore[1] - 1) + abs(settore[2] - 4) - 1)
    else:
        indice = int(fette * (settore[0] - 1) + fetteQ * (settore[1] - 1) + settore[2] - 1)

    try:
        if (xnose != xpunto or ynose != ypunto):  # il naso non ha settore
            volto[indice] = int(volto[indice] + 1)
    except:
        # else:
        print("ERROOOOOOOREEEEEE------")
        print("indice ", indice)

    return indice


immagini = os.listdir('../Lara')

num_volto = 0

for img in immagini:
    if img.find(".jpg") > 0:

        tick_detector = time.time()

        im2 = "Lara/" + str(img)

        foto = cv2.imread(im2)

        volto = np.zeros(s1)

        xnose = 0
        ynose = 0
        raggio = 0

        xlont = 0
        ylont = 0

        foto = imutils.resize(foto, width=512)
        gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

        tick_detector = time.time()

        rects = detector(foto, 1)

        dista = 0
        raggio = 0

        m = 0
        d = 0
        n = 1
        imga = zeros([512, 512, 3])

        if size(rects) == 1:
            for (i, rect) in enumerate(rects):
                tick_predictor = time.time()

                shape = predictor(gray, rect)

                shape = face_utils.shape_to_np(shape)
                (x, y, w, h) = face_utils.rect_to_bb(rect)
                # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                xnose = shape[33][0]
                ynose = shape[33][1]

                for (x, y) in shape:
                    tick_volto = time.time()

                    dista = distanza(xnose, ynose, x, y)
                    if (dista > raggio):
                        raggio = dista
                        xlont = x  # coordinata x del punto più lontano dal naso
                        ylont = y  # coordinata y del punto più lontano dal naso
                for (x, y) in shape:
                    settore = [0, 0, 0]
                    if (y == ynose):
                        m = 0
                    else:
                        m = (x - xnose) / (y - ynose)
                    m = abs(m)

                    d = distanza(xnose, ynose, x, y)

                    tick_punto = time.time()

                    nnn = aggiungi(xnose, ynose, raggio, x, y, d, m, imga)

        else:
            continue

        dizionario[num_volto] = volto

        nomeimagine = str(img)
        dimensione = len(nomeimagine)
        nomeimagine = nomeimagine[:dimensione - 4]

        dizionario_str[num_volto] = int(nomeimagine)

        for (a) in array:
            if (a[0]) == (dizionario_str[num_volto]):
                dizionario_gen[num_volto]=int(a[4])
                break


        file[num_volto] = np.append(dizionario[num_volto], [dizionario_str[num_volto]] )
        file[num_volto] = np.append(file[num_volto], [dizionario_gen[num_volto]])

        num_volto = num_volto + 1
        if ((num_volto % 200) == 0):
            print(num_volto)

pd.DataFrame(file).to_csv("../file2.csv")

print(num_volto)