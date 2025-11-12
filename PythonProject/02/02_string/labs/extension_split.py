# 02/02_string/labs/extension_split.py

# 1. 사용자로부터 파일명을 입력받습니다.
# 예시 입력: report.docx
filename = input("filename: ")

# 2. 문자열을 가장 마지막 '.'을 기준으로 분리하고 마지막 요소를 확장자로 추출합니다.
# rsplit(separator, maxsplit)을 사용하면 오른쪽(r)부터 분리 횟수(maxsplit)를 지정하여
# 파일 이름 중간에 '.'이 있어도 안전하게 처리할 수 있습니다.
# 예를 들어, 'data.2025.report.docx'의 경우 ['data.2025.report', 'docx']가 됩니다.
extension = filename.rsplit('.', 1)[-1]

# 3. 결과를 요구 사항에 맞게 출력합니다.
print(f"extension: {extension}")

# 예시 입력: report.docx
# 예시 출력: extension: docx
