from bs4 import BeautifulSoup
import csv

# Sample HTML 파일을 읽기
with open('Sample.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_content, 'html.parser')

# 클래스 명과 헤더 매핑
class_to_header = {
    'Text-sc-1a1lydu-0 gEOePO': 'name',
    'Text-sc-1a1lydu-0 hxQRuT': 'address',
    'Text-sc-1a1lydu-0 hkqWjl': 'Key_money',
    'Text-sc-1a1lydu-0 jPNcpb': 'area'
}

# 추출된 데이터를 저장할 딕셔너리
data = {header: [] for header in class_to_header.values()}

# 각 클래스에 대한 데이터 추출
for class_name, header in class_to_header.items():
    spans = soup.find_all('span', class_=class_name)
    for span in spans:
        data[header].append(span.get_text())

# 최대 행 길이 계산
max_length = max(len(column) for column in data.values())

# CSV 파일에 저장할 데이터 준비
csv_data = []
for i in range(max_length):
    row = []
    for header in data:
        # 데이터가 있는 경우에만 추가, 없으면 빈 문자열 추가
        row.append(data[header][i] if i < len(data[header]) else '')
    csv_data.append(row)

# CSV 파일에 4개 컬럼으로 저장
csv_filename = 'crawled_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # 헤더 작성
    writer.writerow(class_to_header.values())
    # 데이터 작성
    writer.writerows(csv_data)

# 저장된 CSV 파일의 경로 반환
csv_filename

