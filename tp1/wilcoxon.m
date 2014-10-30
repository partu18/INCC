X = importdata('data2.csv');

bloques = [];
avbloques = [];
b = cell(2,1);

p1=2
p2=8
p3=3

s = 0;
f = 10;
nuevoBloque = X(X(:,5)<0.3 & X(:,2)>=s & X(:,2)<f & X(:,6)==p1 & X(:,7)==p2 & X(:,8)==p3,5);
b{1} = nuevoBloque;

s = 20;
f = 30;
nuevoBloque = X(X(:,5)<0.3 & X(:,2)>=s & X(:,2)<f & X(:,6)==p1 & X(:,7)==p2 & X(:,8)==p3,5);
b{2} = nuevoBloque;

ranksum(b{1},b{2})