#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:56:46 2018

@author: caseytaylor
"""

import random

def lambda_handler(request, context):
    # read request, write a response 
    request_type = request["request"] ["type"]
    speech_text = ""
    end_session = True
    sa = {}
   
    
    
    if  request_type == "LaunchRequest":
        speech_text = "Hello World"
        
    elif request["request"]["intent"]["name"] == "AMAZON.HelpIntent":
        speech_text = "no help is available"
        
    elif  request_type == "IntentRequest":
        intent = request["request"]["intent"]["name"]
        
        
        if "slots" in request["request"] ["intent"]:
            slots = request["request"] ["intent"]["slots"]
            
            
        if intent == "RandomNumberIntent":
            lowBound = 0
            highBound = 10
            
            if "value" in slots["low"]:
                if slots["low"]["value"] == "?":
                    lowBound = 0
                else:
                    lowBound = int(slots["low"]["value"])
                
                
            if "value" in slots["high"]:
                if slots["high"]["value"] == "?":
                    highBound = 10
                else:
                    highBound = int(slots["high"]["value"])
                
            
            
            randomNum = random.randint(lowBound,highBound)
            speech_text = str(randomNum)
                
            

  
        if intent == "DoArithmeticIntent":
            operation = request["request"]["intent"]["slots"]["operation"]["value"]
            firstNumber = None
            secondNumber = None
        
            if "value" in slots["FirstNumber"]:
                firstNumber = slots["FirstNumber"]["value"]
            if "value" in slots["SecondNumber"]:
                secondNumber = slots["SecondNumber"]["value"]
        
            sa = {"first": firstNumber, "second": secondNumber,"operation":operation}
        
            if firstNumber == "?":
                speech_text = "Please repeat the first number."
                end_session = False
                
            elif secondNumber == "?":
                speech_text = "Please repeat the second number."
                end_session = False
                
            elif firstNumber != "?" and secondNumber != "?":
                if operation == "add":
                    firstNumber = int(slots["FirstNumber"]["value"])
                    secondNumber = int(slots["SecondNumber"]["value"])
                    sum =  firstNumber + secondNumber
                    speech_text = str(sum)
                
                if operation == "multiply":
                    firstNumber = int(slots["FirstNumber"]["value"])
                    secondNumber = int(slots["SecondNumber"]["value"])
                    product =  firstNumber * secondNumber
                    speech_text = str(product)
                
            
            
     
        if intent == "AnswerIntent":
            operation = request["session"]["attributes"]["operation"]
            firstNumber = request["session"]["attributes"]["first"]
            secondNumber = request["session"]["attributes"]["second"]
            
            if operation == "add":
                if firstNumber == "?":
                    firstNumber = int(request["request"]["intent"]["slots"]["number"]["value"])
                    
                elif secondNumber == "?":
                    secondNumber = int(request["request"]["intent"]["slots"]["number"]["value"])
                    
                sum =  int(firstNumber) + int(secondNumber)
                speech_text = str(sum)
                
            if operation == "multiply":
                if firstNumber == "?":
                    firstNumber = int(request["request"]["intent"]["slots"]["number"]["value"])
                    
                elif secondNumber == "?":
                    secondNumber = int(request["request"]["intent"]["slots"]["number"]["value"])
                    
                product =  int(firstNumber) * int(secondNumber)
                speech_text = str(product)
            
            
    r = {"outputSpeech":{"type":"PlainText", "text":speech_text}, 
         "shouldEndSession":end_session}
    response = {"version":"1.0","response":r, "sessionAttributes":sa}
    return response
