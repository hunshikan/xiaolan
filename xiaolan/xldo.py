# -*- coding: utf-8 -*-
# 小蓝中央控制

import sys
import os
import pyaudio
import pygame
import requests
import json
import snowboydecoder
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
import speaker
import nlp
sys.path.append('/home/pi/xiaolan/xiaolan/skills/')
import clock
import xlonly
import weather
import music
import tuling
import joke
import news
import smarthome
import camera
import snowboytrain
import ts
import onesay

def welcome():

    print('''

    #################*******###################
    #         小蓝-中文智能家居对话机器人         #
    #      (c)蓝之酱-1481605673@qq.com         #
    #   www.github.com/xiaoland/xiaolan-dev   #                                   
    #               欢迎使用!!!  :)            #              
    ###########################################

    ''')
    
    print('Check xiaolan')
    os.system('omxplayer /home/pi/xiaolan/xiaolan/musiclib/welcome.mp3')
    os.system('pulseaudio --start')

def awaken():

    detector = snowboydecoder.HotwordDetector("/home/pi/xiaolan/xiaolan/snowboy/blueberry.pmdl", sensitivity=0.5, audio_gain=1)
    detector.start(detected_callback)

def detected_callback():
    print "检测到唤醒，转交指令给xldo"
    try:
        sys.exit(-1)
    except SystemExit:
        xldo.convenstation()
    
def convenstation():
    
    b = baidu_stt(1, 3, 2, '{')
    r = recorder()
    s = skills()
    
    speaker.ding()
    r.record()
    speaker.dong()
        
    tok = b.get_token()
    text = b.stt('./voice.wav', tok)
    intent = nlp.get_intent(text)
    s.getskills(intent, text, tok)

def sconvenstation():

    speaker.speacilrecorder()
        
class skills(object):
    
    def __init__(self):
        pass
        
    def getskills(self, witch, text, tok):
        s = skills()
        if witch == 'clock':
            s.clock(tok)
        elif witch == 'xlonly':
            s.xlonly(tok)
        elif witch == 'camera':
            s.camera(tok)
        elif witch == 'smarthome':
            s.smarthome(tok)
        elif witch == 'weather':
            s.weather(tok)
        elif witch == 'music':
            s.music(tok)
        elif witch == 'ts':
            s.ts(tok)
        elif witch == 'email':
            s.email(tok)
        elif witch == 'story':
            s.story(tok)
        elif witch == 'joke':
            s.joke(tok)
        elif witch == 'news':
            s.news(tok)
        elif witch == 'smarthome':
            s.smarthome(tok)
        elif witch == 'caream':
            s.caream(tok)
        elif witch == 'video':
            s.video(tok)
        elif witch == 'hotelSearch':
            s.hotel(tok)
        elif witch == 'no':
            sconvenstation(tok)
        elif witch == 'reintent':
            nlp.do_intent(text)
        elif witch == 'snowboytrain':
            s.snowboytrain(tok)
        elif witch == 'translate':
            s.ts(tok)
        else:
            s.tuling(text, tok)
    
    def clock(self, tok):
        clock.start(tok)
        
    def xlonly(self, tok):
        
        xlonly.start(tok)
    
    def weather(self, tok):
        
        weather.start(tok)
        
    def camera(self, tok):
        
        camera.start(tok)
        
    def music(self, tok):
        
        music.start(tok)
        
    def tuling(self, text, tok):
        
        tuling.start(text, tok)
    
    def story(self, tok):
        
        story.start(tok)
        
    def joke(self, tok):
        
        joke.start(tok)
        
    def news(self, tok):
        
        news.start(tok)
        
    def smarthome(self, tok):
        
        s = smartHome()
        s.start(tok)
    
    def video(self, tok):
        
        video.start(tok)
    
    def hotel(self, tok):
        
        hotel.start(tok)
        
    def snowboytrain(self, tok):
        
        snowboytrain.start(tok)
    
    def ts(self, tok):
        
        ts.start(tok)
        
welcome()
awaken()




