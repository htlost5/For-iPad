import bcrypt

def hash_password(password):
    # ソルトを自動生成してパスワードをハッシュ化
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

def verify_password(stored_hash, provided_password):
    # 保存されたハッシュと提供されたパスワードを照合
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hash)

# 使用例
password = "RkUdbN4ChmfH"
hashed_password = hash_password(password)
print(hashed_password)
# ハッシュ値をデータベースに保存

# パスワード検証
is_valid = verify_password(hashed_password, "RkUdbN4ChmfH")