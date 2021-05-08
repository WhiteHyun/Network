%A와 f 는 1, 1Hz로 가정하였기에 변수로 넣지 않았음.
variable = 9;  % maximum number
t = 0:.01:3.14;
y = zeros(2, length(t));
%x = zeros(size(t));
for k = 1:2:variable  %1부터 variable까지
    y((k+1)/2,:) = (4 / pi) * sin(2 * pi * k * t) / k; %주기 = 1/k 임, 즉 주파수 = k.
end
Peak_amplitude = max(y, [], 2); %Peak amplitude
k = 1:2:variable;
%시간 영역
plot(t, y)
title('Time domain')
xlabel('x = Time')
ylabel('y = Amplitude')
legend('k = 1', 'k = 3', 'k = 5', 'k = 7', 'k = 9')
grid on
%주파수 영역
figure
bar(k, Peak_amplitude, 0.1)  %막대그래프, k에 따른 Peak_amplitude를 그림
title('Frequency domain')
xlabel('x = Frequency')
ylabel('y = Amplitude')