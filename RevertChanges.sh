#!/bin/sh

ADIR=Interface/AddOns

if [ -e $ADIR/ClassTimer/ClassTimer.old.lua ]
then
    echo "Reverting ClassTimer"
    mv $ADIR/ClassTimer/ClassTimer.old.lua $ADIR/ClassTimer/ClassTimer.lua
fi

if [ -e $ADIR/SexyMap/SexyMap.old.lua ]
then
    echo "Reverting SexyMap"
    mv $ADIR/SexyMap/SexyMap.old.lua $ADIR/SexyMap/SexyMap.lua
fi

if [ -e $ADIR/sct/sct.old.lua ]
then
    echo "Reverting SCT"
    mv $ADIR/sct/sct.old.lua $ADIR/sct/sct.lua
fi

if [ -e $ADIR/Dominos_XP/xp.old.lua ]
then
    echo "Reverting Dominos"
    mv $ADIR/Dominos_XP/xp.old.lua $ADIR/Dominos_XP/xp.lua
fi

