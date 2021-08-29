@echo off
:menu 
color C  
echo MM        MM  AAAAAAAAAAAA  X       X   EEEEEEEEEEEE  NN        N  CCCCCCCCCCCC  OOOOOOOOOOOOO
echo M M      M M  A          A   X     X    E             N N       N  C             O           O
echo M  M    M  M  AAAAAAAAAAAA    X   X     E             N  N      N  C             O           O
echo M   M  M   M  A          A     X X      EEEEEEEEEEE   N   N     N  C             O           O
echo M    MM    M  A          A      XX      E             N    N    N  C             O           O
echo M          M  A          A     X  X     E             N     N   N  C             O           O
echo M          M  A          A    X    X    E             N      N  N  C             O           O
echo M          M  A          A   X      X   E             N       N N  C             O           O
echo M          M  A          A  X        X  EEEEEEEEEEEE  N        NN  CCCCCCCCCCCC  OOOOOOOOOOOOO
echo.
echo 1.Lancer le bot
echo 2.Afficher les credits
echo 3.Quitter
echo.
set /p reponse="Quel programme voulez-vous executer ?"

If /i "%reponse%"=="1" goto :bot
If /i "%reponse%"=="2" goto :credits
If /i "%reponse%"=="3" goto :fin

:bot
cls
call py main.py
cls
goto :menu

:credits
cls
start txt\credits.txt\
cls
goto :menu

:fin
exit