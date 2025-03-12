def checkmate(board): 
    rows = board.splitlines()  # แยกแถวจากกระดานหมากรุก

    # ตรวจสอบให้แน่ใจว่าทุกแถวมีความยาวเท่ากัน
    row_length = len(rows[0])
    for row in rows:
        if len(row) != row_length:
            print("Fail")  # ถ้าแถวใดมีความยาวไม่เท่ากัน ให้แสดง Fail
            return

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
        
        # ตรวจสอบการโจมตีจากเรือ (R) หรือราชินี (Q) ในแนวนอนและแนวตั้ง
        # แนวนอน (ซ้าย-ขวา)
        for i in range(y + 1, len(rows[0])):
            if rows[x][i] in ('R', 'Q'):
                return True
            if rows[x][i] != '.':
                break
        for i in range(y - 1, -1, -1):
            if rows[x][i] in ('R', 'Q'):
                return True
            if rows[x][i] != '.':
                break
        
        # แนวตั้ง (บน-ล่าง)
        for i in range(x + 1, len(rows)):
            if rows[i][y] in ('R', 'Q'):
                return True
            if rows[i][y] != '.':
                break
        for i in range(x - 1, -1, -1):
            if rows[i][y] in ('R', 'Q'):
                return True
            if rows[i][y] != '.':
                break
        
        # ตรวจสอบการโจมตีจากบิชอป (B) หรือราชินี (Q) ในแนวทแยง
        # ทแยงซ้าย-ขวา
        for i in range(1, min(len(rows) - x, len(rows[0]) - y)):
            if rows[x + i][y + i] in ('B', 'Q'):
                return True
            if rows[x + i][y + i] != '.':
                break
        for i in range(1, min(x + 1, y + 1)):
            if rows[x - i][y - i] in ('B', 'Q'):
                return True
            if rows[x - i][y - i] != '.':
                break
        
        # ทแยงขวา-ซ้าย
        for i in range(1, min(len(rows) - x, y + 1)):
            if rows[x + i][y - i] in ('B', 'Q'):
                return True
            if rows[x + i][y - i] != '.':
                break
        for i in range(1, min(x + 1, len(rows[0]) - y)):
            if rows[x - i][y + i] in ('B', 'Q'):
                return True
            if rows[x - i][y + i] != '.':
                break

        return False

    if is_in_check(king_position):
        print("Success")
    else:
        print("Fail")