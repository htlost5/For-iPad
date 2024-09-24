price = 100
while True:
    print(f'商品は{price}円です。')
    money = int(input("お金を投入してください："))
    if money >= price:
        print("お金が投入されました。")
        touch = input("購入しますか？ y/n :")
        if touch == "y":
            print("商品をお取りください。")
            if money > price:
                print(f'おつりは{money-price}です。')
            else:
                pass
    
        else:
            print("購入を中止します。")
            print(f"お金をお取りください。({money}円)")
            