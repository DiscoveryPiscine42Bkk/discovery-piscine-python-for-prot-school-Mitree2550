def checkmate(board):  
    rows = board.splitlines()

    # ตรวจสอบความกว้างของกระดานให้เท่ากัน
    row_length = len(rows[0])
    i = 0
    while i < len(rows):
        if len(rows[i]) != row_length:
            print("Fail")
            return
        i += 1

    # หาตำแหน่งของราชา
    king_position = next(((i, row.index('K')) for i, row in enumerate(rows) if 'K' in row), None)
    
    if not king_position:
        print("Error")
        return

    x, y = king_position  # ตำแหน่งของราชา

    # ฟังก์ชันตรวจสอบการโจมตี
    def check_direction(dx, dy, pieces):
        i, j = x + dx, y + dy
        while 0 <= i < len(rows) and 0 <= j < len(rows[0]):
            if rows[i][j] in pieces:
                return True
            if rows[i][j] != '.':
                break
            i, j = i + dx, j + dy
        return False

    # ตรวจสอบเบี้ย
    if x + 1 < len(rows) and ((y - 1 >= 0 and rows[x + 1][y - 1] == 'P') or (y + 1 < row_length and rows[x + 1][y + 1] == 'P')):
        print("Success")
        return

    # ตรวจสอบการโจมตีจากเรือ (R), ราชินี (Q) แนวตรงและแนวนอน
    if any(check_direction(dx, dy, {'R', 'Q'}) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        print("Success")
        return

    # ตรวจสอบการโจมตีจากบิชอป (B), ราชินี (Q) แนวทแยง
    if any(check_direction(dx, dy, {'B', 'Q'}) for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]):
        print("Success")
        return

    print("Fail")
