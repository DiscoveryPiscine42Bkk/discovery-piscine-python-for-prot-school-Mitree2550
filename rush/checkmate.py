def checkmate(board):  
    rows = str(board).split()

    # ตรวจสอบความกว้างของกระดานให้เท่ากัน
    row_length = len(rows[0])
    i = 0
    while i < len(rows):
        if len(rows[i]) != row_length:
            print("Fail")
            return
        i += 1
    
    # ตรวจสอบจำนวนราชา
    king_count = sum(row.count('K') for row in rows)
    if king_count != 1:
        print(f"Error: พบ king {king_count} ตัว")
        return

    # หาตำแหน่งของราชา
    king_position = None
    i = 0
    while i < len(rows):
        row = rows[i]
        if 'K' in row:
            king_position = (i, row.index('K'))
            break
        i += 1    
    #เช็คว่าเจอ k ไหม
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
