###
- sum() : 모든원소의 합을 계산
- mean() : 산술평균, 크기가 0 -> NaN
- std() : 표준편차
- var() : 분산 선택적으로 자유도, 분모의 기본값은 n
- min() : 최소값
- max() : 최대값
- argmin(): 최소원소의 색인값
- argmax() : 최대원소의 색인값
- cumsum() : 각원소의 누적합
- cumprod() : 각 원소의 누적곱  
- any() : 하나이상의 값이 True 인지 검사.
- all() : 모든원소가 True 인지 검사.
- unique(x) : x 중복된 원소는 제거, 남은 원소를 정렬된 형태로 반환.
- intersect1d(x, y): 배열 x,y에 공통적으로 존재하는 원소를 정렬 반환.
- union1d(x, y): 두 배열의 합집합 반환
- in1d(x,y): x원소가 y원소에 포함되었는지 불리언 배열 반환.
- setdiff1d(x,y): x,y의 차집합 반환.
- setxor1d(x,y): 한 배열에는 포함, 두배열 모두 포함되지ㅏ 않은 원소들의 집합(대칭차집합) 반환.
### 선형대수
- diag(): 정사각형의 대각|비대각 원소를 1차원 배열로 반환
    * 1차원 배열을 대각선 원소로 하고, 나머지는 0으로 채운 단위행렬 반환.
- dot(): 행렬곱셈
- trace(): 행렬의 대각선 원소의 합계산
- det(): 행렬식을 계산
- eig(): 정사각 행렬의 고유값과 고유벡터를 계산
- inv(): 정사각 행렬의 역행렬 계산
- pinv(): 정사각 행렬의 무어-펜로즈 유사역원 역행렬을 구한다.
- qr(): QR 분해를 계산
- svd(): 특잇값 분해(SVD) 계산
- solve(): A가 정사각 행렬일때 Ax = b 만족하는 x를 구한다.
- lstsq(): Ax = b 를 만족하는 최소제곱을 구한다.
### RANDOM
- seed(): 난수생성기의 시드를 지정
- permutation(): 순서를 임의로 바꾸거나 임의의 순열을 반환한다.
- shuffle(): 리스트나 배열를 뒤섞는다.
- rand(): 균등분포에서 표본을 추출한다.
- randint(): 주어진 최소/최대 범위안에서 임의의 난수를 추출.
- randn(): 표준편차 1이고, 평균값 0인 정규분포(매트랩방식)에서 표본을 추출.
- binomial(): 이항분포에서 표본을 추출.
- normal(): 정규분포(가우시안)에서 표본을 추출.
- beta(): 베타분포에서 표본을 추출.
- chisquare(): 카이제곱분포에서 표본을 추출.
- gamma(): 감마분포에서 표본을 추출.
- uniform(): 균등(0,1) 분포에서 표본을 추출.
