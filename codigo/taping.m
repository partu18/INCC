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
for i = 1:30
	%Show images exactly 2 refresh cycles apart of each other:
	if mod(i,2) == 0
        Screen('FillRect',win,white);
        Screen('FillOval', win, black, [800, 450, 900, 550]);
	else
		Screen('FillRect',win,white);
	end
	vbl = Screen('Flip',win,vbl+(20-0.1)*refresh);
	%Keyboard checks, whatever...Next loop iteration.
end;
%End of animation loop, blankscreen, record offset time:
toffset = Screen('Flip',win,vbl+(2-0.5)*refresh);
toc
Screen('CloseAll');
ShowCursor;
