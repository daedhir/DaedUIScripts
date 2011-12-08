#!/usr/bin/env python

from shutil import copyfile
import os
import difflib

if not os.path.exists('Interface/AddOns/ClassTimer/ClassTimer.old.lua'):
    print 'Found fresh ClassTimer install, modifying...'
    copyfile('Interface/AddOns/ClassTimer/ClassTimer.lua', 'Interface/AddOns/ClassTimer/ClassTimer.old.lua')
    fin = open('Interface/AddOns/ClassTimer/ClassTimer.old.lua', 'r')
    fout = open('Interface/AddOns/ClassTimer/ClassTimer.lua', 'w')

    for line in fin.readlines():
        if line.lstrip().strip() == 'self.db = LibStub("AceDB-3.0"):New("ClassTimerDB", self.defaults)':
            print 'Replacing line:'
            print line
            fout.write('\tself.db = LibStub("AceDB-3.0"):New("ClassTimerDB", self.defaults, true)\n')
        else:
            fout.write(line.rstrip() + '\n')

    fin.close()
    fout.close()



if not os.path.exists('Interface/AddOns/SexyMap/SexyMap.old.lua'):
    print 'Found fresh SexyMap install, modifying...'
    copyfile('Interface/AddOns/SexyMap/SexyMap.lua', 'Interface/AddOns/SexyMap/SexyMap.old.lua')
    fin = open('Interface/AddOns/SexyMap/SexyMap.old.lua', 'r')
    fout = open('Interface/AddOns/SexyMap/SexyMap.lua', 'w')

    for line in fin.readlines():
        if line.lstrip().strip() == 'self.db = LibStub("AceDB-3.0"):New("SexyMapDB", defaults)':
            print 'Replacing line:'
            print line
            fout.write('\tself.db = LibStub("AceDB-3.0"):New("SexyMapDB", defaults, true)\n')
        else:
            fout.write(line.rstrip() + '\n')

    fin.close()
    fout.close()

if not os.path.exists('Interface/AddOns/sct/sct.old.lua'):
    print 'Found fresh SCT install, modifying...'
    copyfile('Interface/AddOns/sct/sct.lua', 'Interface/AddOns/sct/sct.old.lua')
    fin = open('Interface/AddOns/sct/sct.old.lua', 'r')
    fout = open('Interface/AddOns/sct/sct.lua', 'w')
    
    for line in fin.readlines():
        if line.lstrip().strip() == 'self.db = LibStub("AceDB-3.0"):New("SCT_CONFIG", self:GetDefaultConfig())':
            print 'Replacing line:'
            print line
            fout.write('  self.db = LibStub("AceDB-3.0"):New("SCT_CONFIG", self:GetDefaultConfig(), true)\n')
        else:
            fout.write(line.rstrip() + '\n')
    fin.close()
    fout.close()

if not os.path.exists('Interface/AddOns/Dominos_XP/xp.old.lua'):
    print 'Found fresh Dominos install, modifying...'
    copyfile('Interface/AddOns/Dominos_XP/xp.lua', 'Interface/AddOns/Dominos_XP/xp.old.lua')
    fin = open('Interface/AddOns/Dominos_XP/xp.old.lua', 'r')
    fout = open('Interface/AddOns/Dominos_XP/xp.lua', 'w')
    
    for line in fin.readlines():
        if line.lstrip().strip() == "self.value = value":
            fout.write(line.rstrip() + '\n')
            fout.write("\n")
            fout.write("\tlocal blank = CreateFrame('StatusBar', nil, value)\n")
            fout.write("\tblank:EnableMouse(false)\n")
            fout.write("\tblank:SetAllPoints(self)\n")
            fout.write("\tself.blank = blank\n")
        elif line.lstrip().strip() == "local text = value:CreateFontString(nil, 'OVERLAY', 'GameFontHighlight')":
            fout.write("\tlocal text = blank:CreateFontString(nil, 'OVERLAY', 'GameFontHighlight')\n")
        elif line.lstrip().strip() == "local click = CreateFrame('Button', nil, value)":
            fout.write("\tlocal click = CreateFrame('Button', nil, blank)\n")
        elif line.lstrip().strip() == "self.rest:SetStatusBarColor(0.25, 0.25, 1)":
            fout.write("\tself.rest:SetStatusBarColor(0.5, 0.65, 1)\n")
        elif line.lstrip().strip() == "self.value:SetStatusBarColor(0.6, 0, 0.6)":
            fout.write("\tself.value:SetStatusBarColor(1.0, 1.0, 0.86)\n")
        elif line.lstrip().strip() == "self.bg:SetVertexColor(0.3, 0, 0.3, 0.6)":
            fout.write("\tself.bg:SetVertexColor(0., 0., 0., 0.5)\n")
        else:
            fout.write(line.rstrip() + '\n')
    fin.close()
    fout.close()

