# 02/02_string/labs/domain_split.py

# 1. 사용자로부터 웹페이지 주소를 입력받습니다.
# 예시 입력: http://www.naver.com/edit/page/7022
address = input("address: ")

# 2. URL에서 경로를 제거하고 도메인 부분만 추출합니다.
# 첫 번째 '/' 이후의 문자열을 제거합니다.
# 이 예제에서는 http://www.naver.com/ 에서 세 번째 '/' 이후를 제거하면 됩니다.
# 가장 간단한 방법은 'com', 'net', 'org' 뒤의 '/'를 찾는 것입니다.

# 첫 번째 분리: 주소의 끝에서 첫 번째 '/'를 찾고 그 앞부분만 사용합니다.
# 'http://www.naver.com/edit/page/7022' -> 'http://www.naver.com' (혹은 그에 가까운 형태)
if '/' in address[7:]:  # 'http://' 이후에 '/'가 있다면
    # 주소를 '/'를 기준으로 분리하고 첫 번째 요소만 사용합니다.
    # 하지만 URL 구조가 복잡하므로, 가장 일반적인 도메인 이름(naver.com)까지만 추출하는 방법을 사용합니다.

    # 2-1. URL에서 프로토콜과 서브도메인을 제거하고 'naver.com/...' 부분만 남깁니다.
    # 'http://' 또는 'https://'와 'www.'를 제거합니다.
    if address.startswith('http://'):
        domain_start = address[7:]
    elif address.startswith('https://'):
        domain_start = address[8:]
    else:
        domain_start = address  # 프로토콜이 없는 경우

    if domain_start.startswith('www.'):
        domain_start = domain_start[4:]

    # 2-2. 첫 번째 '/'를 기준으로 분리하여 도메인 이름(naver.com) 부분만 얻습니다.
    # '/'가 없으면 전체를 사용합니다.
    domain_name_with_path = domain_start.split('/')[0]

# 3. 도메인 이름('naver.com')을 '.'으로 분리하고 마지막 요소를 추출합니다.
# 'naver.com' -> ['naver', 'com']
domain_parts = domain_name_with_path.split('.')

# 4. 마지막 요소(도메인 확장자, 예: 'com')를 추출합니다.
domain = domain_parts[-1]

# 5. 결과를 요구 사항에 맞게 출력합니다.
print(f"domain: {domain}")

# 예시 입력: http://www.naver.com/edit/page/7022
# 예시 출력: domain: com