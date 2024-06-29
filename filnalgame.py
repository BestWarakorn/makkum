def initialize_board():
    #สร้างตารางหมากขุม
    return [7] * 7 + [0] + [7] * 7 + [0]


def print_board(pits):
    # พิมพ์ตารางหมากขุม
    print("\nตารางหมากขุม:")
    print("    ", pits[8], pits[9], pits[10], pits[11], pits[12], pits[13], pits[14])
    print(pits[7], "                     ", pits[15])
    print("    ", pits[6], pits[5], pits[4], pits[3], pits[2], pits[1], pits[0])


def make_move(pits, start_pit):
    stones = pits[start_pit]#ให้มือมีจำนวนเท่ากับหลุมที่เริ่ม
    pits[start_pit] = 0#ทำให้หลุมว่าง
    index = start_pit#ให้เริ่มต้นที่ตำแหน่งเริ่มต้น

    while stones > 0:#ให้ทำงานบรรทัดที่20-46จนกว่าลูกแก้วจะหมด
        index = (index + 1) % 16#ขยับหลุม
        if index == 7 and start_pit > 6:  # ข้ามหลุมใหญ่ของผู้เล่น 1 เมื่อผู้เล่น 2 เล่น
            continue
        elif index == 15 and start_pit <= 6:  # ข้ามหลุมใหญ่ของผู้เล่น 2 เมื่อผู้เล่น 1 เล่น
            continue

        stones -= 1 #วางลูกแก้ว

        if stones == 0:#ถ้าลูกแก้วหมดมือให้ทำบรรทัดที่29-46
            if index == 7 or index == 15:#ตรวจสอบว่าเป็นหลุมหัวเมืองหรือไม่
                pits[index] += 1#เพิ่มลูกแก้วในหัวเมือง
                break#หยุดทำงาน บรรทัดที่20-46
            elif pits[index] > 0:#ถ้าหลุมมีลูกแก้วอยู่ให้ทำบรรทัดที่33
                stones = pits[index] + 1#หยิบลูกแก้ว
                pits[index] = -1#ทำให้ในหลุมมีลูกแก้วเป็น-1
            elif pits[index] == 0:#ถ้าไม่มีลูกแก้วในหลุม
                if start_pit > 6 and index > 6 and pits[14 - index] > 0:#ถ้าเป็นผู้เล่นคนที่2ตกในแดนตน ให้ทำบรรทัดที่ 37-39 
                    pits[15] += pits[14 - index] + 1#เพิ่มค่าในหัวเมืองตามหลุมตรงข้ามและในมือลูกสุดท้าย
                    print(f"รับเพิ่มจากการตกที่ตก{pits[14-index]+1}ลูก")#แสดงผล
                    pits[14 - index] = 0#ทำให้หลุมตตรงข้ามที่ตกมีค่าเป็น0
                elif start_pit <= 6 and index <= 6 and pits[14 - index] > 0:#ถ้าเป็นผู้เล่นคนที่2ตกในแดนตน ให้ทำบรรทัดที่ 41-43
                    pits[7] += pits[14 - index] + 1#เพิ่มค่าในหัวเมืองตามหลุมตรงข้ามและในมือลูกสุดท้าย
                    print(f"รับเพิ่มจากการตกที่ตก{pits[14-index]+1}ลูก")#แสดงผล
                    pits[14 - index] = 0#ทำให้หลุมตตรงข้ามที่ตกมีค่าเป็น0
                else:#ถ้าไม่เข้าเงื่อนไขไดๆให้ทำบรรทัดที่45
                    pits[index] = 1 # ให้หลุมมีลูกแก้วเป็น1
                break#หยุดทำงาน บรรทัดที่20-46
        
        pits[index] += 1#เพิ่มลูกในหลุม

    return index#เมื่อจบการทำงาน บรรทัดที่20-46 ให้ส่งค่าตำแหน่งสุดท้ายที่ตกกลับไป


def play_game():
    n=7
    pits = initialize_board()#ทำงานบรรทัดที่3
    current_player = 1#ให้ผู้เล่น1เริ่มก่อน
    
    while True:#ให้ทำงานบรรทัดที่ 59-123 ไปเรื่อยๆ
        print_board(pits)#ทำงานบรรทัดที่8-11
        if pits[7] + pits[15] == n * 14:#ตรวจสอบว่าเกิดการชนะหรือไม่
            if pits[7] > pits[15]:#ถ้าคนที่1ชนะ ให้แสดงผลว่าคนที่1ชนะ
                print("ผู้เล่น1ชนะ")
            elif pits[7] < pits[15]:#ถ้าคนที่2ชนะ ให้แสดงผลว่าคนที่1ชนะ
                print("ผู้เล่น2ชนะ")
            else:#เสมอ ให้แสดงว่าเสมอ
                print("เสมอ")
            break#หยุดทำงานบรรทัดที่ 59-123
        elif pits[7]>n*7:#ถ้าคนที่1ชนะ ให้แสดงผลว่าคนที่1ชนะ
            print("ผู้เล่น1ชนะ")
            break#หยุดทำงานบรรทัดที่ 59-123
        elif pits[15]>n*7:#ถ้าคนที่2ชนะ ให้แสดงผลว่าคนที่1ชนะ
            print("ผู้เล่น2ชนะ")
            break#หยุดทำงานบรรทัดที่ 59-123
        
        
        print(f"\nผู้เล่น {current_player}'s เทิร์น:")#แสดงผู้เล่นปัจจุบัน

        while True:#ทำบรรทัดที่ 79-123 ไปเรื่อยๆ
            try:#ตรวจสอบความถูกต้องของการเลือกหลุมถึงบรรทัดที่ 94
                start_pit = int(input("เลือกหลุมที่จะเล่น (1-7): "))#เลือกหลุม
                if start_pit > 7 or start_pit < 1:
                    print("หลุมที่เลือกไม่ถูกต้อง หรือหลุมนั้นไม่มีลูกอยู่.")
                    continue
                if current_player == 1:
                    start_pit = 7 - start_pit
                else:
                    start_pit = 15 - start_pit

                if pits[start_pit] > 0 and start_pit != 7 and start_pit != 15:
                    break#หยุดทำงานบรรทัดที่ 59-123
                else:
                    print("หลุมที่เลือกไม่ถูกต้อง หรือหลุมนั้นไม่มีลูกอยู่.")
            except ValueError:
                print("กรุณาใส่จำนวนเต็ม.")

        last_pit = make_move(pits, start_pit)#เล่น (ทำงานบรรทัดที่ 15-50)
        if last_pit == 7:#แสดงผลถ้าตกหัวเมืองคนที่ 1
            print(f"ตกหลุมเมืองคนที่1เป็นหลุมสุดท้าย")
        elif last_pit == 15:#แสดงผลถ้าตกหัวเมืองคนที่ 2
            print(f"ตกหลุมเมืองคนที่2เป็นหลุมสุดท้าย")
        elif last_pit > 7:#แสดงผลถ้าตกฝั่งของคนที่ 2
            print(f"ตกหลุม{15 - last_pit}ของคนที่2เป็นหลุมสุดท้าย")
        else:#แสดงผลถ้าตกฝั่งของคนที่ 1
            print(f"ตกหลุม{7 - last_pit}ของคนที่1เป็นหลุมสุดท้าย")
        if current_player == 1 and last_pit == 7:#ถ้าตกหัวเมืองตนเองเล่นต่อ
            continue
        elif current_player == 2 and last_pit == 15:#ถ้าตกหัวเมืองตนเองเล่นต่อ
            continue

        #ตรวจสอบว่าผู้เล่นฝั่งตรงข้ามสามารถเล่นต่อไปได้หรือไม่ ถ้าไม่ให้คนเดิมเล่นต่อไปเรื่อยๆ
        f1 = 0
        f2 = 0
        for i in range(0, 7, 1):
            if pits[i] > 0:
                f1 = 1
            if pits[8 + i] > 0:
                f2 = 1
        if f1 == 0:
            current_player = 2
        elif f2 == 0:
            current_player = 1
        else:
            current_player = 2 if current_player == 1 else 1


play_game()# ทำงานบรรทัดที่ 54-123
