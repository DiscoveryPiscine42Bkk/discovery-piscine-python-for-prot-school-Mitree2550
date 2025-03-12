def checkmate(board):
    rows = board.splitlines()  # แยกแถวจากกระดานหมากรุก
    
    # หาตำแหน่งของราชา
    king_position = None
    for i, row in enumerate(rows):
        if 'K' in row:
            king_position = (i, row.index('K'))
            break

    if not king_position:
        print("Error")
        return

    # ฟังก์ชันเพื่อตรวจสอบว่า ราชาอยู่ในเช็คหรือไม่
    def is_in_check(king_pos):
        x, y = king_pos
        # ตรวจสอบการโจมตีจากเบี้ย (P)
        if x + 1 < len(rows) and y - 1 >= 0 and rows[x + 1][y - 1] == 'P':
            return True
        if x + 1 < len(rows) and y + 1 < len(rows[0]) and rows[x + 1][y + 1] == 'P':
            return True
        # เพิ่มการตรวจสอบหมากรุกอื่น ๆ เช่น บิชอป (B), เรือ (R), ราชินี (Q) ได้
        return False

    if is_in_check(king_position):
        print("Success")
    else:
        print("Fail")
