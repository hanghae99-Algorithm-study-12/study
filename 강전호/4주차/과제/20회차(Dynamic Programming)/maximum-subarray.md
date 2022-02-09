
![카데인알고리즘](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FHWPk6%2Fbtq0MUz3EZ7%2F31qB99RIGXylLjW9J30ja0%2Fimg.jpg)
A[5]까지 부분합은 A[4]의 부분합을 통해서 구할 수 있다.

A[4]의 Sum을 보면, [-1, 3, 0, 1, -1]이라는 값이 있다.

그 다음 A[5]의 Sum을 보면 [1, 5, 2, 3, 1]이 있는데, 이 값들은 이전 A[4]의 배열에서 A[5]의 값인 2를 더해준 값이다.

A[4]의 최대값은 3, A[5]의 최대값은 5로 둘 차이는 2만큼이다.

이 말은, Sum은 모든 값을 가져 갈 필요 없이 내 위치를 포함한 최대값만 가져가면 된다.
