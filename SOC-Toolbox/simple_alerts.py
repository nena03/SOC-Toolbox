def alert_on_keywords(file_path, keywords):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for keyword in keywords:
        for i, line in enumerate(lines):
            if keyword.lower() in line.lower():
                print(f"[ALERT] '{keyword}' pronađeno u liniji {i + 1}: {line.strip()}")

if __name__ == "__main__":
    path = input("Unesi putanju do fajla: ").strip()
    keywords = input("Unesi ključne reči za alarm (razdvojene zarezom): ").split(",")
    alert_on_keywords(path, [kw.strip() for kw in keywords])
