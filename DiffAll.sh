#!/bin/sh

ADIR=Interface/AddOns
dos2unix $ADIR/ClassTimer/ClassTimer.old.lua
diff -u $ADIR/ClassTimer/ClassTimer.old.lua $ADIR/ClassTimer/ClassTimer.lua > ClassTimer.patch
dos2unix $ADIR/SexyMap/SexyMap.old.lua
diff -u $ADIR/SexyMap/SexyMap.old.lua $ADIR/SexyMap/SexyMap.lua > SexyMap.patch
dos2unix $ADIR/sct/sct.old.lua
diff -u $ADIR/sct/sct.old.lua $ADIR/sct/sct.lua > sct.patch
dos2unix $ADIR/Dominos_XP/xp.old.lua
diff -u $ADIR/Dominos_XP/xp.old.lua $ADIR/Dominos_XP/xp.lua > Dominos_XP.patch
