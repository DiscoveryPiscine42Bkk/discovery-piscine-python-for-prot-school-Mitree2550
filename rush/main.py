from checkmate import checkmate  # นำเข้าฟังก์ชัน checkmate จาก checkmate.py

def main():
    # ตัวอย่างของกระดานหมากรุก 1 และ 2
    board1 = """\
R...
.K..
..P.
....
"""
    board2 = """\
R...
.K..
"""
    # เรียกฟังก์ชัน checkmate กับกระดานทั้งสอง
    print("Testing Board 1:")
    checkmate(board1)  # ตรวจสอบกระดาน 1
    
    print("Testing Board 2:")
    checkmate(board2)  # ตรวจสอบกระดาน 2

if __name__ == "__main__":
    main()
