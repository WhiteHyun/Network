%A와 f 는 1, 1Hz로 가정하였기에 변수로 넣지 않았음.
value = 10001;  %끝 수
t = 0:.01:3.14;%x축
x = zeros(size(t));
y = zeros(1, length(t));

    for k = 1:2:value  %1부터 value까지 더하는 반복문(복합신호 계산 반복문)
        x = x + (4 / pi) * sin(2 * pi * k * t) / k;
        %y((k+1)/2,:) = x;  %여러 복합 신호 출력용 - //1
        %legend_label((k+1)/2) = "k = 1 ~ " + k; %여러 복합 신호 legend 출력용 - //1
    end
%복합신호
y(:) = x;   %단일 복합 신호 출력용 - //2
plot(t, y);
title('Composite Signal');
xlabel('x = Time');
%legend(legend_label);  %여러 복합 신호 legend - //1