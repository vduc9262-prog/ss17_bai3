
teams_list = []
match_schedule = []


def input_teams():


    global teams_list

    text = input("Nhập các đội (cách nhau bởi dấu phẩy): ")

    teams = [
        team.strip().upper()
        for team in text.split(",")
        if team.strip()
    ]

    teams_list = []

    for team in teams:
        if team not in teams_list:
            teams_list.append(team)

    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")


def create_schedule():

    global match_schedule

    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return

    match_schedule = []

    for i in range(len(teams_list)):
        for j in range(i + 1, len(teams_list)):

            match = teams_list[i] + " vs " + teams_list[j]

            match_schedule.append(match)

    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---\n")

    for i, match in enumerate(match_schedule, 1):
        print(f"{i}. {match}")

    print(f"\nTổng số trận đấu: {len(match_schedule)} trận.")


def create_match_id():

    if len(match_schedule) == 0:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    print("\n--- MÃ TRẬN ĐẤU ---\n")

    for i, match in enumerate(match_schedule, 1):

        team1, team2 = match.split(" vs ")

        code1 = team1[:3].ljust(3, "X")
        code2 = team2[:3].ljust(3, "X")

        match_id = f"M{i:02d}-{code1}-{code2}"

        print(f"Trận {i} ({match}) -> ID: {match_id}")



def main():

    while True:
        choice = input("""============= ESPORTS MATCHMAKER =============
1. Nhập danh sách Đội tuyển
2. Tạo lịch thi đấu (Combinations)
3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)
4. Đóng hệ thống
==============================================
Chọn chức năng (1-4):""")

        if choice == "1":

            print("\n NHẬP DANH SÁCH ")

            input_teams()

        elif choice == "2":

            create_schedule()

        elif choice == "3":

            create_match_id()

        elif choice == "4":

            print("Đóng hệ thống")
            break

        else:

            print("Lựa chọn không hợp lệ")


main()