'''
로또 구현하기 2
1부터 45 까지의 랜덤한 숫자를 6개 출력하는 코드를 작성하시오.
단, 수의 중복이 허용되지 않으며, 오름차순 정렬하여 출력해야 한다.

출력 예시
8
12
20
33
38
45
'''

# ===========================================================================
# TODO 1. random 라이브러리를 import를 사용해서 불러오세요.
?????? random
my_number = []

# ===========================================================================
# TODO 2. 6개의 숫자가 my_number에 저장되기 전까지 반복하세요. len은 리스트에 저장된 원소의 개수를 구하는 함수입니다.
while len(????????) < 6:
    # ===========================================================================
    # TODO 3. a는 1부터 45까지의 랜덤한 정수를 저장하도록 설정하세요.
    a = random.???????(?, ?)
    # ===========================================================================
    # TODO 4. 중복되지 않았는지 확인합니다. 구체적으로 my_number 리스트 안에 없는 경우(not) 에만 값을 추가합니다.
    if a ??? in my_number:
        my_number.append(a)

# ===========================================================================
# TODO 5. my_number 리스트를 정렬(sort) 하고 출력하세요.
my_number.????()
for i in my_number:
    print(i)