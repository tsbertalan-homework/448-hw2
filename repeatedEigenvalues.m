format
A = [1 1 1; 2 1 -1; 0 -1 1]
[v, l] = eig(A);
v = v/v(3,1);
v=v*2;
v(:,2:3) = v(:,2:3) / v(3,2)
l
ksi = v(:,2)
eta = [-1;-1;0]  % from Mathematica

% verify
B = A - l(2,2) * eye(3);
disp('B * eta - ksi is about 0   :')
B * eta - ksi  % ~0
