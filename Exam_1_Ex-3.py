def readPriceProducts(fName="PriceFile.txt"):
    try:
        with open(fName, "r") as file:
            result = []
            for line in file.readlines():
                try:
                    code, price = line.split()
                    result.append((code, float(price)))
                except (ValueError, IndexError):
                    continue
        return result
    except IOError:
        print("There was a problem accessing the file")
        raise SystemExit
    
def readStockProducts(file_path):
    try:
        with open(file_path, 'r') as file:
            result = []
            for line in file.readlines():
                try:
                    code, color, quantity = line.split()
                    result.append((code, int(color), int(quantity)))
                except (ValueError, IndexError):
                    continue
        return result
    except IOError:
        print("There was a problem accessing the file")
        raise SystemExit
    
def readPriceProductsDict(fName="PriceFile.txt"):
    try:
        with open(fName, "r") as file:
            result = {}
            for line in file.readlines():
                try:
                    code, price = line.split()
                    result[code] = float(price)
                except (ValueError, IndexError):
                    continue
        return result
    except IOError:
        print("There was a problem accessing the file")
        raise SystemExit

def fillOrder(colCod, qtty, stock_info, price_info):
    result = []
    for code, color, quantity in stock_info:
        if color == colCod and quantity >= qtty:
            unit_price = price_info.get(code)
            if unit_price is not None:
                total_price = unit_price * qtty
                result.append((code, total_price))
    return result
