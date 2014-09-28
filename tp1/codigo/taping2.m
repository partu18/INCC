addpath('/home/partu/INCC/codigo/func_aux.m');

screenNum = 0;
res = [1600 900];
clrdepth = 24;
[win,rect] = Screen('OpenWindow',screenNum,0,[0 0 res(1) res(2)],clrdepth);
black = BlackIndex(win);
white = WhiteIndex(win);
Screen('FillRect',win,white);
refresh = Screen('GetFlipInterval',win)
%Synchronize to retrace at start of trial/animation loop:
vbl = Screen('Flip',win);
%Loop:Cycle through 300images:
tic
for i = 1:10
	%Show images exactly 2 refresh cycles apart of each other:
	if mod(i,3) == 0
        Screen('FillRect',win,white);
        dibujar_puntito(win);
	else
		Screen('FillRect',win,white);
    end
    Screen('FillRect',win,black,[800,0,805,900]);
    
    %dibujo flecha
    %Screen('FillArc',win,black,[1000,350,1200,400],90,90)
    
    
    vbl = Screen('Flip',win,vbl+(20-0.1)*refresh);
	%Keyboard checks, whatever...Next loop iteration.
end;
%End of animation loop, blankscreen, record offset time:
toffset = Screen('Flip',win,vbl+(2-0.5)*refresh);
toc
Screen('CloseAll');
ShowCursor;


