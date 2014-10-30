X = importdata('data2.csv');
p1 = [1,2];
p2 = [3,4];

nombres = {'LH-T-','LH-A-','RH-T-','RH-A-'};

bloques = [];
avbloques = [];
b = cell(11,1);

for i = 0:8
    s = i*5;
    f = (i+1)*5;
    nuevoBloque = X(X(:,5)<0.3 & X(:,2)>=s & X(:,2)<f & X(:,6)==2 & X(:,7)==8 & X(:,8)==3,5);
    b{i+1} = nuevoBloque;
end

for i = 0:8
    currB = b{i+1};
    n = mean(currB);
    avbloques = [avbloques,n];
end

x = 0:8;
X = [x; ones(1,length(x))];
[reg,bint] = regress(avbloques.',X.');

res = [];
for i = 0:8
    res = [res,i*reg(1)+reg(2)];
end

h=figure;
plot(x,avbloques);
hold
plot(x,res);

saveas(h,'RH-DA-T','jpg');
bint
