class Stock:
    def __init__(self, code, open_price, close_price):
        self.code = code
        self.open_price = open_price
        self.close_price = close_price

def read_stock_data(filename):
    stocks = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            if len(data) == 3:
                code, open_price, close_price = data
                stocks.append(Stock(code, float(open_price), float(close_price)))
    return stocks

def calculate_price_difference(stocks):
    price_diff = {}
    for stock in stocks:
        if stock.code not in price_diff:
            price_diff[stock.code] = []
        price_diff[stock.code].append(stock.close_price - stock.open_price)
    return price_diff

def print_sorted_stock_codes(stocks):
    sorted_codes = sorted(set(stock.code for stock in stocks))
    print("Danh sách mã chứng khoán theo thứ tự tăng dần:")
    for code in sorted_codes:
        print(code)

def print_average_price_difference(price_diff):
    print("Giá trị trung bình của hiệu (giá đóng cửa - giá mở cửa) trong 10 ngày với mỗi mã chứng khoán:")
    for code, differences in price_diff.items():
        average_diff = sum(differences) / len(differences)
        print(f"Mã chứng khoán {code}: {average_diff:.3f}")

def search_by_stock_code(stocks, code):
    found = False
    max_close = float('-inf')
    min_close = float('inf')
    for stock in stocks:
        if stock.code == code:
            found = True
            max_close = max(max_close, stock.close_price)
            min_close = min(min_close, stock.close_price)
    if found:
        print(f"Giá đóng cửa cao nhất trong 10 ngày: {max_close:.3f}")
        print(f"Giá đóng cửa thấp nhất trong 10 ngày: {min_close:.3f}")
    else:
        print("Không tìm thấy mã chứng khoán này.")

def search_trending_stocks(stocks):
    trending_stocks = []
    for stock in stocks:
        if len(stock) >= 2 and stock[0].close_price > stock[0].open_price and stock[1].close_price > stock[1].open_price:
            trending_stocks.append(stock[0].code)
    print("Các mã chứng khoán có xu hướng tăng đồng thời trong cả ngày 1 và ngày 2:")
    for code in trending_stocks:
        print(code)

def find_longest_increasing_streak(price_diff):
    max_streak = max(len(diff) for diff in price_diff.values())
    longest_streaks = [code for code, diff in price_diff.items() if len(diff) == max_streak]
    print(f"Mã có số ngày tăng lớn nhất ({max_streak} ngày):")
    for code in longest_streaks:
        print(code)

def main():
    filename = 'data.txt'
    stocks = read_stock_data(filename)
    while True:
        print("\nMenu:")
        print("1. Đọc file và hiển thị thông tin")
        print("2. Tìm kiếm theo mã chứng khoán")
        print("3. Tìm mã chứng khoán có xu hướng tăng")
        print("4. Tìm mã có số ngày tăng lớn nhất")
        print("5. Thoát chương trình")
        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            print_sorted_stock_codes(stocks)
            price_diff = calculate_price_difference(stocks)
            print_average_price_difference(price_diff)
        elif choice == '2':
            code = input("Nhập mã chứng khoán: ")
            search_by_stock_code(stocks, code)
        elif choice == '3':
            search_trending_stocks(stocks)
        elif choice == '4':
            price_diff = calculate_price_difference(stocks)
            find_longest_increasing_streak(price_diff)
        elif choice == '5':
            print("Thông tin tác giả: [Họ và tên sinh viên] [MSSV]")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
