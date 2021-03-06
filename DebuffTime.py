
# coding=utf-8

import os
import sys
import string 
import argparse
import random

#================================================================================ 
# 攻速是A下/秒，有%B的概率造成C秒眩晕。新的眩晕会覆盖原来的效果。求眩晕覆盖率。
#================================================================================    
def debuff_time(apm, prob, time):
    _apm = float(apm)
    _prob = float(prob)/100
    _time = float(time) * 1000

    #private

    #time:ms
    _atkTime = 1000 / _apm
    _totalTime = 10000*1000
    _totalBuffTime = 0
    _buffTime = 0
    _timer = 0

    # statics
    for i in range(_totalTime):
        _timer += 1
        if _timer >= _atkTime:
            _timer = 0
            if random.random() <= _prob:
                _buffTime = _time
        
        _buffTime -= 1
        if _buffTime > 0:
            _totalBuffTime += 1

    # result
    result = float(_totalBuffTime)/_totalTime

    # print
    print("apm: " + str(apm) + "/s, probability: " + str(prob) + "%, buff duration: " + str(time)  + "s\n")
    print("coverage rate: " + str(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apm", help="apm")
    parser.add_argument("-b", "--probability", help="probability")
    parser.add_argument("-c", "--time", help="buff duration")

    args = parser.parse_args()
    debuff_time(args.apm,args.probability,args.time)
