from path import Path


def main():
    # 작업할 폴더 및 파일 경로 설정
    folder = Path("./local_lib/test_folder")
    file_path = folder / "test_file.txt"

    # 폴더 생성 (이미 존재하는 경우 아무 일도 하지 않음)
    folder.mkdir(parents=True, exist_ok=True)

    # 파일에 내용 작성
    with open(file_path, "w") as file:
        file.write("Hello, path library!")

    # 파일 내용 읽기
    with open(file_path, "r") as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    main()
